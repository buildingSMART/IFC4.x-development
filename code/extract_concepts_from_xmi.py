import os
import sys
import json
import re
import glob
import operator
import traceback

from collections import defaultdict

import express
import concept_interpretation
from generators.util.xmi_document import xmi_document
from concept_extractor import extractor

class predefined_type_attribute: pass

class property_set_class: pass


def get_concept_block(all_templates, concept):
    tmpl = [t for t in all_templates if os.path.abspath(t).split(os.sep)[-2].lower().replace(" ", "") == concept.lower()][0]
    concept_blocks = re.findall(r"concept\s*\{.+?\}", open(tmpl, encoding='utf-8').read(), flags=re.S)
    if not concept_blocks:
        print(f"Warning: no concept block on {concept}")
        return
    return concept_blocks[0]


def get_concept_root(all_templates, concept):
    concept_block = get_concept_block(all_templates, concept)
    if concept_block is None:
        return

    lhs = set(n.split(":")[0] for n in re.findall("([\:\w]+)\s*\->", concept_block))
    rhs = set(n.split(":")[0] for n in re.findall("\->\s*([\:\w]+)", concept_block))
    roots = list(lhs - rhs)
    if len(roots) != 1:
        print(f"Warning: multiple roots on {concept}")
        return
    return roots[0].split("_")[0]


def parse_bindings(concept, all_templates=None, fn=None, to_xmi=False, definitions_by_name=None):
    if fn:
        all_templates = glob.glob(os.path.join(os.path.dirname(fn), "../docs/templates/**/*.md"), recursive=True)
        
    concept_block = get_concept_block(all_templates, concept)
    if concept_block is None:
        return
        
    for a,b,c in re.findall(r'(\w+):(\w+)\[binding="(.+?)"\]', concept_block):
        
        if to_xmi:
            t = get_all_attributes(a).get(b, '').replace("OPTIONAL ", "").replace("UNIQUE ", "")
            if (a,b) in [('IfcPropertySet', 'Name'), ('IfcElementQuantity', 'Name'), ('IfcMaterialProperties', 'Name'), ('IfcProfileProperties', 'Name')]:
                # In UML we have property sets as defined classes, which in
                # IFC are fully late-bound type definitions. Selection of the
                # appropriate psets happens through Name, which is IfcLabel
                # which will match the (p|q)set class name in UML.
                type_node = property_set_class()
            elif not t and b == "PredefinedType":
                # PredefinedType is not really an attribute with a specific
                # type in the sense that all entities define their own version
                # of the attribute and there isn't a general basis for all
                # enumerations.
                type_node = predefined_type_attribute()
            else:
                if " OF " in t:
                    # strip off aggregate information
                    t = t.split(" OF ")[1]
                type_node = xmi_doc.xmi.by_id[definitions_by_name[t].id]
            
            yield c, (a,b), type_node
            
        else:
            if b == "PredefinedType":
                yield c, ('', '')
            else:
                yield c, (a,b)
    

    
