import argparse
import json
import logging
import re
from collections import defaultdict, namedtuple
from datetime import datetime
from pathlib import Path

from tqdm import tqdm

from version import schema_date, version_tuple

from .util.name_improve import AGGREGATION_BOUND, definition_improve, name_improve
from .util.xmi_document import missing_markdown, xmi_document

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = REPO_ROOT / "schemas" / "ifc4x3_add2.uml"
DEFAULT_OUTPUT = REPO_ROOT / "output" / "bsdd"

TOP = "IfcRoot"
ANCHORS = (
    "IfcObject",
    "IfcContext",
    "IfcMaterial",
    "IfcCoordinateOperation",
    "IfcCoordinateReferenceSystem",
    "IfcStructuralLoad",
)
MATERIAL_CLASSES = {"IfcMaterial", "IfcConstructionMaterialResource"}

DOCS_URL = "https://standards.buildingsmart.org/IFC/RELEASE/IFC%s/HTML/"

CHAR_LIMIT = 50
DEPRECATED_STATUS = "Inactive"
PREDEFINED_TYPE = "PredefinedType"
ENUM_FILLERS = ("USERDEFINED", "NOTDEFINED")
DATA_TYPES = {"string": "String", "real": "Real", "number": "Real", "integer": "Integer", "boolean": "Boolean"}
PROPERTY_KINDS = {
    "PropertySingleValue": "Single",
    "PropertyEnumeratedValue": "Single",
    "PropertyBoundedValue": "Range",
    "PropertyReferenceValue": "Complex",
    "PropertyListValue": "List",
    "PropertyTableValue": "Complex",
}

VALUE_EXPLANATION = re.compile(r":\s*[A-Z]{2,}.*")
ANNOTATABLE_MIN_LEN = 4

SINGLE_VALUE_NOTE = (
    "Technical note: in IFC this property takes '%s' as value. Such objects are not included in bSDD "
    "for simplicity reason. IFC also doesn't enforce particular units, but recommends using metric SI "
    "units (metre, kilogram, etc.). Read the IFC documentation for more information."
)
REFERENCE_NOTE = (
    "Technical note: this is a specific property from IFC that takes as its value a reference to %s. "
    "Read the IFC documentation for more information."
)
TABLE_NOTE = (
    "Technical note: this is a specific property from IFC that takes a table as its value. That table "
    "has two columns (lists), mapping from the values in one list to the values in the other. Read the IFC "
    "documentation for more information."
)
PREDEFINED_TYPE_NOTE = (
    "Technical note: Because this class is a 'Predefined Type' in IFC, meaning a specialisation of its "
    "parent class, in IFC it should be represented by the parent class."
)


def entity_tree(entities):
    supertype_of = {e.name: e.meta["supertypes"][0] for e in entities if e.meta.get("supertypes")}
    children_of = defaultdict(set)
    for child, parent in supertype_of.items():
        children_of[parent].add(child)
    return supertype_of, dict(children_of)


def descendants(root, children_of):
    found, stack = set(), [root]
    while stack:
        name = stack.pop()
        if name not in found:
            found.add(name)
            stack.extend(children_of.get(name, ()))
    return found


def spine_to_top(name, supertype_of, top=TOP):
    spine = []
    while name in supertype_of:
        name = supertype_of[name]
        spine.append(name)
    return spine if spine and spine[-1] == top else []


def in_anchor_cones(anchors, entity_names, supertype_of, children_of):
    scope = set()
    for anchor in anchors:
        if anchor not in entity_names:
            logging.warning("Anchor %s does not exist in this schema; skipped.", anchor)
            continue
        scope |= descendants(anchor, children_of) | set(spine_to_top(anchor, supertype_of))
    return scope


