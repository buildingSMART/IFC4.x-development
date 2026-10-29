import os
import polib
from pathlib import Path
import importlib
import pytest 
import sys 
import subprocess

JOBS = int(os.environ.get("TRANSLATE_JOBS", os.cpu_count() or 1))

REPO_URL = "https://github.com/buildingSMART/IFC4.3.x-output.git"
REPO_BRANCH = os.environ.get("TRANSLATIONS_BRANCH", "translations")

def write_po(po_path: Path, entries: dict[str, str]) -> None:
    po_path.parent.mkdir(parents=True, exist_ok=True)
    po = polib.POFile()
    for k, v in entries.items():
        po.append(polib.POEntry(msgid=k, msgstr=v))
    po.save(po_path.as_posix())

def mo_for(src_dir: Path, build_dir: Path, po_path: Path) -> Path:
    rel = os.path.relpath(po_path.as_posix(), src_dir.as_posix())
    rel_mo = os.path.splitext(rel)[0] + ".mo"
    return build_dir / rel_mo

def test_build_cache_first_and_incremental(tmp_path, monkeypatch):
    src = tmp_path / "translations_repo" / "translations"
    build = tmp_path / "compiled"
    po_hash = build / "po_hash_map.json"

    # point translate.py to our temp dirs
    monkeypatch.setenv("TRANSLATIONS_SRC_DIR", src.as_posix())
    monkeypatch.setenv("TRANSLATIONS_BUILD_DIR", build.as_posix())
    monkeypatch.setenv("PO_HASH_PATH", po_hash.as_posix())

    # Import fresh module after setting env
    translate = importlib.import_module("generators.html.translate")
    importlib.reload(translate)

    # 1) create a minimal .po (Dutch)
    po_path = src / "nl-NL" / "IfcWall_(Dutch).po"
    write_po(po_path, {
        "IfcWall": "Wand",
        "IfcWall_DESCRIPTION": "Beschrijving",
    })

    # 2) first build (clean + hash)
    rc = translate.build_cache(clean=True, jobs=JOBS, pool="thread")
    assert rc == 0
    assert build.is_dir()
    assert po_hash.is_file()

    mo_path = mo_for(src, build, po_path)
    assert mo_path.is_file()

    langs = translate.list_languages()
    assert "Dutch" in langs

    out = translate.translate_resource("Dutch", "IfcWall")
    assert out["resource_translation"] == "Wand"
    assert out["DESCRIPTION"] == "Beschrijving"

    write_po(po_path, {
        "IfcWall": "Wand",
        "IfcWall_DESCRIPTION": "Beschrijving",
        "IfcWall_DEFINITION": "Definitie",
    })
    rc2 = translate.build_cache(jobs=JOBS, pool="thread")
    translate.clear_translation_caches()
    assert rc2 == 0

    out2 = translate.translate_resource("Dutch", "IfcWall")
    assert out2["DEFINITION"] == "Definitie"

    po_path.unlink()
    rc3 = translate.build_cache(jobs=JOBS, pool="thread")
    assert rc3 == 0

def test_compiled_lang_dir_for_and_iter_mo(tmp_path, monkeypatch):
    src = tmp_path / "translations_repo" / "translations"
    build = tmp_path / "compiled"
    po_hash = build / "po_hash_map.json"

    monkeypatch.setenv("TRANSLATIONS_SRC_DIR", src.as_posix())
    monkeypatch.setenv("TRANSLATIONS_BUILD_DIR", build.as_posix())
    monkeypatch.setenv("PO_HASH_PATH", po_hash.as_posix())

    translate = importlib.import_module("generators.html.translate")
    importlib.reload(translate)

    po_nl = src / "nl-NL" / "IfcDoor_(Dutch).po"
    po_de = src / "de-DE" / "IfcDoor_(German).po"
    write_po(po_nl, {"IfcDoor": "Deur"})
    write_po(po_de, {"IfcDoor": "Tür"})

    rc = translate.build_cache(clean=True, use_hash=True, jobs=JOBS, pool="process")
    assert rc == 0
    compiled_nl_dir = translate.compiled_lang_dir_for("Dutch")
    assert Path(compiled_nl_dir).is_dir()
    mos_nl = translate.iter_mo_files_for_lang("Dutch")
    assert any(fn.endswith(".mo") for fn in mos_nl)

    compiled_de_dir = translate.compiled_lang_dir_for("German")
    assert Path(compiled_de_dir).is_dir()
    mos_de = translate.iter_mo_files_for_lang("German")
    assert any(fn.endswith(".mo") for fn in mos_de)


def test_list_languages_cached(tmp_path, monkeypatch):
    src = tmp_path / "translations_repo" / "translations"
    build = tmp_path / "compiled"
    po_hash = build / "po_hash_map.json"

    monkeypatch.setenv("TRANSLATIONS_SRC_DIR", src.as_posix())
    monkeypatch.setenv("TRANSLATIONS_BUILD_DIR", build.as_posix())
    monkeypatch.setenv("PO_HASH_PATH", po_hash.as_posix())
    
    monkeypatch.setenv("LANG_MAP_TTL", "1")

    translate = importlib.import_module("generators.html.translate")
    importlib.reload(translate)

    write_po(src / "nl-NL" / "IfcWall_(Dutch).po", {"IfcWall": "Wand"})
    translate.build_cache(clean=True, use_hash=True, jobs=JOBS, pool="thread")

    langs1 = translate.list_languages()
    assert "Dutch" in langs1

    write_po(src / "fr-FR" / "IfcWall_(French).po", {"IfcWall": "Mur"})
    langs_cached = translate.list_languages()
    assert "French" not in langs_cached

    import time as _t
    _t.sleep(1.2)
    langs2 = translate.list_languages()
    assert "French" in langs2


@pytest.mark.integration
def test_build_cache_against_live_repo(tmp_path, monkeypatch):

    repo_dir = tmp_path / "translations_repo"
    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, repo_dir.as_posix()],
        check=True
    )

    src = repo_dir / "translations"            
    build = tmp_path / "compiled"
    po_hash = build / "po_hash_map.json"

    monkeypatch.setenv("TRANSLATIONS_SRC_DIR", src.as_posix())
    monkeypatch.setenv("TRANSLATIONS_BUILD_DIR", build.as_posix())
    monkeypatch.setenv("PO_HASH_PATH", po_hash.as_posix())

    if "generators.html.translate" in sys.modules:
        del sys.modules["generators.html.translate"]
    translate = importlib.import_module("generators.html.translate")

    rc = translate.build_cache(clean=True, jobs=JOBS, pool="process")
    assert rc == 0
    assert build.is_dir()

    langs = translate.list_languages()
    assert isinstance(langs, list) and len(langs) > 0

    try:
        _ = translate.get_translations("IfcWall")
    except Exception as e:
        pytest.fail(f"Failed to translate against live repo: {e}")