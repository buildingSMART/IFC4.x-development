import os
import re
import glob
import platform
import tempfile
import operator
import itertools
import subprocess

from md import parse_document

import rdflib

import xmi

from rdflib import Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.collection import Collection

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

SHACL = Namespace("http://www.w3.org/ns/shacl#")

SCHEMA_FILE = os.path.join(tempfile.gettempdir(), "schema.ttl")
INFERRED_SCHEMA_FILE = os.path.join(tempfile.gettempdir(), "schema-inferred.ttl")
SHAPES_FILE = relative_path("shapes.ttl")
MAX_INFERENCE_ITERATIONS = 20

def process_document(g, fn, subj, cls):
    g.add((subj, RDF.type, cls))
        
    fn_parts = list(map(rdflib.Literal, fn.replace("\\", "/")[len(base_path)+1:].split("/")))[::-1]
    c = Collection(g, fqdn(f"doc_{i}_filename"), fn_parts)
    g.add((subj, fqdn("hasFilename"), c.uri))
    
    def write(s, ct):
        heading = ct.heading.strip()
        
        m = re.search(r"\[([\w\- ]+)\]", heading)
        if m:
            mvd = m.group(1)
            g.add((s, fqdn("hasContext"), rdflib.Literal(mvd)))
            li = [c for c in heading]
            li[slice(*m.span())] = []
            heading = (mvd, "".join(li).strip())
    
        g.add((s, fqdn("hasCleanHeading"), rdflib.Literal(heading)))
        g.add((s, fqdn("hasHeading"), rdflib.Literal(ct.heading)))
        if ct.content.strip():
            g.add((s, fqdn("hasText"), rdflib.Literal(ct.content)))
        
        for i, ch in enumerate(ct.children):
            s2 = s + f"_{i}"
            g.add((s2, fqdn("containedIn"), s))
            write(s2, ch)
        
    contents = parse_document(fn=fn)
    if contents:
        write(subj, contents)
    

if not os.path.exists(SCHEMA_FILE):

    d = xmi.doc(relative_path("../schemas/ifc4x3_add2.uml"))
    
    id_to_node = {}
    g = rdflib.Graph()

    def fqdn(s):
        if s.startswith("{"):
            return rdflib.URIRef("/".join(s[1:].split("}")))
        else:
            return rdflib.URIRef(f"http://example.org/ifc43Shapes/{s}")
        
    all_ids = set(filter(None, (nd.attributes().get('xmi:id') for nd in d.traverse())))
    
    for nd in d.traverse():
        nd_id = nd.attributes().get('xmi:id')
        if nd_id is None:
            continue
        s = fqdn(nd_id)
        g.add((s, RDF.type, fqdn(nd.xml.tagName)))
        if xmi_type := nd.attributes().get('xmi:type'):
            g.add((s, RDF.type, fqdn(xmi_type.removeprefix('uml:'))))

        for ch in nd.child_with_tag('generalization'):
            gen = ch.attributes().get('general')
            if gen is None:
                gen = next(ch.child_with_tag('general')).attributes()['href'].split('#')[-1]
            g.add((s, RDFS.subClassOf, fqdn(gen)))
                    
        for k, v in nd.attributes().items():
            if v in all_ids:
                g.add((s, fqdn(k), fqdn(v)))
            elif v and v.split() and all(x in all_ids for x in v.split()):
                for x in v.split():
                    g.add((s, fqdn(k), fqdn(x)))
            else:
                g.add((s, fqdn(k), rdflib.Literal(v)))

        for ch in nd.children:
            if href := ch.attributes().get('href'):
                g.add((s, fqdn(ch.xml.tagName), fqdn(href.split('#')[-1])))

        if nd.xml.tagName == "ownedComment":
            g.add((s, fqdn('body'), rdflib.Literal(next(iter(nd.children)).text)))

        if nd.parent:
            if pid := nd.parent.attributes().get('xmi:id'):
                g.add((s, fqdn("containedIn"), fqdn(pid)))
    
    base_path = relative_path("..")
    
    for i,fn in enumerate(glob.glob(os.path.join(base_path, "docs/properties/**/*.md"), recursive=True)):
        process_document(g, fn, fqdn(f"doc_{i}"), fqdn("MarkdownPropertyDefinition"))

    for i,fn in enumerate(glob.glob(os.path.join(base_path, "docs/schemas/**/*.md"), recursive=True), start=i):
        process_document(g, fn, fqdn(f"doc_{i}"), fqdn("MarkdownResourceDefinition"))

    g.serialize(SCHEMA_FILE, format="turtle", encoding="utf-8")