class schema_items:
    def __init__(self, xmi_doc):
        self.entities, self.psets, self.enumerations, self.item_by_id = [], [], {}, {}
        for item in tqdm(list(xmi_doc), desc="Collecting items from XMI"):
            self.item_by_id[item.id] = item
            if item.type == "ENTITY":
                self.entities.append(item)
            elif item.type in ("ENUM", "PENUM"):
                self.enumerations[item.name] = item
            elif item.type == "PSET":
                self.psets.append(item)


def is_deprecated(item):
    markdown = item.markdown
    return bool(markdown) and "DEPRECAT" in markdown


def to_str(s):
    if isinstance(s, str):
        return s
    if s and not isinstance(s, missing_markdown):
        logging.warning("Expected a string, skipped: %r", s)
    return ""


def build_element_index(xmi):
    index = {}
    uml_types = ("uml:Class", "uml:DataType", "uml:Enumeration")
    for uml_type in uml_types:
        for element in xmi.by_tag_and_type["packagedElement"][uml_type]:
            index.setdefault(element.name, element)
    for uml_type in uml_types:
        for element in xmi.by_tag_and_type["packagedElement"][uml_type]:
            index.setdefault(AGGREGATION_BOUND.split(element.name)[0], element)
    return index


def base_generalization(element, xmi):
    links = element / "generalization"
    while links:
        element = xmi.by_id[links[0].resolve("general")]
        links = element / "generalization"
    return element


def class_definition(item):
    return definition_improve(to_str(item.markdown_content))


def entity_classes(entities, scope, material_classes):
    classes, class_by_entity_id = {}, {}
    for item in tqdm(entities, desc="Building classes"):
        if item.name not in scope:
            continue
        supertypes = item.meta.get("supertypes") or []
        entry = {
            "Parent": supertypes[0] if supertypes else "",
            "Definition": class_definition(item),
            "Name": name_improve(item.name),
            "Package": to_str(item.package),
            "ClassType": "Material" if item.name in material_classes else "Class",
            "Deprecated": is_deprecated(item),
            "Psets": {},
        }
        classes[item.name] = entry
        class_by_entity_id[item.id] = entry
    return classes, class_by_entity_id


def predefined_type_enum(entity, enumerations, xmi):
    attributes = [c for c in entity.children if c.name == PREDEFINED_TYPE]
    if not attributes:
        return None
    type_node = xmi.by_id[attributes[0].node.resolve("type")]
    return enumerations.get(type_node.name)


def expand_predefined_types(schema, classes, class_by_entity_id, xmi):
    for entity in tqdm(schema.entities, desc="Expanding predefined types"):
        if entity.name not in classes:
            continue
        enum = predefined_type_enum(entity, schema.enumerations, xmi)
        if enum is None:
            continue
        parent = classes[entity.name]
        parent["Psets"].setdefault("Attributes", {})[PREDEFINED_TYPE] = predefined_type_property(entity, enum)
        for literal in enum.children:
            if literal.name in ENUM_FILLERS:
                continue
            child = {
                "Parent": entity.name,
                "Definition": definition_improve(to_str(literal.markdown)),
                "Description": PREDEFINED_TYPE_NOTE,
                "Name": name_improve(literal.name),
                "Package": to_str(entity.package),
                "ClassType": "Class",
                "Deprecated": parent["Deprecated"] or is_deprecated(literal),
                "Psets": {},
                "PredefinedPin": literal.name,
            }
            classes[entity.name + literal.name] = child
            class_by_entity_id[literal.id] = child


def predefined_type_property(entity, enum):
    package = to_str(entity.package)
    return {
        "Type": "string",
        "Name": name_improve(PREDEFINED_TYPE),
        "Definition": "Predefined type of %s." % entity.name,
        "Kind": "Single",
        "Package": package,
        "Values": value_entries([c.name for c in enum.children], "", package),
        "ValuesPerClass": True,
    }


