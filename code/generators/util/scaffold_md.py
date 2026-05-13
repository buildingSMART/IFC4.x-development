"""MD scaffolding tool — generates skeleton .md docs from UML entity/enum names.

Usage:
    python scaffold_md.py <schema_uml_path> <docs_root> <entity_name> [<entity_name>...]

Example:
    python scaffold_md.py \\
        /path/to/schemas/IfcSharedBldgElements.uml \\
        /path/to/docs \\
        IfcArchElement IfcArchElementType IfcArchElementTypeEnum

Reads the UML to determine kind (uml:Class, uml:Enumeration), attributes,
WHERE rules, and supertype. Writes scaffolds to:
    {docs_root}/schemas/<layer>/<schema>/Entities/<Name>.md
    {docs_root}/schemas/<layer>/<schema>/Types/<Name>.md  (for enums)
    {docs_root}/schemas/<layer>/<schema>/PropertySets/<Name>.md  (for psets)

Prose is intentionally placeholder — replace with real content from the
tunnel-team exec summary (or equivalent source) before merge.

Per `local/pipeline-changes.md` item E (Markdown scaffolding) and Thomas's
2026-05-01 ask about reducing the manual MD authoring burden.
"""
import argparse
import sys
from pathlib import Path
from xml.dom import minidom


def _attrs(el):
    return {a.name: a.value for a in (el.attributes or {}).values()}


def _children_by_tag(parent, tag):
    return [c for c in parent.childNodes if c.nodeType == c.ELEMENT_NODE and c.tagName == tag]


def _walk_classes(doc):
    """Yield every <packagedElement> with xmi:type."""
    for el in doc.getElementsByTagName("packagedElement"):
        t = el.getAttribute("xmi:type")
        if t:
            yield el


def _find_entity(doc, name):
    for el in _walk_classes(doc):
        if el.getAttribute("name") == name:
            return el
    return None


def _supertype_name(entity_el):
    """Return the supertype's name if findable via <generalization>."""
    for g in _children_by_tag(entity_el, "generalization"):
        for gen in _children_by_tag(g, "general"):
            href = gen.getAttribute("href")
            if href and "#" in href:
                # <general href="OtherFile.uml#cl_IfcFoo"/>
                _, frag = href.split("#", 1)
                return frag.replace("cl_", "").replace("dt_", "")
        # attribute form: <generalization general="cl_..."/>
        gen_attr = g.getAttribute("general")
        if gen_attr:
            return gen_attr.replace("cl_", "").replace("dt_", "")
    return None


def _own_attrs(entity_el):
    """Return [(name, type_name)] for entity attributes."""
    out = []
    for a in _children_by_tag(entity_el, "ownedAttribute"):
        nm = a.getAttribute("name")
        if not nm:
            continue
        # type may be attribute-form ("type=en_X") or child-href form
        ty = a.getAttribute("type")
        if not ty:
            for tn in _children_by_tag(a, "type"):
                href = tn.getAttribute("href")
                if href and "#" in href:
                    ty = href.split("#", 1)[1]
                    break
        ty = ty.replace("en_", "").replace("dt_", "").replace("cl_", "") if ty else "(unknown)"
        out.append((nm, ty))
    return out


def _where_rules(entity_el):
    """Return [(name, body_first_line)] for owned WHERE rules."""
    rules = []
    for r in _children_by_tag(entity_el, "ownedRule"):
        rname = r.getAttribute("name")
        body = ""
        for spec in _children_by_tag(r, "specification"):
            for bn in _children_by_tag(spec, "body"):
                if bn.childNodes:
                    body = (bn.childNodes[0].nodeValue or "").strip().splitlines()[0][:140]
                    break
        rules.append((rname, body))
    return rules


def _enum_literals(entity_el):
    out = []
    for lit in _children_by_tag(entity_el, "ownedLiteral"):
        nm = lit.getAttribute("name")
        if nm:
            out.append(nm)
    return out


