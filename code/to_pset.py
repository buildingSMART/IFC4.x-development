import os
import re
import sys
import glob
import html
import json
import subprocess
import concurrent.futures

import xml.etree.ElementTree as ET
from xml.dom import minidom
from collections import defaultdict

from xmi_document import xmi_document, SCHEMA_NAME
import md as mdp

GUID_PATTERN = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(r'\s+')
def strip_html(s):
    S = html.unescape(s or '')
    i = S.find('\n')
    return re.sub(HTML_TAG_PATTERN, '', S)
    
    
def strip(s):
    return strip_html(s).replace("bSI Documentation", "").strip().replace("''", "'").encode('ascii', 'xmlcharrefreplace').decode('ascii')
    
    
def format(s):
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip()


def get_parent_of_pt(xmi_doc, enum_or_select_type):
    # @todo move out of function locals
    attrs = sum([[c for a in c/"ownedAttribute" if a.name == "PredefinedType" and a.resolve('type') == enum_or_select_type.id] for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]], [])
    
    # We move the type objects last, because xmi_document would have already augmented the
    # entity associations with a tuple of (typeobjectid, predefined type str), so here
    # we should find the non-type object.
    def is_typeobject_subtype(a):
        return 'IfcTypeObject' in xmi_doc.supertypes(a.id)
    attrs.sort(key=is_typeobject_subtype)

    return attrs[0].name


def build_property_defs(xmi_doc, pset, node, by_name):  
    # property definitions are contained in their own markdown file, but the pset markdown
    # can contain specific comment to augment the definition
    try:
        pset_specific_comments = dict(mdp.markdown_attribute_parser(fn=pset.markdown_filename, heading_name="Comments"))
    except FileNotFoundError as e:
        pset_specific_comments = {}
    
    for (a_name, a_markdown), (nm, (ty_ty_arg)) in zip([(c.name, c.markdown) for c in pset.children], pset.definition):
    
        # augment definition with pset-specific comment
        definition = a_markdown
        psc = pset_specific_comments.get(a_name)
        if psc:
            definition += f"\n\n{psc}"
        
        is_pset = pset.name.startswith('Pset_')
        
        pd = ET.SubElement(node, "PropertyDef" if is_pset else 'QtoDef')
        ET.SubElement(pd, 'Name').text = a_name
        ET.SubElement(pd, 'Definition').text = definition
        pt = ET.SubElement(pd, 'PropertyType' if is_pset else 'QtoType')
        
        if is_pset:
            ty, ty_args = ty_ty_arg
            
            if ty in ("PropertySingleValue", "PropertyBoundedValue", "PropertyListValue"):
            
                ty_arg = next(iter(ty_args.values()))
                            
                tpsv = ET.SubElement(pt, 'Type' + ty)
                
                if ty == "PropertyListValue":
                    # unnecessary intermediate node
                    tpsv = ET.SubElement(tpsv, 'ListValue')
                
                ET.SubElement(tpsv, 'DataType').set('type', ty_arg)
                
            elif ty == "PropertyEnumeratedValue":
                
                ty_arg = next(iter(ty_args.values()))
            
                tpev = ET.SubElement(pt, 'TypePropertyEnumeratedValue')
                el = ET.SubElement(tpev, 'EnumList')
                el.set('name', ty_arg)
                
                enum_type = by_name[ty_arg]
                
                for pv in [c.name for c in enum_type.children]:
                    ET.SubElement(el, 'EnumItem').text = pv
                    
            elif ty == "PropertyComplexProperty":
                
                ty_arg = list(ty_args.values())[0]
                
                tcp = ET.SubElement(pt, 'TypeComplexProperty')
                tcp.set('name', ty_arg)
                
                build_property_defs(xmi_doc, by_name[ty_arg], tcp, by_name)

            elif ty == "PropertyReferenceValue":
                
                ty_arg = list(ty_args.values())[0]
                
                tprv = ET.SubElement(pt, 'TypePropertyReferenceValue')
                tprv.set("reftype", ty_arg)
                
            elif ty == "PropertyTableValue":
                
                tptv = ET.SubElement(pt, 'TypePropertyTableValue')
                
                # what's this?
                ET.SubElement(tptv, 'Expression')
                
                ET.SubElement(ET.SubElement(tptv, 'DefiningValue'), "DataType").set("type", ty_args["Defining"])
                ET.SubElement(ET.SubElement(tptv, 'DefinedValue'), "DataType").set("type", ty_args["Defined"])
            
        else:
            pt.text = f"Q_{ty_ty_arg.removeprefix('IfcQuantity').removeprefix('Ifc').removesuffix('Measure').upper()}"


