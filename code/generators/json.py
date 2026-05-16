import argparse
import csv
import glob
import os
from pathlib import Path
import re
import json
import operator

from collections import defaultdict

from .util.xmi_document import xmi_document
from .util.compare_pset import read as read_psd

CODE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = CODE_DIR.parent

#@todo this may need to get revised
hierarchy = [
    ("Core data schemas", [
        ("IfcKernel", defaultdict(list)),
        ("IfcControlExtension", defaultdict(list)),
        ("IfcProcessExtension", defaultdict(list)),
        ("IfcProductExtension", defaultdict(list)), 
    ]),
    ("Shared element data schemas", [
        ("IfcSharedBldgElements", defaultdict(list)),
        ("IfcSharedBldgServiceElements", defaultdict(list)),
        ("IfcSharedComponentElements", defaultdict(list)),
        ("IfcSharedFacilitiesElements", defaultdict(list)),
        ("IfcSharedMgmtElements", defaultdict(list)),
        ("IfcSharedInfrastructureElements", defaultdict(list)),
    ]),
    ("Domain specific data schemas", [
        ("IfcArchitectureDomain", defaultdict(list)),
        ("IfcBuildingControlsDomain", defaultdict(list)),
        ("IfcConstructionMgmtDomain", defaultdict(list)),
        ("IfcElectricalDomain", defaultdict(list)),
        ("IfcHvacDomain", defaultdict(list)),
        ("IfcPlumbingFireProtectionDomain", defaultdict(list)),
        ("IfcPortsAndWaterwaysDomain", defaultdict(list)),
        ("IfcRailDomain", defaultdict(list)),
        ("IfcRoadDomain", defaultdict(list)),
        ("IfcStructuralAnalysisDomain", defaultdict(list)),
        ("IfcStructuralElementsDomain", defaultdict(list)),
    ]),
    ("Resource definition data schemas", [
        ("IfcActorResource", defaultdict(list)),
        ("IfcApprovalResource", defaultdict(list)),
        ("IfcConstraintResource", defaultdict(list)),
        ("IfcCostResource", defaultdict(list)),
        ("IfcDateTimeResource", defaultdict(list)),
        ("IfcExternalReferenceResource", defaultdict(list)),
        ("IfcGeometricConstraintResource", defaultdict(list)),
        ("IfcGeometricModelResource", defaultdict(list)),
        ("IfcGeometryResource", defaultdict(list)),
        ("IfcMaterialResource", defaultdict(list)),
        ("IfcMeasureResource", defaultdict(list)),
        ("IfcPresentationAppearanceResource", defaultdict(list)),
        ("IfcPresentationDefinitionResource", defaultdict(list)),
        ("IfcPresentationOrganizationResource", defaultdict(list)),
        ("IfcProfileResource", defaultdict(list)),
        ("IfcPropertyResource", defaultdict(list)),
        ("IfcQuantityResource", defaultdict(list)),
        ("IfcRepresentationResource", defaultdict(list)),
        ("IfcStructuralLoadResource", defaultdict(list)),
        ("IfcTopologyResource", defaultdict(list)),
        ("IfcUtilityResource", defaultdict(list)),
    ]),
]

def format_TypePropertySingleValue(prop):
    try:
        return prop["_children"][0]["@type"]
    except KeyError as e:
        return ""

def format_TypePropertyEnumeratedValue(prop):
    name = prop['_children'][0].get('@name', '')
    items = map(operator.itemgetter("#text"), prop["_children"][0]["_children"])
    return f"{name}({', '.join(items)})"

def format_TypePropertyTableValue(prop):
    return "/".join((
        child_by_tag(prop, "DefinedValue")["_children"][0]["@type"],
        child_by_tag(prop, "DefiningValue")["_children"][0]["@type"]
    ))

def format_TypePropertyReferenceValue(prop):
    return prop["@reftype"]

def format_TypePropertyListValue(prop):
    return prop["_children"][0]["_children"][0]["@type"]

def format_TypeComplexProperty(prop):
    return " ".join(map(lambda n: child_by_tag(n, "Name")["#text"], prop["_children"]))

format_TypePropertyBoundedValue = format_TypePropertySingleValue

def get_schema(name):
    for cat, schemas in hierarchy:
        for schema_name, members in schemas:
            if schema_name == name: return members

