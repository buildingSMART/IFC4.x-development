import os
import sys
import html
import subprocess

import operator
import platform
import functools

import concurrent.futures

from collections import defaultdict, namedtuple
from shutil import copyfile

import xmi
from xmi_document import xmi_document
import express
import json

from hilbertcurve.hilbertcurve import HilbertCurve as HC

try:
    xmi_fn = sys.argv[1]
except:
    print("Usage: python process_schema.py <schema.xmi>", file=sys.stderr)
    exit(1)
    
# https://stackoverflow.com/questions/16259923/how-can-i-escape-latex-special-characters-inside-django-templates
def tex_escape(text):
    import re
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(key) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

# Property is built within Association or within Class
# One property node doesn't represent a characteristics in itself
class Property(object):
    def __init__(self, xmi_property):

        self.supplies = {'xmi:id': None, 'relationtype': None, 'ifcname': None}
        self.isclient = {'xmi:id': None, 'relationtype': None, 'ifcname': None}

        self.partofassociation = None

        self.xmi_property = xmi_property
        attributes = xmi_property.attributes()
        self.xmi_id = attributes['xmi:id']
        self.xmi_type = attributes['xmi:type']
        if 'name' in attributes.keys():
            self.name = attributes['name']
        else:
            self.name = None

        # Find type
        self.types = xmi_property / "type"

        if len(self.types) == 1:
            self.type_ref = self.types[0]
        else:
            self.type_ref = None

        # Register boundaries
        self.boundaries = {}
        uv = self.xmi_property / "upperValue"
        lv = self.xmi_property / "lowerValue"
        if lv == 1:
            lv_attr = lv.attributes()
            self.boundaries['lv'] = lv_attr['value']

        if uv == 1:
            uv_attr = uv.attributes()
            self.boundaries['uv'] = uv_attr['value']


class Type(object):
    def __init__(self, xmi_type):
        self.substitution_rel = {'clientof': [], 'supplierof': []}
        self.realization_rel = {'clientof': [], 'supplierof': []}
        self.dependency_rel = {'clientof': [], 'supplierof': []}
        self.assoc_rel = {'clientof': [], 'supplierof': []}
        
        self.xmi_type = xmi_type
        attributes = xmi_type.attributes()
        self.xmi_id = attributes['xmi:id']
        self.name = attributes['name']

        # Handle UML Constraints
        self.rules = (self.xmi_type / "ownedRule")
        if len(self.rules):
            self.constraints = set(Constraint(i) for i in self.rules)
        else:
            self.constraints = None


# Constraint is built within a Class or a DataType
class Constraint(object):
    def __init__(self, xmi_constraint):
        self.xmi_constraint = xmi_constraint
        attributes = xmi_constraint.attributes()
        self.xmi_id = attributes['xmi:id']
        self.xmi_type = attributes['xmi:type']
        self.name = attributes['name']
        specifications = (self.xmi_constraint/"specification")
        if len(specifications):
            spec_attr = specifications[0].attributes()
            self.content = spec_attr['body']
        else:
            self.content = None


class EnumerationValue(object):
    def __init__(self, xmi_enumeration_value):
        self.xmi_enumeration_value = xmi_enumeration_value


# Relation covers Substitution, Realization, and Dependency
class Relation(object):
    def __init__(self, xmi_relation):
        self.xmi_substitution = xmi_relation
        attributes = xmi_relation.attributes()
        self.xmi_type = attributes['xmi:type']
        self.xmi_id = attributes['xmi:id']
        if xmi_relation.type == 'uml:Association':
            try:
                self.supplier, self.client = map(lambda n:(n|"type").idref, xmi_relation/"ownedEnd")
                self.supplier_name, self.client_name = [n.name for n in (xmi_relation/"ownedEnd")]
                self.supplier_end_id, self.client_end_id = [n.id for n in (xmi_relation/"ownedEnd")]
                self.valid = True
            except Exception as e:
                print(e)
                self.valid = False
        else:
            self.client = attributes['client']
            self.supplier = attributes['supplier']
            self.valid = True
            self.supplier_name, self.client_name = None, None
            self.supplier_end_id, self.client_end_id = None, None


