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
import csv
import glob
import os
import re
import sys
from pathlib import Path
from xml.dom import minidom


# ---------------------------------------------------------------------------
# DocEntity.xml lookup — pull real attribute / WHERE-rule prose from the
# bSI-InfraRoom/IFC-Specification repo. Path layout:
#   <spec-dir>/IFC4x3/Sections/*/Schemas/*/Entities/<EntityName>/DocEntity.xml
# Entities new in IFC 4.4 (TM16, etc.) won't be present — caller falls back
# to convention-based synthesis (see _synth_attr_doc).
# ---------------------------------------------------------------------------


def _find_doc_entity_xml(spec_dir, entity_name):
    """Return the first DocEntity.xml path matching the entity, or None."""
    if not spec_dir:
        return None
    pattern = os.path.join(
        spec_dir, "IFC4x3", "Sections", "*", "Schemas", "*", "Entities",
        entity_name, "DocEntity.xml",
    )
    hits = glob.glob(pattern)
    return hits[0] if hits else None


def _text_of(node):
    """Concatenate all text-node children of an element."""
    if node is None:
        return ""
    parts = []
    for c in node.childNodes:
        if c.nodeType in (c.TEXT_NODE, c.CDATA_SECTION_NODE):
            parts.append(c.nodeValue or "")
    return "".join(parts)


def _clean_doc_text(s):
    """Normalise the raw <Documentation> text:
    - minidom already decodes &gt; / &lt; / &amp; / &apos; in text content.
    - But the DocEntity sources use a literal '&amp;nbsp;' sequence (an
      escaped HTML entity inside XML); after one round of XML decoding we
      see '&nbsp;' which we want as a real space.
    - Strip trailing whitespace per-line, drop a leading/trailing blank line.
    """
    if not s:
        return ""
    # &amp;nbsp; → &nbsp; → real space (NBSP would also be fine but breaks
    # plain-text diffs; collapse to a regular space).
    s = s.replace("&nbsp;", " ")
    # Some sources double-escape: &amp;amp; → &amp; → keep as-is.
    # Normalise line endings, strip trailing whitespace.
    lines = [ln.rstrip() for ln in s.replace("\r\n", "\n").split("\n")]
    # Drop leading / trailing empties.
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def load_doc_entity(spec_dir, entity_name):
    """Return (attr_docs, rule_docs) dicts read from DocEntity.xml.

    attr_docs: {attribute_name: cleaned documentation string}
    rule_docs: {where_rule_name: cleaned documentation string}

    Returns ({}, {}) when the file is missing or unparseable.
    """
    path = _find_doc_entity_xml(spec_dir, entity_name)
    if not path:
        return {}, {}
    try:
        doc = minidom.parse(path)
    except Exception as e:
        print(f"[warn] failed to parse {path}: {e}", file=sys.stderr)
        return {}, {}

    attr_docs = {}
    for attrs_block in doc.getElementsByTagName("Attributes"):
        for da in _children_by_tag(attrs_block, "DocAttribute"):
            nm = da.getAttribute("Name")
            if not nm:
                continue
            doc_children = _children_by_tag(da, "Documentation")
            if not doc_children:
                continue
            txt = _clean_doc_text(_text_of(doc_children[0]))
            if txt:
                attr_docs[nm] = txt

    rule_docs = {}
    for rules_block in doc.getElementsByTagName("WhereRules"):
        for dr in _children_by_tag(rules_block, "DocWhereRule"):
            nm = dr.getAttribute("Name")
            if not nm:
                continue
            doc_children = _children_by_tag(dr, "Documentation")
            if not doc_children:
                continue
            txt = _clean_doc_text(_text_of(doc_children[0]))
            if txt:
                rule_docs[nm] = txt

    return attr_docs, rule_docs


# ---------------------------------------------------------------------------
# Convention-based synthesis for entities not yet in the IFC-Specification
# repo (new TM16/TM17/... entities). The upstream convention for
# `PredefinedType` is extremely consistent across IfcBeam / IfcColumn /
# IfcWall / IfcSlab / IfcMember / IfcPile etc., so we can synthesise the
# prose from the entity name alone.
# ---------------------------------------------------------------------------


