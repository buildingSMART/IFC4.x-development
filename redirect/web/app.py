"""Single-route redirect service.

Every request (including would-be 404s) is answered with a 301 redirect to the
new GitHub Pages location. Paths and query strings are preserved by default.
"""

import os

from flask import Flask, redirect, request

# Where the docs now live.
NEW_PREFIX = os.environ.get(
    "REDIRECT_TARGET",
    "https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML",
).rstrip("/")

# If true, "/some/path?x=1" becomes "<NEW_PREFIX>/some/path?x=1".
# If false, every request is sent straight to NEW_PREFIX (path dropped).
PRESERVE_PATH = os.environ.get("PRESERVE_PATH", "1") == "1"

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_everything(path: str):
    """Redirect unconditionally, regardless of whether the path existed."""
    target = NEW_PREFIX
    if PRESERVE_PATH:
        target += request.path  # request.path keeps the original encoding
    if request.query_string:
        target += "?" + request.query_string.decode("utf-8")
    return redirect(target, code=301)
