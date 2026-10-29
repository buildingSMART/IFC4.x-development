"""
`determine_mvd_scope.py` can be used to generate a list of entities that are INCLUDED in the IFC4X3 Model View Definitions (MVDs)
by extracting the entities listed in concept templates marked as in scope of a given MVD.
The output of that step is `mvd_entity_usage.json` which has the names of the MVDs as keys, with a list of entities as values for each.

This script does the opposite: it generates a list of entities that are EXCLUDED (out of scope) for a given MVD definition
by introspecting the IFC schema and iterating through all entities.
Any entity name not found in `mvd_entity_usage.json` is considered out of scope of that MVD and included in the output `mvd_entity_exclusions.json`.

This list of excluded entities is then included in the MVD best practice checks (e.g. rules IFC430 and IFC431 for IFC 4.3) gherkin rules for the Validation Service

Example usage:
    python determine_mvd_exclusions.py IFC4X3_ADD2 mvd_entity_usage.json
"""
from enum import StrEnum, auto
from typing import Dict, List

import ifcopenshell


class SchemaVersionEnum(StrEnum):
    IFC2X3 = auto()
    IFC4 = auto()
    IFC4X3_ADD2 = auto()


def get_all_entities(schemaversion) -> List[str]:
    entities = list()
    schema_definition = ifcopenshell.schema_by_name(schemaversion.value)
    for declaration in schema_definition.entities():
            entities.append(declaration.name())

    return entities


def get_mvd_entity_usage(data_filename: str = "mvd_entity_usage.json") -> Dict:
    with open(data_filename, 'r') as fd:
        data = json.load(fd)
    return data


def get_mvd_excluded_entities(all_entities: List[str], entity_usage_data: Dict) -> Dict:
    mvd_defs = entity_usage_data.keys()
    excluded_entities = {
        mvd: list() for mvd in mvd_defs
    }

    for mvd in mvd_defs:
        for entity in all_entities:
            try:
                _ = entity_usage_data[mvd][entity]
            except KeyError:
                excluded_entities[mvd].append(entity)

    return excluded_entities


if __name__ == "__main__":
    import sys
    import json

    schema_version_string, entity_usage_filename = sys.argv[1:]

    print(
        f"[INFO] Generating list of excluded (out of scope entities) for {schema_version_string} Model View Definitions...")
    entity_list = get_all_entities(SchemaVersionEnum(schema_version_string.lower()))
    entity_usage = get_mvd_entity_usage(data_filename=entity_usage_filename)

    excluded_entity_data = get_mvd_excluded_entities(all_entities=entity_list, entity_usage_data=entity_usage)

    out_file = "mvd_entity_exclusions.json"
    print(f"[INFO] Writing excluded entities to '{out_file}'...")
    with open(out_file, "w") as f:
        json.dump(excluded_entity_data, f, indent=1)
    print("Done.")
