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


def test_application_unique_rule_descriptions(tmp_path):
    from generators.html.builder import StaticTemplateRenderer
    from generators.html.config import BuildConfig

    renderer = StaticTemplateRenderer(
        BuildConfig.from_repo_root(tmp_path),
        structure={"entity_where_clauses": {"IfcApplication": [
            ("UR1", "UNIQUE ApplicationIdentifier"),
            ("UR2", "UNIQUE ApplicationFullName, Version"),
        ]}},
    )

    result = renderer.get_formal_propositions(
        "IfcApplication", SimpleNamespace(formal_propositions=[])
    )

    assert [(item["name"], item["description"]) for item in result["items"]] == [
        ("UR1", "The attribute ApplicationIdentifier should be unique"),
        ("UR2", "The combination of attributes ApplicationFullName and Version should be unique"),
    ]
