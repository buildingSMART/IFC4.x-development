from __future__ import annotations

import json
import re
from pathlib import Path

import wordninja

from .refiner import BeautifulSoup

CAMEL_BOUNDARY = re.compile(
    r"(?<=[a-z])(?=[A-Z0-9])"
    r"|(?<=[A-Z][A-Z])(?=[0-9])"
    r"|(?<=[0-9])(?=[a-z])"
    r"|(?<=[0-9])(?=[A-Z][A-Za-z])"
    r"|(?<=[A-Z])(?=[A-Z][a-z])"
)

class SearchIndexBuilder:
    SKIP_SELECTORS = (
        ".search-skip",
        "#translations-aside",
        ".anchor",
        "a.link",
        "a.toggle-icon",
        ".toggle-icon",
    )

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def build(self, public_paths: list[str]) -> list[dict[str, str]]:
        documents = []
        for public_path in public_paths:
            file_path = self._output_file(public_path)
            if not file_path.exists():
                continue
            document = self._extract_document(public_path, file_path)
            if document is not None:
                documents.append(document)
        return documents

    def write(self, public_paths: list[str], destination: Path) -> list[dict[str, str]]:
        documents = self.build(public_paths)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(documents, indent=2, ensure_ascii=False), encoding="utf-8")
        return documents

    def _output_file(self, public_path: str) -> Path:
        if public_path == "/":
            return self.output_dir / "index.html"
        relative = public_path.lstrip("/")
        path = self.output_dir / relative
        if public_path.endswith("/"):
            return path / "index.html"
        return path

    def _extract_document(self, public_path: str, file_path: Path) -> dict[str, str] | None:
        soup = BeautifulSoup(file_path.read_text(encoding="utf-8"))
        main_content = soup.find(id="main-content")
        if main_content is None:
            return None

        fragment = BeautifulSoup(str(main_content))
        root = fragment.find(id="main-content")
        if root is None:
            return None

        for selector in self.SKIP_SELECTORS:
            for element in root.select(selector):
                element.decompose()

        for element in root.find_all(["script", "style"]):
            element.decompose()

        title = self._extract_title(public_path, soup, root)

        if m := re.match(r'((\d+\.)+\d+) (.+)$', title):
            # remove the numbering prefix from the search, people likely do not search for this.
            title = m.groups()[-1]

        headings = self._normalize_text(" ".join(node.get_text(" ", strip=True) for node in root.find_all(["h2", "h3", "h4", "h5", "h6"])))

        first_heading = root.find("h1")
        if first_heading is not None:
            first_heading.decompose()

        text = self._normalize_text(root.get_text(" ", strip=True))
        if not text:
            return None

        return {
            "id": public_path,
            "path": public_path,
            "title": title,
            "kind": self._kind_for(public_path),
            "headings": headings,
            "text": text,
        }

    def _extract_title(self, public_path: str, soup, root) -> str:
        heading = root.find("h1")
        if heading is not None:
            title = self._normalize_text(heading.get_text(" ", strip=True))
            if title:
                return title

        if public_path == "/":
            return "Cover"

        title_tag = soup.find("title")
        if title_tag is not None:
            title = self._normalize_text(title_tag.get_text(" ", strip=True))
            if " - " in title:
                title = title.split(" - ", 1)[0]
            if title:
                return title

        if public_path.startswith("/content/"):
            return public_path.rsplit("/", 1)[-1][:-4].replace("_", " ").title()
        if public_path.startswith("/chapter-"):
            return public_path.strip("/").replace("-", " ").title()
        if public_path.endswith("/content.html"):
            return public_path.strip("/").rsplit("/", 1)[0].replace("_", " ").title()

        return public_path

    def _kind_for(self, public_path: str) -> str:
        if public_path == "/" or public_path.startswith("/content/"):
            return "content"
        if public_path.startswith("/chapter-"):
            return "chapter"
        if public_path.startswith("/lexical/"):
            return "resource"
        if public_path.startswith("/property/"):
            return "property"
        if public_path.startswith("/concepts/"):
            return "concept"
        if public_path.endswith("/content.html"):
            return "schema"
        return "page"

    def _normalize_text(self, value: str, n: int = 4) -> str:
        result = []
        for piece in re.split(r"([_\s]+)", value):
            if not piece:
                continue
            # Preserve original separators.
            if re.fullmatch(r"[_\s]+", piece):
                result.append(re.sub(r"\s+", " ", piece))
                continue
            result.append(piece)
            partes = []
            for token in CAMEL_BOUNDARY.split(piece):
                if not token:
                    continue
                if token.isalpha() and token.isupper() and len(token) > n:
                    parts = wordninja.split(token.lower())
                else:
                    parts = [token.lower()]
                partes.extend(
                    part.removeprefix("ifc")
                    for part in parts
                    if part.removeprefix("ifc")
                )
            if len(partes) > 1 or (partes and partes[0] != piece.lower()):
                result.append(" (" + " ".join(partes) + ")")
        return "".join(result).strip()
