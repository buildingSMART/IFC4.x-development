"""csv_to_penum_md.py

Generates PropertyEnumeration markdown docs from the normalized PEnum CSV.

Input CSV columns (as produced by ifc4x4_properties/normalize_penums.py):
    Index, Penum Name, Original Values, Values for initial upload,
    Explanation for changes made on values, Original Description

For each PEnum it writes <output_dir>/<Penum Name>.md in the format the
HTML generator expects (matching e.g. PEnum_BoreholeState.md): a header,
a short-definition paragraph, the end-of-short-definition marker, then
an "## Items" section with "### <VALUE>" headings + their descriptions.

The short-definition line is left as a TODO placeholder. The CSV does not
carry a PEnum-level description; authors fill it in by hand after running.

Usage:
    python csv_to_penum_md.py <csv_path> <output_dir> [--name PEnum_Foo ...]

Examples:
    # Just one PEnum (TM-16):
    python csv_to_penum_md.py \\
        /path/to/1_penum_normalized.csv \\
        ../docs/schemas/shared/IfcSharedBldgElements/PropertyEnumerations \\
        --name PEnum_SegmentJointType

    # Every PEnum in the CSV at once:
    python csv_to_penum_md.py /path/to/1_penum_normalized.csv ./out
"""

import argparse
import csv
from collections import OrderedDict
from pathlib import Path


def read_groups(csv_path: Path) -> "OrderedDict[str, list[tuple[str, str]]]":
    groups: "OrderedDict[str, list[tuple[str, str]]]" = OrderedDict()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("Penum Name") or "").strip()
            value = (row.get("Values for initial upload") or "").strip()
            desc = (row.get("Original Description") or "").strip()
            if not name or not value:
                continue
            groups.setdefault(name, []).append((value, desc))
    return groups


def render_md(name: str, items: list[tuple[str, str]]) -> str:
    lines = [
        f"# {name}",
        "",
        f"<!-- TODO: short definition of {name} -->",
        "<!-- end of short definition -->",
        "",
        "## Items",
        "",
    ]
    for value, desc in items:
        lines.append(f"### {value}")
        if desc:
            lines.append(desc)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", type=Path, help="normalized PEnum CSV path")
    p.add_argument("output_dir", type=Path, help="target PropertyEnumerations dir")
    p.add_argument("--name", action="append", default=[],
                   help="restrict to named PEnum (repeatable). Omit to emit every PEnum in the CSV.")
    args = p.parse_args()

    groups = read_groups(args.csv)
    targets = args.name or list(groups.keys())

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name in targets:
        if name not in groups:
            print(f"warning: {name} not in CSV — skipping")
            continue
        out = args.output_dir / f"{name}.md"
        out.write_text(render_md(name, groups[name]), encoding="utf-8")
        print(f"wrote {out}  ({len(groups[name])} values)")


if __name__ == "__main__":
    main()
