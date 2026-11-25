import pytest

from generators.util.xmi_document import xmi_document

# IfcBuiltSystem has no type class in the Object Typing concept
OBJECT_TYPING = {"IfcElementAssembly": "IfcElementAssemblyType", "IfcWall": "IfcWallType"}
ENTITIES = ["IfcBuiltSystem", *OBJECT_TYPING, *OBJECT_TYPING.values()]

# a predefined type of an entity is a class named <enumeration>.<literal>,
# on the type class that is added it is a tuple of (type class, literal)
SYSTEM = "IfcBuiltSystemTypeEnum.TUNNEL_PRESUPPORT"
VAULT = "IfcElementAssemblyTypeEnum.PRESUPPORTVAULT"
FACE = "IfcElementAssemblyTypeEnum.PRESUPPORTFACE"
VAULT_TYPE = ("IfcElementAssemblyType", "PRESUPPORTVAULT")
FACE_TYPE = ("IfcElementAssemblyType", "PRESUPPORTFACE")

# applicable classes in UML order and the type classes they give; the id names what the case proves.
CASES = [
    ("class-without-type-first", [SYSTEM, VAULT, FACE], [VAULT_TYPE, FACE_TYPE]),
    ("class-without-type-in-the-middle", [VAULT, SYSTEM, FACE], [VAULT_TYPE, FACE_TYPE]),
    ("class-without-type-last", [VAULT, FACE, SYSTEM], [VAULT_TYPE, FACE_TYPE]),
    ("class-without-type-and-predefined-type-first", ["IfcBuiltSystem", VAULT, FACE], [VAULT_TYPE, FACE_TYPE]),
    ("no-class-with-a-type", [SYSTEM, "IfcBuiltSystem"], []),
    ("no-predefined-types", ["IfcBuiltSystem", "IfcWall", "IfcElementAssembly"], ["IfcWallType", "IfcElementAssemblyType"]),
    ("one-class", [VAULT], [VAULT_TYPE]),
]

MODEL = """<?xml version="1.0" encoding="UTF-8"?>
<uml:Model xmi:version="20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmlns:uml="http://www.eclipse.org/uml2/5.0.0/UML" xmi:id="md_test" name="test">
  <packagedElement xmi:type="uml:Package" xmi:id="pk_IfcProductExtension" name="IfcProductExtension">
    %s
    <packagedElement xmi:type="uml:Class" xmi:id="cl_Pset_Test" name="Pset_Test">
      <ownedComment xmi:type="uml:Comment" xmi:id="cl_Pset_Test_comment_0"><body>%s</body></ownedComment>
    </packagedElement>
    %s
  </packagedElement>
</uml:Model>
"""


def _applicable_classes(tmp_path, template_type, applicable):
    """Write a schema with one property set and return the applicable classes xmi_document gives it, by name."""
    xmi_id = lambda name: "cl_" + name.replace(".", "_")
    classes = [f'<packagedElement xmi:type="uml:Class" xmi:id="{xmi_id(n)}" name="{n}"/>' for n in dict.fromkeys(ENTITIES + applicable)]
    dependencies = [f'<packagedElement xmi:type="uml:Dependency" xmi:id="dp_{i}" client="cl_Pset_Test" supplier="{xmi_id(n)}"/>' for i, n in enumerate(applicable)]
    concepts = tmp_path / "mvd" / "GeneralUsage"
    concepts.mkdir(parents=True)
    (concepts / "ObjectTyping.csv").write_text("ApplicableEntity,RelatingType\n" + "".join(f"{a},{b}\n" for a, b in OBJECT_TYPING.items()), encoding="utf-8")
    (tmp_path / "test.uml").write_text(MODEL % ("\n    ".join(classes), template_type, "\n    ".join(dependencies)), encoding="utf-8")

    doc = xmi_document(str(tmp_path / "test.uml"))
    pset, = (item for item in doc if item.type == "PSET")
    name = lambda id_: doc.xmi.by_id[id_].name
    return [(name(ref[0]), *ref[1:]) if isinstance(ref, tuple) else name(ref) for ref in pset.meta["refs"]]


@pytest.mark.parametrize("applicable, type_classes", [case[1:] for case in CASES], ids=[case[0] for case in CASES])
def test_type_driven_override_adds_type_classes_with_their_own_predefined_types(tmp_path, applicable, type_classes):
    assert _applicable_classes(tmp_path, "PSET_TYPEDRIVENOVERRIDE", applicable) == applicable + type_classes


@pytest.mark.parametrize("applicable, type_classes", [case[1:] for case in CASES], ids=[case[0] for case in CASES])
def test_type_driven_only_keeps_type_classes_with_their_own_predefined_types(tmp_path, applicable, type_classes):
    assert _applicable_classes(tmp_path, "PSET_TYPEDRIVENONLY", applicable) == type_classes


def test_occurrence_driven_set_gets_no_type_classes(tmp_path):
    assert _applicable_classes(tmp_path, "PSET_OCCURRENCEDRIVEN", [SYSTEM, VAULT, FACE]) == [SYSTEM, VAULT, FACE]
