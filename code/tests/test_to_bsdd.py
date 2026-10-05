import json
import os
import re
import subprocess
import sys
import urllib.request
from types import SimpleNamespace
from urllib.parse import urlparse

import pytest

from generators import bsdd
from generators.bsdd import (
    ANCHORS,
    DEFAULT_SCHEMA,
    MATERIAL_CLASSES,
    REPO_ROOT,
    annotation_pattern,
    attach_entity_attributes,
    class_property_code,
    data_type_for,
    documentation_url,
    entity_classes,
    entity_tree,
    expand_predefined_types,
    in_anchor_cones,
    property_entry,
    render_allowed_values,
    render_class_properties,
    render_property_once,
    schema_items,
    value_entries,
    wrap_wikilinks,
)
from generators.util.xmi_document import xmi_document
from version import version_tuple

SUPERTYPE = {
    "IfcObjectDefinition": "IfcRoot",
    "IfcRelationship": "IfcRoot",
    "IfcObject": "IfcObjectDefinition",
    "IfcTypeObject": "IfcObjectDefinition",
    "IfcProduct": "IfcObject",
    "IfcWall": "IfcProduct",
    "IfcWallType": "IfcTypeObject",
    "IfcRelAggregates": "IfcRelationship",
    "IfcGeometricRepresentationItem": "IfcRepresentationItem",
    "IfcStructuralLoad": "IfcStructuralLoadOrResult",
    "IfcCartesianPoint": "IfcGeometricRepresentationItem",
}
CHILDREN = {}
for child, parent in SUPERTYPE.items():
    CHILDREN.setdefault(parent, set()).add(child)
NAMES = set(SUPERTYPE) | set(SUPERTYPE.values())

ANCHORS = ("IfcObject", "IfcStructuralLoad")


def test_scope_is_anchor_cones_plus_spine_to_root():
    scope = in_anchor_cones(ANCHORS, NAMES, SUPERTYPE, CHILDREN)
    for name in ("IfcObject", "IfcProduct", "IfcWall", "IfcObjectDefinition", "IfcRoot", "IfcStructuralLoad"):
        assert name in scope, name
    for name in ("IfcTypeObject", "IfcWallType", "IfcRelationship", "IfcRelAggregates",
                 "IfcRepresentationItem", "IfcGeometricRepresentationItem", "IfcCartesianPoint",
                 "IfcStructuralLoadOrResult"):
        assert name not in scope, name


def test_anchor_missing_from_schema_is_skipped():
    assert in_anchor_cones(("IfcBogus",), NAMES, SUPERTYPE, CHILDREN) == set()


def test_class_property_code():
    assert class_property_code("FireRating", "Pset_WallCommon") == "FireRating_from_WallCommon"
    long = class_property_code("IsCurrentTolerancePositiveOnly",
                               "Pset_ProtectiveDeviceTrippingUnitTimeAdjustment")
    assert long == "IsCurrentTolerancePositiveOnly_from_...PPDTUTA"
    squeezed = class_property_code("SomeRatherLongPropertyName", "Pset_SomeRatherLongPropertySetName")
    assert "..." in squeezed and len(squeezed) <= 50


def test_data_type_for():
    assert data_type_for("string") == "String"
    assert data_type_for("REAL") == "Real"
    assert data_type_for("PEnum_Status") == "String"
    assert data_type_for("IfcWindowStyleOperationEnum") == "String"
    assert data_type_for("logical") is None


def test_wrap_wikilinks():
    pattern = annotation_pattern({"IfcWall", "IfcAlignmentSegment"}, {"IfcWall", "IfcAlignmentSegment", "IfcCartesianPoint"})
    assert wrap_wikilinks("An _IfcWall_ is", pattern) == "An [[IfcWall]] is"
    assert wrap_wikilinks("IfcAlignmentSegment", pattern) == "[[IfcAlignmentSegment]]"
    assert wrap_wikilinks("IfcWall and _IfcWall_", pattern) == "[[IfcWall]] and [[IfcWall]]"
    assert wrap_wikilinks("An _IfcCartesianPoint_ is", pattern) == "An IfcCartesianPoint is"
    assert wrap_wikilinks("IfcCartesianPoint here", pattern) == "IfcCartesianPoint here"


def test_value_entries_description_is_the_sentence_around_the_value():
    entries = value_entries(["SOLIDWALL", "OTHER"], "A wall. Use SOLIDWALL for solid ones; rest.", "P")
    assert [e["Description"] for e in entries] == ["Use SOLIDWALL for solid ones", "Other"]


