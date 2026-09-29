import os
import json
import re
import subprocess

CODE_DIR = os.path.dirname(os.path.abspath(__file__))

version_dict = json.load(open(os.path.join(CODE_DIR, 'version.json'), encoding='utf-8'))
version_tuple = version_dict['version']
status = version_dict['status']
status_number = list(version_dict['@status-options'].keys()).index(status)
status_message = version_dict['@status-options'][status]
prefixes = ('IFC', 'X', '_ADD', '_TC')
schema_version_string = ''.join(''.join(map(str, t)) if t[1] else '' for t in zip(prefixes, version_tuple))
spec_version_string = f'IFC {".".join(map(str, version_tuple))}'
REPO_DIR = os.path.abspath(os.environ.get("REPO_DIR", os.path.join(CODE_DIR, "..")))


def _git(*args):
    return subprocess.check_output(['git', '-C', REPO_DIR, *args]).decode('ascii').strip()


try:
    suffix = _git('log', '-1', '--format=%cd', '--date=format:%Y%m%d')
    assert len(suffix) == 8 and suffix.isdigit()
except:
    import traceback
    traceback.print_exc()
    suffix = '?'

spec_version_string_full = f"{spec_version_string} build {suffix}"

# Non-official builds get level + date of the last schema change, e.g. IFC4X4_DEV_20260525.
# --no-merges: the preview's build-time merges would otherwise set the date to today.
SCHEMA_LEVELS = {'DEVELOPMENT': 'DEV', 'PREVIEW': 'PREVIEW'}
schema_level = '' if status == 'OFFICIAL' else SCHEMA_LEVELS.get(status, 'DRAFT')
try:
    schema_date = _git('log', '-1', '--no-merges', '--format=%as', '--', 'schemas/*.uml').replace('-', '')
    assert len(schema_date) == 8 and schema_date.isdigit()
except:
    # no git history (shallow checkout): fall back to the build date
    schema_date = suffix if suffix != '?' else 'UNDATED'
schema_name = schema_version_string + (f'_{schema_level}_{schema_date}' if schema_level else '')
schema_name_re = re.compile(r'_(DEV|PREVIEW|DRAFT)_(\d{8}|UNDATED)$')
