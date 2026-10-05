import os
import glob
import json
import operator

from collections import defaultdict

from generators.util import xml_dict

enumeration_properties = {}
complex_properties = {}
pset_stereotypes = set()
qto_datatypes = set()

psets = []
qtos = []

NS_QTO = "http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd"

# @nb hard-coded filepath
spec_dir = os.path.join(os.path.dirname(__file__), "../../IFC-Specification/IFC4x3/Sections")
fns = glob.glob(os.path.join(spec_dir, "**", "*Set.xml"), recursive=True)
fn_parts = map(lambda s: s.split(os.sep), fns)
set_to_package = {pts[-2]:pts[-4] for pts in fn_parts}

prop_type_to_package = defaultdict(list)

def format_TypePropertySingleValue(package, prop):
    try:
        return prop.children[0].attributes["type"]
    except KeyError as e:
        raise ValueError("No SingleValue DataType")
        
def assign_and_validate(mapping, name, values):
    if name in mapping:
        if mapping[name] != values:
            breakpoint()
    else:
        mapping[name] = values

def format_TypePropertyEnumeratedValue(package, prop):
    name = prop.children[0].attributes['name']
    values = {
        "name": name,
        "values": sorted(set(map(operator.attrgetter("text"), prop.children[0].children)))
    }
    assign_and_validate(enumeration_properties, name, values)
    return name    
    
def format_TypePropertyTableValue(package, prop):
    return [
        prop.child_with_tag("DefinedValue").children[0].attributes["type"],
        prop.child_with_tag("DefiningValue").children[0].attributes["type"]
    ]

def format_TypePropertyReferenceValue(package, prop):
    return prop.attributes["reftype"]

def format_TypePropertyListValue(package, prop):
    return prop.children[0].children[0].attributes["type"]

def format_TypeComplexProperty(package, prop):
    name = prop.attributes['name']
    values = {
        'name': name,
        'properties': handle_property_defs(package, name, prop.children)
    }
    assign_and_validate(complex_properties, name, values)
    return name

format_TypePropertyBoundedValue = format_TypePropertySingleValue

def handle_property_defs(package, name, pdefs):
    L = []
    for prop in pdefs:
        pname = prop.child_with_tag("Name").text
        
        proptypenode = prop.child_with_tag('PropertyType').children[0]
        proptype = proptypenode.tag
        
        try:
            proptypeargs = globals()[f"format_{proptype}"](package, proptypenode)
        except Exception as e:
            print(str(e)+":", name + "." + pname)
            continue
        
        uml_type = proptype[4:]
        if not uml_type.startswith("Property"):
            uml_type = "Property" + uml_type
            
        if isinstance(proptypeargs, str):
            if proptypeargs in enumeration_properties or proptypeargs in complex_properties:
                prop_type_to_package[proptypeargs].append(package)
        
        L.append({
            'name': pname,
            'type': uml_type,
            'type_arg': proptypeargs
        })            
    return L

def get_property_definitions():
    for fn in glob.glob("../reference_schemas/psd/Pset_*.xml"):
        D = {}
        psets.append(D)
    
        xd = xml_dict.read(fn)
        D['name'] = psname = xd.child_with_tag("Name").text
        D['package'] = set_to_package[psname]
        
        try:
            D['type'] = xd.attributes['templatetype']
            
            if not D['type'].lower().startswith("pset_"):
                print(f"Templatetype {D['type']}:", psname)
                D['type'] = None
        except:
            print("No templatetype:", psname)
            D['type'] = None
               
        if D['type'] is None:
            # assume as default for now
            D['type'] = "PSET_TYPEDRIVENOVERRIDE"
            
        pset_stereotypes.add(D['type'])
               
        D['properties'] = handle_property_defs(D['package'], psname, xd.child_with_tag("PropertyDefs").children)
        
    for fn in glob.glob("../reference_schemas/psd/Qto_*.xml"):
        D = {}
        qtos.append(D)
        
        breakpoint()
        
        xd = xml_dict.read(fn)
        D['name'] = qset = xd.child_with_tag(f'{{{NS_QTO}}}Name').text
        D['package'] = set_to_package[qset]
        D['quantities'] = []
        
        for prop in xd.child_with_tag(f'{{{NS_QTO}}}QtoDefs').children:
            qname = prop.child_with_tag(f'{{{NS_QTO}}}Name').text
            qtype = prop.child_with_tag(f'{{{NS_QTO}}}QtoType').text
            
            assert qname
            assert qtype
            
            qto_datatypes.add(qtype)
        
            D['quantities'].append({
                'name': qname,
                'type': qtype,
            })

def augment_package(di):
    packages = prop_type_to_package[di['name']]
    if len(packages) == 1:
        p = packages[0]
    else:
        p = None
    r = {'package': p}
    r.update(di)
    return r

if __name__ == "__main__":
    get_property_definitions()
    json.dump({
        'enumeration_properties': list(map(augment_package, enumeration_properties.values())),
        'complex_properties': list(map(augment_package, complex_properties.values())),
        'pset_stereotypes': sorted(pset_stereotypes),
        'qto_datatypes': sorted(qto_datatypes),
        
        'property_sets': psets,
        'quantity_sets': qtos        
    }, open("pset_qto_data.json", "w"), indent=2)