import os
import re
import sys
import glob
import json
import uuid
import datetime
import operator
import traceback

from collections import defaultdict
from xml.etree import ElementTree as ET

import bs4
import markdown
import networkx
import xmlschema

import md
from xmi_document import SCHEMA_NAME

def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features='lxml')

schema_name = SCHEMA_NAME.split('_')[0]
try:
    schema_name_postfix = SCHEMA_NAME.split('_')[1]
except:
    schema_name_postfix = ''

try:
    REPO_DIR = sys.argv[2]
except:
    REPO_DIR = os.path.join(os.path.dirname(__file__), "..")

mvd_s = xmlschema.XMLSchema(os.path.join(os.path.dirname(__file__), 'mvdXML_V1.1_add1.xsd'))

def generate_uuid(content):
    assert content
    return str(uuid.uuid5(uuid.UUID(int=0), content))
    
def read_scope():
    soup = BeautifulSoup(markdown.markdown(open(os.path.join(REPO_DIR, "content/scope.md"), encoding='utf-8').read()))
    nodes = (n for n in soup.h2.nextSiblingGenerator())
    return "\n".join(map(str, nodes)).strip()

structure_path = os.path.join(REPO_DIR, "output", "structure.json")
if not os.path.exists(structure_path):
    raise FileNotFoundError(f"Required schema structure not found: {structure_path}")
entity_supertype = json.load(open(structure_path, encoding="utf-8"))["entity_supertype"]

def yield_supertypes(x):
    yield x
    s = entity_supertype.get(x)
    if s:
        yield from yield_supertypes(s)

templates_by_name = {}
concept_mapping = {}
root_level_concepts = {}
unapplicable_concepts = []

fns = glob.glob(os.path.join(REPO_DIR, "docs/templates/**/README.md"), recursive=True)
for fn in sorted(fns, key=len):
    path = os.path.normpath(fn).split(os.sep)[:-1]
    
    parent = path[-2]
    name = path[-1]
    
    if parent == 'docs':
        continue
        
    concept_uuid = generate_uuid('/'.join(path[path.index('templates')+1:]))
    
    # assert no duplicate template names
    assert name.replace(' ', '') not in templates_by_name
    
    templates_by_name[name.replace(' ', '')] = (concept_uuid, name)
    