# Generalization 
class Generalization(object):
    def __init__(self, general, specific):
        self.general = general
        self.specific = specific


class Association(object):
    def __init__(self, xmi_association):
        self.xmi_association = xmi_association
        attributes = self.xmi_association.attributes()
        ownedend = self.xmi_association / "ownedEnd"


class UMLclass_Ifc_Entity(object):
    def __init__(self, xmi_class):
            
        self.substitution_rel = {'clientof': [], 'supplierof': []}
        self.realization_rel = {'clientof': [], 'supplierof': []}
        self.dependency_rel = {'clientof': [], 'supplierof': []}
        self.assoc_rel = {'clientof': [], 'supplierof': []}

        self.subtypes = []
        self.supertypes = []

        self.xmi_class = xmi_class
        attributes = self.xmi_class.attributes()
        self.xmi_id = attributes['xmi:id']
        self.name = attributes['name']
        self.xmi_type = attributes['xmi:type']

        # Handle UML Constraints
        self.rules = (self.xmi_class / "ownedRule")
        if len(self.rules):
            self.constraints = set(Constraint(i) for i in self.rules)
        else:
            self.constraints = None

        # Handle UML Properties
        self.attributes = (self.xmi_class / "ownedAttribute")

        if len(self.attributes):
            self.properties = list(Property(i) for i in self.attributes)
        else:
            self.properties = None


def process_relations(xmi):
    substitutions = set(Relation(i) for i in xmi.by_tag_and_type["packagedElement"]["uml:Substitution"] if Relation(i).valid)
    realizations = set(Relation(i) for i in xmi.by_tag_and_type["packagedElement"]["uml:Realization"] if Relation(i).valid)
    dependencies = set(Relation(i) for i in xmi.by_tag_and_type["packagedElement"]["uml:Dependency"] if Relation(i).valid)
    associations = set(Relation(i) for i in xmi.by_tag_and_type["packagedElement"]["uml:Association"] if Relation(i).valid)

    return (substitutions, realizations, dependencies, associations)


def process_properties(xmi, relations):
    properties = set(Property(i) for i in xmi.by_tag_and_type["packagedElement"]["uml:Property"])

    return properties


def process_generalizations(xmi, typeobj):
    if typeobj == 'class':
        usetype = 'uml:Class'
    elif typeobj == 'type':
        usetype = 'uml:DataType'

    generalizationlist = []
    for element in xmi.by_tag_and_type['packagedElement'][usetype]:
        elem_attr = element.attributes()

        generalizations = element / "generalization"
        if len(generalizations):
            for g in generalizations:
                gen_attr = g.attributes()
                general_id = gen_attr['general']
                try:
                    general_node = xmi.by_id[general_id]
                except:
                    continue
                general_node_attr = general_node.attributes()

                if 'name' in general_node_attr.keys():
                    general_name = general_node_attr['name']
                else:
                    general_name = None

                general = (general_id, general_name)
                specific_id = elem_attr['xmi:id']
                if 'name' in elem_attr.keys():
                    specific_name = elem_attr['name']
                else:
                    specific_name = None
                specific = (specific_id, specific_name)

                generalizationlist.append(Generalization(general, specific))

    all_generalizations = defaultdict(list)

    for l in generalizationlist:
        all_generalizations[l.general[0]].append(l)

    return all_generalizations


def process_types(xmi):
    types = []
    for element in xmi.by_tag_and_type['packagedElement']['uml:DataType']:
        types.append(Type(element))

    all_types = defaultdict(list)

    for l in types:
        all_types[l.name].append(l)

    return all_types


