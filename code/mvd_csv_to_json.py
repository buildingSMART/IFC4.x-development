"""Write xmi_mvd_concepts.json from schemas/mvd.csv.

The CSV lists the concept templates (column 3, "<section number>  <name>") and one
column per model view definition; a non-empty cell means the concept is part of
that view. The JSON maps view name -> list of concept names with all non-word
characters removed, which is the key format determine_mvd_scope.py and the HTML
generator (concept listing) expect. This used to be the tail of the deprecated
extract_concepts_from_xmi.py.

Usage: python mvd_csv_to_json.py ../schemas [output.json]
"""
import csv
import json
import os
import re
import sys


def main(schemas_dir, output="xmi_mvd_concepts.json"):
    with open(os.path.join(schemas_dir, "mvd.csv"), newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter=",", quotechar='"'))
    views = {v.strip(): i for i, v in enumerate(rows[0]) if v.strip()}
    concepts = {
        view: [
            re.sub(r"[^\w]", "", re.split(r"\s+", row[3], maxsplit=1)[1])
            for row in rows[2:]
            if row[column].strip()
        ]
        for view, column in views.items()
    }
    with open(output, "w", encoding="utf-8") as f:
        json.dump(concepts, f, indent=1)
    for view, names in concepts.items():
        print(f"{view}: {len(names)} concepts")


if __name__ == "__main__":
    main(*sys.argv[1:3])