VALIDATE_PATH = "shaclvalidate.sh"
INFER_PATH = "shaclinfer.sh"
if platform.system() == 'Windows':
    default_shacl_path = r"C:\Apps\shacl-1.5.0"
    if not os.path.exists(default_shacl_path):
        default_shacl_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'shacl-1.5.0')

    SHACL_PATH = os.environ.get("SHACL_HOME", default_shacl_path)
    VALIDATE_PATH = os.path.join(SHACL_PATH, 'bin', 'shaclvalidate.bat')
    INFER_PATH = os.path.join(SHACL_PATH, 'bin', 'shaclinfer.bat')
    
    if not os.path.exists(VALIDATE_PATH) or not os.path.exists(INFER_PATH):
        raise RuntimeError(
            "Unable to find shaclvalidate and shaclinfer \n"
            "Download shacl from https://repo1.maven.org/maven2/org/topbraid/shacl/1.5.0/shacl-1.5.0-bin.zip\n"
            "Extract it to C:\\Apps\\shacl-1.5.0 or set SHACL_HOME."
        )
        
    os.environ['SHACL_HOME'] = SHACL_PATH

def run_shacl_tool(args, allow_nonzero=False):
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode and not allow_nonzero:
        raise RuntimeError(
            f"{os.path.basename(args[0])} failed with exit code {proc.returncode}\n"
            + stderr.decode("utf-8", errors="replace")
            + stdout.decode("utf-8", errors="replace")
        )
    return stdout

def parse_turtle(data):
    g = rdflib.Graph()
    if data.strip():
        g.parse(data=data.decode("utf-8"), format="ttl")
    return g

def add_new_triples(target_graph, inferred_graph):
    new_count = 0
    for triple in inferred_graph:
        if triple not in target_graph:
            target_graph.add(triple)
            new_count += 1
    return new_count

def infer_to_fixpoint():
    data_graph = rdflib.Graph()
    data_graph.parse(SCHEMA_FILE, format="ttl")

    for iteration in range(1, MAX_INFERENCE_ITERATIONS + 1):
        data_graph.serialize(INFERRED_SCHEMA_FILE, format="turtle", encoding="utf-8")
        inferred_stdout = run_shacl_tool([INFER_PATH, "-datafile", INFERRED_SCHEMA_FILE, "-shapesfile", SHAPES_FILE])
        new_count = add_new_triples(data_graph, parse_turtle(inferred_stdout))
        if new_count == 0:
            data_graph.serialize(INFERRED_SCHEMA_FILE, format="turtle", encoding="utf-8")
            return iteration

    raise RuntimeError(f"SHACL inference did not converge after {MAX_INFERENCE_ITERATIONS} iterations")

infer_to_fixpoint()

stdout = run_shacl_tool(
    [VALIDATE_PATH, "-datafile", INFERRED_SCHEMA_FILE, "-shapesfile", SHAPES_FILE],
    allow_nonzero=True)
stdout = stdout.decode("utf-8")

g = rdflib.Graph()
g.parse(data=stdout, format="ttl")

results = []

with open(relative_path('../output/shacl-result.md'), "w") as f:

    for s,_,__ in g.triples((None, RDF.type, SHACL.ValidationResult)):
        for _,__, rM in g.triples((s, SHACL.resultMessage, None)):
            for _,__,sS in g.triples((s, SHACL.sourceShape, None)):
                results.append((sS, rM))
                
    for k, vs in itertools.groupby(sorted(results), key=operator.itemgetter(0)):
        f.write(f"## {k.split('/')[-1]}\n\n")
        for _, v in vs:
            f.write(f"* {v}\n")
        f.write("\n")