def _entity_noun(entity_name):
    """IfcArchElement → 'arch element'; IfcBeam → 'beam'.

    Split CamelCase, drop the leading 'Ifc', lowercase. Multi-word entities
    get spaces (matching upstream phrasing like 'built element').
    """
    s = entity_name
    if s.startswith("Ifc"):
        s = s[3:]
    # CamelCase split
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    s = re.sub(r"([A-Z])([A-Z][a-z])", r"\1 \2", s)
    return s.lower()


def _indefinite_article(noun):
    """Best-effort a/an. Upstream uses 'a beam', 'a column'; vowel start → 'an'."""
    return "an" if noun[:1] in "aeiou" else "a"


def _synth_attr_doc(entity_name, attr_name, attr_type):
    """Synthesise upstream-convention prose for an attribute.

    Currently handles PredefinedType (the dominant case across TM16-shape
    entities). Returns None for attributes we don't have a convention for —
    caller falls back to the FILL-IN placeholder.
    """
    if attr_name == "PredefinedType":
        noun = _entity_noun(entity_name)
        article = _indefinite_article(noun)
        # Paired type entity name: IfcArchElement → IfcArchElementType.
        type_entity = f"{entity_name}Type"
        return (
            f"Predefined generic type for {article} {noun} that is specified in an "
            f"enumeration. There may be a property set given specifically for the "
            f"predefined types.\n"
            f"> NOTE  The _PredefinedType_ shall only be used, if no _{type_entity}_ "
            f"is assigned, providing its own _{type_entity}.PredefinedType_."
        )
    return None


def _synth_rule_doc(entity_name, rule_name):
    """Synthesise upstream-convention prose for a WHERE rule.

    Handles the two common rules paired with PredefinedType:
    CorrectPredefinedType and CorrectTypeAssigned.
    """
    noun = _entity_noun(entity_name)
    type_entity = f"{entity_name}Type"
    enum_name = f"{entity_name}TypeEnum"
    if rule_name == "CorrectPredefinedType":
        return (
            f"Either the _PredefinedType_ attribute is unset (e.g. because an "
            f"_{type_entity}_ is associated), or the inherited attribute "
            f"_ObjectType_ shall be provided, if the _PredefinedType_ is set to "
            f"USERDEFINED."
        )
    if rule_name == "CorrectTypeAssigned":
        return (
            f"Either there is no {noun} type object associated, i.e. the "
            f"_IsTypedBy_ inverse relationship is not provided, or the associated "
            f"type object has to be of type _{type_entity}_."
        )
    return None


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


def _build_supertype_lookup(uml_dir):
    """Build {entity_name: supertype_name} dict across all .uml files in uml_dir."""
    lookup = {}
    for uml_file in sorted(glob.glob(os.path.join(uml_dir, "*.uml"))):
        try:
            doc = minidom.parse(uml_file)
        except Exception:
            continue
        for el in _walk_classes(doc):
            if el.getAttribute("xmi:type") == "uml:Class":
                nm = el.getAttribute("name")
                sup = _supertype_name(el)
                if nm and nm not in lookup:
                    lookup[nm] = sup
    return lookup


def _supertype_chain(entity_name, lookup):
    """Return ordered chain: [entity, supertype, super-supertype, ...] until root."""
    chain = [entity_name]
    current = entity_name
    seen = {entity_name}
    while current in lookup and lookup[current]:
        sup = lookup[current]
        if sup in seen:
            break
        chain.append(sup)
        seen.add(sup)
        current = sup
    return chain


def _filename_to_heading(csv_filename):
    """PropertySetsforObjects.csv → 'Property Sets for Objects'.

    Handles CamelCase + lowercase prepositions + digit boundaries.
    Best-effort: matches the convention used by the HTML builder.
    """
    name = csv_filename.replace(".csv", "")
    # Pre-split standalone prepositions (must be lowercase island between
    # camelcase boundaries). Only "for", "to", "with", "and", "of" are common
    # in canonical names. Avoid "on"/"in" — too many false positives
    # (e.g. "Classification" → "Classificati on Association").
    for prep in ("for", "to", "with", "and", "of"):
        name = re.sub(r"([a-z])" + prep + r"([A-Z])", r"\1 " + prep + r" \2", name)
    # CamelCase boundaries
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z])([A-Z][a-z])", r"\1 \2", name)
    # Digit-after-lowercase boundary (Axis3DGeometry: don't split 3D itself)
    name = re.sub(r"([a-z])(\d)", r"\1 \2", name)
    return name


