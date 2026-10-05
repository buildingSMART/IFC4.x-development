from collections import defaultdict

from generators.util import xml_dict

from generators.util.append_xmi import XMI, uml_package, context as xmi_context

D = xml_dict.read("..\schemas\IFC.xml")

def recurse(fn, nd=None, stack=None):
    if nd is None: nd = D
    if stack is None: stack = []
    
    r = fn(nd, stack)
    if r is not None:
        return r

    for ch in nd.children:
        r = recurse(fn, ch, stack + [nd])
        if r is not None:
            return r

to_node = {}
to_idref = defaultdict(list)

def v(nd, stack):
    if nd.tag == "packagedElement" and "name" in nd.attributes:
        to_node[(
            nd.attributes[XMI.type],
            nd.attributes["name"]
        )] = nd
        to_node[
            nd.attributes["name"]
        ] = nd
        
    id_ = nd.attributes.get(XMI.id)
    if id_:
        to_node[id_] = nd
        
    idref = nd.attributes.get(XMI.idref)
    if idref:
        to_idref[idref].append(nd)
        
recurse(v)

superclass = {}
subclasses = defaultdict(list)

def v(nd, stack):
    if nd.tag == "packagedElement" and nd.attributes.get(XMI.type) == "uml:Class":
        gens = [ch for ch in nd.children if ch.tag == "generalization"]
        if gens:
            gen_name = to_node[gens[0].attributes['general']].attributes["name"]
            self_name = nd.attributes["name"]
            superclass[self_name] = gen_name
            subclasses[gen_name].append(self_name)
        
recurse(v)

pset_package = to_node[("uml:Package", "PropertySetsforObjects")]

to_move = []

for assoc in pset_package.children:
    members = assoc.children_with_tag("memberEnd")
    get_end = lambda e: to_node[e.attributes[XMI.idref]]
    get_typename = lambda e: to_node[e.child_with_tag("type").attributes[XMI.idref]].attributes['name']
    
    type_names = list(map(get_typename, map(get_end, members)))
    if any("PHistory" in tn for tn in type_names):
        to_move.append(assoc)

pset_package.children = [a for a in pset_package.children if a not in to_move]

perf_package = uml_package("PropertySetsforPerformance")
xmi_context.insert(pset_package.parent, perf_package)
perf_package.xml.children = to_move

xml_dict.serialize([D], "../schemas/IFC_moved.xml")
