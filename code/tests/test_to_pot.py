from to_bsdd import pot_entry
from to_pot import dedupe_translations, write_pot_files


def test_pot_files_group_by_package_and_dedupe_first_wins(tmp_path, caplog):
    to_translate = [
        pot_entry("IfcWall", "Wall", "Core"),
        pot_entry("IfcWall_DEFINITION", "A wall.", "Core"),
        pot_entry("IfcWall", "Wall", "Core"),                 # identical duplicate: silent
        pot_entry("IfcWall_DEFINITION", "Another wall.", "Core"),  # conflicting duplicate: warned
        pot_entry("FireRating", "Fire Rating", "Shared"),
        pot_entry("", "dropped", "Core"),
        pot_entry("NoSource", "", "Core"),
    ]
    deduped = dedupe_translations(to_translate)
    assert [t["msgid"] for t in deduped] == ["IfcWall", "IfcWall_DEFINITION", "FireRating"]
    assert deduped[1]["msgstr"] == "A wall."
    assert "IfcWall_DEFINITION" in caplog.text

    write_pot_files(to_translate, tmp_path)
    core = (tmp_path / "pot" / "Core.pot").read_text(encoding="utf-8")
    assert 'msgid "IfcWall"\nmsgstr "Wall"' in core and core.count('msgid "IfcWall"') == 1
    assert "X-Crowdin-SourceKey: msgstr" in core
    shared = (tmp_path / "pot" / "Shared.pot").read_text(encoding="utf-8")
    assert 'msgid "FireRating"\nmsgstr "Fire Rating"' in shared
