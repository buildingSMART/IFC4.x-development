import pytest

from generators.json import _synthesize_pset_concepts_from_uml


def _has(concepts, concept, entity, predef, pset):
    rows = concepts.get("GeneralUsage", {}).get(concept, [])
    return any(
        r.get("ApplicableEntity") == entity
        and r.get("PredefinedType", "") == predef
        and r.get("PsetName") == pset
        for r in rows
    )


TM16 = {
    "id": "TM16",
    "psets": {
        "Pset_ArchElementCommon": {"applicability": ["IfcArchElement"]},
        "Pset_ArchElementTypeSegment": {"applicability": ["IfcArchElement/SEGMENT"]},
        "Pset_ArchElementTypeSteelRib": {"applicability": ["IfcArchElement/STEELRIB"]},
        "Qto_ArchElementBaseQuantities": {"applicability": ["IfcArchElement"]},
    },
    "supertype": {
        "IfcArchElement": "IfcBuildingElement",
        "IfcArchElementType": "IfcBuildingElementType",
    },
    "expected_bindings": [
        ("PropertySetsforObjects", "IfcArchElement", "",         "Pset_ArchElementCommon"),
        ("PropertySetsforObjects", "IfcArchElement", "SEGMENT",  "Pset_ArchElementTypeSegment"),
        ("PropertySetsforObjects", "IfcArchElement", "STEELRIB", "Pset_ArchElementTypeSteelRib"),
        ("QuantitySets",           "IfcArchElement", "",         "Qto_ArchElementBaseQuantities"),
    ],
    "leak_marker": "ArchElement",
}

TM24 = {
    "id": "TM24",
    "psets": {
        "Pset_GeoAspects": {
            "applicability": ["IfcTunnelTypicalSection/GEOTECH"],
        },
        "Pset_PreSupportCommon": {
            "applicability": [
                "IfcBuiltSystem/TUNNEL_PRESUPPORT",
                "IfcTunnelTypicalSection/EXCAVATIONSUPPORT",
                "IfcElementAssembly/PRESUPPORTVAULT",
                "IfcElementAssembly/PRESUPPORTFACE",
            ],
        },
        "Pset_SupportCommon": {
            "applicability": [
                "IfcBuiltSystem/TUNNEL_SUPPORT",
                "IfcTunnelTypicalSection/EXCAVATIONSUPPORT",
            ],
        },
    },
    "supertype": {
        "IfcTunnelTypicalSection": "IfcSpatialZone",
        "IfcBuiltSystem":          "IfcSystem",
        "IfcElementAssembly":      "IfcElement",
    },
    "expected_bindings": [
        ("PropertySetsforObjects", "IfcTunnelTypicalSection", "GEOTECH",           "Pset_GeoAspects"),
        ("PropertySetsforObjects", "IfcBuiltSystem",          "TUNNEL_PRESUPPORT", "Pset_PreSupportCommon"),
        ("PropertySetsforObjects", "IfcTunnelTypicalSection", "EXCAVATIONSUPPORT", "Pset_PreSupportCommon"),
        ("PropertySetsforObjects", "IfcElementAssembly",      "PRESUPPORTVAULT",   "Pset_PreSupportCommon"),
        ("PropertySetsforObjects", "IfcElementAssembly",      "PRESUPPORTFACE",    "Pset_PreSupportCommon"),
        ("PropertySetsforObjects", "IfcBuiltSystem",          "TUNNEL_SUPPORT",    "Pset_SupportCommon"),
        ("PropertySetsforObjects", "IfcTunnelTypicalSection", "EXCAVATIONSUPPORT", "Pset_SupportCommon"),
    ],
    "leak_marker": "Tunnel",
}


def _run_synthesis(pkg):
    xmi_concepts = {}
    _synthesize_pset_concepts_from_uml(xmi_concepts, pkg["psets"], pkg["supertype"])
    return xmi_concepts


@pytest.mark.parametrize("pkg", [pytest.param(TM16, id="TM16"), pytest.param(TM24, id="TM24")])
class TestCase:
    def test_all_expected_bindings_present(self, pkg):
        result = _run_synthesis(pkg)
        for concept, entity, predef, pset_name in pkg["expected_bindings"]:
            assert _has(result, concept, entity, predef, pset_name), (
                f"Missing: GeneralUsage/{concept} {entity}/{predef!r} -> {pset_name}"
            )

    def test_package_psets_do_not_leak_to_other_buckets(self, pkg):
        result = _run_synthesis(pkg)
        for concept in (
            "PropertySetsforMaterials",
            "PropertySetsforProfiles",
            "PropertySetsforContexts",
            "PropertySetsforPerformance",
        ):
            for row in result.get("GeneralUsage", {}).get(concept, []):
                assert pkg["leak_marker"] not in row.get("ApplicableEntity", ""), (
                    f"{pkg['id']} leaked to {concept}: {row}"
                )


ALL_BRANCHES_PSETS = {
    "Pset_WallCommon":         {"applicability": ["IfcWall", "IfcWall"]},
    "Pset_FooPHistory":        {"applicability": ["IfcFoo"]},
    "Pset_MaterialCommon":     {"applicability": ["IfcMaterial"]},
    "Pset_ProfileMechanical":  {"applicability": ["IfcArbitraryClosedProfileDef"]},
    "Pset_ProjectCommon":      {"applicability": ["IfcProject"]},
    "Qto_WallBaseQuantities":  {"applicability": ["IfcWall"]},
}

ALL_BRANCHES_SUPERTYPE = {
    "IfcMaterial":                  "IfcMaterialDefinition",
    "IfcArbitraryClosedProfileDef": "IfcProfileDef",
    "IfcProject":                   "IfcContext",
}

_ALL_CONCEPTS = (
    "PropertySetsforObjects",
    "PropertySetsforPerformance",
    "PropertySetsforMaterials",
    "PropertySetsforProfiles",
    "PropertySetsforContexts",
    "QuantitySets",
)


def _run_all_branches():
    xmi_concepts = {}
    _synthesize_pset_concepts_from_uml(xmi_concepts, ALL_BRANCHES_PSETS, ALL_BRANCHES_SUPERTYPE)
    return xmi_concepts


def test_no_duplicate_rows_per_bucket():
    result = _run_all_branches()
    for concept in _ALL_CONCEPTS:
        rows = result.get("GeneralUsage", {}).get(concept, [])
        unique = {(r["ApplicableEntity"], r.get("PredefinedType", ""), r["PsetName"]) for r in rows}
        assert len(rows) == len(unique), f"Duplicate rows in {concept}: {len(rows)} total, {len(unique)} unique"


def test_synthesized_view_name_is_generalusage():
    result = _run_all_branches()
    gu = result.get("GeneralUsage", {})
    for concept in _ALL_CONCEPTS:
        assert gu.get(concept), f"Missing concept under GeneralUsage: {concept}"
    assert "PropertySets" not in result
    assert "QuantitySets" not in result