def scaffold_entity(name, supertype, attrs, rules):
    lines = [f"# {name}", ""]
    lines.append(
        f"An _{name}_ represents <!-- FILL IN: short one-paragraph definition. "
        f"Source: tunnel-team exec summary or equivalent. -->"
    )
    lines.append("<!-- end of short definition -->")
    lines.append("")
    lines.append("<!-- FILL IN: extended definition (background, usage notes, references). -->")
    lines.append("")
    if supertype:
        lines.append(
            f"> NOTE Subtype of _{supertype}_ — see that entity's documentation "
            f"for inherited attributes and behavior."
        )
        lines.append("")
    lines.append("> HISTORY New entity in IFC 4.4.")
    lines.append("")

    if attrs:
        lines.append("## Attributes")
        lines.append("")
        for a_name, a_type in attrs:
            lines.append(f"### {a_name}")
            lines.append(
                f"<!-- FILL IN: description of {a_name} ({a_type}). -->"
            )
            lines.append("")

    if rules:
        lines.append("## Formal Propositions")
        lines.append("")
        for r_name, r_body in rules:
            lines.append(f"### {r_name}")
            preview = (r_body or "<!-- FILL IN: rule description -->").replace("\n", " ")
            lines.append(f"<!-- FILL IN: prose explaining the rule. EXPRESS body: `{preview}` -->")
            lines.append("")

    lines.append("## Concepts")
    lines.append("")
    lines.append("<!-- FILL IN: geometry, material, spatial containment concepts. -->")
    lines.append("")

    return "\n".join(lines) + "\n"


def scaffold_enum(name, literals):
    lines = [f"# {name}", ""]
    lines.append(
        f"This enumeration defines the predefined types of <!-- FILL IN: which entity uses this enum -->."
    )
    lines.append("<!-- end of short definition -->")
    lines.append("")
    lines.append("> HISTORY New enumeration in IFC 4.4.")
    lines.append("")
    lines.append("## Items")
    lines.append("")
    for lit in literals:
        lines.append(f"### {lit}")
        lines.append(f"<!-- FILL IN: description of {lit}. -->")
        lines.append("")
    return "\n".join(lines) + "\n"


def find_target_path(uml_path, docs_root, ent_name, kind):
    """Best-effort path resolution: <docs_root>/schemas/<layer>/<schema>/<dir>/<name>.md.

    <schema> is the uml filename stem.
    <layer> is read from <docs_root>/schemas/*/<schema>/ — we don't reliably know
    the layer from the UML, so we look it up in docs_root.
    """
    docs_root = Path(docs_root)
    schema = Path(uml_path).stem  # e.g. IfcSharedBldgElements

    # PEnums live in IfcSharedBldgElements regardless of their UML file (propertytypes.uml)
    if kind == "penum":
        schema = "IfcSharedBldgElements"

    layer = None
    for cand in (docs_root / "schemas").iterdir() if (docs_root / "schemas").is_dir() else []:
        if (cand / schema).is_dir():
            layer = cand.name
            break
    if layer is None:
        layer = "shared"  # fallback

    subdir = {"entity": "Entities", "enum": "Types", "penum": "PropertyEnumerations", "pset": "PropertySets", "qto": "QuantitySets"}[kind]
    return docs_root / "schemas" / layer / schema / subdir / f"{ent_name}.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("uml_path", help="UML file containing the entity/enum")
    parser.add_argument("docs_root", help="Root docs directory (parent of schemas/)")
    parser.add_argument("names", nargs="+", help="Entity / enum names to scaffold")
    parser.add_argument("--force", action="store_true", help="Overwrite existing .md files")
    parser.add_argument("--dry-run", action="store_true", help="Don't write anything, just print")
    args = parser.parse_args()

    doc = minidom.parse(args.uml_path)
    written, skipped = 0, 0

    for nm in args.names:
        el = _find_entity(doc, nm)
        if el is None:
            print(f"[skip] {nm}: not found in {args.uml_path}", file=sys.stderr)
            skipped += 1
            continue

        kind_xmi = el.getAttribute("xmi:type")
        if kind_xmi == "uml:Enumeration":
            content = scaffold_enum(nm, _enum_literals(el))
            kind = "penum" if nm.startswith("PEnum_") else "enum"
        elif kind_xmi == "uml:Class":
            content = scaffold_entity(
                nm, _supertype_name(el), _own_attrs(el), _where_rules(el)
            )
            kind = "qto" if nm.startswith("Qto_") else "pset" if nm.startswith("Pset_") else "entity"
        else:
            print(f"[skip] {nm}: unsupported xmi:type {kind_xmi}", file=sys.stderr)
            skipped += 1
            continue

        target = find_target_path(args.uml_path, args.docs_root, nm, kind)
        if target.exists() and not args.force:
            print(f"[skip] {target} exists; use --force to overwrite", file=sys.stderr)
            skipped += 1
            continue

        if args.dry_run:
            print(f"--- {target} ---")
            print(content)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            print(f"[wrote] {target}")
            written += 1

    print(f"\n{written} written, {skipped} skipped.", file=sys.stderr)


if __name__ == "__main__":
    main()
