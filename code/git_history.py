import base64
import hashlib
from pathlib import Path
import re
import subprocess
from functools import lru_cache
import html
from urllib.request import Request, urlopen

_GITHUB_NOREPLY = re.compile(r"^(?:\d+\+)?([^@]+)@users\.noreply\.github\.com$")

def _initials(name: str) -> str:
    parts = re.findall(r"[^\W\d_]+", name, flags=re.UNICODE)

    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    if parts:
        return parts[0][:2].upper()
    return "?"


def _initials_avatar(name: str) -> str:
    initials = html.escape(_initials(name))

    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="16" fill="#9ca3af"/>
  <text x="16" y="16"
        text-anchor="middle"
        dominant-baseline="central"
        font-family="sans-serif"
        font-size="11"
        font-weight="600"
        fill="white">{initials}</text>
</svg>"""

    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def _avatar_url(name: str, email: str):
    match = _GITHUB_NOREPLY.match(email)
    if match:
        return f"https://github.com/{match.group(1)}.png?size=32"
    digest = hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()
    # &d=404 means "return 404 if no gravatar exists", which is what we want, so we can fall back to our own initials avatar.
    gravatar_url = f"https://www.gravatar.com/avatar/{digest}?s=32&d=identicon&d=404"

    try:
        raise ValueError("")
        request = Request(gravatar_url, method="HEAD")
        with urlopen(request, timeout=2):
            return gravatar_url
    except BaseException as e:
        return _initials_avatar(name)


@lru_cache(maxsize=None)
def page_history(repo_dir : Path | str | None, path : str):
    """Return contributor and last-change data from the checked-out tree."""
    if not path:
        return None

    """
    --format=%aN%x00%aE%x00%aI%x00%B%x00%x1e ── Record Separator (0x1E)
              │   │  │   │  │   │  |  └──────── NUL
              │   │  │   │  │   │  └─────────── %B: raw commit message (subject + body)             
              │   │  │   │  │   └────────────── NUL
              │   │  │   │  └────────────────── %aI: author date, strict ISO 8601 
              │   │  │   └───────────────────── NUL
              │   │  └───────────────────────── %aE: author email, respecting .mailmap
              │   └──────────────────────────── NUL
              └──────────────────────────────── %aN: author name, respecting .mailmap
    """

    result = subprocess.run(
        [
            "git", "-C", str(repo_dir), "log", "--follow",
            "--format=%aN%x00%aE%x00%aI%x00%B%x00%x1e", "--", path,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    records = []
    for record in result.stdout.split("\x1e"):
        fields = record.strip().rstrip("\x00").split("\x00", 3)
        if len(fields) == 4:
            name, email, date, message = fields
            records.append({
                "name": name,
                "email": email,
                "date": date,
                "message": message.strip(),
            })
    if not records:
        return None

    contributors : dict[str, dict] = {}
    for commit in records:
        key = commit["email"].lower()
        contributor = contributors.setdefault(key, {
            "name": commit["name"],
            "avatar_url": _avatar_url(commit["name"], commit["email"]),
            "commits": 0,
        })
        contributor["commits"] += 1

    return {
        "contributors": sorted(contributors.values(), key=lambda c: c["commits"], reverse=True),
        "last_change": records[0],
    }
