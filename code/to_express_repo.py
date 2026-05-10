# @todo: double encoding e.g Role &amp;lt;&amp;gt;
# @todo: schema name not really discoverable
# @todo: ControlPointsList / ColourList : LIST [2:?] OF LIST [2:?]
# @todo: IfcClassificationReference.HasReferences self referential inverse
# @todo: schema namespace different in constraint expression

import sys
import html

import operator
import functools

from collections import defaultdict, namedtuple

import xmi
import express
import json

try:
    fn = sys.argv[1]
except:
    print("Usage: python to_express.py <schema.xml>", file=sys.stderr)
    print("       writes converted Express schema to stdout", file=sys.stderr)
    exit()
    
xmi = xmi.doc(fn)

connector_data = namedtuple("connector_data", ("is_inverse", "inverse_order", "aggregation_type", "is_optional"))
association_data = namedtuple("association_data", ("own_end", "type", "other_end", "asssocation"))
# The order in which definitions are to appear in the Express schema
EXPRESS_ORDER=("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")





# Extract some data from the connectors for use later on
connectors = defaultdict(dict)
for c in xmi/"connector":
    src = c|"source"
    tgt = c|"target"
    for st, en in [(src, tgt), (tgt, src)]:
        cls = (st|"model").name
        other_cls = (en|"model").name
        is_inverse = "ExpressInverse" in st.tags()
        inverse_order = int(st.tags().get("ExpressOrderingInverse", 0))
        is_optional = "ExpressOptional" in st.tags()
        connectors[c.idref][other_cls] = connector_data(is_inverse, inverse_order, st.tags().get("ExpressAggregation"), is_optional)
    
# Extract some data from the associations for use later on
associations = defaultdict(list)
for assoc in xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
    c1, c2 = assoc/'ownedEnd'
    t1, t2 = map(lambda c: (c|"type").idref, (c1, c2))
    tv1, tv2 = map(lambda t: xmi.by_id[t].name, (t1, t2))
    cv1, cv2 = map(operator.attrgetter('name'), (c1, c2))
    associations[tv1].append(association_data(c2, xmi.by_id[t2], c1, assoc))
    associations[tv2].append(association_data(c1, xmi.by_id[t1], c2, assoc))

order = dict()
for o in xmi/"thecustomprofile:ExpressOrdering":
    d = o.attributes()
    dk = [k for k in d.keys() if k.startswith('base_')][0]
    order[d[dk]] = int(d['ExpressOrdering'])

