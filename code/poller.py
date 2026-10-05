import os
import sys
import time
import requests
import subprocess

XML_PATH = "/tmp/ifc43-xml"
os.makedirs(XML_PATH, exist_ok=True)

REPO_DIR = os.environ.get("REPO_DIR", os.path.join(os.path.dirname(__file__), ".."))
REPO_BRANCH = os.environ.get("REPO_BRANCH", "xmi-refresh")

TRANSLATIONS_REPO = os.environ.get("TRANSLATIONS_REPO_DIR", "/app/translations") # git root of translations repo
TRANSLATIONS_BRANCH = os.environ.get("TRANSLATIONS_BRANCH", "translations")

os.environ.setdefault("TRANSLATIONS_SRC_DIR", os.environ.get("TRANSLATIONS_SRC_DIR", os.path.join(TRANSLATIONS_REPO, "translations")))
os.environ.setdefault("TRANSLATIONS_BUILD_DIR",os.environ.get("TRANSLATIONS_BUILD_DIR", "/data/translations-build"))

JOBS = int(os.environ.get("TRANSLATE_JOBS", os.cpu_count() or 1))
POOL = os.environ.get("TRANSLATE_POOL", "process")

import translate 

def head(repo):
    try:
        return subprocess.check_output(["git", "-C", repo, "rev-parse", "HEAD"]).strip()
    except subprocess.CalledProcessError:
        return b""
    
def update_repo(repo, branch):
    before = head(repo)
    subprocess.check_call(["git", "-C", repo, "fetch", "origin"])
    subprocess.check_call(["git", "-C", repo, "reset", "--hard", f"origin/{branch}"])
    after = head(repo)
    return before != after


while True:
    main_changed = update_repo(REPO_DIR, REPO_BRANCH)
    trans_changed = update_repo(TRANSLATIONS_REPO, TRANSLATIONS_BRANCH)
    first_time = not os.listdir(XML_PATH)
    
    if main_changed or first_time:
    
        subprocess.call([sys.executable, "transform_to_xml.py", os.path.join(REPO_DIR, "docs"), XML_PATH])
        subprocess.call(["/solr-8.6.3/bin/solr", "create_core", "-force", "-c", "ifc"])
        subprocess.call(["/solr-8.6.3/bin/post", "-c", "ifc", XML_PATH])
        
        subprocess.call([sys.executable, "to_pset.py", os.path.join(REPO_DIR, "schemas/ifc4x3_add2.uml"), "psd/"])
        subprocess.call("zip ../psd.zip *", cwd="psd", shell=True)
        subprocess.call([sys.executable, "parse_xmi.py", os.path.join(REPO_DIR, "schemas/ifc4x3_add2.uml")])
        subprocess.call([sys.executable, "-m", "generators.express", os.path.join(REPO_DIR, "schemas/ifc4x3_add2.uml"), "-o", "IFC.exp"])
        subprocess.call([sys.executable, "-m", "generators.xsd", "IFC.exp", "IFC.xsd"])
        subprocess.call([sys.executable, "change_log.py", REPO_DIR])
        subprocess.call([sys.executable, "parse_examples.py", REPO_DIR])

        subprocess.call([sys.executable, "templates_to_mvdxml.py", 'IFC4.3.mvdxml', REPO_DIR])
        subprocess.call([sys.executable, "determine_mvd_scope.py", 'IFC.exp', 'IFC4.3.mvdxml'])
        
        subprocess.call([sys.executable, "process_schema.py", os.path.join(REPO_DIR, "schemas/ifc4x3_add2.uml")])
        
        if first_time:
            translate.build_cache(clean=True, jobs=JOBS, pool=POOL)
            # First time. Spider the site to build indices in Redis. Then terminate.
            subprocess.call("wget -q --recursive --spider -S localhost:5000".split(" "))
            requests.post("http://localhost:5000/build_index")
            subprocess.call("redis-cli shutdown".split(" "))
        else: # main changed
            translate.build_cache(jobs=JOBS, pool=POOL)
    
    if trans_changed:
        translate.build_cache(jobs=JOBS, pool=POOL)
         
    time.sleep(60)