if __name__ == "__main__":
    raise RuntimeError("This module is deprecated. Concepts are now stored in .CSV files.")


    try:
        fn = sys.argv[1]
    except:
        fn = os.path.join(os.path.dirname(__file__), '..', 'schemas', 'IFC.xml')

    xmi_doc = xmi_document(fn)

    definitions = list(xmi_doc)
    definitions_by_name = {x.name: x for x in definitions}
    
    all_templates = glob.glob(os.path.join(os.path.dirname(fn), "../docs/templates/**/*.md"), recursive=True)  

    def get_predefined_types_for_entity(e):
        if "PredefinedType" in dict(e.definition.attributes):
            type_attr = dict(e.definition.attributes)["PredefinedType"]
            type_name = type_attr.split(" ")[-1]
            type_def = definitions_by_name[type_name].definition
            type_optional = "OPTIONAL" in type_attr
            if isinstance(type_def, express.select):
                for option in type_def.values:
                    yield from get_predefined_types_enum(definitions_by_name[option])
            else:
                yield from get_predefined_types_enum(type_def)
                

    def get_predefined_types_enum(e):
        # can be an xmi_item in case of selects, otherwise express definition
        vs = e.values if hasattr(e, 'values') else e.definition.values
        for nm in vs:
            yield f"{e.name}.{nm}"


    def yield_supertypes_items(a):
        yield a
        try:
            yield from yield_supertypes_items(definitions_by_name[a.definition.supertype])
        except: pass


    def get_predefined_type_listing(items):
        return dict((e.node.idref, [name_to_node[x] \
        for x in get_predefined_types_for_entity(e)]) for e in items if list(get_predefined_types_for_entity(e)))
        

    def get_all_attributes(nm):
        # In the concept instance diagram, class names may be postfixed
        # with _\d to allow for multiple instances of the same type. When
        # looking up attributes this postfix needs to be removed.
        nm = nm.split("_")[0]
        
        
        d = dict(definitions_by_name[nm].definition.attributes)
        for inv in definitions_by_name[nm].definition.inverses:
            k,v = inv.split(" : ")
            k = k.strip()
            # Either take first symbol after OF, or just first symbol
            # when the inverse attribute is not of type aggregate
            v = (re.findall('OF (\w+)', v) + v.split(" "))[0]
            d[k] = v
        st = definitions_by_name[nm].definition.supertype
        if st:
            d.update(get_all_attributes(st))
        return d


    def yield_supertypes(a):
        yield a
        
        try:
            # entity supertypes
            yield from yield_supertypes(xmi_doc.xmi.by_id[(a | "generalization").general])
        except: pass
        
        # select membership
        for sel in name_to_realization_ids.get(a.name, ()):
            yield from yield_supertypes(xmi_doc.xmi.by_id[sel])


    def make_get_binding(bindings):
        def inner(el):
            for nm, attr, nd in bindings:
                if isinstance(nd, predefined_type_attribute):
                    if el.id in all_predtype_ids:
                        return nm
                elif isinstance(nd, property_set_class):
                    if el.id in psets_and_qsets:
                        return nm
                elif nd in set(yield_supertypes(el)):
                    return nm
                else:
                    enum = xmi_doc.xmi.by_id.get(realizes.get(el.id))
                    if enum and (enum.parent.parent.name or '').lower().startswith('ifc4x'):
                        # enum from schema, types should match
                        if nd == enum:
                            return nm
                    elif enum and nd.type == 'uml:DataType':
                        # enum from concept, should be label the name
                        # of the enum in that case is built up like the
                        # pattern below
                        if el.name.startswith(f"{el.parent.name}{nm}Values."):
                            return nm
        return inner
        
    def is_no_concept_node(n):
        """
        The SIMPLE_UNARY concept type is based on a uml:Class
        that is part of the uml:Package for this concept, which
        is then associated to schema classes.
        
        The N-ARY concept will have additional enumeration literals
        defined under package scope. These have a dependency to the
        enumeration itself and should still be take into account
        """
        return not (n.parent.parent.parent.name == "Views" and realizes.get(n.id) is None)


    non_type_definitions = [x for x in definitions if definitions_by_name["IfcObject"] in yield_supertypes_items(x)]

    entities = [e for e in definitions if e.type == "ENTITY"]
    name_to_node = {c.name: c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}
    name_to_id = {c.name: c.id for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}

    # @nb this includes qsets in the xmi_document iteration,
    #     where qsets are only disambiguated based on name prefix
    psets_and_qsets = set(n.node.idref for n in definitions if n.type == 'PSET')

    entity_to_predtypes = get_predefined_type_listing(entities)
    all_predtypes = sum(entity_to_predtypes.values(), [])
    all_predtype_ids = set(x.id for x in all_predtypes)

    predtype_to_entity = dict((v.id, k) for k, vs in entity_to_predtypes.items() for v in vs)

    # proritize predtype->entity mappings for the subtypes of ifcobject as opposed to ifctypeobject
    entity_to_predtypes_non_type = get_predefined_type_listing(non_type_definitions)
    predtype_to_entity_non_type = dict((v.id, k) for k, vs in entity_to_predtypes_non_type.items() for v in vs)
    predtype_to_entity.update(predtype_to_entity_non_type)
    
    name_to_realization_ids = defaultdict(list)
    selects = [d for d in definitions if d.type == "SELECT"]
    for s in selects:
        for v in s.definition.values:
            name_to_realization_ids[v].append(s.node.idref)

    realizes = {x.supplier: x.client for x in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Realization"]}

    result = defaultdict(lambda: defaultdict(list))
    
    psets = {item.id: item for item in definitions if item.type == "PSET"}
    
    # now that we lookup psets from xmi_document we should take care of only processing a pset once
    # even if it is listed multiple times in the association table.
    psets_processed = set()
    
    # explore nested dict as 3-tuples
    for view_name, xmi_concept, pairs in [(k1, k2, v) for k1, d2 in xmi_doc.concept_associations.items() for k2, v in d2.items()]:
        if concept_interpretation.get(xmi_concept) in (
            concept_interpretation.concept_type.PROPERTY_OR_QUANTITY_SET,
            concept_interpretation.concept_type.OBJECT_TYPING,
            concept_interpretation.concept_type.DIRECTIONAL_GROUPED,
            concept_interpretation.concept_type.SIMPLE_UNARY,
            concept_interpretation.concept_type.DIRECTIONAL_BINARY,
            concept_interpretation.concept_type.NARY,
        ):
            try:
                bindings = list(parse_bindings(xmi_concept, all_templates=all_templates, to_xmi=True, definitions_by_name=definitions_by_name))
            except IndexError as e:
                print("Unable to get bindings for template, skipping")
                traceback.print_exc()
                continue
            get_binding = make_get_binding(bindings)

            for p in pairs:
                elems = list(filter(is_no_concept_node, map(xmi_doc.xmi.by_id.__getitem__, p)))
                
                pset_matches = set(e.id for e in elems) & psets.keys()
                if pset_matches:
                    # For PSETs we don't rely on the actual applicability table, because the pset
                    # association is augmented/modified in xmi_document based on the template type
                    
                    from to_pset import get_parent_of_pt
                    
                    assert len(pset_matches) == 1
                    pset_id = list(pset_matches)[0]
                    
                    if pset_id in psets_processed:
                        continue
                        
                    psets_processed.add(pset_id)
                    
                    pset = psets[pset_id]                    
                    
                    for x in (pset.meta.get("refs") or []):                    
                        predefined_type_label = None
                        if isinstance(x, tuple):
                            x, predefined_type_label = x
                        
                        if "." in xmi_doc.xmi.by_id[x].name:
                            x = [c for c in definitions_by_name[xmi_doc.xmi.by_id[x].name.split(".")[0]] if c.name == xmi_doc.xmi.by_id[x].name.split(".")[1]][0]
                        else:
                            x = definitions_by_name[xmi_doc.xmi.by_id[x].name]
                        
                        D = {}

                        entity = x.name
                        if x.parent and get_parent_of_pt(xmi_doc, x.parent.node):
                            entity = get_parent_of_pt(xmi_doc, x.parent.node)
                            predefined_type_label = x.name
                            
                        D["ApplicableEntity"] = entity
                            
                        if predefined_type_label:
                            assert "." not in predefined_type_label
                            D["PredefinedType"] = predefined_type_label
                            
                        D["PsetName"] = pset.name
                        
                        result[view_name][xmi_concept].append(D)
                    
                    continue
                
                appl = None
                elem_binds = None
                if concept_interpretation.get(xmi_concept) == concept_interpretation.concept_type.DIRECTIONAL_BINARY:
                    # We know that the first element is the source of the association, which
                    # is the ApplicableEntity of the concept parametrization
                    appl = elems.pop(0)
                elif len(elems) == 1:
                    # If we have a single element, we already know it's the ApplicableEntity,
                    # continuing with the binding process may cause false matches.
                    elem_binds = [None]
                
                if elem_binds is None:
                    elem_binds = list(map(get_binding, elems))
                
                predtype_bind = all_predtype_ids & set(e.id for e in elems)
                if concept_interpretation.get(xmi_concept) == concept_interpretation.concept_type.PROPERTY_OR_QUANTITY_SET and predtype_bind:
                    # when binding to a predefined type, we can infer the ApplicableEntity
                    elem_binds.append(None)
                    elems.append(xmi_doc.xmi.by_id[predtype_to_entity[next(iter(predtype_bind))]])
                    
                if appl is not None:
                    # Restore the appl after binding
                    elem_binds.append(None)
                    elems.append(appl)
                    
                # a single element should not be bound, that is the ApplicableEntity
                assert len([x for x in elem_binds if x is None]) == 1
                elem_binds[elem_binds.index(None)] = "ApplicableEntity"
                
                binding_names = ["ApplicableEntity"] + [b[0] for b in bindings if b[0] in elem_binds]
                # For concept-specific enum literals we need to remove the prefix
                # if e.parent.parent.parent.name == 'Views' else e.name
                # In fact let's just always remove the prefix, because it's sometimes also wrong
                elem_names = [e.name.split(".")[-1] for e in elems]
                d = {x: elem_names[elem_binds.index(x)] for x in binding_names}
                
                result[view_name][xmi_concept].append(d)
                
    any_sep = re.compile(r"\\|/")
    all_template_names = [any_sep.split(x)[-2] for x in all_templates if "Partial" not in x][1:]
    # also non-leafs are now included, because they appear to be frequently documented on this level.
    # non_leafs = {any_sep.split(x)[-3]:any_sep.split(x)[-2] for x in all_templates if "Partial" not in x}.keys()
    remaining = set(s.replace(" ", "") for s in all_template_names) - \
        xmi_doc.concept_associations['GeneralUsage'].keys() - \
        set(s[0].replace(" ", "") for s in concept_interpretation.concepts.keys())
        # set(s.replace(" ", "") for s in non_leafs)
        
    condensed_to_spaced = {s.replace(" ", ""): s for s in all_template_names}
        
    print("Parameterizations solely based on template definition")
    print("=====================================================")
        
    for concept_name in remaining:
        root = get_concept_root(all_templates, concept_name)
        if root:
            print(condensed_to_spaced[concept_name], "->", root) 
            result["GeneralUsage"][concept_name].append({"ApplicableEntity": root})

    json.dump(result, open("xmi_concepts.json", "w", encoding="utf-8"), indent=1)

    """
    xmi_mvd_concepts = {}
    views = {p.name: p for p in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Package"]}['Views']
    for sub in views / "packagedElement":
        if sub.parent == views and sub.name != 'GeneralUsage':
            xmi_mvd_concepts[sub.name] = list(map(operator.attrgetter('name'), sub / "packagedElement"))
    """

    import csv, re
    with open(f'{os.path.dirname(fn)}/mvd.csv', newline='', encoding='utf-8') as csvfile:
        rd = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(rd)
        views = {v.strip():i for i, v in enumerate(rows[0]) if v.strip()}
        
    xmi_mvd_concepts = {v: [re.sub(r'[^\w]', '', re.split('\s+', r[3], maxsplit=1)[1]) for r in rows[2:] if r[i].strip()] for v, i in views.items()}
    json.dump(xmi_mvd_concepts, open("xmi_mvd_concepts.json", "w", encoding="utf-8"), indent=1)
    