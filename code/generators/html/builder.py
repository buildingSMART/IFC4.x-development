from __future__ import annotations

from collections import Counter
import importlib
import hashlib
import itertools
import json
import mimetypes
import operator
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
import tempfile
from types import SimpleNamespace
from urllib.parse import unquote

from jinja2 import BaseLoader, Environment, FileSystemLoader, select_autoescape
import pydot
from slugify import slugify
import tabulate
import markdown

from .markdown import markdown_mixin
from .config import BuildConfig
from .refiner import BeautifulSoup, HtmlRefiner, ListingCollector
from .search import SearchIndexBuilder
from . import translate
from ..util.xmi_document import SCHEMA_NAME
from . import md as mdp

REPO_BRANCH = os.environ.get("REPO_BRANCH", "xmi-refresh")
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
DOC_ANNOTATION_PATTERN = re.compile(r"\{\s*\..+?\}")

class RenderAbort(Exception):
    def __init__(self, status_code: int):
        super().__init__(f"render aborted with status {status_code}")
        self.status_code = status_code


@dataclass(frozen=True)
class StaticResponse:
    body: bytes
    mimetype: str


@dataclass(order=True, eq=True, frozen=True)
class toc_entry:
    text: str

    number: str = None
    url: str = None

    parent: object = None
    children: list = None
    
    mvds: list = None

    def find(self, lbl):
        def traverse(te, path=None):
            p = (path or []) + [te]
            if te.text == lbl:
                yield p
            else:
                for ch in (te.children or []):
                    yield from traverse(ch, p)
        li = list(traverse(self))
        if li:
            return li[0][-1]


def _generated_output_root(config: BuildConfig) -> Path:
    return config.repo_root / "output"


def _generated_file(config: BuildConfig, name: str) -> Path:
    candidate = _generated_output_root(config) / name
    if candidate.exists():
        return candidate
    return config.code_dir / name

class SectionNumberGenerator:
    def __init__(self, number = "1"):
        self.number = number

    def reset(self, number):
        self.number = number

    def generate(self):
        numbers = self.number.split(".")
        numbers[-1] = str(int(numbers[-1]) + 1)
        self.number = ".".join(numbers)
        return self.number

    def begin_subsection(self):
        self.number += ".0"

    def end_subsection(self):
        self.number = ".".join(self.number.split(".")[0:-1])



class resource_documentation_builder:
    def __init__(self, resource, renderer : StaticTemplateRenderer):
        self.resource = resource
        self.renderer = renderer
        self.md = renderer.get_resource_path(resource)

    @property
    def markdown(self):
        with open(self.md, "r", encoding="utf-8") as f:
            return re.sub(DOC_ANNOTATION_PATTERN, "", "\n".join(f.readlines()[2:]))

    def get_markdown_content(self, heading):
        attrs = []
        direct_attrs = []

        entity = self.resource
        while entity:
            markdown_filename = self.renderer.get_resource_path(entity)

            try:
                md_entity = re.sub(DOC_ANNOTATION_PATTERN, "", open(markdown_filename, encoding="utf-8").read())
            except:
                md_entity = None

            entity_attrs = []
            try:
                if md_entity:
                    entity_attrs = list(mdp.markdown_attribute_parser(data=md_entity, heading_name=heading, as_text=False))
            except:
                import traceback

                traceback.print_exc()


            if heading == "Attributes":
                entity_attr_di = dict(entity_attrs)
                for a in [k.split(".")[1] for k in self.renderer.structure['entity_attributes'].keys() if k.startswith(f"{entity}.")][::-1]:
                    content = entity_attr_di.get(a, "")
                    is_fwd, attr_entity = self.renderer.structure['entity_attributes'][".".join((entity, a))]
                    attrs.append((entity, a, attr_entity, content))
                    if is_fwd == "forward":
                        direct_attrs.append(a)
            else:
                for a, content in entity_attrs[::-1]:
                    # remove underscored words:
                    attrs.append((entity, a, content))
            entity = self.renderer.structure['entity_supertype'].get(entity)

        attrs = attrs[::-1]

        if heading == "Attributes":
            # Decorate with attribute index
            attr_index = {b: a for a, b in enumerate(direct_attrs[::-1], 1)}
            attrs = [(a, attr_index.get(b, ""), b, c, d) for a, b, c, d in attrs]

        return attrs

    @property
    def attributes(self):
        return self.get_markdown_content("Attributes")

    @property
    def formal_propositions(self):
        return self.get_markdown_content("Formal Propositions")

    @property
    def concepts(self):
        return self.get_markdown_content("Concepts")

