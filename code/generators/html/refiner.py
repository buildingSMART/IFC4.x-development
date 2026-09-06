from __future__ import annotations

from dataclasses import dataclass
from html import escape
import re
import sys
import uuid
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse, urlunparse

import bs4
from pygments.formatters import HtmlFormatter
from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text

# Path.relative_to(walk_up=True)
assert not (tuple(sys.version_info) < (3,12))

import warnings
from bs4 import XMLParsedAsHTMLWarning
warnings.filterwarnings("error", category=XMLParsedAsHTMLWarning)


def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features="lxml")


_EXPRESS_SECTION_KEYWORDS = (
    "ENTITY",
    "END_ENTITY",
    "TYPE",
    "END_TYPE",
    "FUNCTION",
    "END_FUNCTION",
    "LOCAL",
    "END_LOCAL",
    "BEGIN",
    "END",
    "IF",
    "THEN",
    "ELSE",
    "END_IF",
    "REPEAT",
    "END_REPEAT",
    "CASE",
    "END_CASE",
    "OTHERWISE",
    "RULE",
    "END_RULE",
    "SCHEMA",
    "END_SCHEMA",
)

_EXPRESS_BUILTINS = (
    "OPTIONAL",
    "NOT",
    "OR",
    "EXISTS",
    "SET",
    "SIZEOF",
    "SELF",
    "TYPEOF",
    "AND",
    "IN",
    "ONEOF",
    "LIST",
    "QUERY",
    "ARRAY",
    "INTEGER",
    "LOGICAL",
    "HIINDEX",
    "NVL",
    "STRING",
    "REAL",
    "BINARY",
)

_EXPRESS_KEYWORDS = (
    "SUBTYPE",
    "OF",
    "WHERE",
    "ENUMERATION",
    "ABSTRACT",
    "SUPERTYPE",
    "INVERSE",
    "FOR",
    "TO",
    "RETURN",
    "DERIVE",
    "UNIQUE",
    "FIXED",
    "SELECT",
)


class ExpressLexer(RegexLexer):
    name = "EXPRESS"
    aliases = ["express"]
    flags = re.IGNORECASE | re.MULTILINE
    tokens = {
        "root": [
            (r"\s+", Text),
            (r"\(\*[\s\S]*?\*\)", Comment.Multiline),
            (r"--.*?$", Comment.Single),
            (words(_EXPRESS_SECTION_KEYWORDS, suffix=r"\b"), Keyword.Declaration),
            (words(_EXPRESS_BUILTINS, suffix=r"\b"), Name.Builtin),
            (words(_EXPRESS_KEYWORDS, suffix=r"\b"), Keyword),
            (r"\.(?:T|F|U)\.", Keyword.Constant),
            (r"'(?:''|[^'])*'", String.Single),
            (r"[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[Ee][+-]?\d+)?", Number),
            (r"Ifc[A-Za-z0-9_]+", Name.Class),
            (r"[A-Za-z_][A-Za-z0-9_]*", Name),
            (r"[:=<>*/+\\-]+", Operator),
            (r"[()[\]{},.;|]", Punctuation),
        ]
    }


class Step21Lexer(RegexLexer):
    name = "STEP21"
    aliases = ["step21"]
    flags = re.IGNORECASE | re.MULTILINE
    tokens = {
        "root": [
            (r"\s+", Text),
            (r"/\*[\s\S]*?\*/", Comment.Multiline),
            (r"(?:ISO-10303-21|END-ISO-10303-21)(?=\s*;)", Keyword.Declaration),
            (words(("HEADER", "DATA", "ENDSEC"), suffix=r"\b"), Keyword.Declaration),
            (r"#\d+", Name.Label),
            (r"\.[A-Z0-9_]+\.", Name.Constant),
            (r"\$", Keyword.Constant),
            (r"'(?:''|[^'])*'", String.Single),
            (r'"(?:""|[^"])*"', String.Double),
            (r"[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[Ee][+-]?\d+)?", Number),
            (r"IFC[A-Z0-9_]+", Name.Class),
            (r"[A-Z_][A-Z0-9_]*", Name),
            (r"[/:=*]", Operator),
            (r"[(),;]", Punctuation),
        ]
    }