# remove trailing semi-colon if any
trailing_semi = lambda s: s[:-1] if s.endswith(";") else s

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate IFC bSDD export files.")
    parser.add_argument("schema", type=Path, help="Path to the input schema XML.")
    parser.add_argument("psets", type=Path, help="Path to the input pset XML files.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=REPO_ROOT / "output" / "structure.json",
        help="Output directory for generated bSDD files.",
    )
    args = parser.parse_args()

    xmi_doc = xmi_document(args.schema)

    entity_to_package = {}
    supertype = {}
    subtypes = defaultdict(list)
    roots = []
    attributes = {}
    definitions = {}
    resource_to_package = {}
    psets = {}
    deprecated_entities = []
    abstract_entities = []
    type_values = {}
    where_clauses = {}


    for item in xmi_doc:
        item_package = item.package
        if item.package == "propertytypes":
            # @todo move these in the XMI
            item_package = "IfcSharedBldgElements"

        if get_schema(item_package) is None:
            print(f"Warning: for {item.name} package {item_package} is not registered")
            continue
        
        if item.type == "ENTITY":
        
            if "deprecated" in ((c|"body").text.lower() for c in (item.node/"ownedComment")):
                deprecated_entities.append(item.name)

            if item.definition.is_abstract:
                abstract_entities.append(item.name)
            
            entity_to_package[item.name] = item_package
            resource_to_package[item.name] = get_schema(item_package)
            get_schema(item_package)['Entities'].append(item.name)
            if item.definition.supertype:
                supertype[item.name] = item.definition.supertype
                subtypes[item.definition.supertype].append(item.name)
            else:
                roots.append(item.name)
                
            for a in item.definition.attributes:
                attributes[".".join((item.name, a[0]))] = ("forward", a[1])

            for nm, ty in item.definition.inverses:
                attributes[".".join((item.name, nm))] = ("inverse", ty)
                
            for nm, defi in item.definition.derived:
                parts = [nm, *defi.split(':=', 1)]
                name, type, definition = parts
                # Such as SELF\IfcNamedUnit.Dimensions
                if "SELF\\" in name:
                    name = name.split(".")[-1]
                attributes[".".join((item.name, name))] = ("derived", (type, definition))
                
        elif item.type in ("TYPE", "SELECT", "ENUM", "PENUM"):
            resource_to_package[item.name] = get_schema(item_package)
            heading = 'PropertyEnumerations' if item.type == "PENUM" else 'Types'
            get_schema(item_package)[heading].append(item.name)
            if item.type in ("SELECT",):
                type_values.setdefault(item.name, []).extend(item.definition.values)
            if item.type in ("ENUM", "PENUM"):
                type_values.setdefault(item.name, []).extend([c.name for c in item.children])

        elif item.type in ("FUNCTION", "RULE"):
            name = re.split(r"\s", item.name)[0]
            get_schema(item_package)[f"{item.type[0]}{item.type[1:].lower()}s"].append(name)

        if item.type in ("ENTITY", "TYPE", "SELECT", "ENUM", "FUNCTION", "RULE"):
            name = item.name
            if item.type in ("FUNCTION", "RULE"):
                name = re.split(r"\s", item.name)[0]
            definitions[name] = str(item.definition)

        if item.type == "ENTITY":
            where_clauses[item.name] = item.definition.where_clauses
            
            where_clauses[item.name].extend((a[0], f"UNIQUE {a[1]}") for a in item.definition.unique_clauses)
        
        if item.type == "TYPE":
            #@todo unify this with entity
            where_clauses[item.name] = [tuple(map(trailing_semi, map(str.strip, c))) for c in item.definition.constraints]
            
        if item.type == "PSET":
            if item.name.startswith("Pset"):
                get_schema(item_package)['Property Sets'].append(item.name)
            else:
                get_schema(item_package)['Quantity Sets'].append(item.name)

    def child_by_tag(node, tag):
        return [c for c in node["_children"] if c['#tag'] == tag][0]
        
    for fn in args.psets.glob("*.xml"):
        xml = read_psd(fn)
        
        psetname = child_by_tag(xml, "Name")["#text"]
        try:
            classes = list(map(operator.itemgetter("#text"), child_by_tag(xml, "ApplicableClasses")["_children"]))
        except:
            classes = []

        props = []
        definition = {
            'name': psetname,
            'applicability': classes,
            'template_type': xml.get("@templatetype", None),
            'properties': props
        }

        if xml['#tag'] == 'PropertySetDef':
            heading = 'Property Sets'
        
            for prop in child_by_tag(xml, 'PropertyDefs').get("_children", []):
                propname = child_by_tag(prop, "Name")["#text"]
                try:
                    proptypenode = child_by_tag(prop, 'PropertyType')["_children"][0]
                    proptype = proptypenode["#tag"]
                    proptypeargs = globals()[f"format_{proptype}"](proptypenode)
                    proptypeifc = f"Ifc{proptype[4:]}"
                except IndexError as e:
                    proptypeifc = "INVALID"
                
                props.append({
                    'name': propname,
                    'type': proptypeifc,
                    'data': proptypeargs
                })
                
        elif xml['#tag'] == 'QtoSetDef':
            heading = 'Quantity Sets'
            
            for prop in child_by_tag(xml, 'QtoDefs').get("_children", []):
                propname = child_by_tag(prop, "Name")["#text"]
                proptype = child_by_tag(prop, "QtoType")["#text"]
                proptype = proptype[2].upper() + proptype[3:].lower()
                proptype = f"IfcQuantity{proptype}"
                
                props.append({
                    'name': propname,
                    'data': proptype
                })
                
        else:
            raise ValueError(xml['#tag'])
        
        definition['kind'] = heading.lower().replace(" ", "_")[:-1]

        psets[psetname] = definition
            
    for cat, schemas in hierarchy:
        for schema_name, members in schemas:
            for member_names in members.values():
                member_names.sort()

    with open("inheritance_listing.txt", "w") as f:
        def do_print(k, indent=0):
            print(" " * indent + k, file=f)
            for l in sorted(subtypes[k]):
                 do_print(l, indent+1)
             
        for x in sorted(roots):
            do_print(x)

    mvd_root = REPO_ROOT / "schemas" / "mvd"
    xmi_concepts = {}
    for fp in sorted(glob.glob(str(mvd_root / "**" / "*.csv"), recursive=True)):
        rel = os.path.relpath(fp, mvd_root)
        keys = [x.split('.')[0] for x in rel.split(os.sep)]
        cur = xmi_concepts
        for k in keys[:-1]:
            cur = cur.setdefault(k, {})
        with open(fp, newline='', encoding='utf-8') as cf:
            cur[keys[-1]] = list(csv.DictReader(cf))

    json.dump({
        "entity_supertype": supertype,
        "entity_to_package": entity_to_package,
        "hierarchy": hierarchy,
        "entity_attributes": attributes,
        "entity_definitions": definitions,
        "pset_definitions": psets,
        "deprecated_entities": deprecated_entities,
        "abstract_entities": abstract_entities,
        "type_values": type_values,
        "entity_where_clauses": where_clauses,
        "xmi_concepts": xmi_concepts
    }, open(args.output, "w", encoding="utf-8"))
