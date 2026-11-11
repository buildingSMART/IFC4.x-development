import argparse
from pathlib import Path

from . import bsdd, express, json, pset, xsd
from .util.xmi_document import xmi_document

REPO_ROOT = Path(__file__).resolve().parents[2]

STEPS = {
    "express": express.run,
    "xsd": xsd.run,
    "pset": pset.run,
    "json": json.run,
    "bsdd": bsdd.run,  # last: sets doc.should_translate_pset_types = False
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Parse the IFC UML schema once and generate the output files.")
    parser.add_argument("schema", type=Path, help="Path to the input schema UML.")
    parser.add_argument("-o", "--output", type=Path, default=REPO_ROOT / "output", help="Output directory.")
    parser.add_argument("--only", nargs="+", choices=STEPS, default=list(STEPS), help="Run only these steps, always in pipeline order.")
    args = parser.parse_args(argv)

    doc = xmi_document(args.schema)
    for name, step in STEPS.items():
        if name in args.only:
            step(doc, args.output)


if __name__ == "__main__":
    main()
