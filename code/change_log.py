import os
import re
import ast
import glob
import sys
import json
import operator
import itertools
import functools

from deepdiff import DeepDiff
   
from ifcopenshell.express import express_parser

from collections import defaultdict
from xmi_document import fix_schema_name
from md import markdown_attribute_parser

import markdown
import bs4
def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features='lxml')
    
deprecation_pattern = re.compile(r'(IFC.+?) DEPRECATION (.+)')
change_pattern = re.compile(r'^(IFC.+?) CHANGE (.+)')
rename_pattern = re.compile(r'renamed from (Ifc[\w]+)')

changes_by_schema = []
changes_by_type = defaultdict(dict)

# to be overwritten in __main__
repo_dir = os.path.join(os.path.dirname(__file__), "..")

def get_notice(fn, subs=False, pattern=deprecation_pattern):
    if not fn.endswith(".md"):
        fns = glob.glob(os.path.join(repo_dir, "docs", "schemas", "**", fn + ".md"), recursive=True)
        
        # if the entity has been deleted we can't show deprecation content anymore for previous version,
        # maybe we shouldn't delete?
        
        if not fns:
            return
            
        fn = fns[0]
        
    default_strs = (
        re.compile(r"This entity is deprecated(\.\s*)?"),
        re.compile(r"This attribute is deprecated and shall no longer be used(\.\s*)?")
    )
    
    def remove_default_strs(s):
        for p in default_strs:
            s = p.sub('', s)
        return s.strip()
        
    def apply_to_line(l):
        m = pattern.match(l)
        if m:
            return (
                m.group(1).lower().replace(".", "").replace("x", "")[:len("ifcxy")].rstrip("0"),
                remove_default_strs(m.group(2))
            )
        
    if subs:
        
        d = dict(markdown_attribute_parser(fn=fn, linesep="\n", heading_name=subs))
        for anm, desc in d.items():
            lines = [l.strip() for l in desc.split("\n") if l.strip()]
            yield from map(lambda tup: (tup[0], anm, tup[1]), filter(None, map(apply_to_line, lines)))
        
    else:
        
        soup = BeautifulSoup(markdown.markdown(open(fn, encoding='utf-8').read()))
        lines = [l.strip() for l in soup.text.split("\n") if l.strip()]
        
        for heading in ('Attributes', 'Items', 'Comments', 'Formal Propositions', 'Concepts'):
            if heading in lines:
                lines = lines[:lines.index(heading)]
        
        yield from filter(None, map(apply_to_line, lines))


rename_messages = defaultdict(dict)
def build_rename_messages():
    fns = glob.glob(os.path.join(repo_dir, "docs", "schemas", "**", "*.md"), recursive=True)
    for fn in fns:
        for schema_version, msg in get_notice(fn, pattern=change_pattern):
            if rename_pattern.search(msg):
                rename_messages[schema_version][rename_pattern.search(msg).group(1)] = rename_pattern.sub(f'renamed to {os.path.basename(fn)[:-3]}', msg)
        

is_iso = os.environ.get('ISO', '0') == '1'

def to_dict(decl, depr=[]):
    if type(decl).__name__ == "EntityDeclaration":
        def format_attribute(attr):
            return {
                # 'type': 'attribute',
                'name': attr.name,
                'optional': attr.optional,
                'type': str(attr.type)
            }
            
        def format_inverse(attr):
            name, definition = list(map(str.strip, str(attr).split(":", 1)))
            return {
                # 'type': 'inverse_attribute',
                'name': name,
                'type': definition
            }
            
        def format_rule(rl, type):
            return {
                # 'type': type,
                'name': rl[0],
                'definition': fix_schema_name(rl[1], remove=True)
            }
    
        return {
            'type': 'entity',
            'name': decl.name,
            'supertype': decl.subtype.super_type if decl.subtype else None,
            'abstract': decl.abstract,
            'attribute': [format_attribute(a) for a in decl.attributes],
            'inverse attribute': [format_inverse(a) for a in decl.inverse],
            'derived attribute': [format_rule(a, 'derived_attribute') for a in (decl.derived or [])],
            'where rule': [format_rule(a, 'where_rule') for a in decl.where],
            'unique rule': [format_rule(a, 'unique_rule') for a in decl.unique],
            'deprecated': decl.name in depr
        }
    else:
        print(type(decl))
        