# Concept names that are ALWAYS shown when bound to the entity or any
# supertype (vs noisy body-geometry variants). Empirically the top of
# upstream entity MDs.
_PRIORITY_CONCEPTS = {
    "Property Sets for Objects",
    "Object Typing",
    "Quantity Sets",
    "Material Set",
    "Material Profile Set Usage",
    "Material Layer Set Usage",
    "Material Single",
    "Material Constituent Set",
    "Spatial Containment",
    "Product Assignment",
    "Product Local Placement",
    "Element Composition",
    "Element Decomposition",
    "Port Nesting",
    "Aggregation",
}

# Body-geometry variants that bind to most generic supertypes — too many
# to emit them all; user picks the one matching their entity's geometry.
# Treated as a single "family" — at most one shown in the scaffold.
_BODY_GEOMETRY_FAMILY = "Body"


def _applicable_concepts(uml_dir, supertype_chain, max_results=12):
    """For each MVD CSV under <uml_dir>/mvd/GeneralUsage/, return concepts where any
    entity in supertype_chain appears in the ApplicableEntity column.

    Filters: prioritise concepts bound to the entity itself or its direct
    supertype; cap at max_results. Returns list of (concept_heading, inherited_from).
    """
    mvd_dir = os.path.join(uml_dir, "mvd", "GeneralUsage")
    if not os.path.isdir(mvd_dir):
        return []
    chain_set = set(supertype_chain)
    raw = []  # (heading, inherited_from, chain_idx)
    for csv_file in sorted(glob.glob(os.path.join(mvd_dir, "*.csv"))):
        heading = _filename_to_heading(os.path.basename(csv_file))
        try:
            with open(csv_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                best_idx = None
                best_ent = None
                for row in reader:
                    ent = (row.get("ApplicableEntity") or "").strip()
                    if ent in chain_set:
                        idx = supertype_chain.index(ent)
                        if best_idx is None or idx < best_idx:
                            best_idx = idx
                            best_ent = ent
                if best_ent is not None:
                    raw.append((heading, best_ent, best_idx))
        except Exception:
            continue
    # Score: priority concepts ALWAYS first (regardless of inheritance depth),
    # then by chain idx (direct bindings before inherited), then alphabetical.
    def score(item):
        h, ent, idx = item
        is_priority = 0 if h in _PRIORITY_CONCEPTS else 1
        return (is_priority, idx, h)
    raw.sort(key=score)
    # Collapse Body-geometry family: at most one Body* heading, the closest
    # binding. Author can add more after seeing what their entity needs.
    capped = []
    body_seen = False
    for h, ent, idx in raw:
        if h.startswith(_BODY_GEOMETRY_FAMILY) and h not in _PRIORITY_CONCEPTS:
            if body_seen:
                continue
            body_seen = True
        capped.append((h, ent, idx))
        if len(capped) >= max_results:
            break
    return [(h, ent) for h, ent, idx in capped]


def scaffold_entity(name, supertype, attrs, rules, applicable_concepts=None,
                    attr_docs=None, rule_docs=None):
    """Build the .md scaffold body.

    attr_docs / rule_docs: optional dicts of prose harvested from
    DocEntity.xml in the IFC-Specification repo. When a key is present, the
    real prose replaces the FILL-IN placeholder. When absent, we try
    convention-based synthesis (_synth_attr_doc / _synth_rule_doc) and only
    fall back to the FILL-IN placeholder if that also returns None.
    """
    attr_docs = attr_docs or {}
    rule_docs = rule_docs or {}
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
            if a_name in attr_docs:
                lines.append(attr_docs[a_name])
            else:
                synth = _synth_attr_doc(name, a_name, a_type)
                if synth is not None:
                    lines.append(synth)
                else:
                    lines.append(
                        f"<!-- FILL IN: description of {a_name} ({a_type}). -->"
                    )
            lines.append("")

    if rules:
        lines.append("## Formal Propositions")
        lines.append("")
        for r_name, r_body in rules:
            lines.append(f"### {r_name}")
            if r_name in rule_docs:
                lines.append(rule_docs[r_name])
            else:
                synth = _synth_rule_doc(name, r_name)
                if synth is not None:
                    lines.append(synth)
                else:
                    preview = (r_body or "<!-- FILL IN: rule description -->").replace("\n", " ")
                    lines.append(
                        f"<!-- FILL IN: prose explaining the rule. EXPRESS body: `{preview}` -->"
                    )
            lines.append("")

    lines.append("## Concepts")
    lines.append("")
    if applicable_concepts:
        # Data-driven: detected from supertype chain via MVD CSV bindings
        lines.append("<!-- Auto-detected from the supertype chain via MVD CSV bindings in")
        lines.append("     schemas/mvd/GeneralUsage/*.csv. Each heading below is canonical and")
        lines.append("     will be picked up by the HTML builder. Add entity-specific extras")
        lines.append("     (e.g. Body SweptSolid Geometry, Axis 3D Geometry) by appending more")
        lines.append("     ### <heading> sections that match a filename in mvd/GeneralUsage/. -->")
        lines.append("")
        for heading, inherited_from in applicable_concepts:
            comment = ""
            if inherited_from and inherited_from != name:
                comment = f"  <!-- inherited from {inherited_from} -->"
            lines.append(f"### {heading}{comment}")
            lines.append("")
    else:
        # Fallback: emit the 4 most-common canonical headings as a guess
        lines.append("<!-- The subsection headings below MUST match the canonical concept names")
        lines.append("     from schemas/mvd/GeneralUsage/*.csv (189 total). The HTML builder")
        lines.append("     drops non-matching headings silently.")
        lines.append("")
        lines.append("     This is the FALLBACK list (top-4 by frequency in upstream entity MDs).")
        lines.append("     For accurate data-driven detection, run scaffold_md.py from a")
        lines.append("     worktree where schemas/mvd/GeneralUsage/ is accessible. -->")
        lines.append("")
        lines.append("### Property Sets for Objects")
        lines.append("")
        lines.append("### Object Typing")
        lines.append("")
        lines.append("### Quantity Sets")
        lines.append("")
        lines.append("### Material Set")
        lines.append("<!-- Default for most entities. For specific geometries, replace with:")
        lines.append("       ### Material Profile Set Usage  — swept-profile (IfcBeam, IfcColumn,")
        lines.append("                                          IfcArchElement, IfcMember, IfcPile)")
        lines.append("       ### Material Layer Set Usage    — layered (IfcWall, IfcSlab, IfcRoof,")
        lines.append("                                          IfcPlate, IfcCovering)")
        lines.append("       ### Material Single             — uniform single material")
        lines.append("       ### Material Constituent Set    — composite/non-uniform")
        lines.append("     If material doesn't apply to this entity, delete this subsection. -->")
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
    parser.add_argument(
        "--ifc-spec-dir",
        default=None,
        help=(
            "Path to bSI-InfraRoom/IFC-Specification checkout. When set, attribute "
            "and WHERE-rule prose is harvested from "
            "IFC4x3/Sections/*/Schemas/*/Entities/<EntityName>/DocEntity.xml. "
            "Entities not present (e.g. new TM16/TM17 entities) fall back to "
            "convention-based synthesis."
        ),
    )
    args = parser.parse_args()

    doc = minidom.parse(args.uml_path)
    written, skipped = 0, 0

    # Data-driven Concepts: build entity → supertype lookup across all UMLs in
    # the same schemas/ dir, then for each entity find which MVD CSVs bind it
    # (or any of its ancestors). Falls back to the static top-4 list if mvd/
    # isn't available next to the UML.
    uml_dir = str(Path(args.uml_path).parent)
    supertype_lookup = _build_supertype_lookup(uml_dir)

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
            chain = _supertype_chain(nm, supertype_lookup)
            applicable = _applicable_concepts(uml_dir, chain)
            attr_docs, rule_docs = load_doc_entity(args.ifc_spec_dir, nm)
            if args.ifc_spec_dir and not (attr_docs or rule_docs):
                # Useful diagnostic for the common "new entity, no DocEntity.xml"
                # case — silent fallback would otherwise look identical to a
                # bug. Not an error: convention-synthesis still runs.
                print(
                    f"[info] {nm}: no DocEntity.xml under --ifc-spec-dir; "
                    f"falling back to convention-based synthesis",
                    file=sys.stderr,
                )
            content = scaffold_entity(
                nm, _supertype_name(el), _own_attrs(el), _where_rules(el),
                applicable_concepts=applicable,
                attr_docs=attr_docs, rule_docs=rule_docs,
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
