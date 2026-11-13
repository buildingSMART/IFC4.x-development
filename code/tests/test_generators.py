import json
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


def test_second_json_run_does_not_duplicate_hierarchy_members(monkeypatch, tmp_path):
    from generators import json as structure

    monkeypatch.chdir(tmp_path)
    pset = SimpleNamespace(package="IfcKernel", type="PSET", name="Pset_X")
    structure.run([pset], tmp_path)
    structure.run([pset], tmp_path)
    hierarchy = json.loads((tmp_path / "structure.json").read_text(encoding="utf-8"))["hierarchy"]
    kernel = dict(dict(hierarchy)["Core data schemas"])["IfcKernel"]
    assert kernel["Property Sets"] == ["Pset_X"]