def compare(depr0, depr1, e0, e1, schema_version):
    depr0, depr1 = map(lambda fn: json.load(open(fn)), (depr0, depr1))
    dd0, dd1 = map(to_dict, (e0, e1), (depr0, depr1))
    
    result = DeepDiff(dd0, dd1, ignore_order=True, cutoff_intersection_for_pairs=0.5)
    for i, (ke, lbl) in enumerate([("iterable_item_added", "additions"), ("values_changed", "modifications"), ("iterable_item_removed", "deletions")]):
        di = result.to_dict().get(ke, {})
        for k, v in di.items():
            path = list(map(ast.literal_eval, re.findall(r"\[(.+?)\]", k)))
            if lbl in ("additions", "deletions") and isinstance(path[-1], int):
                path = path[:-1]
            for pi, pp in list(enumerate(path)):
                if isinstance(pp, int):
                    path[pi] = dd0[path[pi - 1]][pp]['name']
            path = list(map(str, path))
            if lbl == "modifications" and path[0] == "where rule" and isinstance(v['new_value'], dict) and v['new_value'].keys() == {'name', 'definition'}:
                yield (e0.name, "deletions", "where rule", v['old_value']['name'])
                yield (e0.name, "additions", "where rule", v['new_value']['name'])
            else:
                if isinstance(v, dict) and v.keys() == {'old_value', 'new_value'}:
                    a, b = v['old_value'], v['new_value']
                    if all(map(lambda x: isinstance(x, dict), v.values())):
                        for vk in a.keys() | b.keys():
                            if a.get(vk) != b.get(vk):
                                yield (e0.name, lbl, " ".join(path + [vk]), "Changed from\n\"%s\"\nto\n\"%s\"" % (a.get(vk), b.get(vk)))
                    else:
                        msg_postfix = ""
                        
                        if path[-1] == "deprecated" and (a,b) == (False, True):
                            # See if we can get the deprecation notice from the markdown docs
                            msg_postfix = dict(get_notice(e0.name)).get(schema_version) or ''
                            if msg_postfix:
                                msg_postfix = f". {msg_postfix}"
                        
                        if (a,b) == (False, True):
                            msg = "Is now %s" % path[-1]
                            # path = path[:-1]
                        elif (a, b) == (True, False):
                            msg = "Is no longer %s" % path[-1]
                            # path = path[:-1]
                        else:
                            msg = "Changed from\n\"%s\"\nto\n\"%s\"" % (a, b)
                            
                        msg += msg_postfix
                            
                        yield (e0.name, lbl, " ".join(path), msg)
                else:
                    if lbl in ("additions", "deletions"):
                        v = v['name']
                    yield (e0.name, lbl, " ".join(path), v)

    attr_deprs = dict(t[1:] for t in get_notice(e1.name, subs="Attributes") if t[0] == schema_version)
    for anm in map(operator.itemgetter('name'), dd1['attribute']):
        if anm in attr_deprs:
            postfix = attr_deprs[anm]
            if postfix:
                postfix = f". {postfix}"
            yield (e0.name, "modifications", f"attribute {anm}", f"Is now deprecated{postfix}")

def eq(a, b):
    if (type(a) != type(b)):
        return False
    elif isinstance(a, (express_parser.StringType, express_parser.AggregationType, express_parser.BinaryType, str, express_parser.ExplicitAttribute, express_parser.InverseAttribute, express_parser.SimpleType)):
        return str(a) == str(b)
    elif isinstance(a, (express_parser.SelectType, express_parser.EnumerationType)):
        return set(map(str, a.values)) == set(map(str, b.values))
    else:
        # @todo
        import pdb; pdb.set_trace()

