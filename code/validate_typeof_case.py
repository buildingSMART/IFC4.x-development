"""Validate type-name literals in TYPEOF membership and set intersections in EXPRESS."""

import argparse
from pathlib import Path

import pyparsing as pp


def wrong_case_literals(schema):
    """Yield the line number and quoted spelling of each non-uppercase type name."""
    string = pp.Regex(r"'(?:''|[^'])*'")
    remark = pp.Regex(r"--[^\n]*") | pp.nested_expr("(*", "*)", ignore_expr=None)
    typeof = (
        pp.CaselessKeyword("TYPEOF") + pp.nested_expr(ignore_expr=string | remark)
    ).suppress()

    def record_literal(source, offset, tokens):
        return [(pp.lineno(offset, source), tokens[0])]

    literal = string.copy().set_parse_action(record_literal)
    names = pp.Suppress("[") + literal + pp.ZeroOrMore(pp.Suppress(",") + literal) + pp.Suppress("]")
    times = pp.Suppress("*")
    comparison = (
        (literal + pp.CaselessKeyword("IN").suppress() + typeof)
        | (typeof + times + names)
        | (names + times + typeof)
    ).ignore(remark)

    # Consume other strings and comments whole so their contents cannot match.
    expressions = remark.suppress() | comparison | string.suppress()
    for literals, _, _ in expressions.scan_string(schema):
        for line, name in literals:
            if name != name.upper():
                yield line, name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema", type=Path, help="Generated EXPRESS file to check")
    path = parser.parse_args().schema
    errors = list(wrong_case_literals(path.read_text(encoding="utf-8")))
    for line, name in errors:
        print(f"::error::{path}:{line}: TYPEOF compares against {name}, expected {name.upper()}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