for fn in sorted(fns, key=len):
    path = os.path.normpath(fn).split(os.sep)[:-1]
    
    parent = path[-2]
    name = path[-1]
    
    if parent == 'docs':
        continue
        
    concept_uuid = templates_by_name[name.replace(' ', '')][0]
        
    txt = open(fn, encoding='utf-8').read()
    soup = BeautifulSoup(markdown.markdown(txt))
    
    try:
        soup.h1.decompose()
    except:
        # print(fn)
        # traceback.print_exc()
        pass
        
    try:
        soup.code.decompose()
    except:
        # print(fn)
        # traceback.print_exc()
        pass
        
    if soup.text.strip():
        definition = soup.body.encode_contents().decode('utf-8').strip()
    else:
        definition = ''
    
    concept_blocks = re.findall(r"concept\s*\{.+?\}", txt, flags=re.S)
    rules = None
    root = None
    
    if concept_blocks:
        block = concept_blocks[0]

        edges = re.findall(r"([\:\w]+)\s*\->\s*([\-\:\w]+)", block)
        rule_bindings = dict(re.findall(r'(\w+:\w+)\[binding="(.+?)"\]', block))
        constraint_expressions = dict(re.findall(r'(constraint_[\d+])\[label="=(.+?)"\]', block))
                
        rules = {}
        G = networkx.DiGraph()

        for a,b in edges:
            rb = rule_bindings.get(a)
            attr = a.split(':')[1] if ':' in a else None
            a,b = map(lambda x: x.split(':')[0], (a,b))
            if attr:
                G.add_edge(a, f'{attr}_{a}')
                G.add_edge(f'{attr}_{a}', b)
                G.nodes[f'{attr}_{a}']['type'] = 'AttributeRule'
                G.nodes[f'{attr}_{a}']['binding'] = rb
            else:
                G.add_edge(a, b)
                if not b.startswith("Ifc"):
                    if b.startswith("constraint"):
                        G.nodes[b]['type'] = 'Constraint'
                    else:
                        G.nodes[b]['type'] = 'Reference'

        if len(G):
            root = min(G.in_degree(), key=operator.itemgetter(1))[0]

            Gadj = networkx.to_dict_of_lists(G)

            def build(x, at=rules, otherat=None):
                ty = G.nodes[x].get('type', 'EntityRule')
                
                if ty in ("Reference", "Constraint"):
                    # breakpoint()
                    
                    try: otherat.pop('EntityRules')
                    except: pass
                    try: otherat.pop('AttributeRules')
                    except: pass
                    
                    if ty == "Reference":
                        v = {'Template': [{'@ref': templates_by_name[x.replace("_", "")][0]}]}
                    else:
                        # get predecessor/predecessor/binding to encode expression
                        variable = G.nodes[list(G.predecessors(list(G.predecessors(x))[0]))[0]]['binding']
                        if variable is None:
                            # @todo in case of no binding / ruleid what's the lhs of a constraint?
                            variable = list(G.predecessors(list(G.predecessors(x))[0]))[0].split('_')[0]
                        v = {'Constraint': [{'@Expression': f"{variable}[Value] = {constraint_expressions[x]}"}]}
                        
                    if otherat.get(f"{ty}s"):
                        kk, vv = list(v.items())[0]
                        otherat[f"{ty}s"][kk].extend(vv)
                    else:
                        otherat[f"{ty}s"] = v

                    return
                
                ruleid = G.nodes[x].get('binding')
                other_ty = next(iter({'EntityRule', 'AttributeRule'} - {ty}))

                if not ty in at:
                    at[ty] = []
                    
                at[ty].append({
                    '@' + ty.replace('Rule', 'Name'): x.split("_")[0] if "_" in x else x,
                })
                
                if Gadj[x]:
                    # only initiate next level if we have out edges
                    child = {}
                    at[ty][-1][f'{other_ty}s'] = child
                    
                if ruleid:
                    at[ty][-1]['@RuleID'] = ruleid
                    
                for k in Gadj[x]:
                    build(k, child, at[ty][-1])

            build(root)

            try:
                rules = list(rules.values())[0][0]['AttributeRules']
            except KeyError:
                try:
                    rules = {'References': list(rules.values())[0][0]['References']}
                except:
                    rules = []

    di = {
        '@applicableEntity': [root.split("_")[0] if root else None],
        '@applicableSchema': [schema_name],
        '@name': name,
        '@status': 'sample',
        '@uuid': concept_uuid,
        '@isPartial': "Partial Templates" in path or (root is not None and "IfcRoot" not in yield_supertypes(root.split("_")[0])),
        'Definitions': {
            'Definition': {
                'Body': {
                    '$': definition,
                    '@lang': 'en'
                }
            }
        }
    }
    
    if rules:
        di['Rules'] = rules
        
    concept_mapping[name] = di
    
    
    if parent == 'templates':
        root_level_concepts[name] = di
    else:
        sub = concept_mapping[parent]['SubTemplates'] = concept_mapping[parent].get('SubTemplates', {'ConceptTemplate': []}) 
        li = sub['ConceptTemplate']
        li.append(di)
        
    if root is None:
        unapplicable_concepts.append(di)
        
for templ in reversed(unapplicable_concepts):
    if templ.get('SubTemplates'):
        sub_applicabilities = list(filter(None, map(lambda x: x.get('@applicableEntity', [None])[0], templ['SubTemplates']['ConceptTemplate'])))
        if sub_applicabilities:
            sub_appl_supertypes = [list(yield_supertypes(x)) for x in sub_applicabilities]
            sub_appl_supertype_sets = list(map(set, sub_appl_supertypes))
            shared = set.intersection(*sub_appl_supertype_sets)
            if shared:
                most_specific = sorted(shared, key=sub_appl_supertypes[0].index)[0]
                templ['@applicableEntity'] = [most_specific]
                continue
            else:
                print(*sub_applicabilities, "have no shared supertype")
    
    print("Unable to determine applicable entity for template", templ['@name'])
    del templ['@applicableEntity']
        
templates = [a[1] for a in sorted(root_level_concepts.items())]