def property_entry(name, markdown, type_name, kind, package, values=None, description=None, deprecated=False):
    entry = {
        "Type": type_name,
        "Name": name_improve(name),
        "Definition": VALUE_EXPLANATION.sub("...", definition_improve(to_str(markdown))),
        "Kind": kind,
        "Package": package,
        "Deprecated": deprecated,
    }
    if description:
        entry["Description"] = description
    if values:
        entry["Values"] = value_entries(values, markdown, package)
    return entry


def value_entries(values, markdown, package):
    text = to_str(markdown)
    entries = []
    for value in values:
        sentence = re.search(r"[^.;!,]*%s[^.;!,]*" % re.escape(value), text, re.IGNORECASE)
        description = definition_improve(sentence.group(0).strip()) if sentence else name_improve(value)
        entries.append({"Value": value, "Description": description, "Package": package})
    return entries


def technical_note(prop_type, ifc_type, type_name):
    if prop_type == "PropertySingleValue" and ifc_type != "IfcText":
        return SINGLE_VALUE_NOTE % ifc_type
    if prop_type == "PropertyReferenceValue":
        return REFERENCE_NOTE % type_name
    if prop_type == "PropertyTableValue":
        return TABLE_NOTE
    return None


def pset_property(pset, attr, type_spec, element_index, xmi, deprecated):
    package = to_str(pset.package)
    if pset.name.startswith("Qto"):
        return property_entry(attr.name, attr.markdown, "real", "Single", package, deprecated=deprecated)
    prop_type, type_args = type_spec
    # table values carry {Defining, Defined}; the entered value is the Defined column
    ifc_type = type_args.get("Defined") or next(iter(type_args.values()))
    kind = PROPERTY_KINDS[prop_type]
    if prop_type == "PropertyEnumeratedValue":
        literals = [x.name for x in element_index[ifc_type] / "ownedLiteral"]
        return property_entry(attr.name, attr.markdown, ifc_type, kind, package,
                              values=literals, deprecated=deprecated)
    element = element_index.get(ifc_type)
    if element is None:
        logging.warning("%s.%s: type %s not found in XMI; skipping", pset.name, attr.name, ifc_type)
        return None
    type_name = base_generalization(element, xmi).name
    return property_entry(attr.name, attr.markdown, type_name, kind, package,
                          description=technical_note(prop_type, ifc_type, type_name), deprecated=deprecated)


def attach_pset_properties(schema, class_by_entity_id, element_index, xmi):
    for pset in tqdm(schema.psets, desc="Attaching property sets"):
        targets = [class_by_entity_id[ref] for ref in pset.meta.get("refs") or [] if ref in class_by_entity_id]
        if not targets:
            logging.warning("%s: no published applicability target; skipped", pset.name)
            continue
        pset_deprecated = is_deprecated(pset)
        for attr, (_, type_spec) in zip(pset.children, pset.definition, strict=True):
            prop = pset_property(pset, attr, type_spec, element_index, xmi,
                                 deprecated=pset_deprecated or is_deprecated(attr))
            if prop is None:
                continue
            code = AGGREGATION_BOUND.split(attr.name)[0]
            for entry in targets:
                entry["Psets"].setdefault(pset.name, {})[code] = prop


def attribute_property(entity, attr, schema, xmi):
    type_item = schema.item_by_id.get(attr.node.resolve("type"))
    if type_item is None or type_item.type not in ("TYPE", "ENUM"):
        return None
    package = to_str(entity.package)
    deprecated = is_deprecated(attr)
    if type_item.type == "TYPE":
        type_name = base_generalization(xmi.by_id[type_item.id], xmi).name.lower()
        return property_entry(attr.name, attr.markdown, type_name, "", package, deprecated=deprecated)
    literals = [c.name for c in type_item.children]
    return property_entry(attr.name, attr.markdown, type_item.name, "", package,
                          values=literals, deprecated=deprecated)


