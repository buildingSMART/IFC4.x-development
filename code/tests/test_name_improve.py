import pytest

from name_improve import INPUT_CORRECTIONS, definition_improve, name_improve

# one case per rendering rule; the id names what the case proves.
# bare correction keys are not listed here, they are covered wholesale below.
CASES = [
    ("ifc-prefix-then-camel-split", "IfcActionRequest", "Action Request"),
    ("wordninja-splits-allcaps", "APPROACHSIGNAL", "Approach Signal"),
    ("aggregation-suffix", "Locations_LU[1:?]_L[1:2]", "Locations"),
    ("acronym-after-camel-split", "GlobalId", "Global ID"),
    ("acronym-trailing", "IfcGeographicCRS", "Geographic CRS"),
    ("digits-separated", "IC60269", "IC 60269"),
    ("trailing-plural-merged", "HEATEXCHANGERS", "Heat Exchangers"),
    ("longest-correction-wins", "IfcElectricApplianceDISHWASHER", "Electric Appliance Dishwasher"),
    ("pset-prefix-dropped", "Pset_WallCommon", "Wall Common"),
    ("prefix-rule-not-over-applied", "Relaxations", "Relaxations"),
    ("predefined-type-concatenation", "IfcWallSOLIDWALL", "Wall Solid Wall"),
    ("correction-inside-compound", "IfcFacilityPartCommonBELOWGROUND", "Facility Part Common Belowground"),
    ("no-correction-needed", "IfcFacilityPartCommonABOVEGROUND", "Facility Part Common Aboveground"),
    ("underscores-and-lowercase-connector", "WELDED_AND_INSERTABLE", "Welded and Insertable"),
]


@pytest.mark.parametrize("src, want", [(src, want) for _, src, want in CASES],
                         ids=[name for name, _, _ in CASES])
def test_name_improve(src, want):
    assert name_improve(src) == want


def test_every_input_correction_renders_to_its_own_value():
    wrong = {src: name_improve(src) for src, want in INPUT_CORRECTIONS.items() if name_improve(src) != want}
    assert not wrong


def test_definition_improve_flattens_linebreaks():
    assert definition_improve("A wall.\n\nMore text.") == "A wall.; More text."
