"""Compile generated schemas, rather than only checking their XML syntax."""
import subprocess
import sys
from pathlib import Path
import pytest
from lxml import etree

from generators.util.express_to_xsd import run


def generate(tmp_path, declarations, schema_name="IFC4X3_ADD2"):
    express = tmp_path / "schema.exp"
    output = tmp_path / "schema.xsd"
    express.write_text(f"SCHEMA {schema_name};\n{declarations}\nEND_SCHEMA;\n")
    run(express, output)
    tree = etree.parse(str(output))
    return tree, etree.XMLSchema(tree)


@pytest.mark.parametrize("name, suffix", [
    ("IFC4X3_ADD2", "RELEASE/IFC4/3/ADD2"),
    ("IFC4X3_DEV_abc123", "DEV/IFC4/3/DEV/abc123"),
])
def test_namespace_follows_input_schema(tmp_path, name, suffix):
    tree, _ = generate(tmp_path, "ENTITY IfcExample; END_ENTITY;", name)
    assert tree.getroot().get("targetNamespace") == (
        f"https://standards.buildingsmart.org/IFC/{suffix}"
    )


@pytest.mark.parametrize("declarations, valid, invalid", [
    (
    """
    TYPE IfcBinary = BINARY; END_TYPE;
    ENTITY IfcPixelTexture;
      Pixel : LIST [1:?] OF IfcBinary;
    END_ENTITY;
    """, '<IfcPixelTexture Pixel="AABBCC 010203"/>', '<IfcPixelTexture Pixel="GG"/>'),
    (
    """
    TYPE IfcCompoundPlaneAngleMeasure = LIST [3:4] OF INTEGER; END_TYPE;
    ENTITY IfcSite;
      RefLatitude : OPTIONAL IfcCompoundPlaneAngleMeasure;
      RefLongitude : OPTIONAL IfcCompoundPlaneAngleMeasure;
    END_ENTITY;
    """, '<IfcSite RefLatitude="52 30 12" RefLongitude="4 10 2 3"/>', '<IfcSite RefLatitude="52 30"/>'),
    (
    """
    TYPE IfcLabel = STRING; END_TYPE;
    ENTITY IfcDimensionalExponents; END_ENTITY;
    ENTITY IfcNamedUnit;
      Dimensions : IfcDimensionalExponents;
    END_ENTITY;
    ENTITY IfcSIUnit SUBTYPE OF (IfcNamedUnit);
      Name : IfcLabel;
    DERIVE
      SELF\\IfcNamedUnit.Dimensions : IfcDimensionalExponents := ?;
    END_ENTITY;
    ENTITY IfcUnrelatedUnit;
      Dimensions : IfcDimensionalExponents;
    END_ENTITY;
    """, '<IfcSIUnit Name="METRE"/>', '<IfcUnrelatedUnit/>'),
], ids=["binary-list", "named-aggregate-attribute", "derived-required-particle"])
def test_generated_types_compile(tmp_path, declarations, valid, invalid):
    tree, validator = generate(tmp_path, declarations)
    namespace = tree.getroot().get("targetNamespace")

    def document(body):
        return etree.fromstring(f'<ifcXML xmlns="{namespace}">{body}</ifcXML>')

    validator.assertValid(document(valid))
    assert not validator.validate(document(invalid))
    if "IfcSIUnit" in declarations:
        assert not validator.validate(document(
            '<IfcSIUnit><Dimensions ref="d"/></IfcSIUnit>'
            '<IfcDimensionalExponents id="d"/>'
        ))


def test_existing_unbounded_aggregate_fix(tmp_path):
    tree, _ = generate(tmp_path, """
        TYPE IfcLabel = STRING; END_TYPE;
        ENTITY IfcPropertySingleValue;
          Name : IfcLabel;
        END_ENTITY;
        TYPE IfcPropertySetDefinitionSet = SET [1:?] OF IfcPropertySingleValue;
        END_TYPE;
    """)
    assert not tree.xpath('//*[@maxOccurs="?"]')


@pytest.mark.parametrize("entity, attribute, value_type", [
    ("IfcPerson", "MiddleNames", "IfcLabel"),
    ("IfcCartesianPointList3D", "TagList", "IfcLabel"),
    ("IfcSurfaceTexture", "Parameter", "IfcIdentifier"),
    ("IfcTelecomAddress", "TelephoneNumbers", "IfcLabel"),
])
def test_string_aggregates_preserve_item_boundaries(tmp_path, entity, attribute, value_type):
    tree, validator = generate(tmp_path, f"""
        TYPE IfcLabel = STRING(255); END_TYPE;
        TYPE IfcIdentifier = STRING(255); END_TYPE;
        ENTITY {entity};
          {attribute} : OPTIONAL LIST [1:?] OF {value_type};
        END_ENTITY;
    """)
    ns = tree.getroot().get("targetNamespace")
    root = etree.Element(f"{{{ns}}}ifcXML", nsmap={None: ns})
    obj = etree.SubElement(root, f"{{{ns}}}{entity}")
    collection = etree.SubElement(obj, f"{{{ns}}}{attribute}")
    values = ["two words", "", "  leading and trailing  ", "one"]
    for value in values:
        etree.SubElement(collection, f"{{{ns}}}{value_type}-wrapper").text = value
    validator.assertValid(root)
    restored = etree.fromstring(etree.tostring(root))
    assert [node.text or "" for node in restored[0][0]] == values
    assert len(restored[0][0]) == len(values)
    # The old whitespace-separated representation has ambiguous item boundaries.
    obj.remove(collection)
    obj.set(attribute, "two words")
    assert not validator.validate(root)


def test_legacy_cli_uses_the_same_generator_outside_code_directory(tmp_path):
    tree, _ = generate(tmp_path, """
        TYPE IfcBinary = BINARY; END_TYPE;
        TYPE IfcCompoundPlaneAngleMeasure = LIST [3:4] OF INTEGER; END_TYPE;
        ENTITY IfcSite;
          RefLatitude : OPTIONAL IfcCompoundPlaneAngleMeasure;
        END_ENTITY;
        ENTITY IfcPixelTexture;
          Pixel : LIST [1:?] OF IfcBinary;
        END_ENTITY;
    """)
    output = tmp_path / "legacy.xsd"
    result = subprocess.run([
        sys.executable, str(Path(__file__).resolve().parents[1] / "express_to_xsd.py"),
        str(tmp_path / "schema.exp"), str(output),
    ], cwd=tmp_path, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
    legacy = etree.parse(str(output))
    etree.XMLSchema(legacy)
    assert etree.tostring(legacy) == etree.tostring(tree)