def attach_entity_attributes(schema, classes, xmi):
    for entity in tqdm(schema.entities, desc="Attaching entity attributes"):
        target = classes.get(entity.name) or classes.get(entity.name.removesuffix("Type"))
        if target is None:
            continue
        for attr in entity.children:
            if attr.name == PREDEFINED_TYPE:
                continue
            prop = attribute_property(entity, attr, schema, xmi)
            if prop is not None:
                target["Psets"].setdefault("Attributes", {})[AGGREGATION_BOUND.split(attr.name)[0]] = prop


def annotation_codes(classes):
    codes = set(classes)
    for content in classes.values():
        for pset_code, properties in content["Psets"].items():
            codes.add(pset_code)
            for prop_code, prop in properties.items():
                codes.add(prop_code)
                codes.update(value["Value"] for value in prop.get("Values", ()))
    return {code for code in codes if len(code) >= ANNOTATABLE_MIN_LEN}


Markup = namedtuple("Markup", ["strip", "wrap"])


def annotation_pattern(codes, italic_codes):
    def alternation(cs):
        return "|".join(re.escape(c) for c in sorted(cs, key=len, reverse=True))
    return Markup(strip=re.compile(r"_(%s)_" % alternation(italic_codes)),
                  wrap=re.compile(r"\b(%s)\b" % alternation(codes)))


# labels stay plain text: bSDD stores [[..]] literally (live has "[[1000]]")
def strip_italics(s, pattern):
    return pattern.strip.sub(lambda m: m.group(1), to_str(s))


def wrap_wikilinks(s, pattern):
    return pattern.wrap.sub(lambda m: "[[%s]]" % m.group(0), strip_italics(s, pattern))


def pot_entry(msgid, msgstr, package):
    return {"msgid": msgid, "msgstr": msgstr, "package": package}


def class_property_code(prop_code, pset_code):
    if len(prop_code) + len(pset_code) < CHAR_LIMIT:
        return prop_code + "_from_" + re.sub("Pset_|Qto_", "", pset_code)
    # acronym form: these pairs collide under the squeeze and match live bSDD codes
    if prop_code in ("AdjustmentDesignation", "IsCurrentTolerancePositiveOnly") and pset_code in (
        "Pset_ProtectiveDeviceTrippingUnitTimeAdjustment",
        "Pset_ProtectiveDeviceTrippingUnitCurrentAdjustment",
        "Pset_ProtectiveDeviceTrippingFunctionGCurve",
        "Pset_ProtectiveDeviceTrippingFunctionICurve",
    ):
        return prop_code + "_from_..." + "".join(ch for ch in pset_code if ch.isupper())
    suffix = re.sub("Pset_|Qto_", "", pset_code)
    half = (CHAR_LIMIT - len(prop_code) - len("_from_") - len("...")) // 2
    return prop_code + "_from_" + suffix[:half] + "..." + suffix[len(suffix) - half:]


def self_and_ancestors(code, classes):
    while code in classes:
        yield classes[code]
        code = classes[code]["Parent"]


def docs_url(version):
    return DOCS_URL % version.replace(".", "_")


def documentation_url(code, content, version):
    return "%slexical/%s.htm" % (docs_url(version), content["Parent"] if content.get("PredefinedPin") else code)


def render_dictionary(classes, pattern, version):
    rendered_classes, properties, to_translate = [], {}, []
    for code, content in tqdm(classes.items(), desc="Rendering"):
        cls = render_class(code, content, classes, pattern, to_translate, version)
        cls["ClassProperties"] = render_class_properties(code, classes, pattern, properties, to_translate)
        rendered_classes.append(cls)
    return rendered_classes, list(properties.values()), to_translate


