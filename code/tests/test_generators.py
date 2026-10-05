import json
from pathlib import Path
from types import SimpleNamespace


def test_pset_compare_reports_a_changed_pset(tmp_path):
    from generators import pset

    for side, name in (("reference", "A"), ("output", "B")):
        (tmp_path / side).mkdir()
        (tmp_path / side / "Pset_X.xml").write_text(f"<PropertySetDef><Name>{name}</Name></PropertySetDef>", encoding="utf-8")
    report = tmp_path / "report.md"
    pset.compare(str(tmp_path / "reference"), str(tmp_path / "output"), str(report))
    text = report.read_text()
    assert "Pset_X.xml\n==========" in text and "~~A~~ B" in text


def test_table_value_formatter_finds_child_by_tag():
    from generators import json as structure

    table = {"_children": [
        {"#tag": "DefinedValue", "_children": [{"@type": "IfcLabel"}]},
        {"#tag": "DefiningValue", "_children": [{"@type": "IfcReal"}]},
    ]}
    assert structure.format_TypePropertyTableValue(table) == "IfcLabel/IfcReal"


def test_only_runs_named_steps_in_dict_order(monkeypatch):
    import generators.__main__ as orchestrator

    ran = []
    monkeypatch.setattr(orchestrator, "xmi_document", lambda schema: "doc")
    monkeypatch.setattr(orchestrator, "STEPS", {
        name: (lambda doc, out, name=name: ran.append((name, doc, out))) for name in orchestrator.STEPS
    })
    orchestrator.main(["schema.uml", "--output", "out", "--only", "json", "express"])
    assert ran == [("express", "doc", Path("out")), ("json", "doc", Path("out"))]


def test_pot_run_writes_under_bsdd_pot(monkeypatch, tmp_path):
    from generators import bsdd, pot

    entry = {"msgid": "IfcWall", "msgstr": "Wall", "package": "IfcSharedBldgElements"}
    monkeypatch.setattr(bsdd, "dictionary", lambda doc: ({}, [entry]))
    pot.run("doc", tmp_path)
    assert 'msgid "IfcWall"' in (tmp_path / "bsdd" / "pot" / "IfcSharedBldgElements.pot").read_text(encoding="utf-8")


def test_second_json_run_does_not_duplicate_hierarchy_members(monkeypatch, tmp_path):
    from generators import json as structure

    monkeypatch.chdir(tmp_path)
    pset = SimpleNamespace(package="IfcKernel", type="PSET", name="Pset_X")
    structure.run([pset], tmp_path)
    structure.run([pset], tmp_path)
    hierarchy = json.loads((tmp_path / "structure.json").read_text(encoding="utf-8"))["hierarchy"]
    kernel = dict(dict(hierarchy)["Core data schemas"])["IfcKernel"]
    assert kernel["Property Sets"] == ["Pset_X"]


def test_schema_path_parses_into_entities_that_keep_their_attributes():
    from generators.bsdd import DEFAULT_SCHEMA
    from generators.util.xmi_document import xmi_document

    wall = next(item for item in xmi_document(DEFAULT_SCHEMA) if item.type == "ENTITY" and item.name == "IfcWall")
    assert "PredefinedType" in [attr.name for attr in wall.children]
