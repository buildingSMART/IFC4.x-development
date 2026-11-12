from generators.html.search import SearchIndexBuilder, split_words


def test_split_words_camel_case():
    assert split_words("IfcCurtainWall") == ["curtain", "wall"]


def test_split_words_allcaps_via_wordninja():
    assert split_words("APPROACHSIGNAL") == ["approach", "signal"]


def test_split_words_pset_and_penum_identifiers():
    assert split_words("Pset_WallCommon") == ["pset", "wall", "common"]
    assert split_words("PEnum_LifeCyclePhase") == ["p", "enum", "life", "cycle", "phase"]


def test_split_words_drops_punctuation():
    assert split_words("IfcWall.Name, IfcSlab") == ["wall", "name", "slab"]


def test_split_words_numbered_heading():
    assert split_words("8.4.3.2 IfcDoor") == ["8", "4", "3", "2", "door"]


def test_document_keeps_identifier_and_emits_title_words(tmp_path):
    pages = {"penum.html": "PEnum_LifeCyclePhase", "chapter.html": "8 Core data schemas"}
    for name, heading in pages.items():
        (tmp_path / name).write_text(f"<html><body><div id='main-content'><h1>{heading}</h1><p>Body text.</p></div></body></html>")
    penum, chapter = SearchIndexBuilder(tmp_path).build(["/penum.html", "/chapter.html"])
    assert (penum["title"], penum["title_words"]) == ("PEnum_LifeCyclePhase", "p enum life cycle phase")
    assert (chapter["title"], chapter["title_words"]) == ("Core data schemas", "")
