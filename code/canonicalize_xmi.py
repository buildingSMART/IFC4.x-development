import sys
import uuid
import functools

from collections import defaultdict
from dataclasses import dataclass

from generators.util import xml_dict
from generators.util.append_xmi import XMI

fn, ofn = sys.argv[1:]
content = xml_dict.read(fn)

null_uuid = uuid.UUID(bytes=bytes([0])*16)

def recurse(fn, nd=None, stack=None):
    if nd is None: nd = content
    if stack is None: stack = []
    
    r = fn(nd, stack)
    if r is not None:
        return r

    for ch in nd.children:
        r = recurse(fn, ch, stack + [nd])
        if r is not None:
            return r

by_id = {}

@dataclass
class id_data:
    id : str
    id2 : str
    node : object
    

def id_mapping(nd, stack):
    i = nd.attributes.get(XMI.id)
    if i: by_id[i] = id_data(i, None, nd)
    
recurse(id_mapping)



ids = {}

format_uuid = lambda u: "ID_" + str(u).upper().replace("-", "_")

@functools.lru_cache(maxsize=1000)
def generate_uuid(nd):
    if nd.attributes.keys() == {XMI.id, "start", "end"}:
        # Generalization, Substitution, Dependency, ...
        return uuid.uuid5(
            generate_uuid(by_id[nd.attributes["start"]].node),
            str(generate_uuid(by_id[nd.attributes["end"]].node))
        )
        
    elif nd.tag == "ownedAttribute":
        return uuid.uuid5(
            generate_uuid(nd.parent),
            nd.attributes["name"]
        )
        
    elif nd.tag == "ownedEnd":
        return uuid.uuid5(
            generate_uuid(nd.parent),
            "end%d" % nd.parent.children.index(nd)
        )
        
    elif nd.tag == "generalization":
        return uuid.uuid5(
            generate_uuid(nd.parent),
            str(generate_uuid(by_id[nd.attributes["general"]].node))
        )
        
    elif nd.tag == "ownedRule":
        elem = [c for c in nd.children if c.tag == "constrainedElement"][0]
        supplier = by_id[by_id[elem.attributes[XMI.idref]].node.attributes["supplier"]].node.attributes["name"]
        return uuid.uuid5(
            generate_uuid(nd.parent),
            supplier
        )
    
    elif nd.tag == 'packagedElement' and len(nd.attributes.keys() & {"supplier", "client"}) == 2:
        return uuid.uuid5(
            generate_uuid(by_id[nd.attributes["supplier"]].node),
            nd.attributes[XMI.type] + ";" + str(generate_uuid(by_id[nd.attributes["client"]].node))
        )
    
    elif nd.tag == 'packagedElement' and nd.attributes[XMI.type] == "uml:Association":
        ends = [c for c in nd.children if c.tag == "ownedEnd"]
        types = sum([[cc for cc in c.children if cc.tag == "type"] for c in ends], [])
        type_names = [by_id[t.attributes[XMI.idref]].node.attributes["name"] for t in types]
        attr_names = [c.attributes.get("name", "") for c in ends]
        return uuid.uuid5(
            generate_uuid(nd.parent),
            ";".join(type_names + attr_names)
        )
    
    
    attrs = {k: v for k, v in nd.attributes.items() if k != XMI.id}
    idref = attrs.get(XMI.idref)
    if idref:
        attrs[XMI.idref] = format_uuid(generate_uuid(by_id[idref].node))
    attr_string = ";".join(":".join(kv) for kv in sorted(attrs.items()))    
    
    assert "EAID" not in attr_string
    
    if attrs.get(XMI.type) == "uml:Package":
        print(attr_string)
    
    return uuid.uuid5(
        generate_uuid(nd.parent) if nd.parent else null_uuid,
        ";".join((nd.tag, attr_string))
    )


for v in by_id.values():
    v.id2 = format_uuid(generate_uuid(v.node))
    v.node.attributes[XMI.id] = v.id2
    # print(v.id, "->", v.id2)
    

def update_refs(nd, stack):
    for k, v in list(nd.attributes.items()):
        if k != XMI.id:
            if v in by_id:
                nd.attributes[k] = by_id[v].id2
    
recurse(update_refs)

def sort_nodes(nd, stack):
    nd.attributes = {k:v for k, v in sorted(nd.attributes.items())}

recurse(sort_nodes)

cnt = defaultdict(list)
for x in by_id.values():
    cnt[x.id2].append((x.id, x.node))
    
print("Duplicates")
print("----------")

has_any = False

for vs in cnt.values():
    if len(vs) > 1:
        for v in vs:
            print(*v)
            has_any = True
        print()
        exit()
    
if not has_any: print("none")

xml_dict.serialize([content], ofn)
