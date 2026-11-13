import sys
import operator

from generators.util import xml_dict

fns = sys.argv[1:]
xds = list(map(xml_dict.read, fns))

ignored_attributes = ["targetNamespace"]

ignored_paths = {
    "schema/IfcDerivedProfileDef/complexContent/extension/sequence/Operator/attributes",
    "schema/IfcEdge/complexContent/extension/sequence/EdgeStart/attributes",
    "schema/IfcEdge/complexContent/extension/sequence/EdgeEnd/attributes",
    "schema/IfcElement/complexContent/extension/sequence/HasProjections/attributes",
    "schema/IfcElement/complexContent/extension/sequence/HasProjections/child count",
    "schema/IfcElement/complexContent/extension/sequence/HasOpenings/attributes",
    "schema/IfcElement/complexContent/extension/sequence/HasOpenings/child count",
    "schema/IfcGeometricRepresentationContext/complexContent/extension/sequence/WorldCoordinateSystem/attributes",
    "schema/IfcGeometricRepresentationSubContext-temp/complexContent/restriction/child count",
    "schema/IfcGeometricRepresentationSubContext-temp/complexContent/restriction/sequence/child count",
    "schema/IfcMirroredProfileDef/tags",
    "schema/IfcNamedUnit/complexContent/extension/sequence/Dimensions/attributes",
    "schema/IfcOpeningElement/complexContent/extension/sequence/HasFillings/attributes",
    "schema/IfcOrientedEdge-temp/complexContent/restriction/sequence/child count",
    "schema/IfcPixelTexture/complexContent/extension/Pixel/simpleType/restriction/simpleType/list/attributes",
    "schema/IfcSIUnit-temp/complexContent/restriction/sequence/tags",
    "schema/IfcSite/complexContent/extension/RefLatitude/attributes",
    "schema/IfcSite/complexContent/extension/RefLongitude/attributes",
    "schema/IfcStructuralLoadConfiguration/complexContent/extension/sequence/Locations/complexType/sequence/element/attributes",
}

def freeze(x):
    if isinstance(x, dict):
        return frozenset(x.items())
    return x
    
def ignore_attributes(x):
    return {k:v for k,v in x.items() if k not in ignored_attributes}

def compare(args, path=[]):
    tags = list(map(operator.attrgetter("tag"), args))
    attrs = list(map(ignore_attributes, map(operator.attrgetter("attributes"), args)))
    texts = list(map(str.strip, map(operator.attrgetter("text"), args)))
    
    def assert_equal(aspect, vs, abort=True):
        ke = "/".join([x.attributes.get('name') or xml_dict.strip_namespace(x.tag) for x in (path + [args[0]])] + [aspect])
        if ke in ignored_paths:
            return None
            
        if len(set(map(freeze, vs))) != 1:
            print("On", ke)
            print(aspect, "not equal: ", *vs)
            if abort:
                for x in args:
                    x.recursive_print()
                exit(1)
            return False
        return True
        # print(vs[0])
            
    if not assert_equal("tags", tags):
        return
    assert_equal("attributes", attrs)
    assert_equal("text", texts)
    
    children = list(map(operator.attrgetter("children"), args))
    child_count = list(map(len, children))
    
    assert_equal("child count", child_count, abort=min(child_count) < 1000)
    
    
    max_index = min(map(len, children))
    indices = [0 for c in children]
    
    while max(indices) < max_index:
        xs = [c[i] for c, i in zip(children, indices)]
    
        if len(path) == 0:
            tags = [x.tag for x in xs]
            names = [x.attributes.get('name') for x in xs]
            if all(names) and len(set(names)) != 1:
                to_advance = names.index(min(names, key=lambda s: ("-temp" not in s, s)))
                print("Warning, skipped", tags[to_advance], names[to_advance], "in file", to_advance)
                indices[to_advance] += 1
                continue
                
        compare(xs, path + [args[0]])
        
        indices = [i + 1 for i in indices]

compare(xds)
