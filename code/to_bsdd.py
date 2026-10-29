import os
import re
import json
import logging
import sys
from collections import defaultdict
from datetime import date
from xmi_document import xmi_document, missing_markdown
from measure_mapping import MEASURE_MAPPING
from name_improve import name_improve, definition_improve
from tqdm import tqdm


logging.basicConfig(level=logging.INFO)

try:
    fn = sys.argv[1]
    try:
        output_dir = sys.argv[2]
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    logging.warning("Usage: python to_bsdd.py <schema.xml> <output_dir>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
xmi_doc.should_translate_pset_types = False

bsdd_excluded_entites = os.path.abspath(os.path.join(os.path.dirname(__file__), ".", "bsdd_excluded_entites.json"))
with open(bsdd_excluded_entites, "r", encoding="utf-8") as file:
    excluded_entites = json.load(file)
# WHILE ALLOW:  IfcRoot, IfcLightSource, IfcStructuralLoad, IfcStructuralLoadLinearForce,
# IfcStructuralLoadPlanarForce, IfcStructuralLoadSingleForce, IfcStructuralLoadStatic,
# IfcStructuralLoadTemperature

CHAR_LIMIT = 50

TYPE_TO_VALUES = {
    # 'boolean': ["TRUE","FALSE"],
    "logical": ["TRUE", "FALSE", "UNKNOWN"],
}

### shows the schema name if needed (e.g. IFC4X3_ADD2)
# schema_name = xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Package"][0]\
# .name.replace("exp", "").upper()
# schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
# schema_name = re.sub(r"_+", "_", schema_name)
# schema_name = schema_name.strip('_')


def yield_parents(node):
    """Find all the parent elements if available"""
    yield node
    if node.parentNode:
        yield from yield_parents(node.parentNode)


def get_path(xmi_node):
    """Find the element's path in the XML tree"""
    nodes = list(yield_parents(xmi_node.xml))

    def get_name(n):
        """Find element's name in the XML"""
        if n.attributes:
            v = n.attributes.get("name")
            if v:
                return v.value

    node_names = [get_name(n) for n in nodes]
    return node_names[::-1]


# included_packages = set(("IFC 4.2 schema (13.11.2019)", "Common Schema",
# "IFC Ports and Waterways", "IFC Road", "IFC Rail - PSM"))

# def skip_by_package(element):
#     return not (set(get_path(xmi_doc.by_id[element.idref])) & included_packages)

def to_str(s):
    """Turn to string in case it finds a defaultdict or similar"""
    if isinstance(s, str):
        return s
    elif isinstance(s, defaultdict):
        if len(dict(s)) == 0:
            return ""
        else:
            logging.warning("Skipped the term, default dict: %s", str(s))
            return ""
    elif isinstance(s, missing_markdown):
        logging.warning("Skipped the term, missing markdown in: %s", str(s))
        return ""
    elif isinstance(s, dict):
        if not s:
            logging.warning("Empty dictionary: %s", s)
            return ""
        else:
            logging.warning("Unempty dictionary passed as a value: %s", s)
            return str(s)
    else:
        logging.warning("Skipped the term, unknown problem in: %s", str(s))
        return ""


def quote(s):
    """Add quotation around certain words."""
    return '"%s"' % to_str(s)


def annotate(s, uni_codes):
    """Add double brackets [[...]] around certain words."""
    return re.sub(uni_codes, lambda match: "[[%s]]" % match.group(0), to_str(s))


def generalization(pe):
    """Finds a partent object if possible"""
    try:
        P = xmi_doc.xmi.by_id[(pe | "generalization").general]
    except:
        P = None
    if P:
        return generalization(P)
    else:
        return pe


def need_brackets(s):
    """Verify if that name should be annotated with brackets in other definitions.
    The criteria: minimum 4 letters (skip 'ABC')."""
    if len(s) >= 4:
        return True
    else:
        return False
    # and at least 2 capital letters (skip 'Width' etc.).
    # if re.findall(r'\b(?:[a-zA-Z]*[A-Z]){2,}[a-zA-Z]*\b', s):
    #     return True


def list_ancestors(name, full_list, ancestor_list):
    """traverse the list of hierarchy to find all the parents of this object"""
    if not ancestor_list:
        ancestor_list = []
    try:
        ancestor = full_list[name]["Parent"]
    except KeyError:
        logging.warning("The entity %s not found in the IFC.", name)
    if ancestor:
        if ancestor in full_list:
            ancestor_list.append(ancestor)
            list_ancestors(ancestor, full_list, ancestor_list)
        else:
            # TODO handle IfcMaterialDefinition, IfcPreDefinedPropertySet
            logging.warning("Ancestor of %'s' not found in the IFC.", ancestor)
    return ancestor_list


def filter_concepts(di):
    """Skip certain concepts to reduce amount of definitions in bSDD."""

    # children = defaultdict(list)
    # for k, v in di.items():
    #     if v.get("Parent"):
    #         children[v.get("Parent")].append(k)

    def parents(k):
        yield k
        v = di.get(k)
        if v and v.get("Parent"):
            yield from parents(v.get("Parent"))

    # def child_or_self_has_psets(k):
    #     ps = di.get(k, {}).get("Psets")
    #     if ps:
    #         if set(ps.keys()) - {"Attributes"}:
    #             return True
    #     for c in children[k]:
    #         if child_or_self_has_psets(c):
    #             return True
    #     return False

    # def has_child(k):
    #     def has_child_(k2):
    #         if k2 == k: return True
    #         if not children[k2]: return False
    #         return any(has_child_(c) for c in children[k2])
    #     return has_child_

    def should_include(k, v):
        # PREVIOUSLY return ("IfcProduct" in parents(k)) or has_child("IfcProduct")(k) or
        # child_or_self_has_psets(k)
        # but decided to widen to also include all non-products that have psets, like IfcActor.
        # return ("IfcRoot" in parents(k)) or ("IfcMaterialDefinition" in parents(k)) or
        # ("IfcProfileDef" in parents(k)) or child_or_self_has_psets(k)
        # Now skipping relations ('IfcRelAssociatesClassification'), types ('IfcWallType'),
        # property definitions ('IfcPropertySingleValue'), Resources and other abstract concepts.
        x1 = k.startswith(
            (
                "IfcRel",
                "IfcProperty",
                "IfcProperty",
                "IfcQuantity",
                "IfcConnection",
                "IfcCartesian",
                "IfcMaterial",
            )
        )
        x2 = k.endswith(
            (
                "Relationship",
                "Type",
                "Usage",
                "Property",
                "Template",
                "Resource",
                "Select",
                "Measure",
                "Condition",
                "ProfileDef",
                "Value",
                "Property",
                "Quantity",
                "Curve",
                "Number",
                "Reference",
                "Information",
                "Solid",
            )
        )
        x3 = k.endswith("Unit") and not k == "IfcProtectiveDeviceTrippingUnit"
        x4 = k.startswith("IfcAlignment") and not k == "IfcAlignment"
        x5 = k in excluded_entites
        x6 = k != "IfcObjectDefinition" and k.endswith("Definition")
        x7 = any(
            x in parents(k)
            for x in [
                "IfcPropertyAbstraction",
                "IfcConstraint",
                "IfcRepresentationItem",
                "IfcPresentationItem",
                "IfcPresentationStyle",
                "IfcTypeObject",
                "IfcExternalReference",
                "IfcStructuralLoadOrResult",
                "",
            ]
        )
        x8 = any(z.endswith("Resource") for z in parents(k))
        result = False
        if not any([x1, x2, x3, x4, x5, x6, x7, x8]):
            result = True
        # bypass for selected classes:
        elif k in (
            "IfcMaterial"
        ):  # ,'IfcLightSource','IfcBoundingBox','IfcPoint','IfcCurve',
            # 'IfcSegment','IfcDirection','IfcSurface','IfcVector'):
            result = True
        return result

    return {k: v for k, v in di.items() if should_include(k, v)}


def guid_by_id(id):
    # @todo what was this?

    # """add guid information (not the document ID, but IFC_DOC GUID)"""
    # try:
    #     guid = xmi_doc.guids[id]
    # except KeyError:
    
    guid = ""
    return guid


def is_deprecated(elem):
    """Check if the element is deprecated in that IFC version or not."""
    deprecated = False
    if elem.id in getattr(xmi_doc, "deprecated", set()):
        deprecated = True
    # Some objects don't have deprecated status, but their markdown says they are deprecated
    try:
        if "DEPRECAT" in elem.markdown:
            deprecated = True
    except (AttributeError, TypeError):
        pass
    return deprecated


def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in the file
    a: a fully qualifying key as a tuple
    b: the documentation string
    """
    make_defaultdict = lambda: defaultdict(make_defaultdict)
    classes = defaultdict(make_defaultdict)

    # def get_parent_of_pt(enum_type):
    #     enum_id = enum_type.idref
    #     type_refs = []
    #     for assoc in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
    #         try:
    #             c1, c2 = assoc / "ownedEnd"
    #         except ValueError as er:
    #             logging.error("Encountered exception `%s' on %s", er, assoc)
    #             continue
    #         assoc_type_refs = set(map(lambda c: (c | "type").idref, (c1, c2)))
    #         if enum_id in assoc_type_refs:
    #             other_idref = list(assoc_type_refs - {enum_id})[0]
    #             type_refs.append(xmi_doc.xmi.by_id[other_idref].name)
    # TODO filter this based on the inheritance hierarchy
    # type_refs_without_type = [s for s in type_refs if "Type" not in s]
    # return type_refs_without_type[0] if type_refs_without_type else None

    by_id = {}
    item_by_id = {}
    psets = []  # psets are deferred to the end so that all IDs are resolved
    entities = []  # same for entity attributes:
    enumerations = {}  # predefined types are just normal enumerations
    pset_counts_by_stereo = defaultdict(int)

    ### extract all items from XML
    items = list(xmi_doc)
    for item in tqdm(items, desc="Processing items from XMI", total=len(items)):

        item_by_id[item.id] = item

        item.name = to_str(item.name)

        if not is_deprecated(item):
            if item.type in ("ENUM", "PENUM"):
                enumerations[item.name] = item
            elif item.type == "PSET":
                psets.append(item)
                stereo = ((item.node/"ownedComment")[0]|"body").text
                pset_counts_by_stereo[stereo] += 1
            elif item.type == "ENTITY":
                by_id[item.id] = di = classes[item.name]
                st = item.meta.get("supertypes", [])
                if st:
                    di["Parent"] = to_str(st[0])
                # TODO Overcome faulty input until improved source file:
                if item.name in ["IfcShapeAspect", "IfcActorRole"]:
                    di["Definition"] = definition_improve(
                        to_str(item.markdown_definition)
                    )
                else:
                    di["Definition"] = definition_improve(to_str(item.markdown_content))
                # add human-readable name
                di["Name"] = name_improve(item.name)
                di["Guid"] = guid_by_id(item.id)
                di["Package"] = to_str(item.package)  # solely to split POT files
                entities.append(item)
            # skipping: ('FUNCTION','SELECT','RULE','TYPE')

    ### process all found predefined types (entities)
    for entity in tqdm(entities, desc="Processing predefined types"):

        if "IfcTypeObject" in xmi_doc.supertypes(entity.id):
            continue

        predefined_type_attribute = [
            c for c in entity.children if c.name == "PredefinedType"
        ]
        if predefined_type_attribute:
            ptype_id = predefined_type_attribute[0].node.resolve("type")
            ptype_node = xmi_doc.xmi.by_id.get(ptype_id)
            ptype = ptype_node.name if ptype_node is not None else None
            if ptype in enumerations:
                for c in enumerations[ptype].children:
                    if c.name not in ("USERDEFINED", "NOTDEFINED"):
                        by_id[c.id] = di = classes[entity.name + c.name]
                        di["Parent"] = to_str(entity.name)
                        di["Definition"] = definition_improve(
                            to_str(c.markdown)
                        )  # no trimming, those are already short.
                        di["Description"] = (
                            "Technical note: Because this class is a 'Predefined Type' in IFC, meaning a specialisation"
                            " of its parent class, in IFC it should be represented by the parent class."
                        )
                        # add human-readable name, by identifying words in all-caps phrase
                        # (right now the words are hardcoded)
                        di["Name"] = name_improve(c.name)
                        di["Guid"] = guid_by_id(c.id)
                        di["Package"] = to_str(
                            entity.package
                        )  # solely to split POT files

    ### process all found property sets
    for pset in tqdm(psets, desc="Processing psets"):
        refs = set(pset.meta.get("refs") or [])

        for id in refs:

            if isinstance(id, tuple):
                # In case of TypeObject+PredefinedType appl
                # id = id[0]
                # what to do with typedrivenonly?
                # this option is disabled now
                assert False
                continue

            # find the relevant item (dictionary)
            di = by_id.get(id)
            if di is None:
                try:
                    log_attr_2 = xmi_doc.xmi.by_id[id].name
                    logging.warning(
                        "for %s entity %s not emitted", pset.name, log_attr_2
                    )
                except KeyError:
                    log_attr_2 = id
                    logging.warning("id %s not found", id)
                continue

            for a, (nm, (ty_ty_arg)) in zip(pset.children, pset.definition):

                if not is_deprecated(a):
                    if pset.name.startswith("Qto"):
                        type_name = "real"
                        type_values = None
                        kind_name = "Single"
                    else:
                        ty, ty_arg = ty_ty_arg
                        if ty == "PropertyEnumeratedValue":
                            type_name = list(ty_arg.values())[0]
                            enum_types_by_name = [
                                c
                                for c in xmi_doc.xmi.by_tag_and_type["packagedElement"][
                                    "uml:Class"
                                ]
                                if c.name == type_name
                            ]
                            enum_types_by_name += [
                                c
                                for c in xmi_doc.xmi.by_tag_and_type["packagedElement"][
                                    "uml:Enumeration"
                                ]
                                if c.name == type_name
                            ]
                            type_values = [
                                x.name for x in enum_types_by_name[0] / "ownedLiteral"
                            ]
                            kind_name = "Single"
                        else:
                            org_type_name = list(ty_arg.values())[0]
                            pe_types = [
                                c
                                for c in xmi_doc.xmi.by_tag_and_type["packagedElement"][
                                    "uml:Class"
                                ]
                                if c.name == org_type_name
                            ]
                            pe_types += [
                                c
                                for c in xmi_doc.xmi.by_tag_and_type["packagedElement"][
                                    "uml:DataType"
                                ]
                                if c.name == org_type_name
                            ]
                            if not pe_types:
                                # e.g. IfcComplexNumber_A[1:2] -> IfcComplexNumber
                                pe_types = [
                                    c
                                    for c in xmi_doc.xmi.by_tag_and_type[
                                        "packagedElement"
                                    ]["uml:DataType"]
                                    if re.split(r"_\w\[", c.name)[0] == org_type_name
                                ]
                            if not pe_types:
                                logging.warning(
                                    "%s.%s: type %s not found in XMI; skipping",
                                    pset.name, nm, org_type_name,
                                )
                                continue
                            measure = pe_types[0].name
                            root_generalization = generalization(pe_types[0])
                            type_name = root_generalization.name  # .lower()
                            type_values = None

                            if ty == "PropertySingleValue":
                                kind_name = "Single"
                                # TODO if type_name is a measure or quantity...
                                if not org_type_name in ["IfcText"]:  # 'IfcLabel'
                                    di["Psets"][pset.name]["Properties"][a.name][
                                        "Description"
                                    ] = f"Technical note: in IFC this property takes {org_type_name} as value."
                                    "Such objects are not included in bSDD for simplicity reason. IFC also doesn't enforce particular units,"
                                    "but recommends using metric SI units (metre, kilogram, etc.). Read the IFC documentation for more information."
                            elif ty == "PropertyBoundedValue":
                                kind_name = "Range"
                            elif ty == "PropertyReferenceValue":
                                kind_name = "Complex"
                                di["Psets"][pset.name]["Properties"][a.name][
                                    "Description"
                                ] = f"Technical note: this is a specific property from IFC that takes as its value a reference to {type_name}."
                                "Read the IFC documentation for more information."
                            elif ty == "PropertyListValue":
                                kind_name = "List"
                            elif ty == "PropertyTableValue":
                                kind_name = "Complex"
                                di["Psets"][pset.name]["Properties"][a.name][
                                    "Description"
                                ] = "Technical note: this is a specific property from IFC that takes a table as its value. That table has two "
                                "columns (lists), one with definitions and other for defined values. Read the IFC documentation for more information."
                            else:
                                logging.warning(
                                    "%s.%s of type %s <%s> not mapped",
                                    pset.name,
                                    nm,
                                    ty,
                                    ",".join(
                                        map(lambda kv: "=".join(kv), ty_arg.items())
                                    ),
                                )
                                continue

                    di["Psets"][pset.name]["Definition"] = re.sub(
                        r":\s*[A-Z]{2,}.*",
                        "...",
                        definition_improve(to_str(pset.markdown_content)),
                    )

                    di["Psets"][pset.name]["Properties"][a.name]["Type"] = type_name
                    di["Psets"][pset.name]["Properties"][a.name]["Name"] = name_improve(
                        a.name
                    )
                    # remove value explanation from the definition
                    di["Psets"][pset.name]["Properties"][a.name]["Definition"] = re.sub(
                        r":\s*[A-Z]{2,}.*",
                        "...",
                        definition_improve(to_str(a.markdown)),
                    )
                    di["Psets"][pset.name]["Properties"][a.name]["Kind"] = kind_name
                    di["Psets"][pset.name]["Properties"][a.name]["Package"] = to_str(
                        pset.package
                    )  # solely to split POT files
                    if measure.lower().endswith("measure"):
                        # not measure in ('IfcLabel','IfcText','IfcURIReference',
                        # 'IfcTimeSeries','IfcBoolean'):
                        if measure in MEASURE_MAPPING.keys():
                            di["Psets"][pset.name]["Properties"][a.name][
                                "Dimension"
                            ] = MEASURE_MAPPING[measure]
                        else:
                            di["Psets"][pset.name]["Properties"][a.name][
                                "Dimension"
                            ] = "0 0 0 0 0 0 0"
                    if type_values is None:
                        type_values = TYPE_TO_VALUES.get(type_name)
                    if type_values:
                        di["Psets"][pset.name]["Properties"][a.name]["Values"] = []
                        for tv in type_values:
                            # match the whole sentence containing the value, case insensitive
                            matches = re.findall(
                                r"[^.;!,]*" + tv + r"[^.;!,]*",
                                to_str(a.markdown),
                                flags=re.IGNORECASE,
                            )
                            if matches:
                                description = name_improve(matches[0].strip())
                            else:
                                description = name_improve(tv)  # the value but readable
                            di["Psets"][pset.name]["Properties"][a.name][
                                "Values"
                            ].append(
                                {
                                    "Value": tv,
                                    "Description": description,
                                    "Package": to_str(pset.package),
                                }
                            )

    ### process all found entities again by adding properties and attributes to them
    for entity in tqdm(
        entities, desc="Adding properties to entities"
    ):  # TODO +predefined_types:

        entity_name = entity.name
        if entity_name.endswith("Type"):
            entity_name = entity_name[:-4]
        di = classes[entity_name]

        for c in entity.children:

            if not is_deprecated(c):
                try:
                    node = c.node
                    if node.xml.tagName == "attribute":
                        node = xmi_doc.xmi.by_id[c.node.idref]
                        type_type = node | "type"
                        type_id = type_type.idref
                    else:
                        type_id = node.resolve("type")
                        type_type = xmi_doc.xmi.by_id[type_id]
                    type_item = item_by_id[type_id]
                except:
                    logging.warning(
                        "Not emitting %s.%s because of an error", entity.name, c.name
                    )
                    continue
                if c.name == "PredefinedType":
                    logging.warning(
                        "Not emitting %s.%s because it's the PredefinedType attribute",
                        entity.name,
                        c.name,
                    )
                elif type_item.type == "ENTITY":
                    logging.warning(
                        "Not emitting %s.%s attribute because it's taking an ENTITY: %s",
                        entity.name,
                        c.name,
                        type_item.name,
                    )
                elif type_item.type == "SELECT":
                    logging.warning(
                        "Not emitting %s.%s attribute because it's taking a SELECT: %s",
                        entity.name,
                        c.name,
                        type_item.name,
                    )
                elif type_item.type == "TYPE":

                    type_values = None

                    if getattr(type_item.definition, "super_verbatim", None):

                        if not type_item.definition.super.lower().startswith("string"):
                            logging.warning(
                                "Not emitting %s.%s because it has a \
                                    hardcoded express definition %s",
                                entity.name,
                                c.name,
                                type_item.definition.super,
                            )
                            continue
                        else:
                            type_name = "string"

                    else:

                        ty_pe = xmi_doc.xmi.by_id[type_id]
                        ty_gen = generalization(ty_pe)
                        type_name = ty_gen.name.lower()

                    di["Psets"]["Attributes"]["Properties"][c.name]["Type"] = type_name
                    di["Psets"]["Attributes"]["Properties"][c.name]["Name"] = (
                        name_improve(c.name)
                    )
                    # remove value explanation from the definition
                    di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = (
                        re.sub(
                            r":\s*[A-Z]{2,}.*",
                            "...",
                            definition_improve(to_str(c.markdown)),
                        )
                    )
                    di["Psets"]["Attributes"]["Properties"][c.name]["Package"] = to_str(
                        entity.package
                    )  # solely to split POT files
                    if type_values is None:
                        type_values = TYPE_TO_VALUES.get(type_name)
                    if type_values:
                        di["Psets"]["Attributes"]["Properties"][c.name]["Values"] = []
                        for tv in type_values:
                            # match the whole sentence containing the value, case insensitive
                            # matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*",
                            # to_str(c.markdown), flags=re.IGNORECASE)
                            matches = re.findall(
                                r"[^.;!,]*" + tv + r"[^.;!,]*",
                                to_str(c.markdown),
                                flags=re.IGNORECASE,
                            )
                            if matches:
                                description = definition_improve(
                                    matches[0].strip()
                                )  # the whole sentence explaining the value
                            else:
                                description = name_improve(tv)  # the value but readable
                            di["Psets"]["Attributes"]["Properties"][c.name][
                                "Values"
                            ].append(
                                {
                                    "Value": tv,
                                    "Description": description,
                                    "Package": to_str(entity.package),
                                }
                            )

                elif type_item.type == "ENUM":

                    type_name = type_item.name
                    type_values = type_item.definition.values
                    di["Psets"]["Attributes"]["Properties"][c.name]["Type"] = type_name
                    # remove value explanation from the definition
                    di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = (
                        re.sub(
                            r":\s*[A-Z]{2,}.*",
                            "...",
                            definition_improve(to_str(c.markdown)),
                        )
                    )
                    di["Psets"]["Attributes"]["Properties"][c.name]["Values"] = []
                    di["Psets"]["Attributes"]["Properties"][c.name]["Package"] = to_str(
                        entity.package
                    )  # solely to split POT files
                    for tv in type_values:
                        # match the whole sentence containing the value, case insensitive
                        # matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(c.markdown),\
                        # flags=re.IGNORECASE)
                        matches = re.findall(
                            r"[^.;!,]*" + tv + r"[^.;!,]*",
                            to_str(c.markdown),
                            flags=re.IGNORECASE,
                        )
                        if matches:
                            description = definition_improve(
                                matches[0].strip()
                            )  # the whole sentence explaining the value
                        else:
                            description = name_improve(tv)  # the value but readable
                        di["Psets"]["Attributes"]["Properties"][c.name][
                            "Values"
                        ].append(
                            {
                                "Value": tv,
                                "Description": description,
                                "Package": to_str(entity.package),
                            }
                        )
                else:
                    logging.warning(
                        "Not emitting '%s.%s' because it's a '%s' of type '%s'.",
                        entity.name,
                        c.name,
                        type_item.name,
                        type_item.type,
                    )

    for k, v in pset_counts_by_stereo.items():
        print(k + ":", v)

    print("-- TOTAL --", sum(pset_counts_by_stereo.values()))

    return classes


def list_unique_codes(concepts):
    ### iterate all the results to list all unique codes for translations
    codes = set()
    for code, content in tqdm(all_concepts.items(), "Listing all unique codes"):
        if need_brackets(code):
            codes.add(code)
        if content["Psets"]:
            for pset_code, pset_content in content["Psets"].items():
                if need_brackets(pset_code):
                    # TODO fix faulty codes
                    if "IfcGeometricRepresentationContext" in pset_code:
                        pass
                    else:
                        codes.add(pset_code)
                for prop_code, prop_content in pset_content["Properties"].items():
                    if need_brackets(prop_code):
                        # TODO fix faulty codes
                        if "IfcGeometricRepresentationContext" in prop_code:
                            pass
                        else:
                            codes.add(prop_code)
                    if prop_content["Values"]:
                        for val in prop_content["Values"]:
                            if need_brackets(val["Value"]):
                                codes.add(val["Value"])
    return codes


def generate_bsdd_json(classes, props):
    """Generate IFC.json file (using bSDD template)"""
    logging.info("Started saving .json file")
    bsdd_data = {
        "ModelVersion": "2.0",
        "OrganizationCode": "buildingsmart",
        "DictionaryCode": "ifc",
        "DictionaryName": "IFC",
        "DictionaryVersion": "4.3",
        "LanguageIsoCode": "EN",
        "LanguageOnly": False,
        "UseOwnUri": False,
        "License": "CC BY-ND 4.0",
        "LicenseUrl": "https://creativecommons.org/licenses/by-nd/4.0/legalcode",
        "MoreInfoUrl": "https://ifc43-docs.standards.buildingsmart.org/",
        "QualityAssuranceProcedure": "IFC is a standardized digital description\
            of built environment created by buildingSMART International and its\
            community members. For more information read ISO 16739 and IFC schema documentation.",
        "QualityAssuranceProcedureUrl": "https://technical.buildingsmart.org/standards/ifc/",
        "ReleaseDate": date.today().strftime(r"%Y-%m-%d"),
        "Classes": classes,
        "Properties": props,
    }
    with open(os.path.join(output_dir, "IFC.json"), "w", encoding="utf-8") as f:
        json.dump(
            bsdd_data,
            f,
            indent=4,
            default=lambda x: (getattr(x, "to_json", None) or (lambda: vars(x)))(),
            ensure_ascii=False,
        )
        print("-- Saved JSON file. --")
    print(
        "-- Saved IFC.json file with %s classes and %s properties. --"
        % (len(classes), len(props))
    )


def restructure_and_annotate(all_concepts, uni_codes, codes):
    ### iterate again to annotate all descriptions and restructure classes/properties/values:
    classes = []
    psets = []
    props = []
    props = []
    to_translate = []
    unique_props = set()
    unique_psets = set()
    for code, content in tqdm(
        all_concepts.items(), desc="Restructuring and annotating"
    ):
        clas_def = annotate(content["Definition"], uni_codes)
        classes.append(
            {
                "Code": code[0:CHAR_LIMIT],
                "Name": (
                    to_str(content["Name"])
                    if to_str(content["Name"])
                    else name_improve(code)
                ),
                "Definition": clas_def,
                "ClassType": "Class",
                "ClassProperties": [],
            }
        )

        if content["Guid"]:
            classes[-1]["Uid"] = to_str(content["Guid"])
        if content["Parent"]:
            if content["Parent"] in codes:
                classes[-1]["ParentClassCode"] = to_str(content["Parent"])
        if content["Description"]:
            classes[-1]["Description"] = to_str(content["Description"])
            to_translate.append(
                {
                    "msgid": code[0:CHAR_LIMIT] + "_DESCRIPTION",
                    "msgstr": classes[-1]["Description"],
                    "package": content["Package"],
                }
            )
        to_translate.append(
            {
                "msgid": code[0:CHAR_LIMIT],
                "msgstr": classes[-1]["Name"],
                "package": content["Package"],
            }
        )
        to_translate.append(
            {
                "msgid": code[0:CHAR_LIMIT] + "_DEFINITION",
                "msgstr": clas_def,
                "package": content["Package"],
            }
        )
        ancestors = [code]
        ancestors = list_ancestors(code, all_concepts, ancestors)
        unique_p_codes = set()
        # add properties (from this object and all its parents)
        for ancestor_name in ancestors:
            ancestor = all_concepts[ancestor_name]
            # if ancestor['Psets']:
            if ancestor["Psets"]:
                for pset_code, pset_content in ancestor["Psets"].items():
                    for prop_code, prop_content in pset_content["Properties"].items():
                        prop_code = re.split(r"_\w\[", prop_code)[0][0:CHAR_LIMIT]
                        name = to_str(prop_content["Name"])
                        if not name:
                            name = name_improve(prop_code)
                        prop_def = annotate(prop_content["Definition"], uni_codes)
                        # property code must be unique for a given class and shorter than 50 characters
                        if len(prop_code) + len(pset_code) < 50:
                            p_code = (
                                prop_code
                                + "_from_"
                                + re.sub("Pset_|Qto_", "", pset_code)
                            )
                        # special treatment of 5 psets that result in duplicated codes:
                        elif prop_code in (
                            "AdjustmentDesignation",
                            "IsCurrentTolerancePositiveOnly",
                        ) and pset_code in (
                            "Pset_ProtectiveDeviceTrippingUnitTimeAdjustment",
                            "Pset_ProtectiveDeviceTrippingUnitCurrentAdjustment",
                            "Pset_ProtectiveDeviceTrippingFunctionGCurve",
                            "Pset_ProtectiveDeviceTrippingFunctionICurve",
                            "Pset_ProtectiveDeviceTrippingFunctionICurve",
                        ):
                            p_code = (
                                prop_code
                                + "_from_..."
                                + "".join([c for c in pset_code if c.isupper()])
                            )
                        else:
                            # p_code = prop_code+"_"+pset_code[5:51-len(prop_code)]+"..."
                            p_code = (
                                prop_code
                                + "_from_"
                                + re.sub("Pset_|Qto_", "", pset_code)[
                                    : int((41 - len(prop_code)) / 2)
                                ]
                                + "..."
                                + re.sub("Pset_|Qto_", "", pset_code)[
                                    len(re.sub("Pset_|Qto_", "", pset_code))
                                    - int((41 - len(prop_code)) / 2) :
                                ]
                            )
                        classProp = {
                            "PropertyCode": prop_code[0:CHAR_LIMIT],
                            "Code": p_code[0:CHAR_LIMIT],
                            "PropertySet": pset_code[0:CHAR_LIMIT],
                        }

                        #
                        if not p_code in unique_p_codes:
                            classes[-1]["ClassProperties"].append(classProp)
                            unique_p_codes.add(p_code)
                        if not prop_code in unique_props:
                            unique_props.add(prop_code)

                            props.append(
                                {
                                    "Code": prop_code[0:CHAR_LIMIT],
                                    "Name": name,
                                    "Definition": prop_def,
                                    "PropertyValueKind": to_str(prop_content["Kind"]),
                                }
                            )
                            to_translate.append(
                                {
                                    "msgid": prop_code[0:CHAR_LIMIT],
                                    "msgstr": name,
                                    "package": content["Package"],
                                }
                            )
                            to_translate.append(
                                {
                                    "msgid": prop_code[0:CHAR_LIMIT] + "_DEFINITION",
                                    "msgstr": prop_def,
                                    "package": content["Package"],
                                }
                            )

                            if (
                                prop_content["Values"]
                                and prop_content["Type"].lower() != "boolean"
                            ):
                                allowed_values = []
                                for val in prop_content["Values"]:
                                    descr = annotate(val["Description"], uni_codes)
                                    allowed_values.append(
                                        {
                                            "Code": val["Value"][0:CHAR_LIMIT],
                                            "Value": val["Value"],
                                            "Description": descr,
                                        }
                                    )
                                    to_translate.append(
                                        {
                                            "msgid": prop_code[0:CHAR_LIMIT]
                                            + "_"
                                            + val["Value"],
                                            "msgstr": descr,
                                            "package": content["Package"],
                                        }
                                    )
                                props[-1]["AllowedValues"] = allowed_values

                            if prop_content["Description"]:
                                props[-1]["Description"] = annotate(
                                    prop_content["Description"],
                                    uni_codes
                                )
                                to_translate.append(
                                    {
                                        "msgid": prop_code[0:CHAR_LIMIT]
                                        + "_DESCRIPTION",
                                        "msgstr": props[-1]["Description"],
                                        "package": content["Package"],
                                    }
                                )
                            if prop_content["Dimension"]:
                                props[-1]["Dimension"] = prop_content["Dimension"]
                            if prop_content["Type"].lower() == "string":
                                props[-1]["DataType"] = "String"
                            elif prop_content["Type"].lower() in ("real", "number"):
                                props[-1]["DataType"] = "Real"
                            elif prop_content["Type"].lower() == "integer":
                                props[-1]["DataType"] = "Integer"
                            elif prop_content["Type"].lower() == "boolean":
                                props[-1]["DataType"] = "Boolean"
                            elif prop_content["Type"].startswith(
                                "PEnum_"
                            ) or prop_content["Type"].endswith("Enum"):
                                # Assuming that all enums are text.
                                props[-1]["DataType"] = "String"
                            else:
                                # TODO handle: IfcTimeSeries, IfcMaterialDefinition, LOGICAL, IfcExternalReference, IfcPerson, IfcAppliedValue
                                logging.warning(
                                    "Not sure what data type to apply to: '%s'.",
                                    prop_content["Type"],
                                )
    classes.extend(psets)
    return classes, props, to_translate


class pot_file:
    def __init__(self, f):
        self.f = f
        now = date.today()
        print(
            """# Industry Foundation Classes IFC.
# Copyright (C) {year} buildingSMART
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: bsdd_support@buildingsmart.org\\n"
"POT-Creation-Date: {date} {time}\\n"
"X-Crowdin-SourceKey: msgstr\\n"
"Language-Team: buildingSMART community\\n"
""".format(
                year=now.strftime("%Y"),
                date=now.strftime(r"%Y-%m-%d"),
                time=now.strftime("%H:%M"),
            ),
            file=self.f,
        )

    def __getattr__(self, k):
        return getattr(self.f, k)


class pot_dict(dict):

    def __missing__(self, key):
        if not os.path.exists(os.path.join(output_dir, "pot")):
            os.makedirs(os.path.join(output_dir, "pot"))
        if not key:
            key = "UNSPECIFIED_PACKAGE"
        v = self[key] = pot_file(
            open(os.path.join(output_dir, "pot", key + ".pot"), "w+", encoding="utf-8")
        )  # add folder: "pot",
        return v


def generate_translation_template(to_translate, po_files):
    i = 0
    pos = set()
    id_set = set()
    for t in tqdm(to_translate, desc="generating translation"):
        if isinstance(t["package"], defaultdict):
            t["package"] = to_str(t["package"])
        if isinstance(t["msgstr"], defaultdict):
            t["msgstr"] = to_str(t["msgstr"])

        po_file = po_files[t["package"]]

        if t["msgid"] and t["msgstr"]:  # skip empty strings
            if not t["msgid"] in id_set:
                id_set.add(t["msgid"])
                print("msgid", quote(t["msgid"]), file=po_file)
                print("msgstr", quote(t["msgstr"]), file=po_file)
                print(file=po_file)
                pos.add(po_file)
                i += 1
            else:
                logging.warning(
                    "Duplicated msgids '%s' in the pot file: %s.", t["msgid"], po_file
                )
    print("-- Saved %s terms in %s POT files. --" % (i, len(pos)))


all_concepts = generate_definitions()
filtered_concepts = filter_concepts(all_concepts)
uni_codes = list_unique_codes(filtered_concepts)
codes_pattern = re.compile("\\b(%s)\\b" % "|".join(sorted(uni_codes, key=lambda s: -len(s))))
classes, props, to_translate = restructure_and_annotate(filtered_concepts, codes_pattern, uni_codes)
generate_bsdd_json(classes, props)

po_files = pot_dict()
generate_translation_template(to_translate, po_files)