def compare_schemas(s0, depr0, s1, depr1, s1_ver):

    for x in 'simpletypes', 'selects', 'enumerations', 'rules', 'functions':

        d1, d2 = map(operator.attrgetter(x), (s0.schema, s1.schema))
        
        for nm in d1.keys() - d2.keys():
            yield (nm, "deleted", "", "")
        for nm in d2.keys() - d1.keys():
            yield (nm, "added", "", "")
        
        for nm in sorted(d1.keys() & d2.keys()):
        
            if x in ('rules', 'functions'):
                
                def get_canonical_expr(item):
                    return re.sub(
                        # remove schema prefixes
                        (r'(ifc\w+\.)(ifc\w+)'), '\\2',
                        # join and lowercase
                        "".join(item.flat).lower()
                    )
                    
                if get_canonical_expr(d1[nm]) != get_canonical_expr(d2[nm]):
                    yield (nm, "modifications", "", "")
                    
                continue
                
            assert type(d1[nm]) == type(d2[nm])
            
            if not eq(d1[nm], d2[nm]):
                if isinstance(d1[nm], (express_parser.SelectType, express_parser.EnumerationType)):
                    v1 = set(map(str, d1[nm].values))
                    v2 = set(map(str, d2[nm].values))
                    for i, lbl in enumerate(("additions", "deletions")):
                        vs = [v1, v2]
                        if i:
                            vs = vs[::-1]
                        for inm in vs[1] - vs[0]:
                            yield (nm, lbl, "item", inm)
                    
                    item_deprs = dict(t[1:] for t in get_notice(nm, subs="Items") if t[0] == s1_ver)
                    for inm in v2:
                        if inm in item_deprs:
                            postfix = item_deprs[inm]
                            if postfix:
                                postfix = f". {postfix}"
                            yield (nm, "modifications", f"item {inm}", f"Is now deprecated{postfix}")

                else:
                    yield (nm, "modifications", "type", f'Changed from\n"{d1[nm]}"\nto\n"{d2[nm]}"')
                    
            if x == 'simpletypes':
                w1 = dict(s0.schema.types[nm].where)
                w2 = dict(s1.schema.types[nm].where)
                
                for i, lbl in enumerate(("additions", "deletions")):
                    ws = [w1, w2]
                    if i:
                        ws = ws[::-1]
                    for wnm in ws[1].keys() - ws[0].keys():
                        yield (nm, lbl, "where rule", wnm)
                        
                for wnm in (set(w1.keys()) & set(w2.keys())):    
                    if w1 != w2:
                        yield (nm, "modifications", "where rule definition", f'Changed from\n"{w1}"\nto\n"{w2}"')
                        

    s0e, s1e = map(lambda m: set(map(str, m.schema.entities.keys())), (s0, s1))
    for nm in s0e - s1e:
        yield (nm, "deleted", "", rename_messages.get(s1_ver, {}).get(nm, ""))
    for nm in s1e - s0e:
        yield (nm, "added", "", "")
    for nm in s0e & s1e:
        yield from compare(depr0, depr1, s0.schema.entities[nm], s1.schema.entities[nm], s1_ver)

def pset_to_dict(D):
    appl = sorted(set([x.text for x in D.child_with_tag("ApplicableClasses").children]))

    props = []
    for p in (D.child_with_tag("PropertyDefs") or D.child_with_tag("QtoDefs")).children:
        pname = p.child_with_tag("Name").text
        if p.tag == "PropertyDef":
            pnode = p.child_with_tag("PropertyType").children[0]
            ptype = pnode.tag
            ptype = ptype.replace("TypeProperty", "").replace("Value", "").lower()
            try:
                if ptype in ("single", "bounded"):
                    pvalue = pnode.children[0].attributes['type']
                elif ptype == "enumerated":
                    pvalue = pnode.children[0].attributes['name']
                elif ptype == "reference":
                    pvalue = pnode.attributes['reftype']
                elif ptype == "list":
                    pvalue = pnode.children[0].children[0].attributes['type']
                elif ptype == "table":
                    pvalue = " ".join([pnode.child_with_tag(x).children[0].attributes["type"] for x in ["DefiningValue", "DefinedValue"]])
                elif ptype == "typesimpleproperty":
                    # weird 2x3 anomaly
                    ptype = "reference"
                    pvalue = pnode.children[0].attributes['type']
                elif ptype == "typecomplexproperty":
                    ptype = "complex"
                    pvalue = pnode.attributes['name']
                else:
                    raise RuntimeError(f"{ptype} not implemented")
            except:
                pvalue = "invalid"
        else:
            ptype = p.child_with_tag("QtoType").text
            pvalue = None
            if not ptype:
                ptype = "invalid"
        props.append((pname, " ".join(filter(None, (ptype, pvalue)))))
        
    return {
        'name': D.child_with_tag("Name").text,
        'applicability': appl,
        'properties': props
    }