def construct_xml(xmi_doc, pset, path, by_id, by_name):

    # The XMI data contains IFC base64 guids and rfc encoded hex guids
    
    """
    guid = pset.node.tags().get("IFCDOC_GUID")
    if guid is None:
        print("WARNING: no guid for", pset.name)
        guid = ifcopenshell.guid.expand(ifcopenshell.guid.new())
    elif re.match(GUID_PATTERN, guid.lower()):
        guid = guid.lower().replace("-", "")
    else:
        guid = ifcopenshell.guid.expand(guid)
    """

    psd = ET.Element('PropertySetDef' if pset.name.startswith('Pset_') else 'QtoSetDef')
    psd.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    psd.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
    ttype = ((pset.node/"ownedComment")[0]|"body").text
    psd.set('templatetype', ttype)
    
    if pset.name.startswith('Pset_'):
        psd.set('xsi:noNamespaceSchemaLocation', 'http://buildingSMART-tech.org/xml/psd/PSD_IFC4.xsd')
    else:
        psd.set('xsi:noNamespaceSchemaLocation', 'http://buildingSMART-tech.org/xml/psd/QTO_IFC4.xsd')
    # psd.set('xmlns', 'http://buildingSMART-tech.org/xml/psd/PSD_IFC4.xsd')
    
    ET.SubElement(psd, 'IfcVersion').set('version', SCHEMA_NAME)
    
    ET.SubElement(psd, 'Name').text = pset.name
    
    ET.SubElement(psd, 'Definition').text = pset.markdown
    
    ET.SubElement(psd, 'Applicability')
    
    acs = ET.SubElement(psd, 'ApplicableClasses')
    atv = ET.SubElement(psd, 'ApplicableTypeValue')
    
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
            breakpoint()

    atv_values = sorted(atv_values, key=lambda s: ("/" in s, s))

    for nm in atv_values:
        ET.SubElement(acs, 'ClassName').text = nm
    
    atv.text = ",".join(atv_values)
    
    pdefs = ET.SubElement(psd, 'PropertyDefs' if pset.name.startswith('Pset_') else 'QtoDefs')
    
    build_property_defs(xmi_doc, pset, pdefs, by_name)
    
    with open(os.path.join(path, pset.name + ".xml"), 'w', encoding='utf-8') as f:
        f.write(
            minidom.parseString(ET.tostring(psd))\
                .toprettyxml(indent="  ")
        )
        
def run(xmi_doc, path):
    psets = []
    by_id = {}
    by_name = {}
    
    for item in xmi_doc:
        if item.type == "PSET":
            psets.append(item)
        else:
            by_id[item.id] = item
            by_name[item.name] = item
            for c in item.children:
                by_id[c.id] = c
        
    for item in psets:
        construct_xml(xmi_doc, item, path, by_id, by_name)
            
            
def compare(path1, path2, output):
    with open(output, "w") as f:
        fn1, fn2 = map(lambda fn: list(map(os.path.basename, glob.glob(os.path.join(fn, "*.xml")))), (path1, path2))
        
        print(file=f)
        print("Missing in output", file=f)
        print("=================", file=f)
        for p in set(fn1) - set(fn2):
            print("*", p, file=f)
        
        print(file=f)        
        print("Missing in reference", file=f)
        print("=================", file=f)
        for p in set(fn2) - set(fn1):
            print("*", p, file=f)
            
        def compare_one(p):
            print(p, file=sys.stderr)
            return p, subprocess.check_output([
                sys.executable,
                os.path.join(os.path.dirname(__file__), "generators/util/compare_pset.py"),
                os.path.join(path1, p),
                os.path.join(path2, p)])

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for p, data in executor.map(compare_one, set(fn1) & set(fn2)):
                print(file=f)
                if data:
                    print(p, file=f)
                    print("="*len(p), file=f)
                    print(data.decode('ascii'), file=f, flush=True)
            
            
if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        fn, path = sys.argv[1:]
        run(xmi_document(fn), path)
        
    elif len(sys.argv) == 5 and sys.argv[1] == "--compare":
        path, ref_path, md_out = sys.argv[2:]
        compare(ref_path, path, md_out)
        
    else:
        print("Usage: python to_pset.py <schema.xml> <output dir>", file=sys.stderr)
        print("Usage: python to_pset.py --compare <output dir> <ref dir> <markdown output>", file=sys.stderr)
        exit()