def process_classes(xmi, relations=None, properties=None, entities_to_retain=None):
    saved_entities = []
    for element in xmi.by_tag_and_type["packagedElement"]["uml:Class"]:
        attributes = element.attributes()
        if 'name' in attributes.keys():
            name = attributes['name']
            if entities_to_retain is None or name in entities_to_retain:
                # From this point, to replace in method definition
                uml_object = UMLclass_Ifc_Entity(element)
                saved_entities.append(uml_object)

    all_entities = defaultdict(list)

    for l in saved_entities:
        all_entities[l.name].append(l)

    return all_entities
    # return (constraints,properties,generalization)


def add_relations(relations, UML_objects, entities_to_retain = None):
    for i in range(4):
        for pr in relations[i]:
        
            # skip dependencies for now
            if pr.xmi_type == "uml:Dependency":
                continue
        
            try:
                supplier = xmi.by_id[pr.supplier]
                client = xmi.by_id[pr.client]
            except Exception as e:
                print(e)
                continue
                
            sup_att = supplier.attributes()
            cli_att = client.attributes()

            sup = sup_att['name']
            cli = cli_att['name']
            
            stype = sup_att['xmi:type']
            ctype = cli_att['xmi:type']

            sid = sup_att['xmi:id']
            cid = cli_att['xmi:id']
            
            suppressed = xmi.tags['ExpressSuppressRel'].get(pr.client_end_id, '').lower() == 'yes'
            fwd_and_inv = [(sup, cli, pr.client_name, sid), (cli, sup, pr.supplier_name, cid)]
            
            # for some reason we don't depend on directed relationships, so we
            # need to figure out the order from the tags.
            if xmi.tags['ExpressInverse'].get(pr.client_end_id) or (pr.supplier_name and not pr.client_name):
                fwd_and_inv = fwd_and_inv[::-1]
            
            if suppressed:
                # for asymmetric inverses, skip over the explicitly duplicated forward attribute
                fwd_and_inv = [(None,)*4] + fwd_and_inv[1:]

            for ii, (end, other, nm, endid) in enumerate(fwd_and_inv):
                kk = ('clientof', 'supplierof')[ii]
                if end in UML_objects.keys():
                    for instance in UML_objects[end]:
                        if endid == instance.xmi_id:
                            if pr.xmi_type == 'uml:Substitution':
                                instance.substitution_rel[kk].append((other, cid, nm))
                            if pr.xmi_type == 'uml:Realization':
                                instance.realization_rel[kk].append((other, cid, nm))
                            if pr.xmi_type == 'uml:Dependency':
                                instance.dependency_rel[kk].append((other, cid, nm))
                            if pr.xmi_type == 'uml:Association':
                                instance.assoc_rel[kk].append((other, cid, nm))


def add_generalizations(UML_generalizations, UML_objects):
    for k, v in UML_generalizations.items():
        for obj in v:

            if obj.general[1] in UML_objects.keys():
                for t in UML_objects[obj.general[1]]:
                    if t.xmi_id == obj.general[0]:
                        t.supertypes.append(obj.specific)

            if obj.specific[1] in UML_objects.keys():
                for t in UML_objects[obj.specific[1]]:
                    if t.xmi_id == obj.specific[0]:
                        t.subtypes.append(obj.general)