concept_associations = json.load(open("xmi_concepts.json", encoding='utf-8'))

concepts_per_entity = defaultdict(lambda: defaultdict(list))

for concept, bindings in concept_associations['GeneralUsage'].items():
    for b in bindings:
        concepts_per_entity[b['ApplicableEntity']][concept].append(b)

def write_root(k_v):
    entity, concepts = k_v
    
    mdfn = glob.glob(os.path.join(REPO_DIR, f"docs/**/{entity}.md"), recursive=True)
    assert len(mdfn) == 1
    mdfn = mdfn[0]
    
    mdp = md.markdown_attribute_parser(fn=mdfn, as_text=False, heading_name="Concepts")
    concept_definitions = dict(mdp)
    
    def write_concept(k_v):
        name, bindings = k_v
        
        template_ref, spaced_name = templates_by_name[name]
        
        binding_descriptions = mdp.get_children(spaced_name) or {}
        
        def write_binding(di):
            args = " AND ".join(f"{k}[{'Type' if v.startswith('Ifc') else 'Value'}]='{v}'" for k, v in sorted(di.items()) if k != 'ApplicableEntity')
            desc = None
            if binding_descriptions and di.values():
                desc = max((BeautifulSoup(binding_descriptions.get(v, '')).text.strip() for v in di.values()), key=len)
            if args:
                v = {
                    '@Parameters': args
                }
                if desc:
                    v['@Description'] = desc
                return v
        
        cpt = {
            '@name': spaced_name,
            '@override': False,
            '@status': 'sample',
            '@uuid': generate_uuid(f'General Usage/{entity}/{template_ref}'),
            'Template': {'@ref': template_ref}
        }
        
        binding_dicts = list(filter(None, map(write_binding, bindings)))
        if binding_dicts:
            cpt['TemplateRules'] = {'@operator': 'and', 'TemplateRule': binding_dicts}

        definition = (concept_definitions.get(spaced_name) or '').strip()
            
        if definition:
            definition = definition.replace("../../../../figures/", "http://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/figures/")
            
            cpt['Definitions'] = {'Definition': [{'Body': {
                '$': definition, 
                '@lang': 'en'
            }}]}
            
        key_order = ["Definitions", "Template", "TemplateRules", "@name", "@override", "@status", "@uuid"]
        cpt = dict(sorted(cpt.items(), key=lambda x: key_order.index(x[0])))
            
        return cpt
    
    return {
        '@applicableRootEntity': entity,
        '@name': entity,
        '@status': 'sample',
        '@uuid': generate_uuid(f'General Usage/{entity}'),
        'Concepts': {'Concept': list(map(write_concept, concepts.items())) }
    }

roots = list(map(write_root, sorted(concepts_per_entity.items())))

dict = {
    '@name': '',
    '@status': 'sample',
    '@uuid': generate_uuid(schema_name),
    '@xmlns': 'http://buildingsmart-tech.org/mvd/XML/1.1',
    '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xsi:schemaLocation': 'http://www.buildingsmart-tech.org/mvd/XML/1.1 http://www.buildingsmart-tech.org/mvd/XML/1.1/mvdXML_V1.1_add1.xsd',
    'Templates': {
        'ConceptTemplate': templates
    },
    'Views': {
        'ModelView': [{
            '@applicableSchema': schema_name, 
            '@code': schema_name,
            '@copyright': f'&copy; {datetime.datetime.now().year} buildingSMART International Ltd.',
            '@name': 'General Usage',
            '@owner': 'bSI',
            '@status': 'sample',
            '@uuid': generate_uuid('General Usage'),
            '@version': schema_name_postfix,
            'Definitions': {
                'Definition': [{
                    'Body': {
                        '$': read_scope(),
                        '@lang': 'en'
                    },
                }]
            },
            'Roots': {
                'ConceptRoot': roots
            }
        }]
    }
}

elem, errors = mvd_s.encode(dict, validation='lax')

try:
    output_filename = sys.argv[1]
except:
    output_filename = f'{schema_name}.mvdxml'

ET.register_namespace("", dict['@xmlns'])
ET.ElementTree(elem).write(output_filename, encoding="utf-8", xml_declaration=True)

if errors:
    for e in errors:
        print(e)
    exit(1)