def render_class(code, content, classes, pattern, to_translate, version):
    definition = wrap_wikilinks(content["Definition"], pattern)
    cls = {
        "Code": code[:CHAR_LIMIT],
        "Name": content["Name"],
        "Definition": definition,
        "ClassType": content["ClassType"],
        "ClassProperties": [],
    }
    cls["DocumentReference"] = documentation_url(code, content, version)
    if content["Deprecated"]:
        cls["Status"] = DEPRECATED_STATUS
    if content["Parent"] in classes:
        cls["ParentClassCode"] = content["Parent"]
    if "Description" in content:
        cls["Description"] = content["Description"]
        to_translate.append(pot_entry(cls["Code"] + "_DESCRIPTION", content["Description"], content["Package"]))
    to_translate.append(pot_entry(cls["Code"], cls["Name"], content["Package"]))
    to_translate.append(pot_entry(cls["Code"] + "_DEFINITION", definition, content["Package"]))
    return cls


def render_class_properties(code, classes, pattern, properties, to_translate):
    rendered, seen = [], {}
    for ancestor in self_and_ancestors(code, classes):
        for pset_code, pset_properties in ancestor["Psets"].items():
            for prop_code, prop in pset_properties.items():
                short = prop_code[:CHAR_LIMIT]
                cp_code = class_property_code(short, pset_code)[:CHAR_LIMIT]
                if cp_code in seen:
                    if seen[cp_code] != (short, pset_code):
                        logging.warning("ClassProperty Code collision on %s: %s from %s dropped", code, cp_code, pset_code)
                    continue
                seen[cp_code] = (short, pset_code)
                cp = {"PropertyCode": short, "Code": cp_code, "PropertySet": pset_code[:CHAR_LIMIT]}
                if prop.get("ValuesPerClass"):
                    cp["AllowedValues"] = render_allowed_values(prop["Values"], short, pattern, to_translate)
                rendered.append(cp)
                render_property_once(short, prop, pattern, properties, to_translate)
    pin = classes[code].get("PredefinedPin")
    if pin:
        for cp in rendered:
            if cp["PropertyCode"] == PREDEFINED_TYPE:
                cp["AllowedValues"] = [{"Code": pin[:CHAR_LIMIT], "Value": pin, "Description": name_improve(pin)}]
    return rendered


def render_allowed_values(values, prop_code, pattern, to_translate):
    rendered = []
    for value in values:
        description = strip_italics(value["Description"], pattern)
        rendered.append({"Code": value["Value"][:CHAR_LIMIT], "Value": value["Value"], "Description": description})
        to_translate.append(pot_entry(prop_code + "_" + value["Value"], description, value["Package"]))
    return rendered


def render_property_once(code, prop, pattern, properties, to_translate):
    # the first class to render a shared property decides its pot file
    if code in properties:
        return
    definition = wrap_wikilinks(prop["Definition"], pattern)
    rendered = {
        "Code": code,
        "Name": prop["Name"],
        "Definition": definition,
        "PropertyValueKind": prop["Kind"],
    }
    if prop.get("Deprecated"):
        rendered["Status"] = DEPRECATED_STATUS
    if prop.get("Values") and not prop.get("ValuesPerClass") and prop["Type"].lower() != "boolean":
        rendered["AllowedValues"] = render_allowed_values(prop["Values"], code, pattern, to_translate)
    if prop.get("Description"):
        rendered["Description"] = wrap_wikilinks(prop["Description"], pattern)
        to_translate.append(pot_entry(code + "_DESCRIPTION", rendered["Description"], prop["Package"]))
    data_type = data_type_for(prop["Type"])
    if data_type:
        rendered["DataType"] = data_type
    properties[code] = rendered
    to_translate.append(pot_entry(code, prop["Name"], prop["Package"]))
    to_translate.append(pot_entry(code + "_DEFINITION", definition, prop["Package"]))


def data_type_for(type_name):
    if type_name.lower() in DATA_TYPES:
        return DATA_TYPES[type_name.lower()]
    if type_name.startswith("PEnum_") or type_name.endswith("Enum"):
        return "String"
    return None