def build_uml_schema(xmi, entities_to_retain = None):

    xmi_doc = xmi_document(xmi)
    defs = list(xmi_doc)
    entity_names = [d.name for d in defs if d.type == 'ENTITY'] # ["IfcRoot", "IfcOwnerHistory"] # 
    
    if entities_to_retain:
        entity_names = entities_to_retain
 

    # Process all the UML nodes 
    UMLrelations = process_relations(xmi)
    UMLgeneralizations = process_generalizations(xmi, 'class')

    UMLclasses = process_classes(xmi, entities_to_retain=entity_names)
    UMLtypes = {} # process_types(xmi)

    UMLobjects = {}
    UMLobjects.update(UMLclasses)
    UMLobjects.update(UMLtypes)


    # Assign relations to objects
    add_relations(UMLrelations, UMLobjects, entities_to_retain=entities_to_retain)
    add_generalizations(UMLgeneralizations, UMLobjects)

    # # Print out the results
    # for k, v in UMLobjects.items():
    #     if entities_to_retain is None or k in entities_to_retain:
    #         for val in v:
    #             print(val.name)
    #             print('substitutions ', val.substitution_rel,'\n')
    #             print('realizations ', val.realization_rel,'\n')
    #             print('dependencies ', val.dependency_rel,'\n')
    #             print('associations ', val.assoc_rel,'\n')
    #             print('supertypes', val.supertypes,'\n')
    #             print('subtypes', val.subtypes,'\n')
    #             print('properties',  val.properties)
    #             if val.properties != None:
    #                 for p in val.properties:
    #                     print(p.name)
    #             print('\n')
    #             print('constraints', val.constraints)
    #             if val.constraints != None:
    #                 for c in val.constraints:
    #                     print(c.content)

    return UMLobjects
    
assoc_label_counter = {'value': 0}

