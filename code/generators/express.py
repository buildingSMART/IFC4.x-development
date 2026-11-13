import argparse
import logging
from pathlib import Path

import express

from .util.xmi_document import SCHEMA_NAME, xmi_document

CODE_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = CODE_DIR.parent

logging.basicConfig(level=logging.DEBUG)

# The order in which definitions are to appear in the Express schema
EXPRESS_ORDER = ("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")


def sort_key(tup):
    return (EXPRESS_ORDER.index(tup.type), tup.name)


def write_express(doc, output_path: Path) -> None:
    emitted = set()
    definitions = sorted((x for x in doc if x.type in EXPRESS_ORDER), key=sort_key)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output:
        print("SCHEMA %s;" % SCHEMA_NAME, file=output)
        print(file=output)

        for itm in definitions:
            if (itm.type, itm.name) in emitted:
                logging.warning("duplicate definition for %s %s", itm.type, itm.name)
                continue

            emitted.add((itm.type, itm.name))
            print(itm.definition, file=output)
            print(file=output)

        print("END_SCHEMA;", file=output)


def run(doc, output_dir: Path) -> None:
    write_express(doc, output_dir / "IFC.exp")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate the IFC EXPRESS schema.")
    parser.add_argument("schema", type=Path, help="Path to the input schema XML.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=REPO_ROOT / "output" / "IFC.exp",
        help="Path to the generated EXPRESS file.",
    )
    args = parser.parse_args(argv)

    write_express(xmi_document(str(args.schema)), args.output)


if __name__ == "__main__":
    main()