def test_allowed_value_labels_stay_plain_but_lose_italic_markup():
    pattern = annotation_pattern({"Temperature", "IfcWall"}, {"Temperature", "IfcWall"})
    values = [
        {"Value": "OPERATINGTEMPERATURE", "Description": "Operating Temperature", "Package": "P"},
        {"Value": "1000", "Description": "1000", "Package": "P"},
        {"Value": "WALLMOUNTED", "Description": "Mounted on an _IfcWall_", "Package": "P"},
    ]
    rendered = render_allowed_values(values, "Prop", pattern, [])
    assert [v["Description"] for v in rendered] == ["Operating Temperature", "1000", "Mounted on an IfcWall"]


def test_logical_properties_emit_no_allowed_values():
    entry = property_entry("AboveGround", "above ground (TRUE) or below (FALSE)", "logical", "Single", "P")
    assert "Values" not in entry


def test_documentation_url_points_predefined_types_at_their_entity_page():
    entity, child = {"Parent": "IfcProduct"}, {"Parent": "IfcBeam", "PredefinedPin": "BEAM"}
    assert documentation_url("IfcBeam", entity, "4.3") == (
        "https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcBeam.htm")
    assert documentation_url("IfcBeamBEAM", child, "4.3") == documentation_url("IfcBeam", entity, "4.3")


def _prop(name, **extra):
    return {"Type": "string", "Name": name, "Definition": "", "Kind": "Single", "Package": "P", **extra}


CLASSES = {
    "IfcElement": {
        "Parent": "",
        "Package": "P",
        "Psets": {
            "Attributes": {
                "PredefinedType": _prop(
                    "Predefined Type",
                    Values=[{"Value": "SOLIDWALL", "Description": "Solid Wall", "Package": "P"},
                            {"Value": "POLYGONAL", "Description": "Polygonal", "Package": "P"}],
                    ValuesPerClass=True,
                ),
            },
        },
    },
    "IfcWall": {
        "Parent": "IfcElement",
        "Package": "P",
        "Psets": {"Pset_WallCommon": {"FireRating": _prop("Fire Rating")}},
    },
    "IfcWallSOLIDWALL": {
        "Parent": "IfcWall",
        "Package": "P",
        "Psets": {},
        "PredefinedPin": "SOLIDWALL",
    },
}
NO_ANNOTATION = annotation_pattern({"zzz-never-matches"}, {"zzz-never-matches"})


def _render(code):
    return render_class_properties(code, CLASSES, NO_ANNOTATION, {}, [])


def test_class_properties_inherit_down_the_spine_deduped_and_deprecated_inactive():
    codes = [cp["Code"] for cp in _render("IfcWall")]
    assert sorted(codes) == ["FireRating_from_WallCommon", "PredefinedType_from_Attributes"]
    properties = {}
    render_class_properties("IfcWallSOLIDWALL", CLASSES, NO_ANNOTATION, properties, [])
    assert "AllowedValues" not in properties["PredefinedType"]
    render_property_once("Reference", _prop("Reference", Deprecated=True), NO_ANNOTATION, properties, [])
    assert properties["Reference"]["Status"] == "Inactive"
    assert "Status" not in properties["FireRating"]


def test_parent_carries_full_enum_and_child_pins_one_value():
    parent_pt = next(cp for cp in _render("IfcElement") if cp["PropertyCode"] == "PredefinedType")
    assert [v["Value"] for v in parent_pt["AllowedValues"]] == ["SOLIDWALL", "POLYGONAL"]
    child_pt = next(cp for cp in _render("IfcWallSOLIDWALL") if cp["PropertyCode"] == "PredefinedType")
    assert [v["Value"] for v in child_pt["AllowedValues"]] == ["SOLIDWALL"]


def _real_schema_scope():
    schema = schema_items(xmi_document(str(DEFAULT_SCHEMA)))
    supertype_of, children_of = entity_tree(schema.entities)
    return in_anchor_cones(ANCHORS, {e.name for e in schema.entities}, supertype_of, children_of)


@pytest.mark.integration
def test_real_schema_scope_invariants():
    scope = _real_schema_scope()
    for name in ("IfcRoot", "IfcWall", *ANCHORS):
        assert name in scope, name
    for name in ("IfcCartesianPoint", "IfcRelAggregates", "IfcPropertySingleValue", "IfcTypeObject"):
        assert name not in scope, name


@pytest.mark.integration
def test_every_documentation_url_resolves_to_a_documented_entity():
    pages = {path.stem for path in (REPO_ROOT / "docs" / "schemas").glob("*/*/Entities/*.md")}
    assert sorted(_real_schema_scope() - pages) == []