class Tex_object(object):

    def __init__(self, texfilename):
        self.data = {}
        self.tex_file = open(texfilename+".tex", "w")
        self.tex_file_name = texfilename 
        self.tex_content = r'''\documentclass{standalone}
\usepackage{tikz-uml}
\begin{document}
\begin{tikzpicture}'''

        self.tex_classes = set()
        self.tex_relationships = []
        self.I = -1

    def make_connection(self,source,target,connection_type="real",stereo="vec",name=""):
        if '_' in source:
            source = source.replace("_",' ')
        if '_' in target:
            target = target.replace('_',' ')

        tex_connection_type = {
            'real': 'umlreal',
            'depend': 'umldep',
            'herit': 'umlinherit',
            'assoc': 'umluniassoc'
        }.get(connection_type)
        
        if tex_connection_type:
            assoc_label_counter['value'] += 1
            v = assoc_label_counter['value']
            self.tex_content += r''' \%s[%s]{%s}{%s}'''%(tex_connection_type, "name=assoc%d"%v, tex_escape(source), tex_escape(target))
            if name:
                self.tex_content += r'''"\node[above] at (assoc%d-1) {%s}"''' % (v, name);
     
    def write_class2(self, hc, xmi, UMLobject, schema, depth=0):
        self.I += 1
        
        # print('DEPTH ',depth,' Class', UMLobject,' Name',UMLobject.name)

        classname = UMLobject.name
        classname = classname.replace("_"," ")
        classtype = UMLobject.xmi_type
        
        # Build Properties and Constraints content

        properties_and_constraints = []

        if classtype == 'uml:Class' and UMLobject.properties != None:
            for p in UMLobject.properties:
                properties_and_constraints.append(p)
        
        # Don't add constraints for now.
        # if classtype == 'uml:Class' and UMLobject.constraints != None:
        #     for c in UMLobject.constraints:
        #         properties_and_constraints.append(c)    
        
        properties_and_constraints = properties_and_constraints[0:5]
        
        attribute_content = ""
        
        for i, prop in enumerate(properties_and_constraints):
            if not prop.name:
                continue
                
            value = prop.name.replace('_',' ')
            
            # add property type
            if prop.type_ref and prop.type_ref.idref and xmi.by_id.get(prop.type_ref.idref) and xmi.by_id.get(prop.type_ref.idref).attributes().get('name'):
                value += " : %s" % xmi.by_id.get(prop.type_ref.idref).attributes().get('name')
                
            attribute_content += tex_escape(value)
            
            if i != len(properties_and_constraints) - 1:
                attribute_content += r'\\'

        # sign = +1 if self.I % 2 else -1
        # offset = self.I // 2
        # xpos, ypos = hc.coordinates_from_distance(hc.max_h // 2 + sign * offset)
        xpos, ypos = hc.coordinates_from_distance(self.I)
        # start at the top
        ypos = hc.max_x - ypos
        xpos *= 8
        ypos *= 3

        if attribute_content != "": # anchor=north
            tex_content = r'''\umlclass[x=%s, y=%s, width=15ex]{%s}{%s}{} '''%(xpos,ypos,tex_escape(classname),attribute_content)
        else:
            tex_content = r'''\umlsimpleclass[x=%s, y=%s]{%s}  '''%(xpos,ypos,tex_escape(classname))


        self.tex_content += tex_content
        self.tex_classes.add(UMLobject.name)

        if depth < 1:
 
            for rel in ['substitution','realization','dependency', 'association']:

                if rel == 'substitution':
                    dict_to_use = UMLobject.substitution_rel
                    reltype = 'depend'
                elif rel == 'realization':
                    dict_to_use = UMLobject.realization_rel
                    reltype = 'real'
                elif rel == 'association':
                    dict_to_use = UMLobject.assoc_rel
                    reltype = 'assoc'
                else:
                    dict_to_use = UMLobject.dependency_rel
                    reltype = 'depend'
                    
                for order, kk in enumerate(['clientof']): # 'supplierof' <- no inverses for now...
                    rels = dict_to_use[kk]
                    for (other_name, other_id, assoc_name) in rels:
                        if other_name in schema.keys():
                            class_to_write = schema[other_name][0]
                            
                            if class_to_write.name not in self.tex_classes:
                                self.write_class2(hc, xmi, class_to_write,schema, depth=depth + 1)

                            if {UMLobject.name, class_to_write.name} not in self.tex_relationships:
                                args = class_to_write.name, classname
                                if not order:
                                    args = args[::-1]
                                self.make_connection(*args, connection_type=reltype, name=assoc_name)
                                self.tex_relationships.append({UMLobject.name,class_to_write.name})

            # Subtypes, Supertypes

            # 'Type' object has no attribute 'subtypes'
            subtypes = getattr(UMLobject, 'subtypes', [])
            for sub in subtypes:
                e = sub[1]
                if e in schema.keys():
                    class_to_write = schema[e][0]
                    if class_to_write.name not in self.tex_classes:
                        #@nb depth is not incremented
                        self.write_class2(hc, xmi, class_to_write,schema, depth=depth)
                    if {UMLobject.name,class_to_write.name} not in self.tex_relationships:
                        self.make_connection(classname,class_to_write.name,connection_type='herit')
                        self.tex_relationships.append({UMLobject.name,class_to_write.name})

            """
            # 'Type' object has no attribute 'supertypes'
            supertypes = getattr(UMLobject, 'supertypes', [])
            for sup in supertypes:
                e = sup[1]
                if e in schema.keys():
                    class_to_write = schema[e][0]
                    if class_to_write.name not in self.tex_classes:
                        #@nb depth *is* incremented
                        self.write_class2(hc, xmi, class_to_write,schema, depth=depth+1)
                    if {UMLobject.name,class_to_write.name} not in self.tex_relationships:
                        self.make_connection(class_to_write.name,classname,connection_type='herit')
                        self.tex_relationships.append({UMLobject.name,class_to_write.name})
            """

    def generate_tex(self):
        self.tex_content += r'''\end{tikzpicture} 
\end{document}'''
                                
        self.tex_file.write(self.tex_content)
        self.tex_file.close()
        
    def generate_pdf(self):
        subprocess.check_call(['pdflatex', "-interaction=batchmode", os.path.basename(self.tex_file_name+'.tex')], cwd=os.path.dirname(self.tex_file_name), stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':

    xmi = xmi.doc(xmi_fn)
    entities_to_retain = None # {{'IfcBuilding', 'IfcPostalAddress', 'IfcFacility', 'IfcSpatialStructureElement', 'IfcSpatialElement', 'IfcRelContainedInSpatialStructure'} # , 'IfcSlab', 'IfcDoor', 'IfcWindow', 'IfcRail', 'IfcRoad', 'IfcBridge',
                              #  'IfcWallTypeEnum', 'Pset_WallCommon','Pset_WindowCommon','Qto_WindowBaseQuantities', 
                              #  'IfcBuildingElement','IfcELement','IfcWindowStandardCase','RACK-RAIL','GUARD-RAIL','RAIL','STOCK-RAIL','CHECK-RAIL'}


    # Parse XMI file
    UMLobjects = build_uml_schema(xmi, entities_to_retain)

    tex_dir = os.path.join(os.path.dirname(xmi_fn), "..", "output", os.path.basename(xmi_fn))
    if not os.path.exists(tex_dir): os.makedirs(tex_dir)
    if not os.path.exists(os.path.join(tex_dir, "tikz-uml.sty")): copyfile(os.path.join(os.path.dirname(__file__), "tikz-uml.sty"), os.path.join(tex_dir, "tikz-uml.sty"))
    
    html = open(os.path.join(tex_dir, "index.html"), "w")
    html.write("""<html>
<head>
<script>
function filterimages(evt) {
    let t = evt.target.value.toLowerCase();
    let imgs = Array.from(document.querySelectorAll('img'));
    for (let im of imgs) {
        im.parentNode.style.display = t.length >= 3 && im.getAttribute('src').toLowerCase().indexOf(t) !== -1 ? 'block' : 'none';
    }
}
</script>
<style>
* {
    font-family: times;
    font-weight: normal;
}
input {
    padding: 4px;
    margin: 0 0 10px 0;
    display: block;
    border-radius: 3px;
    border: solid 1px gray;
    width: 100%;    
}
img {
    display: block;
}
</style>
</head>
<body>
<h1>IFC UML Image Listing</h1>
<input type='text' oninput="filterimages(event)" placeholder="filter">
""")
    
    def preproc():
        for entity_to_write in UMLobjects.keys():
            if "." in entity_to_write:
                # Fully qualified enum names are also represented as classes in latest XMI version
                continue
                
            # try:
            #     c = UMLobjects[entity_to_write][0].xmi_class
            #     stereotype = (c/"properties")[0].stereotype
            #     if stereotype is not None: 
            #         stereotype = stereotype.lower()
            #     if stereotype is not None and (stereotype.startswith("pset") or stereotype == "$"):
            #         continue
            # except:
            #     pass
            
            
            if any(entity_to_write.lower().startswith(x) for x in ("qto", "pset", "penum", "p_", "q_")):
                continue
                
            UMLobjects[entity_to_write][0].xmi_class
                
            # try:
            tex_fn = os.path.join(tex_dir, entity_to_write)
            print(tex_fn)
            UMLobject = UMLobjects[entity_to_write][0]

            for i in range(4,10):
                # keep trying until hc is large enough
                # to accommodate all elements
                try:
                    hc = HC(i, 2)
                    tex_object = Tex_object(tex_fn)
                    tex_object.write_class2(hc, xmi, UMLobject, UMLobjects)
                    break
                except ValueError as e:
                    continue

            tex_object.generate_tex()
            html.write("<div style='display:none'><img src='%s.png'></div>\n" % entity_to_write)
            yield tex_object
            # except Exception as e:
            #     print(e)
                
                
    texs = list(preproc())
    html.write("</body></html>\n")
    
    # for t in texs:
    #     t.generate_pdf()
    
    full_build = os.environ.get('ISO', '0') == '1' or os.environ.get('PACKAGE', '0') == '1'
    if not full_build:
        # speed up the processing a bit during development
        texs = texs[::32]
    
    completed = 0
    num = len(texs)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        fts = {executor.submit(Tex_object.generate_pdf, t): t for t in texs}
        for future in concurrent.futures.as_completed(fts):
            completed += 1
            print(completed * 100 // num, '%')
            
    subprocess.call(["mogrify", "-format", "png", "-density", "150", "*.pdf"], cwd=tex_dir)
