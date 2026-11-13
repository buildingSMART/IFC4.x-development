import os
import re
import sys
import glob
import html
import json
import uuid
import subprocess
import markdownify

import xml.etree.ElementTree as ET
from enum import Enum
from xml.dom import minidom
from collections import defaultdict
from dataclasses import dataclass, field

import ifcopenshell

from generators.util.xmi_document import xmi_document, SCHEMA_NAME
from parse_xmi import hierarchy
from generators.util import md as mdp


property_types = Enum("property_types", "single bounded list enumerated reference table quantity")

@dataclass(frozen=True)
class property_type:
    type : property_types
    primary : str
    secondary : str = None
    
    def to_tuple(self):
        return tuple(filter(None, (f"p_{self.type.name}value", self.primary, self.secondary)))


@dataclass(unsafe_hash=True)
class property_definition:
    name : str = field(hash=True)
    type : property_type = field(hash=True)
    markdown : set = field(hash=True)
    guid : str = field(default=None, compare=False, hash=False)
    nodes : list = field(default=None, compare=False, hash=False)
    
    id = property(lambda self: f"{self.name}_{self.guid.replace('$','')}")
    PrimaryDataType = property()


def get_parent_of_pt(xmi_doc, enum_or_select_type):
    type_id = enum_or_select_type.id or enum_or_select_type.idref
    attrs = [x for x in xmi_doc.xmi.by_tag_and_type["ownedAttribute"]["uml:Property"] if x.name == "PredefinedType" and (x|"type").idref == type_id]
    if attrs:
        return attrs[0].xml.parentNode.getAttribute("name")
    else:
        return get_parent_of_pt(xmi_doc, xmi_doc.xmi.by_id[[x for x in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Substitution"] if x.client == type_id][0].supplier])


def get_section_from_package(package_name):
    for k, v in hierarchy:
        if package_name in dict(v):
            return k
            
    assert False


def conditionally_compress(s):
    if len(s) <= 22:
        return s
    return ifcopenshell.guid.compress(s.replace("-", ""))


def format_href(name, uid):
    return f"{'x' if name[0].isdigit() else ''}{name}_{conditionally_compress(uid)}".replace('$', '')


tokenize = lambda s: tuple(re.findall(r'\w+', str(s).lower()))


def get_types(di, fn):
    keys = ('PropertyType', 'PrimaryDataType', 'SecondaryDataType')
    defaults = ('p_singlevalue', None, None)
    t = tuple(di.get(*kd) for kd in zip(keys, defaults) if di.get(*kd))
    if t[0] == "p_enumeratedvalue":
        return t[0], dict(minidom.parse(fn).getElementsByTagName("Enumeration")[0].attributes)['href'].value
    else:
        return t


def construct_xml(xmi_doc, pset, path, by_id, by_name, pset_id_mapping, all_properties):

    psd = ET.Element('DocPropertySet' if pset.name.startswith("Pset") else 'DocQuantitySet')
    psd.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    psd.set('Name', pset.name)
    uid = pset_id_mapping.get(pset.name)
    if uid is None:
        uid = ifcopenshell.guid.compress(uuid.uuid5(uuid.NAMESPACE_URL, pset.name).hex)
    psd.set('UniqueId', uid)

    atv_values = []
    
    for x in (pset.meta.get("refs") or []):
        # In order to annotate TypeObject+PredefinedTpye a tuple is used
        # carrying the xmi_id of the type object and the predefined type
        # label as a string
        predefined_type_label = None
        if isinstance(x, tuple):
            x, predefined_type_label = x
        if x in by_id:
            x = by_id[x]
            if x.type == "ENTITY" or (x.parent and x.parent.type == "ENUM"):
                nm = x.name
                if x.parent and get_parent_of_pt(xmi_doc, x.parent.node):
                    nm = get_parent_of_pt(xmi_doc, x.parent.node) + "." + nm
                    
                if predefined_type_label:
                    assert "." not in nm
                    nm = ".".join((nm, predefined_type_label))
                    
                nm = nm.replace(".", "/")
                atv_values.append(nm)
        else:
            print("WARNING:", x, "on", pset.name, "not recorded", file=sys.stderr)
    
    psd.set('ApplicableType', ",".join(atv_values))
    
    ttype = ((pset.node/"ownedComment")[0]|"body").text
    
    psd.set('PropertySetType', ttype)
    
    pdefs = ET.SubElement(psd, 'Properties' if pset.stereotype == "PSET" else 'Quantities')
    
    pset_specific_comments = dict(mdp.markdown_attribute_parser(fn=pset.markdown_filename, heading_name="Comments", as_text=False))
    
    orders = [xmi_doc.try_get_order(x) for x in pset.children]
    
    for _, (a_name, a_markdown), (nm, (ty_ty_arg)) in sorted(zip(orders, [(c.name, c.markdown_content) for c in pset.children], pset.definition)):
    
        # augment definition with pset-specific comment
        definition = a_markdown
        psc = pset_specific_comments.get(a_name)
        if psc:
            definition += f"\n\n<!-- comment -->\n\n{markdownify.markdownify(psc)}"
               
        pd = ET.SubElement(pdefs, "DocProperty" if pset.stereotype == "PSET" else 'DocQuantity')
        
        pd.set('xsi:nil', "true")
        
        if pset.stereotype == "PSET":
            ty, ty_args = ty_ty_arg
            
            ty = ty.replace("Property", "").replace("Value", "")
            ty = getattr(property_types, ty.lower())
            
            if ty == property_types.table:
                p_type = property_type(ty, ty_args["Defined"], ty_args["Defining"])
            else:
                p_type = property_type(ty, list(ty_args.values())[0])
            
            all_properties.append(property_definition(
                a_name,
                p_type,
                definition,
                nodes = [pd]
            ))
        else:
            all_properties.append(property_definition(
                a_name,
                property_type(property_types.quantity, ty_ty_arg),
                definition,
                nodes = [pd]
            ))
       
    path = os.path.join(path, "Sections", get_section_from_package(pset.package), "Schemas", pset.package, "PropertySets" if pset.stereotype == "PSET" else "QuantitySets", pset.name)
    
    os.makedirs(path, exist_ok=True)
        
    with open(os.path.join(path, "Documentation.md"), 'w', encoding='utf-8') as f:
        f.write(pset.markdown)
        
    def write_psd():
        with open(os.path.join(path, "DocPropertySet.xml" if pset.stereotype == "PSET" else "DocQuantitySet.xml"), 'w', encoding='utf-8') as f:
            f.write(
                minidom.parseString(ET.tostring(psd))\
                    .toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            )
        
    return write_psd


def do_try(fn):
    try:
        return fn()
    except: pass
        
        
def run(xmi_doc, path, ref_path):
    psets = []
    penums = []
    by_id = {}
    by_name = {}
    
    fns = glob.glob(f"{ref_path}/**/*.xml", recursive=True)
    lines = [list(open(fn, encoding='utf-8'))[1] for fn in fns if "DocPropertySet" in fn or "DocQuantitySet" in fn]
    dicts = [dict(re.findall("(\w+)=\"([^\"]+)\"", x)) for x in lines]
    pset_id_mapping = {d["Name"]:d["UniqueId"] for d in dicts if {"Name", "UniqueId"} <= d.keys()}
    
    doc_prop_fns = fns2 = [fn for fn in fns if "DocProperty.xml" in fn or "DocQuantity.xml" in fn]
    lines = [list(open(fn, encoding='utf-8'))[1] for fn in fns2]
    dicts = [dict(re.findall("(\w+)=\"([^\"]+)\"", x)) for x in lines]
    prop_id_mapping = defaultdict(list)
    for fn, nm, uid in [(fn, d["Name"], d["UniqueId"]) for fn, d in zip(fns2, dicts) if {"Name", "UniqueId"} <= d.keys()]:
        prop_id_mapping[nm].append((os.path.split(fn)[-1].replace("Doc", "").replace(".xml", "").lower(), uid))
        
    fns3 = [fn for fn in fns if "PropertyConstants" in fn]
    doms = list(map(minidom.parse, fns3))
    dicts = [dict(d.childNodes[0].attributes) for d in doms]
    definitions = [do_try(lambda: [c for c in d.childNodes[0].childNodes if hasattr(c, 'tagName') and c.tagName == 'Documentation'][0].childNodes[0].wholeText) or "" for d in doms]
    constant_id_mapping = {(d["Name"].value, *tokenize(dd)):d["UniqueId"].value for d, dd in zip(dicts, definitions)}
    constant_id_to_name_mapping = {format_href(d['Name'].value.replace('.', '').replace(" ", "_"), d["UniqueId"].value): d['Name'].value.replace('.', '') for d in dicts}
    
    fns4 = [fn for fn in fns if "PEnum_" in fn]
    lines = [list(open(fn, encoding='utf-8'))[1] for fn in fns4]
    dicts = [dict(re.findall("(\w+)=\"([^\"]+)\"", x)) for x in lines]
    penum_id_mapping = {d["Name"]:d["UniqueId"] for d in dicts if {"Name", "UniqueId"} <= d.keys()}
    doms = list(map(minidom.parse, fns4))
    
    def get_constant_name(n):
        try:
            return constant_id_to_name_mapping[n.attributes['href'].value]
        except:
            return n.attributes['Name'].value
            
    penum_constants = {d.childNodes[0].attributes['Name'].value: [get_constant_name(n) for n in d.childNodes[0].getElementsByTagName("Constants")[0].getElementsByTagName("DocPropertyConstant")] for d in doms}
    
    
    all_properties = []
    closures = []
    
    for item in xmi_doc:
        if item.type == "PSET":
            psets.append(item)
        elif item.type == "PENUM":
            penums.append(item)
        else:
            by_id[item.id] = item
            by_name[item.name] = item
            for c in item.children:
                by_id[c.id] = c
        
    for item in psets:
        closures.append(construct_xml(xmi_doc, item, path, by_id, by_name, pset_id_mapping, all_properties))

    all_properties_grouped = defaultdict(list)
    for prop in all_properties:
        all_properties_grouped[prop].append(prop)
        
    for k, v in list(all_properties_grouped.items()):
        k.nodes = [x.nodes[0] for x in v]
        
    all_properties = list(all_properties_grouped.keys())
    
    # all_properties = [p for p in all_properties if p.name == "Reference"]
    
    for prop in all_properties:
    
        prop_def = prop.type.to_tuple() + tokenize(prop.markdown)
    
        candidates = prop_id_mapping[prop.name]

        if candidates:
            prop_quant, uids = zip(*candidates)
            uids_compressed = list(map(conditionally_compress, uids))
            candidates_2 = list(zip(prop_quant, uids_compressed))
            directories = [os.path.join(ref_path, f"{ty[0].upper()}{ty[1:].replace('y', 'ie')}s", prop.name[0].lower(), f"{prop.name}_{uid}") for ty, uid in candidates_2]
            assert all(os.path.exists(d) for d in directories)
            markdown_fns = [os.path.join(d, "Documentation.md") for d in directories]
            candidate_markdowns = [open(fn, encoding='utf-8').read() if os.path.exists(fn) else '' for fn in markdown_fns]
            candidate_xml_fns = [os.path.join(d, f"Doc{ty[0].upper()}{ty[1:]}.xml") for (ty, d) in zip(prop_quant, directories)]
            lines = [list(open(fn, encoding='utf-8'))[1] for fn in candidate_xml_fns]
            dicts = [dict(re.findall("(\w+)=\"([^\"]+)\"", x)) for x in lines]
            prop_types = list(map(get_types, dicts, candidate_xml_fns))
            
            matching_definitions = sorted(id for (ty, id), cm, pty in zip(candidates_2, candidate_markdowns, prop_types) if pty + tokenize(cm) == prop_def)
        else:
            matching_definitions = None
        
        if matching_definitions:
            uid = matching_definitions[0]
            print("Used existing definition", prop.name, uid)
        else:
            s = " ".join(prop_def)
            uid = ifcopenshell.guid.compress(uuid.uuid5(uuid.NAMESPACE_URL, s).hex)
            print("Created new definition", prop.name, uid)
            
        for nd in prop.nodes:
            nd.set('href', f"{prop.name}_{uid}".replace('$', ''))
        
        is_quantity = prop.type.type == property_types.quantity
        ty = "Quantity" if is_quantity else "Property"
        
        fn = os.path.join(path, f"{ty[0].upper()}{ty[1:].replace('y', 'ie')}s", prop.name[0].lower(), f"{prop.name}_{uid}")
        os.makedirs(fn, exist_ok=True)
        
        propdef = ET.Element(f"Doc{ty}")
        propdef.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        propdef.set('id', f"{prop.name}_{uid}".replace('$', ''))
        propdef.set('Name', prop.name)
        
        if matching_definitions:
            # Copy over localizations, if any
            orig_path = [fn for fn in doc_prop_fns if matching_definitions[0] in fn][0]
            orig_tree = ET.parse(orig_path)
            orig_loc = orig_tree.find(".//Localization")
            if orig_loc:
                propdef.append(orig_loc)
            
            # See if original source used compressed, and provide accordingly
            is_compressed = len(orig_tree.getroot().attrib.get('UniqueId', '')) == 22
            if not is_compressed:
                uid = ifcopenshell.guid.split(ifcopenshell.guid.expand(uid))[1:-1].lower()
                
        propdef.set('UniqueId', uid)

        if is_quantity:
            propdef.set('QuantityType', prop.type.primary.lower())
        else:
            keys = 'PropertyType', 'PrimaryDataType', 'SecondaryDataType'
            values = prop.type.to_tuple()
            for k, v in zip(keys, values):
                if v == "p_singlevalue":
                    continue
                propdef.set(k, v)
                if v == "p_enumeratedvalue":
                    # not really correct but just to match the source data
                    propdef.set('PrimaryDataType', 'IfcLabel')
                    break
                
            if values[0] == "p_enumeratedvalue":
                enum = ET.SubElement(propdef, "Enumeration")
                enum.set('xsi:type', 'DocPropertyEnumeration')
                enum.set('xsi:nil', 'true')
                enum.set('href', values[1].replace('$', ''))
            
        # Remove existing indentation
        for x in propdef.iter():
            x.text = (x.text or '').strip(); x.tail = (x.tail or '').strip()
            
        with open(os.path.join(fn, f"Doc{ty}.xml"), 'w', encoding='utf-8') as f:
            f.write(
                minidom.parseString(ET.tostring(propdef))\
                    .toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            )
            
        with open(os.path.join(fn, "Documentation.md"), 'w', encoding='utf-8') as f:
            f.write(prop.markdown)

    prop_constants = {}
    for penum in penums:
        for c in penum.children:
            pc = (c.name, *tokenize(c.markdown or ''))
            if pc not in prop_constants:
                prop_constants[pc] = c.markdown
        
    for pc, defn in prop_constants.items():
        uid_hex = constant_id_mapping.get(pc)
        if uid_hex:
            assert "-" in uid_hex
            print("Used existing definition", pc[0], uid_hex)
        else:
            uid_obj = uuid.uuid5(uuid.NAMESPACE_URL, " ".join(pc))
            uid_hex = str(uid_obj)
            constant_id_mapping[pc] = uid_hex
            print("Created new definition", *pc, uid_hex)

        uid_base64 = ifcopenshell.guid.compress(uid_hex.replace("-", ""))
        
        constantdef = ET.Element(f"DocPropertyConstant")
        constantdef.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        constantdef.set('id', format_href(pc[0], uid_base64))
        constantdef.set('Name', pc[0])
        constantdef.set('UniqueId', uid_hex)
        
        if defn:
            ET.SubElement(constantdef, "Documentation").text = defn
            
        fn = os.path.join(path, "PropertyConstants", pc[0][0].lower(), f"{pc[0]}_{uid_base64}.xml")
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(
                minidom.parseString(ET.tostring(constantdef))\
                    .toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            )

    for penum in penums:
        fn = os.path.join(path, "PropertyEnumerations", penum.name[6].lower(), f"{penum.name}.xml")
        
        uid = penum_id_mapping.get(penum.name)
        if uid:
            print("Used existing definition", penum.name, uid)
        else:
            uid = str(uuid.uuid5(uuid.NAMESPACE_URL, penum.name))
            print("Created new definition", penum.name, c.markdown, uid)
        
        penumdef = ET.Element(f"DocPropertyEnumeration")
        penumdef.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        penumdef.set('id', penum.name)
        penumdef.set('Name', penum.name)
        penumdef.set('UniqueId', uid)
        
        if penum.markdown:
            ET.SubElement(penumdef, "Documentation").text = penum.markdown
        
        items = ET.SubElement(penumdef, "Constants")

        # alphabetical sort, but the items below always come last
        undefined = ("OTHER", "NOTKNOWN", "UNSET", "USERDEFINED", "NOTDEFINED")
        penalize_undefined = lambda s: (s in undefined, s)

        existing_constants = list(map(penalize_undefined, penum_constants.get(penum.name, [])))

        def get_key(item):
            k = penalize_undefined(item.name)
            if k in existing_constants:
                return existing_constants.index(k)
                
            new_position = [i for i, v in enumerate(existing_constants) if k < v]
            if new_position:
                p = new_position[0]
            else:
                p = len(existing_constants)
                
            # I don't think updating the list is necessary because sorted() is stable?
            # existing_constants.insert(p, k)
            return p
        
        penum_children = sorted(penum.children, key=get_key)

        for c in penum_children:
            item = ET.SubElement(items, "DocPropertyConstant")
            item.set('xsi:nil', 'true')
            item.set('href', f"{'x' if c.name[0].isdigit() else ''}{c.name}_{conditionally_compress(constant_id_mapping[(c.name, *tokenize(c.markdown or ''))])}".replace('$', ''))
        
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(
                minidom.parseString(ET.tostring(penumdef))\
                    .toprettyxml(indent="\t", encoding='utf-8').decode('utf-8')
            )

    # commit PSDs to disk after populating hrefs
    for fn in closures:
        fn()
    

if __name__ == "__main__":    
    if len(sys.argv) == 4:
        fn, path, ref_path = sys.argv[1:]
        xmi_doc = xmi_document(fn)
        xmi_doc.should_translate_pset_types = False
        run(xmi_doc, path, ref_path)
    else:
        print("Usage: python to_pset.py <schema.xml> <output dir> <ref path>", file=sys.stderr)
        exit(1)