@pytest.mark.integration
def test_every_document_reference_is_a_published_lexical_page():
    version = "%s.%s" % tuple(version_tuple[:2])
    references = {documentation_url(name, {}, version) for name in _real_schema_scope()}
    lexical_dir = urlparse(next(iter(references))).path.rsplit("/", 1)[0].lstrip("/")
    request = urllib.request.Request(
        "https://api.github.com/repos/buildingSMART/IFC-output/git/trees/main:" + lexical_dir)
    if os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(request) as response:
        published = {entry["path"] for entry in json.load(response)["tree"]}
    assert sorted({r.rsplit("/", 1)[1] for r in references} - published) == []


def _fake_entity(name, children=()):
    return SimpleNamespace(name=name, meta={}, markdown_content="", markdown_definition="",
                           markdown="", package="P", id=name, children=list(children))


def test_predefined_type_children_do_not_inherit_material_classtype():
    predefined_attr = SimpleNamespace(name="PredefinedType", node=SimpleNamespace(resolve=lambda key: "enum_id"))
    entity = _fake_entity("IfcConstructionMaterialResource", children=[predefined_attr])
    literal = SimpleNamespace(name="CONCRETE", markdown="", id="lit_concrete")
    enum = SimpleNamespace(children=[literal])
    schema = SimpleNamespace(entities=[entity], enumerations={"IfcConstructionMaterialResourceTypeEnum": enum})
    xmi = SimpleNamespace(by_id={"enum_id": SimpleNamespace(name="IfcConstructionMaterialResourceTypeEnum")})

    classes, class_by_entity_id = entity_classes([entity], {entity.name}, MATERIAL_CLASSES)
    expand_predefined_types(schema, classes, class_by_entity_id, xmi)

    assert classes["IfcConstructionMaterialResource"]["ClassType"] == "Material"
    assert classes["IfcConstructionMaterialResourceCONCRETE"]["ClassType"] == "Class"


def test_type_entity_attributes_merge_onto_occurrence_class():
    literal = SimpleNamespace(name="A", markdown="", id="l")
    enum = SimpleNamespace(type="ENUM", name="IfcFooEnum", children=[literal])
    attr = SimpleNamespace(name="Shape", markdown="", node=SimpleNamespace(resolve=lambda key: "enum_id"))
    type_entity = _fake_entity("IfcWallType", children=[attr])
    schema = SimpleNamespace(entities=[type_entity], item_by_id={"enum_id": enum})
    classes = {"IfcWall": {"Psets": {}}}
    attach_entity_attributes(schema, classes, None)
    assert "Shape" in classes["IfcWall"]["Psets"]["Attributes"]


ITALIC_MARKUP = re.compile(r"_Ifc\w+_")


@pytest.mark.integration
def test_export_leaves_no_italic_markup_or_boolean_wikilinks(tmp_path):
    code_dir = REPO_ROOT / "code"
    subprocess.run([sys.executable, "-m", "generators.bsdd", str(DEFAULT_SCHEMA), "--output", str(tmp_path)], cwd=code_dir, check=True)
    subprocess.run([sys.executable, "-m", "generators.pot", str(DEFAULT_SCHEMA), "--output", str(tmp_path)], cwd=code_dir, check=True)

    ifc_json = (tmp_path / "IFC.json").read_text(encoding="utf-8")
    assert not ITALIC_MARKUP.findall(ifc_json)

    doc = json.loads(ifc_json)
    labels = [v.get("Description", "") for p in doc["Properties"] for v in p.get("AllowedValues", [])]
    labels += [v.get("Description", "") for c in doc["Classes"] for cp in c["ClassProperties"]
               for v in cp.get("AllowedValues", [])]
    assert labels and not any("[[" in label for label in labels)
    logical = [p for p in doc["Properties"] if p.get("DataType") is None and "AllowedValues" in p
               and {v["Value"] for v in p["AllowedValues"]} <= {"TRUE", "FALSE", "UNKNOWN"}]
    assert not logical

    for unpublished in ("IfcRelAggregates", "IfcLinearPlacement", "IfcLocalPlacement",
                        "IfcShellBasedSurfaceModel", "IfcRelAssignsToGroupByFactor"):
        assert "[[%s]]" % unpublished not in ifc_json, unpublished

    msgstrs = [m.group(1) for pot in (tmp_path / "pot").glob("*.pot")
               for m in re.finditer(r'^msgstr "(.+)"$', pot.read_text(encoding="utf-8"), re.M)]
    assert msgstrs
    assert not any(ITALIC_MARKUP.search(msgstr) for msgstr in msgstrs)