def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: an element in EXPRESS_ORDER
    b: an type/entity/function definition string
    """
    
    for d in xmi.by_tag_and_type["element"]["uml:DataType"]:
    
        dd = xmi.by_id[d.idref]
        try:
            super = [t for t in d/"tag" if t.name == "ExpressDefinition"][0].value            
        except IndexError as e:
            super = xmi.by_id[(dd|"generalization").general].name
        
        cs = sorted(d/"constraint", key=lambda cc: float(cc.weight))
        constraints = map(lambda cc: "\t%s : %s;" % tuple(map(html.unescape, map(functools.partial(getattr, cc), ("name", "description")))), cs)   
        my_constraints = list(constraints)         
        
        yield "TYPE",d.name,super,my_constraints, express.format_simple_type(d.name, super, constraints)
        
    for c in xmi.by_tag_and_type["element"]["uml:Class"]:
    
        stereotype = (c/"properties")[0].stereotype
        
        if stereotype in {"EXPRESS FUNCTION", "EXPRESS RULE"}:
            
            yield stereotype.split(" ")[1],c.name,(c|"behaviour").value, html.unescape((c|"behaviour").value) + ";"
        
        elif stereotype == "EXPRESS SELECT":
            
            values = filter(lambda s: s != c.name, map(lambda s: xmi.by_id[s.start].name, c/"Substitution"))
            my_values = list(values)
            yield "SELECT",c.name,my_values, express.format_type(c.name, "SELECT", values)
            
        elif stereotype == "enumeration":
        
            values = map(operator.itemgetter(1), sorted(map(lambda a: (int([t for t in a/("tag") if t.name == "ExpressOrdering"][0].value), a.name), c/("attribute"))))
            my_values = list(values)
            yield "ENUM", c.name,my_values, express.format_type(c.name, "ENUMERATION OF", values)
            
        else:
        
            is_abstract = (c/"properties")[0].isAbstract == "true" 
        
            attribute_names = set()
            for la in c / ("attribute"):
                iref = la.idref
                a = xmi.by_id[iref]
                n = a.name
                attribute_names.add(n)

            attributes, inverses, derived, subtypes, supertypes = [], [], [], [], []
            
            for g in c/("Generalization"):
                start, end = g.start, g.end
                issub = start == c.idref
                other = [start, end][issub]
                other_name = xmi.by_id[other].name
                [supertypes, subtypes][issub].append(other_name)
            
            for end_node, end_node_type, other_end, assoc_node in associations[c.name]:
                try:
                    nm = end_node.name
                    assert nm
                except:
                    continue
                    
                try:
                    attr_name = other_end.name
                except:
                    attr_name = None
                    
                bound = ""
                try:
                    lv = int((end_node|"lowerValue").value)
                    uv = int((end_node|"upperValue").value)
                    if uv == -1: uv = "?"
                    bound = "[%s:%s]" % (lv, uv)
                except: pass
                attr_entity = end_node_type.name

                is_inverse, inverse_order, express_aggr, is_optional = connectors[assoc_node.xmi_id][c.name]
                is_optional_string = "OPTIONAL " if is_optional else ""

                if express_aggr:
                    attr_entity = "%s %s OF %s" % (express_aggr, bound, attr_entity)

                if nm not in attribute_names:
                    if (is_inverse and attr_name is not None) or assoc_node.xmi_id not in order:
                        inverses.append((inverse_order, "\t%s : %s FOR %s;" % (nm, attr_entity, attr_name)))
                    else:
                        attribute_order = order[assoc_node.xmi_id]
                        attributes.append((attribute_order, "\t%s : %s%s;" % (nm, is_optional_string, attr_entity)))
                    
            for la in c/("attribute"):
                iref = la.idref
                a = xmi.by_id[iref]
                is_optional = "ExpressOptional" in map(operator.attrgetter('name'), la/("tag"))
                is_derived = a.isDerived == "true"
                express_aggr = la.tags().get("ExpressAggregation")
                if express_aggr:
                    bound = ""
                    try:
                        lv = int((a|"lowerValue").value)
                        uv = int((a|"upperValue").value)
                        if uv == -1: uv = "?"
                        bound = "[%s:%s]" % (lv, uv)
                    except: continue
                # or use order[iref]?
                ordering = int(la.tags()["ExpressOrdering"])
                is_optional_string = "OPTIONAL " if is_optional else ""
                n = a.name
                try:
                    t = (a|"type").idref
                except:
                    is_derived = True
                if is_derived:
                    derived.append("\t%s : %s;" % (n, html.unescape((la|"Constraint").notes)))
                    continue
                attribute_names.add(n)
                tv = xmi.by_id[t].name
                if express_aggr:
                    tv = "%s %s OF %s" % (express_aggr, bound, tv)
                attributes.append((ordering, "\t%s : %s%s;" % (n, is_optional_string, tv)))
            
            cs = sorted(c/("constraint"), key=lambda cc: float(cc.weight))
            constraints = map(lambda cc: (cc.type, "\t%s : %s;" % tuple(map(html.unescape, map(functools.partial(getattr, cc), ("name", "description"))))), cs)
            constraints_by_type = defaultdict(list)
            for ct, cc in constraints:
                constraints_by_type[ct].append(cc)

            attributes = map(operator.itemgetter(1), sorted(attributes))
            inverses = map(operator.itemgetter(1), sorted(inverses))

            my_attributes = list(attributes)
            my_inverses = list(inverses)

            
            yield "ENTITY", c.name,my_attributes,derived,my_inverses,constraints_by_type["EXPRESS_WHERE"],constraints_by_type["EXPRESS_UNIQUE"],subtypes,supertypes,is_abstract, express.format_entity(c.name, attributes, derived,inverses, constraints_by_type["EXPRESS_WHERE"], constraints_by_type["EXPRESS_UNIQUE"], subtypes, supertypes, is_abstract)
            
            
def sort_key(tup):
    return (EXPRESS_ORDER.index(tup[0]), tup[1])



print("SCHEMA %s;" % xmi.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper())
print()

# for _, definition in sorted(generate_definitions(), key=sort_key):
#     print(definition)
#     print()




query_dict = []
EXPRESS_ORDER=("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")

for d in generate_definitions():
    final_dict = {}

    if d[0] == 'TYPE':
        final_dict['IFCtype'] = d[0]
        final_dict['name'] = d[1]
        final_dict['super'] = d[2]
        final_dict['constraints'] = d[3]
        final_dict['EXPRESS def'] = d[4]
        
    if d[0] == 'ENUM':
        final_dict['IFCtype'] = d[0]
        final_dict['name'] = d[1]
        final_dict['values'] = d[2]
        final_dict['EXPRESS def'] = d[3]

       
    if d[0] == 'FUNCTION' or d[0] == 'RULE':
        final_dict['IFCtype'] = d[0]
        final_dict['name'] = d[1]
        final_dict['behaviour'] = d[2]
        final_dict['EXPRESS def'] = d[3]

    if d[0] == 'SELECT':
        final_dict['IFCtype'] = d[0]
        final_dict['name'] = d[1]
        final_dict['values'] = d[2]
        final_dict['EXPRESS def'] = d[3]
    
    if d[0] == 'ENTITY':
        final_dict['IFCtype'] = d[0]
        final_dict['name'] = d[1]
        final_dict['attributes'] = d[2]
        final_dict['derived'] = d[3]
        final_dict['inverses'] = d[4]
        final_dict['constraints_where'] = d[5]
        final_dict['constraints_unique'] = d[6]
        final_dict['subtypes'] = d[7]
        final_dict['supertypes'] = d[8]
        final_dict['is_abstract'] = d[9]
        final_dict['EXPRESS def'] = d[10]


    query_dict.append(final_dict)



with open('ifcschema2.json', 'w') as fp:
    json.dump(query_dict, fp)


    


