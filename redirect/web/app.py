"""Single-route redirect service.

Every request (including would-be 404s) is answered with a 301 redirect to the
new GitHub Pages location. Paths and query strings are preserved by default.
"""

import os
import re

from flask import Flask, redirect, request

# Where the docs now live.
NEW_PREFIX = os.environ.get(
    "REDIRECT_TARGET",
    "https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML",
).rstrip("/")

# If true, "/some/path?x=1" becomes "<NEW_PREFIX>/some/path?x=1".
# If false, every request is sent straight to NEW_PREFIX (path dropped).
PRESERVE_PATH = os.environ.get("PRESERVE_PATH", "1") == "1"

# Rewrite ".htm" to ".html" (case-insensitive), e.g. "/x.htm" -> "/x.html".
_HTM_SUFFIX = re.compile(r"\.htm$", re.IGNORECASE)

# Strip this legacy prefix from the start of the path.
STRIP_PREFIX = "/IFC/RELEASE/IFC4x3/HTML/"

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_everything(path: str):
    """Redirect unconditionally, regardless of whether the path existed."""
    target = NEW_PREFIX
    if PRESERVE_PATH:
        # request.path keeps the original encoding.
        new_path = request.path
        if m := re.search(r"chapter-(\d).+$", new_path):
            # rewrite .../chapter-5 or ./chapter-5/index.html -> chapter-5.html
            new_path = new_path[:m.span()[0]] + f"chapter-{m.group(1)}.html"
        if new_path.startswith(STRIP_PREFIX):
            new_path = "/" + new_path[len(STRIP_PREFIX):]
        target += _HTM_SUFFIX.sub(".html", new_path)
    if request.query_string:
        target += "?" + request.query_string.decode("utf-8")
    return redirect(target, code=301)