class FigureNumberer:
    def __init__(self) -> None:
        self.index: dict[str, str] = {}
        self._counts: dict[str | None, int] = {}
        self._replacement_pattern = None

    def generate(self, number: str, parent_number: str | None) -> None:
        count = self._counts.get(parent_number, 0)
        prefix = f"{parent_number}." if parent_number is not None else ""
        generated = prefix + chr(ord("A") + count)
        while generated in self.index.values():
            count += 1
            generated = prefix + chr(ord("A") + count)
        self._counts[parent_number] = count + 1
        self.index[number] = generated
        self._replacement_pattern = None

    def replace_references(self, text: str) -> str:
        if not self.index:
            return text
        if self._replacement_pattern is None:
            placeholders = sorted((re.escape(key) for key in self.index.keys()), key=len, reverse=True)
            if not placeholders:
                return text
            self._replacement_pattern = re.compile(
                r"(?<![A-Za-z0-9_])(Figure|Table)([- ])(" + "|".join(placeholders) + r")(?![A-Za-z0-9_])"
            )

        def repl(match: re.Match[str]) -> str:
            kind, sep, placeholder = match.groups()
            return f"{kind}{sep}{self.index.get(placeholder, placeholder)}"

        return self._replacement_pattern.sub(repl, text)


class ListingCollector:
    def __init__(self) -> None:
        self.references: set[tuple[str, str, str]] = set()
        self.figures: set[tuple[str, str, str]] = set()
        self.tables: set[tuple[str, str, str]] = set()

    def add_reference(self, target: str, page_url: str) -> None:
        self.references.add((target, "", page_url))

    def add_figure(self, caption: str, label: str, page_url: str) -> None:
        self.figures.add((caption or "unnamed", label, page_url))

    def add_table(self, caption: str, label: str, page_url: str) -> None:
        self.tables.add((caption or "unnamed", label, page_url))

    def merge(self, result: "RefineResult") -> None:
        self.references.update(result.references)
        self.figures.update(result.figures)
        self.tables.update(result.tables)

    @staticmethod
    def _to_payload(items: Iterable[tuple[str, str, str]]) -> list[dict[str, str]]:
        return [
            {"title": title, "number": number, "url": url}
            for title, number, url in sorted(set(items))
        ]

    def payloads(self) -> dict[str, list[dict[str, str]]]:
        return {
            "references": self._to_payload(self.references),
            "figures": self._to_payload(self.figures),
            "tables": self._to_payload(self.tables),
        }


@dataclass(frozen=True)
class RefineResult:
    html: str
    references: tuple[tuple[str, str, str], ...]
    figures: tuple[tuple[str, str, str], ...]
    tables: tuple[tuple[str, str, str], ...]


