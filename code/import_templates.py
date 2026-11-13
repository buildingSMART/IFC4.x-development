# imports the markdown definitions for sections from the bSI/IFC repository

import os
import re
import sys
import glob
import json
import itertools

from collections import defaultdict
from dataclasses import dataclass
from xml.etree import ElementTree as ET

from generators.util import xml_dict

entity_attributes = json.load(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "entity_attributes.json"
)))

entity_supertype = json.load(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "entity_supertype.json"
)))

@dataclass(frozen=True,eq=True)
class constraint:
    value : str


class references_by_name_context:
    items = defaultdict(list)
    def clear(self):
        self.items = defaultdict(list)
   
references_by_name = references_by_name_context()
   
@dataclass(frozen=True,eq=True)
class node_reference:
    id : int
    name : str
    
    def __post_init__(self):
        references_by_name.items[self.name.split(":")[0]].append(self)
    
    def __repr__(self):
        refs = [x.id for x in references_by_name.items.get(self.name.split(":")[0]) if ":" not in x.name]
        if len(set(refs)) > 1:
            parts = self.name.split(":")
            parts[0] += f"_{refs.index(self.id)}"
            return ":".join(parts)
        else:
            return self.name
    

def get_attribute(x):
    e, a = x.split(":")
    df = entity_attributes.get(x.replace(":", "."))
    if df:
        return df    
    elif entity_supertype.get(e):
        return get_attribute(entity_supertype[e] + ":" + a)
        
    
def reverse_attr(v):
    try:
        is_fwd, df = get_attribute(v)
    except:
        return ""
    if is_fwd == "forward":
        return ""
    else:
        return ":" + df.split(" FOR ")[-1]
IGNORED_TAGS = IGNORED_ATTRS = set()

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "templates")

Documentation = "Documentation.md"
DocTemplateDefinition = "DocTemplateDefinition.xml"

def join_with(s):
    return lambda *p: os.path.join(*p, s)
    
make_md = join_with(Documentation)
make_xml = join_with(DocTemplateDefinition)

base = os.path.join(dr, "IFC4x3", "Templates")

templates = sorted(set(map(os.path.dirname, 
    glob.glob(make_md(base, "**"), recursive=True) + \
    glob.glob(make_xml(base, "**"), recursive=True)
)))

tmpl_to_name = {}

for tmpl in templates:
    xml = make_xml(tmpl)
    if os.path.exists(xml):
        doc = xml_dict.read(xml)
        if "Name" in doc.attributes and "id" in doc.attributes:
            tmpl_to_name[doc.attributes["id"]] = doc.attributes["Name"]


class unique_list(list):
    """
    Quick and dirty alternative to set to maintain insertion order.
    """
    
    def append(self, item):
        if item not in self:
            list.append(self, item)


for tmpl in templates:

    references_by_name.clear()

    parts = tmpl[len(base)+1:].split(os.sep)
    of = os.path.join(odr, *parts, "README.md")
    try:
        os.makedirs(os.path.dirname(of))
    except:
        pass
        
    md = make_md(tmpl)
    xml = make_xml(tmpl)
    
    if os.path.exists(md):
        contents = open(md, encoding='utf-8-sig').read().strip()
    else:
        contents = ""

    with open(of, "w", encoding="utf-8") as f:
    
        print(parts[-1], file=f)
        print("=" * len(parts[-1]), file=f)
        print(file=f)
        print(contents, file=f)
        
        parent_child = defaultdict(unique_list)
        
        ids = {}
        
        def traverse(n):
            yield n
            for c in n.children:
                yield from traverse(c)
        
        def parse_template(fn):
            doc = xml_dict.read(xml)
            rules = doc.child_with_tag('Rules')
            if rules:
                root = doc.attributes.get("Type")
                for c in rules.children:
                    visit(node_reference(id(doc), root), c)
            
        def visit(parent, r):
            if r.tag == "Value" or r.tag == "DocModelRuleConstraint":
                assert r.child_with_tag("Expression").attributes.get("Operation") == "compareequal"
                val = r.child_with_tag("Expression").child_with_tag("Value").attributes["Literal"]
                parent_child[parent].append(constraint(val))
                return
                
            if r.tag == "DocTemplateDefinition":
                parent_child[parent].append(r.attributes["href"])
                return
                
            if r.attributes.get("href"):
                current_path = xml
                while True:
                    pdoc = xml_dict.read(current_path)
                    nodes = [x for x in traverse(pdoc) if x.attributes.get("id") == r.attributes.get("href")]
                    if nodes:
                        r = nodes[0]
                        break                
                    current_path = os.path.join(os.path.dirname(os.path.dirname(current_path)), 'DocTemplateDefinition.xml')
                
            name = node_reference(id(r), r.attributes["Name"])
            if r.tag == "DocModelRuleAttribute":
                name = node_reference(parent.id, parent.name + ":" + name.name)
            
            parent_child[parent].append(name)
            
            if r.attributes.get("Identification"):
                ids[name] = r.attributes.get("Identification")
                
            for x in r.children:
                for c in x.children:
                    visit(name, c)                    
                    
        parse_template(xml)
        
        if not parent_child:
            continue
    
        print(file=f)
        print("```", file=f)
        print("concept {", file=f)
        
        constraint_counter = 0

        for k, vs in list(parent_child.items()):
            if ':' not in k.name:
                for v in vs:
                    if isinstance(v, constraint):
                        print(f"    {k} -> constraint_{constraint_counter}", file=f)
                        print(f"    constraint_{constraint_counter}[label=\"={v.value}\"]", file=f)
                        constraint_counter += 1
                    elif isinstance(v, str) and "_" in v:
                        print("   ", k, "->", tmpl_to_name[v].replace(" ", "_"), file=f)
                    else:
                        for v2 in parent_child[v]:
                            print(f"    {v} -> {v2}{reverse_attr(v.name)}", file=f)
                        
        for k, v in ids.items():
            print(f"    {k}[binding=\"{v}\"]", file=f)
                            
        print("}", file=f)
        print("```", file=f)
        