class StaticTemplateRenderer(markdown_mixin):
    CONTENT_NAMES = ["scope", "normative_references", "terms_and_definitions", "concepts"]
    CONTENT_NAMES_2 = ["cover", "foreword", "introduction", "bibliography"]
    NAVIGATION = [
        [
            {"name": "Cover", "url": "/"},
            {"name": "Contents", "url": "/toc.html"},
            {"name": "Foreword", "url": "/content/foreword.html"},
            {"name": "Introduction", "url": "/content/introduction.html"},
        ],
        [
            {"number": 1, "name": "Scope", "url": "/content/scope.html"},
            {"number": 2, "name": "Normative references", "url": "/content/normative_references.html"},
            {
                "number": 3,
                "name": "Terms, definitions, and abbreviated terms",
                "url": "/content/terms_and_definitions.html",
            },
            {"number": 4, "name": "Fundamental concepts and assumptions", "url": "/concepts/content.html"},
            {"number": 5, "name": "Core data schemas", "url": "/chapter-5.html"},
            {"number": 6, "name": "Shared element data schemas", "url": "/chapter-6.html"},
            {"number": 7, "name": "Domain specific data schemas", "url": "/chapter-7.html"},
            {"number": 8, "name": "Resource definition data schemas", "url": "/chapter-8.html"},
        ],
        [
            {"number": "A", "name": "Computer interpretable listings", "url": "/annex-a.html"},
            {"number": "B", "name": "Alphabetical listings", "url": "/annex-b.html"},
            {"number": "C", "name": "Inheritance listings", "url": "/annex-c.html"},
            {"number": "D", "name": "Diagrams", "url": "/annex-d.html"},
            {"number": "E", "name": "Examples", "url": "/annex-e.html"},
            {"number": "F", "name": "Change logs", "url": "/annex-f.html"},
        ],
        [
            {"name": "Bibliography", "url": "/content/bibliography.html"},
            {"name": "Index", "url": "/indices.html"},
        ],
    ]
    ANNEX_B_NAVIGATION = [
        {"number": "B.1", "name": "Entities", "url": "/annex-b1.html"},
        {"number": "B.2", "name": "Types", "url": "/annex-b2.html"},
        {"number": "B.3", "name": "Property sets", "url": "/annex-b3.html"},
        {"number": "B.4", "name": "Properties", "url": "/annex-b4.html"},
        {"number": "B.5", "name": "Functions", "url": "/annex-b5.html"},
        {"number": "B.6", "name": "Rules", "url": "/annex-b6.html"},
        {"number": "B.7", "name": "Property Enumerations", "url": "/annex-b7.html"},
    ]

    def __init__(
        self,
        config: BuildConfig,
        *,
        structure: dict | None = None,
        name_to_number: dict[str, str] | None = None,
        listing_payloads: dict[str, list[dict[str, str]]] | None = None,
    ):
        self.config = config
        self.structure = structure or {}
        self.name_to_number = name_to_number or {}
        self.version = importlib.import_module("version")
        self.examples_repo_root = (config.repo_root.parent / "examples").resolve()
        self.examples_models_root = (self.examples_repo_root / "models").resolve()
        self.listing_payloads = listing_payloads or {"references": [], "figures": [], "tables": []}
        self.request = SimpleNamespace(path="/", args={}, form={}, cookies={})
        self.base = ""
        self.numberer = SectionNumberGenerator("1")

        self.template_environment = Environment(
            loader=FileSystemLoader(str(self.config.code_dir / "templates")),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.template_environment.filters["slugify"] = slugify
        self.template_string_environment = Environment(
            loader=BaseLoader(),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render_path(self, public_path: str) -> StaticResponse:
        path = self._normalize_public_path(public_path)
        self.request.path = path
        self.request.args = {}
        self.request.form = {}
        self.request.cookies = {}

        if path == "/":
            return self._render_cover()
        if path == "/indices.html":
            return self._render_index()
        if path == "/search.html":
            return self._render_search()
        if path == "/toc.html":
            return self._render_toc()

        if path.startswith("/content/") and path.endswith(".html"):
            return self._render_content(path[len("/content/") : -5])
        if path.startswith("/lexical/") and path.endswith(".html"):
            return self._render_resource(path[len("/lexical/") : -5])
        if path.startswith("/property/") and path.endswith(".html"):
            return self._render_property(path[len("/property/") : -5])

        if path == "/annex-a.html":
            return self._html_response(
                "annex-a.html",
                navigation=self.get_navigation(),
                has_bsdd=(self.config.repo_root / "output" / "bsdd" / "IFC.json").exists(),
                body_class="annex",
            )
        if path == "/annex-a-express.html":
            return self._html_response(
                "annex-a-express.html",
                navigation=self.get_navigation(),
                express=_generated_file(self.config, "IFC.exp").read_text(encoding="utf-8"),
                link=f"{SCHEMA_NAME}.exp",
                body_class="annex",
            )
        if path == "/annex-a-xsd.html":
            return self._html_response(
                "annex-a-xsd.html",
                navigation=self.get_navigation(),
                link=f"{SCHEMA_NAME}.xsd",
                body_class="annex",
            )
        if path in {f"/{SCHEMA_NAME}.exp", f"/{SCHEMA_NAME}.xsd"}:
            extension = Path(path).suffix
            return self._file_response(_generated_file(self.config, f"IFC{extension}"))
        if path == "/annex-a-psd.zip":
            return self._file_response(_generated_file(self.config, "psd.zip"))

        if path == "/annex-b.html":
            return self._render_annex_b()
        if path == "/annex-b1.html":
            return self._render_annex_b1()
        if path == "/annex-b2.html":
            return self._render_annex_b2()
        if path == "/annex-b3.html":
            return self._render_annex_b3()
        if path == "/annex-b4.html":
            return self._render_annex_b4()
        if path == "/annex-b5.html":
            return self._render_annex_b5()
        if path == "/annex-b6.html":
            return self._render_annex_b6()
        if path == "/annex-b7.html":
            return self._render_annex_b7()

        if path == "/annex-c.html":
            return self._render_annex_c()
        if path == "/annex-d.html":
            return self._render_annex_d()
        match = re.fullmatch(r"/annex_d/(.+)\.html", path)
        if match:
            return self._render_annex_d_diagram_page(unquote(match.group(1)))
        match = re.fullmatch(r"/annex_d/(.+)\.png", path)
        if match:
            return self._file_response(self.config.repo_root / "output" / "ifc4x3_add2.uml" / f"{unquote(match.group(1))}.png")

        if path == "/annex-e.html":
            return self._render_annex_e()
        match = re.fullmatch(r"/annex_e/(.+)\.html", path)
        if match:
            return self._render_annex_e_example_page(unquote(match.group(1)))
        if path == "/annex-f.html":
            return self._render_annex_f()

        if path == "/concepts/content.html":
            return self._render_concept_list()
        match = re.fullmatch(r"/concepts/(.+)/content\.html", path)
        if match:
            return self._render_concept(unquote(match.group(1)))

        match = re.fullmatch(r"/chapter-(\d+)\.html", path)
        if match:
            return self._render_chapter(match.group(1))

        match = re.fullmatch(r"/listing-(references|figures|tables)\.html", path)
        if match:
            return self._render_listing(match.group(1))

        match = re.fullmatch(r"/([^/]+)/content\.html", path)
        if match:
            return self._render_schema(unquote(match.group(1)))

        if path.startswith("/assets/"):
            return self._file_response(self.config.repo_root / "docs" / "assets" / path[len("/assets/") :])
        if path.startswith("/figures/examples/"):
            return self._file_response(self.config.repo_root / "docs" / "figures" / "examples" / path[len("/figures/examples/") :])
        if path.startswith("/figures/"):
            return self._file_response(self.config.repo_root / "docs" / "figures" / path[len("/figures/") :])
        if path.startswith("/examples/"):
            return self._file_response(self.examples_models_root / path[len("/examples/") :])
        if path.startswith("/svgs/"):
            return self._file_response(self.config.code_dir / "svgs" / path[len("/svgs/") :])

        self._abort(404)

    def _normalize_public_path(self, public_path: str) -> str:
        if not public_path:
            return "/"
        path = unquote(public_path)
        if not path.startswith("/"):
            path = "/" + path
        return path

    def _abort(self, status_code: int):
        raise RenderAbort(status_code)

    def _url_for(self, endpoint: str, **values) -> str:
        values.pop("_external", None)
        mapping = {
            "resource": lambda: f"/lexical/{values['resource']}.html",
            "property": lambda: f"/property/{values['prop']}.html",
            "schema": lambda: f"/{values['name']}/content.html",
            "content": lambda: f"/content/{values['s']}.html",
            "chapter": lambda: f"/chapter-{values['n']}.html",
            "get_example_figure": lambda: f"/figures/examples/{values['fig']}",
            "get_asset": lambda: f"/assets/{values['asset']}",
            "get_example": lambda: f"/examples/{values['example']}",
            "annex_e_example_page": lambda: f"/annex_e/{values['s']}.html",
            "annex_d_diagram_page": lambda: f"/annex_d/{values['s']}.html",
        }
        if endpoint not in mapping:
            raise KeyError(f"unsupported endpoint: {endpoint}")
        return mapping[endpoint]()

    def url_for(self, endpoint: str, **values) -> str:
        return self._url_for(endpoint, **values)

    def _file_response(self, path: Path) -> StaticResponse:
        if not path.exists() or not path.is_file():
            self._abort(404)
        content_type, _ = mimetypes.guess_type(str(path))
        return StaticResponse(path.read_bytes(), content_type or "application/octet-stream")

    def _html_response(self, template_name: str, **context) -> StaticResponse:
        html = self._render_template(template_name, **context, relative_base='')
        return StaticResponse(html.encode("utf-8"), "text/html")

    def _render_template(self, template_name: str, **context) -> str:
        template = self.template_environment.get_template(template_name)
        return template.render(self._template_context(**context))

    def _render_string(self, source: str, **context) -> str:
        template = self.template_string_environment.from_string(source)
        return template.render(self._template_context(**context))

    def _template_context(self, **context) -> dict:
        payload = {
            "is_iso": False,
            "is_package": False,
            "schema_version_string": self.version.schema_version_string,
            "spec_version_string": self.version.spec_version_string,
            "spec_version_string_full": self.version.spec_version_string_full,
            "branch": REPO_BRANCH,
            "get_language_icon": translate.get_language_icon,
            "current_lang_slug": slugify("English (default)"),
            "languages": translate.list_languages(),
        }
        payload.update(context)
        return payload

    def _repo_relative(self, path: Path) -> str:
        return path.resolve().relative_to(self.config.repo_root).as_posix()

    def _toc_entry(self, text: str, number: str | None = None, url: str | None = None, children=None, mvds=None):
        return toc_entry(text=text, number=number, url=url, children=children or [], mvds=mvds)

    def chapter_lookup(self, number=None, cat=None):
        def do_lookup(node):
            if isinstance(node, (list, tuple)):
                for value in node:
                    found = do_lookup(value)
                    if found is not None:
                        return found
                return None
            if number is not None and node.get("number") == number:
                return node
            if cat is not None and node["name"].split(" ")[0].lower() == cat:
                return node
            return None

        return do_lookup(self.NAVIGATION)

    def get_navigation(self, resource=None, number=None):
        if resource and not number:
            number = self.name_to_number[resource]

        sections = [[dict(item, subitems=[]) for item in group] for group in self.NAVIGATION]
        numbers: list[str] = []
        if isinstance(number, str):
            numbers = number.split(".")
            if numbers and numbers[0].isdigit():
                number = int(numbers[0])

        for section in sections:
            for item in section:
                item["is_current"] = False
                if item["url"] == self.request.path:
                    item["is_current"] = True
                    continue
                if number and item.get("number") == number:
                    item["is_current"] = True
                    if number in (5, 6, 7, 8) and len(numbers) >= 2:
                        subchapters = [entries for title, entries in self.structure['hierarchy'] if title == item["name"]][0]
                        item["subitems"] = [
                            {
                                "url": self._url_for("schema", name=subchapter[0].lower()),
                                "number": f"{number}.{index}",
                                "name": subchapter[0],
                                "is_current": str(index) == numbers[1],
                            }
                            for index, subchapter in enumerate(subchapters, 1)
                        ]
                    continue
                if "annex-b" in self.request.path and item.get("number") == "B":
                    item["is_current"] = True
                    item["subitems"] = [
                        dict(
                            subitem,
                            is_current=("annex-" + subitem["number"]).lower().replace(".", "") in self.request.path,
                        )
                        for subitem in self.ANNEX_B_NAVIGATION
                    ]
        return sections

    def annotate_hierarchy(self, data=None, start=1, number_path=None):
        level_2_headings = ("Schema Definition", "Types", "Entities", "Property Sets", "Quantity Sets", "Functions", "Rules")

        def items(d):
            if len(number_path or []) == 2:
                return [(heading, dict(d).get(heading, [])) for heading in level_2_headings]
            if isinstance(d, dict):
                return d.items()
            return [(entry, []) if isinstance(entry, str) else entry for entry in d]

        def get_url(idx, text):
            if len(number_path) == 0:
                return f"/chapter-{idx}.html"
            if len(number_path) == 1:
                return f"/{text.lower()}/content.html"
            if len(number_path) == 2:
                fragment = (".".join([part[0] for part in number_path] + [str(idx)]) + "-" + text).replace(" ", "-")
                return f"/{number_path[1][1].lower()}/content.html#{fragment}"
            if len(number_path) == 3:
                return f"/lexical/{text}.html"
            return None

        data = self.structure['hierarchy'] if data is None else data
        number_path = [] if number_path is None else number_path

        return [
            self._toc_entry(
                text=name,
                number=".".join([part[0] for part in number_path] + [str(index)]),
                url=get_url(index, name),
                children=self.annotate_hierarchy(data=children, number_path=number_path + [(str(index), name)]),
            )
            for index, (name, children) in enumerate(items(data), start)
        ]

    def _make_annex_b_navigation(self):
        return [dict(item) for item in self.ANNEX_B_NAVIGATION]

    def _get_content_html(self, slug: str, require_number: bool = True):
        path = self.config.repo_root / "content" / f"{slug}.md"
        if not path.exists():
            self._abort(404)

        title = None
        number = None
        if require_number:
            if slug in self.CONTENT_NAMES:
                number = self.CONTENT_NAMES.index(slug) + 1
                title = self.NAVIGATION[1][number - 1]["name"]
            elif slug in self.CONTENT_NAMES_2:
                title = slug[:1].upper() + slug[1:]
                number = ""
            else:
                self._abort(404)

        content = path.read_text(encoding="utf-8")
        if content.startswith("!template"):
            content = self._render_string(content[len("!template") :].lstrip(), is_iso=False)

        process_quotes = slug != "terms_and_definitions"
        kwargs = {"number_headings": True, "chapter": (int(number), 1)} if slug == "terms_and_definitions" else {}
        rendered = self._render_string(content, base="", is_iso=False)
        html = self.process_markdown("", rendered, process_quotes=process_quotes, **kwargs)
        return path, title, number, html

    def _diagram_names(self) -> list[str]:
        diagram_dir = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        return sorted(path.stem for path in diagram_dir.glob("*.png"))

    def _example_title(self, slug: str) -> str:
        return " ".join(part[:1].upper() + part[1:] for part in slug.split("-"))

    def _build_example_tree(self, return_list_and_tree: bool = False):
        examples = []
        for model in self.examples_models_root.glob("**/*.ifc"):
            readme = model.parent / "README.md"
            if readme.exists():
                examples.append(model.parent.relative_to(self.examples_models_root).as_posix())
        examples = sorted(set(examples))

        root = self._toc_entry("", number="E", children=[])
        for path in examples:
            current = root
            for component in Path(path).parts:
                title = self._example_title(component)
                child = next((entry for entry in current.children if entry.text == title), None)
                if child is None:
                    url = None
                    if component == Path(path).parts[-1]:
                        url = f"/annex_e/{path}.html"
                    child = self._toc_entry(
                        title,
                        url=url,
                        children=[],
                        number=f"{current.number}.{len(current.children) + 1}",
                    )
                    current.children.append(child)
                current = child

        if return_list_and_tree:
            return examples, root
        return root.children

    def _render_cover(self) -> StaticResponse:
        path, _, _, html = self._get_content_html("cover")
        return self._html_response(
            "cover.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            subs=[],
            body_class="cover",
        )

    def _render_content(self, slug: str) -> StaticResponse:
        path, title, number, html = self._get_content_html(slug)
        return self._html_response(
            "static.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            title=title,
            number=number,
            body_class=re.sub(r"[^a-z0-9]+", "-", slug.lower()),
        )

    def _render_property(self, prop: str) -> StaticResponse:
        translations = translate.get_translations(prop)
        safe_prop = "".join(char for char in prop if char.isalnum() or char == "_")
        path = self.config.repo_root / "docs" / "properties" / safe_prop[0].lower() / f"{safe_prop}.md"
        markdown = path.read_text(encoding="utf-8") if path.exists() else ""
        property_sets = [[name] for name, definition in self.structure['pset_definitions'].items() if any(item["name"] == safe_prop for item in definition["properties"])]
        html = self.process_markdown(safe_prop, markdown)
        html += tabulate.tabulate(property_sets, headers=["Referenced in"], tablefmt="html")
        return self._html_response(
            "property.html",
            navigation=self.get_navigation(),
            content=html,
            number="",
            entity=safe_prop,
            translations=translations,
            path=self._repo_relative(path),
        )
    
    @staticmethod
    def resource_paths(pairs, path=None):
        if isinstance(pairs, dict):
            pairs = list(pairs.items())
        if isinstance(pairs[0], str):
            for v in pairs:
                yield v, path
            return
        for p, vs in pairs:
            yield from StaticTemplateRenderer.resource_paths(vs, (path or ()) + ((p.split(" ")[0].lower() if path is None else p),))

    def get_resource_path(self, resource,):
        v = dict(StaticTemplateRenderer.resource_paths(self.structure['hierarchy'])).get(resource)
        if not v:
            raise RuntimeError(resource)
        return str(
            (self.config.repo_root / "docs" / "schemas" / Path(*v) / f"{resource}.md")
        ).replace("Property Sets", "PropertySets").replace("Quantity Sets", "QuantitySets").replace("Rules", "GlobalRules")
        
    def get_definition(self, resource, mdc):
        # Only match up to the first h2
        lines = []
        self.numberer.begin_subsection()
        for line in mdc.split("\n"):
            if line.startswith("## "):
                break
            if line.startswith("### "):
                words = line.split(" ")
                line = " ".join((words[0], self.numberer.generate(), *words[1:]))
            lines.append(line)
        mdc = "\n".join(lines)
        self.numberer.end_subsection()
        return self.process_markdown(resource, mdc)
    
    def get_entity_inheritance(self, resource):
        try:
            return {
                "number": self.numberer.generate(),
                "graph": self.get_inheritance_graph(resource),
            }
        except:
            import traceback

            traceback.print_exc()

    def get_attributes(self, resource, builder):
        attrs = builder.attributes
        supertype_counts = Counter()
        supertype_counts.update([a[0] for a in attrs])
        attrs = [a[1:] for a in attrs]
        supertype_counts = list(supertype_counts.items())[::-1]
        insertion_points = [0] + list(itertools.accumulate(map(operator.itemgetter(1), supertype_counts[::-1])))[:-1]
        group_data = supertype_counts[::-1]
        
        groups = []
        for i, attr in enumerate(attrs):
            if i in insertion_points:
                name, total_attributes = group_data[insertion_points.index(i)]
                group = {
                    "name": name,
                    "attributes": [],
                    "is_inherited": insertion_points[-1] != i,
                    "total_attributes": total_attributes,
                }
                groups.append(group)
                
            attribute = {
                "number": attr[0],
                "name": attr[1],
                "type": attr[2][0] if isinstance(attr[2], list) else attr[2],
                "formal": attr[2][1] if isinstance(attr[2], list) else None,
                # @nb we're not really talking about markdown anymore
                # since the new attribute parser operates on a converted
                # dom, but it appears to work nonetheless.
                "description": self.process_markdown(resource, attr[3]),
                "is_inverse": not attr[0],
            }
            if attribute["name"] == "PredefinedType" and not attribute["description"]:
                description = "A list of types to further identify the object. Some property sets may be specifically applicable to one of these types."
                if "Type" not in group["name"]:
                    description += "\n> NOTE  If the object has an associated IfcTypeObject with a _PredefinedType_, then this attribute shall not be used."
                attribute["description"] = self.process_markdown(resource, description)
            group["attributes"].append(attribute)

        total_inherited_attributes = sum([g["total_attributes"] for g in groups if g["is_inherited"]])

        inherited_groups_with_attributes = [g for g in groups if g["is_inherited"] and g["total_attributes"]]
        if inherited_groups_with_attributes:
            inherited_groups_with_attributes[-1]["is_last_inherited_group"] = True

        return {
            "number": self.numberer.generate(),
            "groups": groups,
            "total_inherited_attributes": total_inherited_attributes,
        }
    
    def get_formal_propositions(self, resource, builder):
        if not builder:
            return

        defs = {k[1]: k[2] for k in builder.formal_propositions}
        clauses = self.structure['entity_where_clauses'].get(resource, [])

        if not clauses:
            return

        return {
            "number": self.numberer.generate(),
            "items": [
                {"name": c[0], "formal": None, "description": f"The attribute {c[1].split(' ')[1]} should be unique" } \
                if c[1].startswith("UNIQUE ") else \
                {"name": c[0], "formal": c[1], "description": self.process_markdown(resource, defs.get(c[0]))} \
                for c in clauses
            ],
        }
    
    def get_property_sets(self, resource):
        ty = resource
        supertype_chain = []
        while ty is not None:
            supertype_chain.append(ty)
            ty = self.structure['entity_supertype'].get(ty)
        supertype_chain = list(reversed(supertype_chain))

        psets = []
        for view_name, xmi_concepts in self.structure.get('xmi_concepts', {}).items():
            for xmi_concept_name, xmi_relationships in xmi_concepts.items():
                if "PropertySets" not in xmi_concept_name and "QuantitySets" not in xmi_concept_name:
                    continue
                for xmi_relationship in xmi_relationships:
                    applicable_entity = xmi_relationship.get("ApplicableEntity", None)
                    if applicable_entity not in supertype_chain:
                        continue
                    name = xmi_relationship.get("PsetName", None) or xmi_relationship.get("QsetName", None)
                    if not name or name not in self.structure['pset_definitions']:
                        continue
                    properties = self.structure['pset_definitions'][name]["properties"]
                    psets.append({
                        "name": name,
                        "predefined_type": xmi_relationship.get("PredefinedType", None),
                        "properties": [p["name"] for p in properties]
                    })

        if psets:
            return {
                "number": self.numberer.generate(),
                "psets": sorted(psets, key=lambda x: x["name"]),
            }
    
    @staticmethod
    def separate_camel(value: str) -> str:
        return " ".join(re.split("(?=[A-Z])", value)[1:])

    @staticmethod
    def get_concept_name(name):
        if isinstance(name, tuple):
            return name[1]
        return name

    def entity_names(self) -> list[str]:
        return sorted(sum([schema.get("Entities", []) for _, cat in self.structure['hierarchy'] for __, schema in cat], []))

    def function_names(self) -> list[str]:
        return sorted(sum([schema.get("Functions", []) for _, cat in self.structure['hierarchy'] for __, schema in cat], []))

    def rule_names(self) -> list[str]:
        return sorted(sum([schema.get("Rules", []) for _, cat in self.structure['hierarchy'] for __, schema in cat], []))

    def type_names(self) -> list[str]:
        return sorted(sum([schema.get("Types", []) for _, cat in self.structure['hierarchy'] for __, schema in cat], []))

    def propertyenumeration_names(self) -> list[str]:
        return sorted(sum([schema.get("PropertyEnumerations", []) for _, cat in self.structure['hierarchy'] for __, schema in cat], []))

    def get_inheritance_graph(self, current_entity):
        graph = []

        tier = []
        for subclass in sorted([name for name, supertype in self.structure['entity_supertype'].items() if supertype == current_entity]):
            tier.append(
                {
                    "name": subclass,
                    "is_deprecated": subclass in self.structure['deprecated_entities'],
                    "is_abstract": subclass in self.structure['abstract_entities'],
                    "is_subclass": True,
                }
            )
        if tier:
            graph.append(tier)

        entity = current_entity
        while entity:
            parent = self.structure['entity_supertype'].get(entity)
            siblings = sorted([name for name, supertype in self.structure['entity_supertype'].items() if supertype == parent]) if parent else [entity]
            tier = []
            for sibling in siblings:
                data = {
                    "name": sibling,
                    "is_deprecated": sibling in self.structure['deprecated_entities'],
                    "is_abstract": sibling in self.structure['abstract_entities'],
                    "is_current": sibling == current_entity,
                    "is_ancestor": sibling == entity,
                }
                if data["is_current"] or data["is_ancestor"]:
                    tier.insert(0, data)
                else:
                    tier.append(data)
            graph.append(tier)
            entity = self.structure['entity_supertype'].get(entity)

        return reversed(graph)

    def make_url(self, fragment=None):
        if not fragment:
            return "/"
        return "/" + fragment.lstrip("/")

    def make_concept(self, path, number_path=None, exclude_partial=True):
        templates_root = self.config.repo_root / "docs" / "templates"
        path_parts = [part for part in path if part]
        current_root = templates_root.joinpath(*path_parts)

        if number_path is None:
            number_path = "4.2" if path == ["Partial Templates"] else "4.1"

        children = enumerate(
            sorted(
                entry.name
                for entry in current_root.iterdir()
                if entry.is_dir()
                and (entry / "README.md").exists()
                and not (exclude_partial and entry.name == "Partial Templates")
            ),
            1,
        )
        relative = "/".join(path_parts).replace(" ", "_")
        url = "/concepts/content.html" if not relative else f"/concepts/{relative}/content.html"
        text = path[-1] if path else ""
        return toc_entry(
            url=url,
            number=number_path,
            text=text,
            children=[self.make_concept(path_parts + [child], number_path=f"{number_path}.{index}", exclude_partial=exclude_partial) for index, child in children],
            mvds=[
                {"abbr": "".join(re.findall(r"[A-Z]|(?<=-)[a-z]", name)), "name": name, "on": re.sub(r"[^\w]", "", text) in values}
                for name, values in self.structure.get("xmi_mvd_concepts", {}).items()
            ],
        )

    def create_concept_table(self, view_name, xmi_concept, types=None):
        rows = list(self.structure.get("xmi_concepts", {}).get(view_name, {}).get(xmi_concept, []))
        bindings = [("ApplicableEntity", ("", ""))] + list(
            self.parse_concept_bindings(xmi_concept)
        )
        bound_keys = set(sum([list(row.keys()) for row in rows], []))
        bound_keys = [key for key, _ in bindings if key in bound_keys]
        headers = [f"{key}<br>{entity}{'.' if entity else ''}{attribute}" for key, (entity, attribute) in bindings if key in bound_keys]
        if types is not None:
            rows = [row for row in rows if row.get("ApplicableEntity") in types]
        rows = sorted([row.get(key, "") for key in bound_keys] for row in rows)
        return headers, rows

    def get_applicable_relationships(self, usage, concept, resource):
        rows = [dict(row) for row in self.structure.get("xmi_concepts", {}).get(usage, {}).get(concept, [])]
        rows = [row for row in rows if row.get("ApplicableEntity") == resource]
        if not rows or len(rows[0].keys()) == 1:
            return

        data = []
        should_show_as_table = False
        headers = []
        for row in rows:
            del row["ApplicableEntity"]
            predefined_type = row.pop("PredefinedType", None)
            should_show_as_table = len(row.values()) > 1
            if should_show_as_table:
                if predefined_type:
                    row["PredefinedType"] = predefined_type
                if not headers:
                    headers.extend(key for key in row.keys() if key != "ApplicableEntity")
                row["name"] = "_".join(value for key, value in row.items() if key != "ApplicableEntity")
                data.append(row)
            else:
                data.append({"predefined_type": predefined_type, "name": list(row.values())[0]})

        return {"relationships": data, "should_show_as_table": should_show_as_table, "headers": headers}

    def parse_concept_bindings(self, concept: str):
        if not hasattr(self, "_concept_template_paths"):
            docs_root = self.config.repo_root / "docs" / "templates"
            self._concept_template_paths = {
                readme.parent.name.lower().replace(" ", ""): readme
                for readme in docs_root.glob("**/README.md")
            }

        readme = self._concept_template_paths.get(concept.lower())
        if readme is None or not readme.exists():
            return []

        markdown_text = readme.read_text(encoding="utf-8")
        blocks = re.findall(r"concept\s*\{.+?\}", markdown_text, flags=re.S)
        if not blocks:
            return []

        bindings = []
        for entity, attribute, binding in re.findall(r'(\w+):(\w+)\[binding="(.+?)"\]', blocks[0]):
            if attribute == "PredefinedType":
                bindings.append((binding, ("", "")))
            else:
                bindings.append((binding, (entity, attribute)))
        return bindings

    def create_entity_definition(self, entity_name, bindings, ports):
        entity_key = entity_name
        entity = entity_name.split("_")[0]
        schema_entity = entity

        table = []
        bindings_seen = set()
        all_attributes = []

        while entity:
            keys = [key for key in self.structure['entity_attributes'].keys() if key.startswith(entity + ".")]
            attributes = list(zip(keys, map(self.structure['entity_attributes'].__getitem__, keys)))[::-1]
            if entity == schema_entity:
                all_attributes = attributes
            else:
                all_attributes.extend(attributes)
            entity = self.structure['entity_supertype'].get(entity)

        forward_index = sum(kind == "forward" for _, (kind, _) in all_attributes)
        for key, (kind, value) in all_attributes:
            if kind == "derived":
                continue

            name = key.split(".")[1]
            label = name
            if kind == "forward":
                label = f"{forward_index}. {name}"
                forward_index -= 1
            elif kind == "inverse":
                label = f"      {name}"

            cardinality = re.findall(r"(\[.+?\])", value)
            if cardinality:
                cardinality = cardinality[0]
            elif kind == "forward":
                cardinality = "[0:1]" if "OPTIONAL" in value else "[1:1]"
            else:
                cardinality = "[1:1]"

            binding = bindings.get((entity_key, name), "")
            if binding:
                table.append({"label": label, "name": name, "cardinality": cardinality, "is_bound": True, "is_port": name in ports})
                bindings_seen.add((entity_key, name))
                table.append({"label": binding, "name": binding, "is_binding": True})
            else:
                table.append({"label": label, "name": name, "cardinality": cardinality, "is_port": name in ports})

        is_first = True
        for (entity, attribute), binding in bindings.items():
            if entity != entity_key or (entity, attribute) in bindings_seen:
                continue
            if is_first:
                table.insert(0, {"label": "...", "name": "..."})
            table.insert(0, {"label": binding, "name": binding, "is_binding": True})
            table.insert(0, {"label": attribute, "name": attribute, "is_bound": True, "is_port": attribute in ports})
            is_first = False

        table.append({"label": schema_entity, "name": schema_entity, "is_title": True})
        table = table[::-1]

        html = '<<table border="0" cellborder="1" cellspacing="0" cellpadding="5px">'
        for row in table:
            height = 18
            align = "left"
            is_bold = False
            bgcolor = "white"
            color = "#333333"

            if row.get("is_title"):
                bgcolor = "#1976d2"
                color = "white"
                is_bold = True
            if row.get("is_binding"):
                is_bold = True
                align = "center"
                bgcolor = "#eeeeee"
            if row.get("is_bound"):
                bgcolor = "#eeeeee"
            if row.get("is_port"):
                bgcolor = "#dddddd"

            name = row["name"]
            html += "<tr>"
            html += f'<td sides="b" width="250" height="{height}" bgcolor="{bgcolor}" align="{align}" port="{name}0">'
            if is_bold:
                html += "<b>"
            html += f'<font color="{color}">{row["label"]}</font>'
            if is_bold:
                html += "</b>"
            html += "</td>"
            html += f'<td sides="b" width="20" height="{height}" bgcolor="{bgcolor}" align="right" port="{name}1">'
            html += row.get("cardinality", "")
            html += "</td></tr>"
        html += "</table>>"
        return html

    def process_graphviz_concept(self, name, markdown_text):
        graphviz_code = filter(lambda value: value.strip().startswith("concept"), re.findall("```(.*?)```", markdown_text, re.S))

        def replace_edge(match):
            is_direct_attribute = True
            entity = match.group(1).split("_")[0]
            attribute = match.group(2)
            while entity:
                data = self.structure['entity_attributes'].get(f"{entity}.{attribute}")
                if data:
                    is_direct_attribute = data[0] == "forward"
                    break
                entity = self.structure['entity_supertype'].get(entity)
            endpoint = match.group(3)
            if ":" not in endpoint:
                endpoint += ":" + endpoint.split("_")[0]
            result = f"{match.group(1)}:{match.group(2)}1 -> {endpoint}"
            if not is_direct_attribute:
                result += "[dir=back]"
            return result

        def replace_edge2(match):
            return f"{match.group(1)} -> {match.group(2)}:{match.group(3)}0"

        for graphviz in graphviz_code:
            hash_value = hashlib.sha256(graphviz.encode("utf-8")).hexdigest()
            file_name = os.path.join("svgs", f"{name}_{hash_value}.dot")
            graph_data = graphviz.replace("concept", "digraph")
            graph_data = re.sub(r"(?<=\w)\-(?=\w)", "", graph_data)

            nodes = set(node.split(":")[0] for node in (re.findall(r"([\:\w]+)\s*\->", graph_data) + re.findall(r"\->\s*([\:\w]+)", graph_data)))
            node_ports = {node: [] for node in nodes}
            for node in (re.findall(r"([\:\w]+)\s*\->", graph_data) + re.findall(r"\->\s*([\:\w]+)", graph_data)):
                if len(node.split(":")) > 1:
                    node_ports[node.split(":")[0]].append(node.split(":")[1])

            graph_data = re.sub(r"(\w+)\:(\w+)\s*\->\s*([\:\w]+)", replace_edge, graph_data)
            graph_data = re.sub(r"([\w\:]+)\s*\->\s*(\w+)\:(\w+)", replace_edge2, graph_data)

            bindings = {}
            for entity, attribute, binding in re.findall(r'(\w+)\:(\w+)\[binding="([\w_]+)"\]', graph_data):
                bindings[(entity, attribute)] = binding
            graph_data = re.sub(r'\w+\:\w+\[binding="[\w_]+"\]', "", graph_data)

            graph = pydot.graph_from_dot_data(graph_data)[0]
            graph.set_node_defaults(shape="plaintext", width="3")
            graph.set_nodesep("0.1")
            graph.set_splines("polyline")
            graph.set_rankdir("LR")

            for node in nodes:
                if node.startswith("Ifc"):
                    graph.add_node(pydot.Node(node, label=self.create_entity_definition(node, bindings, node_ports.get(node, []))))
                elif node.startswith("constraint_"):
                    graph.get_node(node)[0].set_fillcolor("#ffaaaa")
                    graph.get_node(node)[0].set_shape("rect")
                    graph.get_node(node)[0].set_style("filled")
                else:
                    url = {}
                    label = node.replace("_", " ")
                    concept_node = self.make_concept(["Partial Templates"], exclude_partial=False).find(label)
                    if concept_node:
                        url = {"URL": concept_node.url}
                    graph.add_node(pydot.Node(node, label=label, fillcolor="#aaffaa", shape="rect", style="filled", **url))

            graph.obj_dict["nodes"]["node"][0]["sequence"] = -1
            with open(file_name, "w", encoding="utf-8") as handle:
                handle.write(graph.to_string())

            markdown_text = markdown_text.replace(f"```{graphviz}```", f"![](/svgs/{name}_{hash_value}.svg)")

            with tempfile.TemporaryDirectory() as tmpdir:
                # windows graphviz dot chokes on some of the longer paths so move to /tmp as intermediate step
                tmpdir = Path(tmpdir)

                # Keep a short input filename inside the temp dir
                tmp_dot = tmpdir / Path(file_name).name
                shutil.copy2(file_name, tmp_dot)

                subprocess.run(
                    [shutil.which("dot") or "dot", "-O", "-Tsvg", "-Gbgcolor=#ffffff00", tmp_dot.name],
                    cwd=tmpdir,
                    check=True,
                )

                tmp_svg = tmpdir / (tmp_dot.name + ".svg")
                final_svg = file_name + ".svg"
                shutil.copy2(tmp_svg, final_svg)

        return markdown_text

    def get_concept_usage(self, resource, builder, mdc):
        concepts_markdown = mdp.markdown_attribute_parser(data=mdc, heading_name="Concepts", short=False)
        ty = resource
        supertype_chain = []
        while ty is not None:
            supertype_chain.append(ty)
            ty = self.structure['entity_supertype'].get(ty)
        supertype_chain = list(reversed(supertype_chain))

        builder_concepts = list(builder.concepts)

        concept_order = {}
        for a, b, _ in builder_concepts:
            concept_order[a] = concept_order.get(a, []) + [b.lower()]

        # Create a lookup for concept name to URL
        concept_hierarchy = self.make_concept([""])

        def flatten_hierarchy(h):
            yield h
            for ch in h.children:
                yield from flatten_hierarchy(ch)

        concept_lookup = {c.text.replace(" ", ""): (c.text, c.url) for c in flatten_hierarchy(concept_hierarchy)}

        # Grabs concepts from XMI, and then enhances them with human names and descriptions from Markdown
        # Sorry if you need to read this code I found it really confusing good luck.

        # This code block loops through all the concepts defined in XMI and creates a nested dict structure:
        # > IfcWall (ifc_class):
        # > > General Usage (view_name):
        # > > > Property Sets for Objects (xmi_concept_name
        # > > > > Relationships: [Pset_WallCommon, ...]
        # > > > > Is Inherited: True if this concept is defined explicitly for IfcWall
        # > > > > Is Inherited: False if inherited from a supertype
        concept_groups = {}
        groups = []
        for view_name, xmi_concepts in self.structure.get("xmi_concepts", {}).items():
            for xmi_concept_name, xmi_relationships in xmi_concepts.items():
                for xmi_relationship in xmi_relationships:
                    applicable_entity = xmi_relationship.get("ApplicableEntity", None)
                    in_chain = False
                    for ifc_class in supertype_chain:
                        if ifc_class == applicable_entity:
                            in_chain = True
                        if not in_chain:
                            continue
                        is_inherited = ifc_class != applicable_entity

                        concept_groups.setdefault(ifc_class, {})
                        concept_groups[ifc_class].setdefault(view_name, {})
                        concept_groups[ifc_class][view_name].setdefault(
                            xmi_concept_name, {"relationships": [], "is_inherited": is_inherited}
                        )
                        concept_groups[ifc_class][view_name][xmi_concept_name]["relationships"].append(xmi_relationship)

        # With this "simpler" concept_groups nested dict, let's build the necessary data structure for the template
        # Let's start by walking through the inherited classes
        for ifc_class in supertype_chain:
            views = concept_groups.get(ifc_class, {})

            concepts = []
            # For each view (General Usage, Reference View, etc)
            for view_name, view_concepts in views.items():

                # For each concept belonging to that view
                for name, data in view_concepts.items():
                    human_name = concept_lookup.get(name, [name, ""])[0]
                    description = None

                    # Can we potentially enrich the description from the markdown?
                    for markdown_concept in builder_concepts:
                        if markdown_concept[0] != ifc_class:
                            continue
                        markdown_name = self.get_concept_name(markdown_concept[1])
                        stripped_name = markdown_name.replace(" ", "")
                        if stripped_name.lower() == name.lower():
                            description = self.process_markdown(resource, markdown_concept[2])

                    relationships = self.get_applicable_relationships(view_name, name, ifc_class)
                    relationship_descriptions = concepts_markdown.get_children(human_name) if concepts_markdown else None
                    # Let's try to enrich relationships with descriptions from the markdown
                    if relationships and relationships["relationships"] and relationship_descriptions:
                        for relationship in relationships["relationships"]:
                            relationship["description"] = relationship_descriptions.get(relationship["name"])

                    should_show_concept = False
                    if not data["is_inherited"]:
                        # Always show concepts for the active class
                        should_show_concept = True
                    elif data["is_inherited"] and (description or relationships):
                        # If the active class has a description, it may redisplay an inherited concept
                        should_show_concept = True

                    if should_show_concept:
                        concepts.append(
                            {
                                "name": human_name,
                                "is_inherited": data["is_inherited"],
                                "description": description,
                                "usage": self.separate_camel(view_name).replace("General Usage", "General"),
                                "url": concept_lookup.get(name, [None, None])[1],
                                "applicable_relationships": relationships,
                            }
                        )

            groups.append(
                {
                    "name": ifc_class,
                    "is_inherited": ifc_class != resource,
                    "concepts": sorted(concepts, key=lambda x: x["name"]),
                    "total_concepts": len(concepts),
                }
            )

        def lookup_markdown_order(ent, di):
            try:
                return concept_order.get(ent, []).index(di.get('name').lower())
            except ValueError:
                return 10000

        for group in groups:
            group.get('concepts', []).sort(key=lambda item, entity=group.get('name'): lookup_markdown_order(entity, item))

        total_inherited_concepts = sum([g["total_concepts"] for g in groups if g["is_inherited"]])

        inherited_groups_with_concepts = [g for g in groups if g["is_inherited"] and g["total_concepts"]]
        if inherited_groups_with_concepts:
            inherited_groups_with_concepts[-1]["is_last_inherited_group"] = True

        if [g for g in groups if g["total_concepts"]]:
            return {
                "number": self.numberer.generate(),
                "groups": groups,
                "total_inherited_concepts": total_inherited_concepts,
            }

    def get_examples(self, resource):
        examples = []
        for name in self.structure.get("examples_by_type", {}).get(resource.upper()) or []:
            image = self._url_for("get_asset", asset="img/ifc-file-format.png")
            if (self.examples_models_root / name / "thumb.png").exists():
                image = self._url_for("get_example", example=name) + "/thumb.png"
            examples.append(
                {
                    "name": self._example_title(name.split("/")[-1]),
                    "url": self._url_for("annex_e_example_page", s=name),
                    "image": image,
                }
            )
        if examples:
            return {"number": self.numberer.generate(), "examples": examples}

    def get_adoption(self, resource):
        return

    def get_formal_representation(self, resource):
        express = self.structure['entity_definitions'].get(resource)
        if express:
            return {"number": self.numberer.generate(), "express": express}

    def get_references(self, resource):
        references = set()
        for ifc_entity, express in self.structure['entity_definitions'].items():
            if ifc_entity == resource:
                continue
            if resource in re.split(r"[^a-zA-Z]", express):
                references.add(ifc_entity)
        if references:
            return {"number": self.numberer.generate(), "references": sorted(references)}

    def get_changelog(self, resource):
        changelog_data = self.structure.get("changes_by_type", {}).get(resource, {})
        if not changelog_data:
            return

        changelog = {"number": self.numberer.generate(), "sections": []}
        self.numberer.begin_subsection()
        for section, changes in changelog_data.items():
            changelog["sections"].append(
                {
                    "name": section,
                    "number": self.numberer.generate(),
                    "changes": [
                        {
                            "is_addition": "add" in change[0],
                            "is_deletion": "delet" in change[0],
                            "is_modification": "modif" in change[0],
                            "what_changed": change[1],
                            "description": change[2],
                        }
                        for change in changes
                    ],
                }
            )
        self.numberer.end_subsection()
        return changelog

    def get_type_values(self, resource, mdc):
        values = self.structure['type_values'].get(resource)
        if not values:
            return
        has_description = values[0] == values[0].upper()
        if has_description:
            soup = BeautifulSoup(self.process_markdown(resource, mdc))
            described_values = []
            for value in values:
                description = None
                for heading in soup.find_all("h3"):
                    if heading.text != value:
                        continue
                    description = BeautifulSoup("")
                    for sibling in heading.find_next_siblings():
                        if sibling.name == "h3":
                            break
                        description.append(sibling)
                    description = str(description)
                described_values.append({"name": value, "description": description})
            values = described_values
        return {"number": self.numberer.generate(), "has_description": has_description, "schema_values": values}

    def get_applicability(self, resource):
        try:
            template_type_mdc = Path(self.get_resource_path("IfcPropertySetTemplateTypeEnum")).read_text(encoding="utf-8")
        except Exception:
            template_type_mdc = ""
        descriptions = dict(mdp.markdown_attribute_parser(data=template_type_mdc, heading_name="Items")) if template_type_mdc else {}
        definition = self.structure['pset_definitions'][resource]
        return {
            "number": self.numberer.generate(),
            "entities": definition["applicability"],
            "template_type": definition["template_type"],
            "description": descriptions.get(definition["template_type"]),
        }

    def get_properties(self, resource, mdc):
        pset_specific_comments = dict(mdp.markdown_attribute_parser(data=mdc, heading_name="Comments"))

        def make_prop(prop):
            try:
                prop_doc = self.process_markdown(
                    resource,
                    (self.config.repo_root / "docs" / "properties" / prop["name"][0].lower() / f"{prop['name']}.md").read_text(encoding="utf-8"),
                )
            except Exception:
                prop_doc = ""

            prop_type = "" if self.structure['pset_definitions'][resource]["kind"] == "quantity_set" else prop["type"]
            comment = pset_specific_comments.get(prop["name"])
            if comment:
                prop_doc += self.process_markdown(resource, comment)

            data_type = prop["data"]
            if isinstance(data_type, str) and "PEnum" in data_type and "(" in data_type:
                data_type = data_type.split("(")[0]

            return {
                "name": prop["name"],
                "type": prop_type,
                "data_type": data_type,
                "description": prop_doc,
                "edit_url": self._url_for("property", prop=prop["name"]),
            }

        return {
            "number": self.numberer.generate(),
            "is_pset": self.structure['pset_definitions'][resource]["kind"] != "quantity_set",
            "properties": [make_prop(prop) for prop in self.structure['pset_definitions'][resource]["properties"]],
        }

    def find_schema(self, slug: str):
        for title, items in self.structure['hierarchy']:
            for schema_name, members in items:
                if schema_name.lower() == slug:
                    return title, items, schema_name, members
        return None

    def set_listing_payloads(self, listing_payloads: dict[str, list[dict[str, str]]] | None):
        self.listing_payloads = listing_payloads or {"references": [], "figures": [], "tables": []}


    def _render_resource(self, resource: str) -> StaticResponse:
        translations = translate.get_translations(resource)
        index = self.name_to_number[resource]

        self.numberer = SectionNumberGenerator(index)
        self.numberer.begin_subsection()
        definition_number = self.numberer.generate()

        path = Path(self.get_resource_path(resource))
        markdown = path.read_text(encoding="utf-8") if path.exists() else ""

        if "Entities" in path.as_posix():
            builder = resource_documentation_builder(resource, self)
            mvds = [
                {"abbr": "".join(re.findall(r"[A-Z]|(?<=-)[a-z]", name)), "cause": usage[resource]}
                for name, usage in self.structure.get("mvd_entity_usage", {}).items()
                if resource in usage
            ]
            is_product_or_type = False
            entity = resource
            while entity:
                entity = self.structure['entity_supertype'].get(entity)
                if entity in ("IfcProduct", "IfcTypeProduct"):
                    is_product_or_type = True
                    break

            return self._html_response(
                "entity.html",
                navigation=self.get_navigation(resource),
                number=index,
                definition_number=definition_number,
                definition=self.get_definition(resource, markdown),
                entity=resource,
                path=self._repo_relative(path),
                entity_inheritance=self.get_entity_inheritance(resource),
                attributes=self.get_attributes(resource, builder),
                formal_propositions=self.get_formal_propositions(resource, builder),
                property_sets=self.get_property_sets(resource),
                concept_usage=self.get_concept_usage(resource, builder, markdown),
                examples=self.get_examples(resource),
                adoption=self.get_adoption(resource),
                formal_representation=self.get_formal_representation(resource),
                references=self.get_references(resource),
                changelog=self.get_changelog(resource),
                is_deprecated=resource in self.structure['deprecated_entities'],
                is_abstract=resource in self.structure['abstract_entities'],
                mvds=mvds,
                is_product_or_type=is_product_or_type,
                translations=translations,
            )

        if resource in self.structure['pset_definitions']:
            return self._html_response(
                "property.html",
                navigation=self.get_navigation(resource),
                content=self.get_definition(resource, markdown),
                number=index,
                definition_number=definition_number,
                entity=resource,
                path=self._repo_relative(path),
                applicability=self.get_applicability(resource),
                properties=self.get_properties(resource, markdown),
                changelog=self.get_changelog(resource),
                translations=translations,
            )

        builder = resource_documentation_builder(resource, self)
        return self._html_response(
            "type.html",
            navigation=self.get_navigation(resource),
            content=self.get_definition(resource, markdown),
            number=index,
            definition_number=definition_number,
            entity=resource,
            path=self._repo_relative(path),
            type_values=self.get_type_values(resource, markdown),
            formal_propositions=self.get_formal_propositions(resource, builder),
            formal_representation=self.get_formal_representation(resource),
            references=self.get_references(resource),
            changelog=self.get_changelog(resource),
        )

    def _render_concept_list(self) -> StaticResponse:
        path = self.config.repo_root / "docs" / "templates" / "README.md"
        html = self.process_markdown("", path.read_text(encoding="utf-8"))
        return self._html_response(
            "concept_listing.html",
            navigation=self.get_navigation(),
            content=html,
            path=self._repo_relative(path),
            title=self.chapter_lookup(number=4)["name"],
            number=4,
            sections=[
                {"cs": self.make_concept([""], exclude_partial=True).children},
                {
                    "title": "Partial Templates",
                    "number": "4.2",
                    "cs": self.make_concept(["Partial Templates"]).children,
                },
            ],
        )

    def _render_concept(self, concept_path: str) -> StaticResponse:
        docs_root = self.config.repo_root / "docs" / "templates"
        normalized = concept_path.replace("_", " ")
        number = "4"
        title = self.chapter_lookup(number=4)["name"]
        markdown_root = docs_root

        if normalized:
            parts = normalized.split("/")
            if parts[0] == "Partial Templates":
                number = "4.2"
                parts = parts[1:]
                normalized = "/".join(parts)
                markdown_root = docs_root / "Partial Templates"
                if not parts:
                    title = "Partial Templates"
            else:
                number = "4.1"

            if parts:
                title = parts[-1]
                for parent_path in itertools.accumulate([[part] for part in parts]):
                    choices = sorted(
                        entry
                        for entry in os.listdir(markdown_root.joinpath(*parent_path[:-1]))
                        if (markdown_root.joinpath(*parent_path[:-1], entry)).is_dir() and entry != "Partial Templates"
                    )
                    number += f".{choices.index(parent_path[-1]) + 1}"

        path = markdown_root / normalized / "README.md" if normalized else markdown_root / "README.md"
        diagram = None
        if path.exists():
            markdown = path.read_text(encoding="utf-8")
            if "concept {" in markdown:
                diagram_markdown = self.process_graphviz_concept("".join(char for char in normalized if char.isalnum()), markdown[markdown.index("```") :])
                diagram = self.process_markdown("", diagram_markdown)
                soup = BeautifulSoup(diagram)
                for svg in soup.find_all("svg"):
                    svg.attrs["width"] = f"{int(svg.attrs['width'][:-2]) // 4 * 3}px"
                    svg.attrs["height"] = f"{int(svg.attrs['height'][:-2]) // 4 * 3}px"
                diagram = str(soup)
                markdown = markdown[: markdown.index("```")]
            html = self.process_markdown("", markdown)
        else:
            html = ""

        xmi_concept = title.replace(" ", "")
        tables = ""
        for view_name, concepts in self.structure.get("xmi_concepts", {}).items():
            if xmi_concept not in concepts:
                continue
            tables += f"<h3>{self.separate_camel(view_name)}</h3>"
            headers, rows = self.create_concept_table(view_name, xmi_concept, None)
            if rows:
                tables += tabulate.tabulate(rows, headers=headers, tablefmt="unsafehtml")

        if not diagram and not BeautifulSoup(html).text.strip() and not tables:
            html = '<p class="search-skip">This section is intentionally left blank. This template merely serves as a grouping of sub templates.</p>'

        return self._html_response(
            "concept.html",
            navigation=self.get_navigation(number=number),
            content=html,
            diagram=diagram,
            tables=tables,
            path=self._repo_relative(path),
            title=title,
            number=number,
        )

    def _render_chapter(self, number: str) -> StaticResponse:
        try:
            chapter_number = int(number)
        except ValueError:
            self._abort(404)

        chapter = self.chapter_lookup(number=chapter_number)
        title = chapter["name"]
        category = title.split(" ")[0].lower()
        path = self.config.repo_root / "docs" / "schemas" / category / "README.md"
        if path.exists():
            soup = BeautifulSoup(markdown.markdown(path.read_text(encoding="utf-8")))
            heading = soup.find("h1")
            if heading:
                heading.decompose()
            html = str(soup)
        else:
            html = ""

        subchapters = [items for name, items in self.structure['hierarchy'] if name == title][0]
        subs = [
            self._toc_entry(text=name, url=f"/{name.lower()}/content.html", number=f"{chapter_number}.{index}")
            for index, (name, _) in enumerate(subchapters, 1)
        ]

        return self._html_response(
            "chapter.html",
            navigation=self.get_navigation(number=chapter_number),
            content=html,
            path=self._repo_relative(path),
            title=title,
            number=chapter_number,
            subs=subs,
        )

    def _render_schema(self, name: str) -> StaticResponse:
        docs_root = self.config.repo_root / "docs" / "schemas"
        match = self.find_schema(name)
        if match is None:
            self._abort(404)

        category_full, schemas, title, members = match
        category = category_full.split(" ")[0].lower()
        chapter = self.chapter_lookup(cat=category)

        n1 = chapter["number"]
        n2 = [schema_name for schema_name, _ in schemas].index(title) + 1
        number = f"{n1}.{n2}"
        path = docs_root / category / title / "README.md"

        self.numberer = SectionNumberGenerator(number)
        self.numberer.begin_subsection()
        definition = None
        definition_number = None
        if path.exists():
            definition_number = self.numberer.generate()
            definition = self.process_markdown("", path.read_text(encoding="utf-8"))

        order = ["Types", "Entities", "Property Sets", "Quantity Sets", "Functions", "Rules", "PropertyEnumerations"]
        categories = [
            self._toc_entry(
                text=group,
                number=f"{number}.{index}",
                children=[
                    self._toc_entry(text=resource, number=f"{number}.{index}.{subindex}", url=f"/lexical/{resource}.html")
                    for subindex, resource in enumerate(members.get(group, []), 1)
                ],
            )
            for index, group in enumerate(order, 2)
        ]

        return self._html_response(
            "subchapter.html",
            navigation=self.get_navigation(number=number),
            definition=definition,
            path=self._repo_relative(path),
            title=title,
            number=number,
            subnumber=definition_number,
            categories=categories,
        )

    def _render_toc(self) -> StaticResponse:
        subs = list(self.NAVIGATION[1][0:4])
        subs.extend(self.annotate_hierarchy(start=5))
        return self._html_response(
            "chapter.html",
            navigation=self.get_navigation(),
            title="Contents",
            subs=subs,
        )

    def _render_annex_b(self) -> StaticResponse:
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=self._make_annex_b_navigation(),
            body_class="annex",
        )

    def _render_annex_b1(self) -> StaticResponse:
        def get_mvd_qualification(resource: str):
            return [
                {
                    "abbr": "".join(re.findall(r"[A-Z]|(?<=-)[a-z]", name)),
                    "cause": usage.get(resource),
                    "on": resource in usage,
                }
                for name, usage in self.structure.get("mvd_entity_usage", {}).items()
            ]

        def get_product_qualification(resource: str):
            entity = resource
            while entity:
                entity = self.structure['entity_supertype'].get(entity)
                if entity in ("IfcProduct", "IfcTypeProduct"):
                    return True
            return False

        items = [
            {
                "number": self.name_to_number[name],
                "url": f"/lexical/{name}.html",
                "name": name,
                "mvds": get_mvd_qualification(name),
                "is_product_or_type": get_product_qualification(name),
            }
            for name in self.entity_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Entities",
            body_class="annex",
        )

    def _render_annex_b2(self) -> StaticResponse:
        items = [
            {"number": self.name_to_number[name], "url": f"/lexical/{name}.html", "name": name}
            for name in self.type_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Types",
            body_class="annex",
        )

    def _render_annex_b3(self) -> StaticResponse:
        items = [
            {"number": self.name_to_number[name], "url": f"/lexical/{name}.html", "name": name}
            for name in sorted(self.structure['pset_definitions'].keys())
            if name in self.name_to_number
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            is_dictionary=True,
            title="Property sets",
            body_class="annex",
        )

    def _render_annex_b4(self) -> StaticResponse:
        items = [
            {"number": "", "url": f"/property/{name}.html", "name": name}
            for name in sorted({prop["name"] for definition in self.structure['pset_definitions'].values() for prop in definition["properties"]})
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Properties",
            body_class="annex",
        )

    def _render_annex_b5(self) -> StaticResponse:
        items = [{"number": "", "url": f"/lexical/{name}.html", "name": name} for name in self.function_names()]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Functions",
            body_class="annex",
        )

    def _render_annex_b6(self) -> StaticResponse:
        items = [{"number": "", "url": f"/lexical/{name}.html", "name": name} for name in self.rule_names()]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Rules",
            body_class="annex",
        )

    def _render_annex_b7(self) -> StaticResponse:
        items = [
            {"number": "", "url": f"/lexical/{name}.html", "name": name}
            for name in self.propertyenumeration_names()
        ]
        return self._html_response(
            "annex-b.html",
            navigation=self.get_navigation(),
            items=items,
            title="Property Enumerations",
            body_class="annex",
        )

    def _render_annex_c(self) -> StaticResponse:
        entities = []
        indentation_map = {0: entities}
        path = self.config.code_dir / "inheritance_listing.txt"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.rstrip("\n")
                padding = line.count(" ")
                entity = line.strip()
                data = {
                    "number": self.name_to_number[entity],
                    "url": f"/lexical/{entity}.html",
                    "name": entity,
                    "children": [],
                }
                if padding == 0:
                    entities.append(data)
                else:
                    indentation_map[padding - 1]["children"].append(data)
                indentation_map[padding] = data

        return self._html_response(
            "annex-c.html",
            navigation=self.get_navigation(),
            entities=entities,
            body_class="annex",
        )

    def _render_annex_d(self) -> StaticResponse:
        diagrams = [
            self._toc_entry(name, url=f"/annex_d/{name}.html", number=f"D.{index}")
            for index, name in enumerate(self._diagram_names(), 1)
        ]
        return self._html_response(
            "annex-d.html",
            navigation=self.get_navigation(),
            diagrams=diagrams,
            body_class="annex",
        )

    def _render_annex_d_diagram_page(self, name: str) -> StaticResponse:
        diagrams = self._diagram_names()
        if name not in diagrams:
            self._abort(404)
        return self._html_response(
            "annex-d-item.html",
            navigation=self.get_navigation(),
            name=name,
            number=diagrams.index(name) + 1,
            body_class="annex",
        )

    def _render_annex_e(self) -> StaticResponse:
        return self._html_response(
            "annex-e.html",
            navigation=self.get_navigation(),
            examples=self._build_example_tree(),
            body_class="annex",
        )

    def _render_annex_e_example_page(self, example: str) -> StaticResponse:
        examples, tree = self._build_example_tree(True)
        if example not in examples:
            self._abort(404)

        url_to_number = {}

        def visit(entry):
            if entry.url:
                url_to_number[entry.url] = entry.number
            for child in entry.children:
                visit(child)

        visit(tree)

        example_dir = self.examples_models_root / example
        path = example_dir / "README.md"
        parent_path = example_dir.parent / "README.md"
        html = self.process_markdown("", path.read_text(encoding="utf-8"))
        if parent_path.exists():
            html = self.process_markdown("", parent_path.read_text(encoding="utf-8")) + html

        candidates = list(example_dir.glob("*.ifc")) + list(example_dir.glob("*.xml"))
        code = candidates[0].read_text(encoding="ascii", errors="ignore")
        code = re.sub(r"(?<=FILE_SCHEMA\(\(')IFC\w+", SCHEMA_NAME, code)
        code = re.sub(r"(?<=FILE_SCHEMA \(\(')IFC\w+", SCHEMA_NAME, code)

        image_pattern = re.compile(r".*\.(png|jpg|jpeg)", re.IGNORECASE)
        images = [
            f"/examples/{example}/{candidate.name}"
            for candidate in sorted(example_dir.iterdir())
            if candidate.is_file() and image_pattern.match(candidate.name) and candidate.name.lower() != "thumb.png"
        ]

        return self._html_response(
            "annex-e-item.html",
            navigation=self.get_navigation(),
            content=html,
            path=path.resolve().relative_to(self.examples_repo_root).as_posix(),
            repo="buildingSMART/IFC4.3.x-sample-models",
            branch="main",
            title=self._example_title(Path(example).name),
            code=code,
            images=images,
            number=url_to_number[self.request.path],
            body_class="annex",
        )

    def _render_annex_f(self) -> StaticResponse:
        _, _, _, html = self._get_content_html("changelog", require_number=False)
        changelog_data = self.structure.get("changes_by_schema", [])
        changelogs = {"sections": []}
        self.numberer.begin_subsection()
        for section in changelog_data:
            section_name = section[0]
            changes = section[1]
            changelogs["sections"].append(
                {
                    "name": section_name,
                    "changes": [
                        {
                            "entity": change[0],
                            "is_addition": "add" in change[1],
                            "is_deletion": "delet" in change[1],
                            "is_modification": "modif" in change[1],
                            "what_changed": change[2],
                            "description": change[3],
                        }
                        for change in changes
                    ],
                }
            )
        self.numberer.end_subsection()
        return self._html_response(
            "annex-f.html",
            definition=html,
            navigation=self.get_navigation(),
            changelogs=changelogs,
            body_class="annex",
        )

    def _render_index(self) -> StaticResponse:
        items = [
            {"number": "", "title": f"Listing of {kind}", "url": f"/listing-{kind}.html"}
            for kind in ("references", "figures", "tables")
        ]
        return self._html_response("index.html", navigation=self.get_navigation(), items=items, title="Index")

    def _render_search(self) -> StaticResponse:
        return self._html_response(
            "search.html",
            navigation=self.get_navigation(),
            title="Search",
            body_class="search-page",
        )

    def _render_listing(self, kind: str) -> StaticResponse:
        items = list(self.listing_payloads.get(kind, []))
        if kind == "references":
            grouped = []
            for title, group in itertools.groupby(items, key=lambda item: item["title"]):
                refs = []
                for entry in group:
                    url = entry["url"]
                    if url.startswith("/lexical/") and url.endswith(".html"):
                        refs.append(url[len("/lexical/") : -5])
                grouped.append(
                    {
                        "number": title,
                        "url": "",
                        "subitems": [{"url": f"/lexical/{resource}.html", "title": resource} for resource in refs],
                    }
                )
            items = [item for item in grouped if not (len(item["subitems"]) == 1 and item["subitems"][0]["title"] == item["number"])]
        return self._html_response(
            "index.html",
            navigation=self.get_navigation(),
            items=items,
            title=f"Listing of {kind}",
        )