class HtmlRefiner:
    _SKIP_ANCESTORS = {
        "a",
        "code",
        "pre",
        "script",
        "style",
        "title",
        "textarea",
    }
    _HEADING_TAGS = ("h1", "h2", "h3", "h4", "h5", "h6")

    def __init__(
        self,
        resource_names: Iterable[str],
    ):
        self.html_formatter = HtmlFormatter(nowrap=True, classprefix="tok-")
        self.express_lexer = ExpressLexer()
        self.step21_lexer = Step21Lexer()
        canonical = {name.upper(): name for name in sorted(set(resource_names))}
        self.resource_names = tuple(canonical.values())
        self.canonical_names = canonical
        self.name_pattern = re.compile(r"(?<![A-Za-z0-9_])([A-Za-z_][A-Za-z0-9_]*)(?![A-Za-z0-9_])") if canonical else None

    def refine(self, public_path: str, html: str) -> RefineResult:
        collector = ListingCollector()
        soup = BeautifulSoup(html)

        self._decorate_title(soup)
        self._wrap_figures_and_tables(soup)
        self._add_section_anchors(soup)

        if not public_path.endswith("listing-references.html"):
            self._linkify_schema_names(soup, public_path, collector)

        self._highlight_code_blocks(soup)
        self._collect_figures_and_tables(soup, public_path, collector)
        self._normalize_urls(soup, public_path)

        return RefineResult(
            html=str(soup),
            references=tuple(sorted(collector.references)),
            figures=tuple(sorted(collector.figures)),
            tables=tuple(sorted(collector.tables)),
        )

    def _decorate_title(self, soup) -> None:
        title = soup.find("title")
        h1 = soup.find("h1")
        if title and h1:
            title.string = f"{h1.get_text(strip=True)} - {title.get_text(strip=True)}"

    def _normalize_urls(self, soup, public_path: str) -> None:
        for tag, attr in (("a", "href"), ("img", "src"), ("script", "src"), ("link", "href"), ("form", "action")):
            for element in soup.find_all(tag):
                if value := element.get(attr):
                    if normalized := self._normalize_url(public_path, value):
                        element[attr] = normalized

    def _normalize_url(self, public_path: str, value: str) -> str | None:
        if not value or value.startswith(("data:", "mailto:", "javascript:", "tel:", "#", "http:", "https:")):
            return None
        try:
            return Path(value).relative_to(Path(public_path).parent, walk_up=True).as_posix()
        except ValueError:
            print(f"Error normalizing path {value} within page {public_path}")
            return None

    def _wrap_figures_and_tables(self, soup) -> None:
        main_content = soup.find(id="main-content")
        if not main_content:
            return

        numberer = FigureNumberer()

        for img in main_content.find_all(["img", "svg"]):
            parent = img.parent
            if parent is None:
                continue
            if parent.name == "td":
                paragraph = soup.new_tag("p")
                paragraph.append(img.extract())
                parent.append(paragraph)
                parent = paragraph
            elif parent.name == "a":
                parent = parent.parent
            parent.name = "figure"
            has_caption = False
            sibling = parent.find_next_sibling()
            if parent.get_text(strip=True).startswith("Figure"):
                has_caption = True
                figcaption = soup.new_tag("figcaption")
                figcaption.string = parent.get_text()
                extracted = img.extract()
                parent.clear()
                parent.append(extracted)
                parent.append(figcaption)
            elif sibling and sibling.name == "p" and sibling.get_text().startswith("Figure"):
                has_caption = True
                figcaption = sibling.extract()
                figcaption.name = "figcaption"
                parent.append(figcaption)
            elif img.get("title", "").strip():
                has_caption = True
                figcaption = soup.new_tag("figcaption")
                figcaption.string = img["title"].strip()
                parent.append(figcaption)
            if not has_caption:
                figcaption = soup.new_tag("figcaption")
                token = str(uuid.uuid4())
                figcaption.string = "Figure " + token
                parent.append(figcaption)

        for table in main_content.find_all("table"):
            figure = soup.new_tag("figure")
            table.insert_before(figure)
            figure.append(table.extract())
            sibling = figure.find_next_sibling()
            if sibling and sibling.name == "p" and sibling.get_text().startswith("Table"):
                figcaption = sibling.extract()
                figcaption.name = "figcaption"
                figure.append(figcaption)
            else:
                figcaption = soup.new_tag("figcaption")
                token = str(uuid.uuid4())
                figcaption.string = "Table " + token
                figure.append(figcaption)
        current_parent_number = None
        for element in main_content.find_all(self._HEADING_TAGS + ("figure",)):
            if element.name in self._HEADING_TAGS:
                current_parent_number = self._heading_number(element)
                continue

            caption = element.find("figcaption", recursive=False)
            if caption is None:
                continue
            token = self._figure_token(caption.get_text(strip=True))
            if token is not None:
                numberer.generate(token, current_parent_number)

        if not numberer.index:
            return

        for node in list(soup.find_all(string=True)):
            parent = node.parent
            if parent is None or parent.name in {"script", "style"}:
                continue
            text = str(node)
            if "Figure" not in text and "Table" not in text:
                continue
            replaced = numberer.replace_references(text)
            if replaced != text:
                node.replace_with(replaced)

    def _add_section_anchors(self, soup) -> None:
        for element in soup.find_all(["h2", "h3", "h4", "h5", "h6", "figure"]):
            id_element = element
            divs = element.find_all("div", recursive=False)
            if element.name.startswith("h") and len(divs) == 2 and divs[0].get("class") and "number" in divs[0]["class"]:
                anchor_tag = divs[1].get_text(strip=True)
            else:
                value = element.find("figcaption", recursive=False).get_text(strip=True) if element.name == "figure" else element.get_text(strip=True)
                anchor_tag = re.sub("[^0-9a-zA-Z.]+", "-", value)

            anchor_id = soup.new_tag("a")
            anchor_id["id"] = anchor_tag
            anchor_id["class"] = "anchor"
            id_element.insert(0, anchor_id)

            target = element.find("figcaption", recursive=False) if element.name == "figure" else element
            anchor = soup.new_tag("a", href="#" + anchor_tag)
            anchor["class"] = "link"
            icon = soup.new_tag("i")
            icon["data-feather"] = "link"
            anchor.append(icon)
            target.append(anchor)

    def _linkify_schema_names(self, soup, public_path: str, collector: ListingCollector) -> None:
        if not self.name_pattern:
            return

        for node in list(soup.find_all(string=True)):
            parent = node.parent
            if parent is None:
                continue
            if parent.name in self._SKIP_ANCESTORS:
                continue
            if any(ancestor.name in self._SKIP_ANCESTORS or ancestor.name == "svg" for ancestor in node.parents):
                continue
            text = str(node)
            if not text.strip():
                continue

            matches = list(self._iter_schema_matches(text))
            if not matches:
                continue

            replacement = []
            cursor = 0
            for match, canonical in matches:
                start, end = match.span()
                if start > cursor:
                    replacement.append(text[cursor:start])
                raw = match.group(0)
                anchor = soup.new_tag("a", href=f"/lexical/{canonical}.html")
                anchor.string = raw
                replacement.append(anchor)
                collector.add_reference(canonical, public_path)
                cursor = end
            if cursor < len(text):
                replacement.append(text[cursor:])

            node.replace_with(*replacement)

    def _highlight_code_blocks(self, soup) -> None:
        for code in soup.select("pre > code"):
            classes = [cls for cls in (code.get("class") or []) if cls != "hljs"]
            language = next((cls.split("-", 1)[1] for cls in classes if cls.startswith("language-")), None)
            lexer = self._lexer_for(language)
            if lexer is None:
                if classes:
                    code["class"] = classes
                elif code.has_attr("class"):
                    del code["class"]
                continue

            rendered = self._render_highlighted_code(code.get_text(), language, lexer)
            if "pygments" not in classes:
                classes.append("pygments")
            code["class"] = classes
            code["data-highlighted"] = "generator"

            fragment = BeautifulSoup(f"<code>{rendered}</code>")
            highlighted = fragment.code
            code.clear()
            for child in list(highlighted.contents):
                code.append(child.extract())

    def _lexer_for(self, language: str | None):
        if language == "express":
            return self.express_lexer
        if language == "step21":
            return self.step21_lexer
        return None

    def _render_highlighted_code(self, code_text: str, language: str | None, lexer: RegexLexer) -> str:
        parts: list[str] = []
        step_targets = set(re.findall(r"(?m)(#\d+)\s*=", code_text)) if language == "step21" else set()
        for index, token_type, value in lexer.get_tokens_unprocessed(code_text):
            parts.append(self._render_token(code_text, language, step_targets, index, token_type, value))
        return "".join(parts)

    def _render_token(
        self,
        code_text: str,
        language: str | None,
        step_targets: set[str],
        index: int,
        token_type,
        value: str,
    ) -> str:
        if not value:
            return ""

        token_html = self._render_named_segments(token_type, value)
        if language != "step21" or token_type not in Name.Label or not re.fullmatch(r"#\d+", value):
            return token_html

        anchor = value[1:]
        if re.match(r"\s*=", code_text[index + len(value):]):
            return f'<a id="{anchor}"></a>{token_html}'
        if value in step_targets:
            return f'<a href="#{anchor}">{token_html}</a>'
        return token_html

    def _render_named_segments(self, token_type, value: str) -> str:
        if not self._should_link_token(token_type) or not self.name_pattern:
            return self._wrap_token_html(token_type, escape(value))

        segment = self._wrap_token_html(token_type, escape(value))
        canonical = self.canonical_names.get(value.upper())
        if canonical is None:
            return segment
        return f'<a href="/lexical/{canonical}.html">{segment}</a>'

    def _iter_schema_matches(self, value: str):
        for match in self.name_pattern.finditer(value):
            canonical = self.canonical_names.get(match.group(1).upper())
            if canonical:
                yield match, canonical

    def _heading_number(self, element) -> str | None:
        if not element.text:
            return None
        first = element.text.split(" ", 1)[0]
        if not (first[:1].isdigit() or first == "Annex"):
            return None
        if not element.contents:
            return None
        first_content = element.contents[0]
        if isinstance(first_content, str):
            first_text = first_content.strip()
        else:
            first_text = first_content.get_text(" ", strip=True)
        parent_number = first_text.split(" ", 1)[0]
        if parent_number == "Annex":
            try:
                return first_text.split(" ", 2)[1]
            except Exception:
                return parent_number
        return parent_number

    def _figure_token(self, text: str) -> str | None:
        parts = text.split(" ", 2)
        if len(parts) < 2:
            return None
        return parts[1]

    def _should_link_token(self, token_type) -> bool:
        return token_type in Name and not any(
            token_type in excluded
            for excluded in (Name.Attribute, Name.Builtin, Name.Constant, Name.Decorator, Name.Label)
        )

    def _wrap_token_html(self, token_type, text: str) -> str:
        css_class = self.html_formatter._get_css_class(token_type)
        if not css_class:
            return text
        return f'<span class="{css_class}">{text}</span>'

    def _collect_figures_and_tables(self, soup, public_path: str, collector: ListingCollector) -> None:
        for elem in soup.find_all("figure"):
            if not elem.figcaption:
                continue
            is_image = bool(elem.find("img")) or bool(elem.find("svg"))
            text = elem.figcaption.get_text(strip=True)
            if "—" in text:
                label, caption = map(str.strip, text.split("—", 1))
            elif elem.find("img"):
                label = text
                caption = elem.find("img").get("alt", "").strip()
            else:
                continue
            if is_image:
                collector.add_figure(caption, label, public_path)
            else:
                collector.add_table(caption, label, public_path)