def class_property_order(indexed):
    index, cp = indexed
    if cp["PropertySet"] == "Attributes":
        return (cp["PropertySet"], 0, index, "")
    return (cp["PropertySet"], 1, 0, cp["PropertyCode"])


def sort_for_emit(classes, props):
    for cls in classes:
        cls["ClassProperties"] = [cp for _, cp in sorted(enumerate(cls["ClassProperties"]), key=class_property_order)]
    classes.sort(key=lambda c: c["Code"])
    for prop in props:
        prop.get("AllowedValues", []).sort(key=lambda v: v["Value"])
    props.sort(key=lambda p: p["Code"])


def bsdd_document(classes, props, version):
    return {
        "ModelVersion": "2.0",
        "OrganizationCode": "buildingsmart",
        "DictionaryCode": "ifc",
        "DictionaryName": "IFC",
        "DictionaryVersion": version,
        "LanguageIsoCode": "EN",
        "LanguageOnly": False,
        "UseOwnUri": False,
        "License": "CC BY-ND 4.0",
        "LicenseUrl": "https://creativecommons.org/licenses/by-nd/4.0/legalcode",
        "MoreInfoUrl": docs_url(version),
        "QualityAssuranceProcedure": (
            "IFC is a standardized digital description of built environment created by buildingSMART "
            "International and its community members. For more information read ISO 16739 and IFC "
            "schema documentation."
        ),
        "QualityAssuranceProcedureUrl": "https://technical.buildingsmart.org/standards/ifc/",
        "ReleaseDate": datetime.strptime(schema_date, "%Y%m%d").strftime(r"%Y-%m-%d"),
        "Classes": classes,
        "Properties": props,
    }


def dictionary(doc):
    doc.should_translate_pset_types = False
    schema = schema_items(doc)

    supertype_of, children_of = entity_tree(schema.entities)
    entity_names = {e.name for e in schema.entities}
    scope = in_anchor_cones(ANCHORS, entity_names, supertype_of, children_of)

    classes, class_by_entity_id = entity_classes(schema.entities, scope, MATERIAL_CLASSES)
    expand_predefined_types(schema, classes, class_by_entity_id, doc.xmi)
    element_index = build_element_index(doc.xmi)
    attach_pset_properties(schema, class_by_entity_id, element_index, doc.xmi)
    attach_entity_attributes(schema, classes, doc.xmi)

    version = "%s.%s" % tuple(version_tuple[:2])
    codes = annotation_codes(classes)
    schema_names = entity_names | set(schema.enumerations) | {to_str(e.package) for e in schema.entities}
    pattern = annotation_pattern(codes, schema_names | codes)
    rendered_classes, properties, to_translate = render_dictionary(classes, pattern, version)
    sort_for_emit(rendered_classes, properties)
    assert len({c["Code"] for c in rendered_classes}) == len(rendered_classes), "class Code collision after truncation"
    assert len({p["Code"] for p in properties}) == len(properties), "property Code collision after truncation"
    return bsdd_document(rendered_classes, properties, version), to_translate


def write_bsdd(doc, bsdd_dir: Path) -> None:
    document = dictionary(doc)[0]
    bsdd_dir.mkdir(parents=True, exist_ok=True)
    path = bsdd_dir / "IFC.json"
    path.write_text(json.dumps(document, indent=4, ensure_ascii=False), encoding="utf-8")
    print("-- Saved %s with %s classes and %s properties. --" % (path, len(document["Classes"]), len(document["Properties"])))


def run(doc, output_dir: Path) -> None:
    write_bsdd(doc, output_dir / "bsdd")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate the IFC bSDD dictionary (IFC.json).")
    parser.add_argument("schema", nargs="?", type=Path, default=DEFAULT_SCHEMA, help="Path to the input schema UML.")
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT, help="Directory for IFC.json.")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO)
    write_bsdd(xmi_document(str(args.schema)), args.output)


if __name__ == "__main__":
    main()