def compare_pset(fn0, fn1):
    import xml_dict
    d0d1 = list(map(pset_to_dict, map(xml_dict.xml_node.strip_namespaces, map(xml_dict.read, (fn0, fn1)))))
    
    pset = d0d1[0]['name']
    
    appl0, appl1 = map(set, map(operator.itemgetter('applicability'), d0d1))
    for nm in appl0 - appl1:
        yield (pset, "deleted", "applicability", nm)
    for nm in appl1 - appl0:
        yield (pset, "added", "applicability", nm)
 
    prop0, prop1 = map(dict, map(operator.itemgetter('properties'), d0d1))
    for nm in prop0.keys() - prop1.keys():
        yield (pset, "deleted", "property", nm)
    for nm in prop1.keys() - prop0.keys():
        yield (pset, "added", "property", nm)
    for nm in prop0.keys() & prop1.keys():
        v0, v1 = prop0[nm], prop1[nm]
        if v0 != v1:
            yield (pset, "modifications", f"property {nm}", f'Changed from\n"{v0}"\nto\n"{v1}"')

def compare_psets(dir0, dir1):
    p0, p1 = map(set, map(sorted, map(lambda li: [s.lower() for s in li], map(os.listdir, (dir0, dir1)))))
    case0, case1 = ({fn.lower():fn for fn in os.listdir(d)} for d in (dir0, dir1))
    
    for nm in p0 - p1:
        yield (case0[nm][:-4], "deleted", "", "")
    for nm in p1 - p0:
        yield (case1[nm][:-4], "added", "", "")
    for nm in p0 & p1:
        yield from compare_pset(os.path.join(dir0, case0[nm]), os.path.join(dir1, case1[nm]))
            

if __name__ == "__main__":
    
    if len(sys.argv) == 2:    
        repo_dir = sys.argv[1]
    elif len(sys.argv) == 3:
        files = sys.argv[1:]
        
    build_rename_messages()

    if repo_dir:
        d = os.path.join(repo_dir, "reference_schemas")
        names = [
                "ifc4", "IFC4_ADD2_TC1.exp", "deprecated_entities_Ifc4.0.2.2.json", "psd_IFC4_ADD2_TC1",
        ]
        
        if not is_iso:
            names = ["ifc23", "IFC2X3_TC1.exp", "deprecated_entities_Ifc2.3.0.1.json", "psd_IFC2x3"] + names

            names += [
                # no IfcDoc branch for 4x1
                "ifc41", "IFC4x1.exp", "deprecated_entities_Ifc4.0.2.2.json", "psd_IFC4x1",
                "ifc42", "IFC4x2.exp", "deprecated_entities_Ifc4.2.0.1.json", "psd_IFC4x2"
            ]
            
        files = list(map(functools.partial(os.path.join, d), names))
        files += [
            "ifc43", 
            "IFC.exp",
            "deprecated_entities.json",
            "psd",
        ]

    specs = [[files[i], express_parser.parse(files[i+1]), *files[i+2:i+4]] for i in range(0, len(files), 4)]
    
    for (ver_a, schema_a, depr_a, psd_a), (ver_b, schema_b, depr_b, psd_b) in zip(specs[:-1], specs[1:]): 
        differences = sorted(compare_schemas(schema_a, depr_a, schema_b, depr_b, ver_b)) \
            + sorted(compare_psets(psd_a, psd_b))
            
        schema_name = schema_b.schema.name.replace("X", ".")
        
        changes_by_schema.append((schema_name, differences))
        
        for ty, changes in itertools.groupby(differences, key=operator.itemgetter(0)):
            changes_by_type[ty][schema_name] = [x[1:] for x in changes]
    
    json.dump(changes_by_schema, open("changes_by_schema.json", "w"), indent=2)
    json.dump(changes_by_type, open("changes_by_type.json", "w"), indent=2)