def _destination_for(config: BuildConfig, public_path: str) -> Path:
    if public_path == "/":
        return config.output_dir / "index.html"
    stripped = public_path.lstrip("/")
    target = config.output_dir / stripped
    if public_path.endswith("/"):
        return target / "index.html"
    return target

_RENDERER = None
_REFINER = None

def init_worker(
    config: BuildConfig,
    structure: dict,
    name_to_number: dict[str, str],
    listing_payloads: dict[str, list[dict[str, str]]] | None,
    resource_names: tuple[str, ...],
):
    global _RENDERER, _REFINER
    _RENDERER = StaticTemplateRenderer(
        config,
        structure=structure,
        name_to_number=name_to_number,
        listing_payloads=listing_payloads,
    )
    _REFINER = HtmlRefiner(resource_names)

def _render_html_path_task(
    config: BuildConfig,
    public_path: str,
):
    os.chdir(config.code_dir)

    response = _RENDERER.render_path(public_path)
    html = response.body.decode("utf-8")

    result = _REFINER.refine(public_path, html)

    destination = _destination_for(config, public_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(result.html, encoding="utf-8")

    return result


class StaticSiteBuilder:
    def __init__(self, config: BuildConfig):
        self.config = config
        self.structure = None
        self.name_to_number: dict[str, str] = {}
        self.collector = ListingCollector()
        self.errors: list[tuple[str, int]] = []

    def build(self) -> dict[str, int]:
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(self.config.code_dir)
        self.errors = []
        self.collector = ListingCollector()

        translate.build_cache(jobs=self.config.threads, pool="thread")
        self._prepare_generated_assets()

        structure_path = self.config.repo_root / "output" / "structure.json"
        self.structure = json.loads(structure_path.read_text(encoding="utf-8"))
        resource_names = self.structure['entity_definitions'].keys() | self.structure['pset_definitions'].keys() | self.structure['type_values'].keys()
        resource_names = tuple(sorted(resource_names))

        def name_to_number():
            ntn = {}

            for i, (cat, schemas) in enumerate(self.structure['hierarchy'], start=5):
                for j, (schema_name, members) in enumerate(schemas, start=1):
                    for k, ke in enumerate(
                        ["Types", "Entities", "Property Sets", "Quantity Sets", "Functions", "Rules", "PropertyEnumerations"], start=2
                    ):
                        for l, name in enumerate(members.get(ke, ()), start=1):
                            ntn[name] = ".".join(map(str, (i, j, k, l)))

            return ntn
        
        self.name_to_number = name_to_number()

        self._copy_static_support_files()
        self._render_html_paths(self._content_paths(), collect=True, resource_names=resource_names)

        payloads = self.collector.payloads()
        self._write_listing_json(payloads)
        self._render_html_paths(self._listing_paths(), collect=False, listing_payloads=payloads, resource_names=resource_names)
        self._render_html_paths(self._utility_paths(), collect=False, resource_names=resource_names)

        self._copy_generated_svgs()
        if not self.config.no_index:
            self._build_search_index()

        return {
            "written": len([path for path in self.config.output_dir.rglob("*") if path.is_file()]),
            "errors": len(self.errors),
        }

    def _prepare_generated_assets(self) -> None:
        (self.config.code_dir / "svgs").mkdir(parents=True, exist_ok=True)

        psd_zip = self.config.repo_root / "output" / "psd.zip"
        if psd_zip.exists() or (self.config.code_dir / "psd.zip").exists():
            return

        psd_zip.parent.mkdir(parents=True, exist_ok=True)

        for source_dir in (
            self.config.repo_root / "output" / "psd",
        ):
            if not source_dir.is_dir():
                continue
            archive = shutil.make_archive(
                str(psd_zip.with_suffix("")),
                "zip",
                root_dir=source_dir,
            )
            if Path(archive) != psd_zip:
                Path(archive).replace(psd_zip)
            break

    def _content_paths(self) -> list[str]:
        return [
            "/",
            "/toc.html",
            "/content/foreword.html",
            "/content/introduction.html",
            "/content/scope.html",
            "/content/normative_references.html",
            "/content/terms_and_definitions.html",
            "/content/bibliography.html",
            "/concepts/content.html",
            "/chapter-5.html",
            "/chapter-6.html",
            "/chapter-7.html",
            "/chapter-8.html",
            "/annex-a.html",
            "/annex-a-express.html",
            "/annex-a-xsd.html",
            "/annex-b.html",
            "/annex-b1.html",
            "/annex-b2.html",
            "/annex-b3.html",
            "/annex-b4.html",
            "/annex-b5.html",
            "/annex-b6.html",
            "/annex-b7.html",
            "/annex-c.html",
            "/annex-d.html",
            "/annex-e.html",
            "/annex-f.html",
            *self._sample_paths(self._schema_paths()),
            *self._sample_paths(self._resource_paths()),
            *self._sample_paths(self._property_paths()),
            *self._sample_paths(self._concept_paths()),
            *self._sample_paths(self._example_paths()),
            *self._sample_paths(self._diagram_page_paths()),
        ]

    def _sample_paths(self, paths: list[str]) -> list[str]:
        if self.config.sample_percent >= 100.0 or len(paths) <= 1:
            return paths

        target_count = max(1, int(round(len(paths) * (self.config.sample_percent / 100.0))))
        if target_count >= len(paths):
            return paths

        indices = sorted({min(int(i * len(paths) / target_count), len(paths) - 1) for i in range(target_count)})
        return [paths[index] for index in indices]

    def _listing_paths(self) -> list[str]:
        return ["/indices.html", "/listing-references.html", "/listing-figures.html", "/listing-tables.html"]

    def _utility_paths(self) -> list[str]:
        return ["/search.html"]

    def _schema_paths(self) -> list[str]:
        return [
            f"/{schema_name.lower()}/content.html"
            for _, schemas in self.structure['hierarchy']
            for schema_name, _ in schemas
        ]

    def _resource_paths(self) -> list[str]:
        return [f"/lexical/{name}.html" for name in sorted(self.name_to_number.keys())]

    def _property_paths(self) -> list[str]:
        property_names = sorted(
            {
                prop["name"]
                for definition in self.structure['pset_definitions'].values()
                for prop in definition["properties"]
            }
        )
        return [f"/property/{name}.html" for name in property_names]

    def _concept_paths(self) -> list[str]:
        templates_root = self.config.repo_root / "docs" / "templates"
        paths = []
        for readme in sorted(templates_root.glob("**/README.md")):
            if readme.parent == templates_root:
                continue
            relative = readme.parent.relative_to(templates_root).as_posix().replace(" ", "_")
            paths.append(f"/concepts/{relative}/content.html")
        return paths

    def _example_paths(self) -> list[str]:
        examples_root = self.config.repo_root.parent / "examples" / "models"
        paths = []
        if not examples_root.exists():
            return paths
        for model in sorted(examples_root.glob("**/*.ifc")):
            if (model.parent / "README.md").exists():
                relative = model.parent.relative_to(examples_root).as_posix()
                paths.append(f"/annex_e/{relative}.html")
        return sorted(set(paths))

    def _diagram_page_paths(self) -> list[str]:
        diagram_root = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        if not diagram_root.exists():
            return []
        return [f"/annex_d/{path.stem}.html" for path in sorted(diagram_root.glob("*.png"))]

    def _search_source_paths(self) -> list[str]:
        excluded = {"/toc.html", "/search.html"}
        return [
            public_path
            for public_path in self._content_paths()
            if public_path not in excluded and not public_path.startswith("/annex")
        ]

    def _should_render(self, path: str) -> bool:
        if self.config.include_paths is None:
            return True

        normalized = path.strip("/")
        return any(
            normalized == include.strip("/")
            or (
                include.strip("/")
                and normalized.startswith(include.strip("/") + "/")
            )
            for include in self.config.include_paths
        )

    def _render_html_paths(
        self,
        public_paths: list[str],
        *,
        collect: bool,
        listing_payloads: dict[str, list[dict[str, str]]] | None = None,
        resource_names: tuple[str, ...],
    ) -> None:
        public_paths = [p for p in public_paths if self._should_render(p)]

        if self.config.profile or self.config.threads == 1:
            for public_path in public_paths:
                try:
                    init_worker(self.config, self.structure, self.name_to_number, listing_payloads, resource_names)
                    result = _render_html_path_task(self.config, public_path)
                except RenderAbort as exc:
                    self.errors.append((public_path, exc.status_code))
                    continue
                if collect:
                    self.collector.merge(result)
            return

        with ProcessPoolExecutor(
            max_workers=self.config.threads,
            initializer=init_worker,
            initargs=(self.config, self.structure, self.name_to_number, listing_payloads, resource_names),
        ) as executor:
            futures = {
                executor.submit(_render_html_path_task, self.config, public_path): public_path
                for public_path in public_paths
            }
            for future in as_completed(futures):
                public_path = futures[future]
                try:
                    result = future.result()
                except RenderAbort as exc:
                    self.errors.append((public_path, exc.status_code))
                    continue
                if collect:
                    self.collector.merge(result)

    def _write_listing_json(self, payloads: dict[str, list[dict[str, str]]]) -> None:
        for kind, payload in payloads.items():
            path = self.config.code_dir / f"listing_{kind}.json"
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _build_search_index(self) -> None:
        search_builder = SearchIndexBuilder(self.config.output_dir)
        search_builder.write(
            self._search_source_paths(),
            self.config.output_dir / "assets" / "search" / "search-index.json",
        )

    def _copy_static_support_files(self) -> None:
        self._copy_tree(self.config.repo_root / "docs" / "assets", self.config.output_dir / "assets")
        self._copy_tree(self.config.repo_root / "docs" / "figures", self.config.output_dir / "figures")
        self._copy_tree(self.config.repo_root.parent / "examples" / "models", self.config.output_dir / "examples")
        self._copy_tree(self.config.repo_root / "output" / "bsdd", self.config.output_dir / "bsdd")

        self._copy_file(_generated_file(self.config, "IFC.exp"), self.config.output_dir / f"{SCHEMA_NAME}.exp")
        self._copy_file(_generated_file(self.config, "IFC.xsd"), self.config.output_dir / f"{SCHEMA_NAME}.xsd")
        self._copy_file(_generated_file(self.config, "psd.zip"), self.config.output_dir / "annex-a-psd.zip")

        diagram_root = self.config.repo_root / "output" / "ifc4x3_add2.uml"
        annex_d_root = self.config.output_dir / "annex_d"
        if diagram_root.exists():
            annex_d_root.mkdir(parents=True, exist_ok=True)
            for path in diagram_root.glob("*.png"):
                self._copy_file(path, annex_d_root / path.name)

    def _copy_generated_svgs(self) -> None:
        self._copy_tree(self.config.code_dir / "svgs", self.config.output_dir / "svgs")

    def _copy_tree(self, source: Path, destination: Path) -> None:
        if source.exists():
            shutil.copytree(source, destination, dirs_exist_ok=True)

    def _copy_file(self, source: Path, destination: Path) -> None:
        if not source.exists():
            return
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
