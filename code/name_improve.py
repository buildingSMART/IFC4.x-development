import json
import re
from pathlib import Path

import wordninja

from extract_definition import MARKER

_corrections = json.loads(
    Path(__file__).with_name("name_corrections.json").read_text("utf-8")
)
INPUT_CORRECTIONS = _corrections["input_corrections"]
TOKEN_RENDER = {k.lower(): v for k, v in _corrections["token_render"].items()}
CORRECTION_PATTERN = re.compile(
    "|".join(re.escape(k) for k in sorted(INPUT_CORRECTIONS, key=len, reverse=True))
)

AGGREGATION_BOUND = re.compile(r"_\w+\[")  # IfcComplexNumber_A[1:2] -> IfcComplexNumber
CAMEL_BOUNDARY = re.compile(
    r"(?<=[a-z])(?=[A-Z0-9])"
    r"|(?<=[A-Z][A-Z])(?=[0-9])"
    r"|(?<=[0-9])(?=[a-z])"
    r"|(?<=[0-9])(?=[A-Z][A-Za-z])"
    r"|(?<=[A-Z])(?=[A-Z][a-z])"
)

MAX_ACRONYM_LEN = 4
PLURAL_TAIL = re.compile(r"^[A-Z](s|es)$")
ACRONYM_PLURAL = re.compile(rf"^[A-Z]{{2,{MAX_ACRONYM_LEN}}}(s|es)$")

MULTIPLE_LINEBREAK_PATTERN = re.compile("\n+")
MULTIPLE_SPACE_PATTERN = re.compile(r"\s+")
HTML_TAG_PATTERN = re.compile("<.*?>")
CURLY_BRACKET_PATTERN = re.compile(
    "{.*?}.*"
)  # also removes all text after curly brackets
FIGURE_PATTERN = re.compile("[^.,;]*(Figure|the figure)[^.,;]*")
LIST_PATTERN = re.compile(r"[^.,;]*:\s?")

REPLACEMENTS = [
    (MULTIPLE_LINEBREAK_PATTERN, "; "),
    (re.compile(r"\*{2}"), " "),
    (re.compile(r":(?!\s)"), ": "),
    (re.compile(r"SELF\\"), ""),
    (
        re.compile(r"(?<!\.)\.\.(?!\.)"),
        ".",
    ),  # remove double dots but not triple (ellipsis)
    (HTML_TAG_PATTERN, " "),
    (CURLY_BRACKET_PATTERN, " "),
    (FIGURE_PATTERN, ""),
    (LIST_PATTERN, ""),
    (MULTIPLE_SPACE_PATTERN, " "),
]


DROPPED_PREFIX_TOKENS = {"rel", "pset", "qto"}


def _split_identifier(s):
    s = s.removeprefix("Ifc")
    out = []
    for piece in re.split(r"[_\s]+", s):
        out.extend(t for t in CAMEL_BOUNDARY.split(piece) if t)
    if out and out[0].lower() in DROPPED_PREFIX_TOKENS:
        out = out[1:]
    return out


def _rejoin_acronym_fragments(tokens):
    # ['I','Ds'] -> ['IDs']; ['CO','2'] -> ['co2']
    out, i = [], 0
    while i < len(tokens):
        cur, nxt = tokens[i], tokens[i + 1] if i + 1 < len(tokens) else None
        if (
            nxt
            and cur.isalpha()
            and cur.isupper()
            and len(cur) <= MAX_ACRONYM_LEN
            and PLURAL_TAIL.match(nxt)
        ):
            out.append(cur + nxt)
            i += 2
        elif nxt and (cur + nxt).lower() in TOKEN_RENDER:
            out.append((cur + nxt).lower())
            i += 2
        else:
            out.append(cur)
            i += 1
    return out


def _render(tokens):
    rendered = []
    for t in tokens:
        override = TOKEN_RENDER.get(t.lower())
        if override is not None:
            if override.islower() and not rendered:
                rendered.append(override.capitalize())
            else:
                rendered.append(override)
        elif t.isdigit() or ACRONYM_PLURAL.match(t):
            rendered.append(t)
        else:
            rendered.append(t.capitalize())
    return " ".join(rendered)


def _merge_plural_s(pieces):
    # ['EXCHANGER', 'S'] -> ['EXCHANGERS']
    merged = []
    for piece in pieces:
        if piece.lower() == "s" and merged:
            merged[-1] += piece
        else:
            merged.append(piece)
    return merged


def _render_span(s):
    tokens = []
    for tok in _split_identifier(s):
        if (
            tok.isalpha()
            and tok.isupper()
            and len(tok) > MAX_ACRONYM_LEN
            and tok.lower() not in TOKEN_RENDER
        ):
            tokens.extend(_merge_plural_s(wordninja.split(tok)))
        else:
            tokens.append(tok)
    return _render(_rejoin_acronym_fragments(tokens))


def _split_into_literal_and_process_parts(s):
    parts, last = [], 0
    for m in CORRECTION_PATTERN.finditer(s):
        if m.start() > last:
            parts.append(("process", s[last : m.start()]))
        parts.append(("literal", INPUT_CORRECTIONS[m.group(0)]))
        last = m.end()
    if last < len(s):
        parts.append(("process", s[last:]))
    return parts


def name_improve(s):
    s = AGGREGATION_BOUND.split(s)[0]
    out = []
    for kind, val in _split_into_literal_and_process_parts(s):
        if kind == "literal":
            out.append(val)
        else:
            rendered = _render_span(val)
            if rendered:
                out.append(rendered)
    return " ".join(out).strip()


def remove_unwanted(s):
    for pat, subs in REPLACEMENTS:
        s = re.sub(pat, subs, s)
    return s


def clean(s):
    s = remove_unwanted(s)
    cleaned = "".join(
        c for c in s if c.isalnum() or c in ":.,()-+ —=;α°_/!?$%@<>'\"\\*"
    )
    cleaned = cleaned.replace('"', "'")
    return re.sub(MULTIPLE_SPACE_PATTERN, " ", cleaned).strip()


def definition_improve(s):
    return clean(s.split(MARKER.strip(), 1)[0].strip())
