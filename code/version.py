import os
import json
import subprocess

version_tuple = json.load(open('version.json'))
prefixes = ('IFC', 'X', '_ADD', '_TC')
schema_version_string = ''.join(''.join(map(str, t)) if t[1] else '' for t in zip(prefixes, version_tuple))
spec_version_string = f'IFC {".".join(map(str, version_tuple))}'
REPO_DIR = os.path.abspath(os.environ.get("REPO_DIR", os.path.join(os.path.dirname(__file__), "..")))

try:
    suffix = subprocess.check_output(
        ['git', '-C', REPO_DIR, 'log', '-1', '--format=%cd', '--date=format:%Y%m%d']
    ).decode('ascii').strip()
    assert len(suffix) == 8 and suffix.isdigit()
except:
    import traceback
    traceback.print_exc()
    suffix = '?'

spec_version_string_full = f"{spec_version_string} build {suffix}"
