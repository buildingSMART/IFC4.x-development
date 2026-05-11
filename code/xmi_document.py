REPO_URL = "https://github.com/buildingSMART/IFC4.3.x-development/edit/xmi-refresh/"

import csv
import os
from pathlib import Path
import re
import sys
import html

import operator
import functools
import itertools
import subprocess

from collections import defaultdict, namedtuple, Counter
from typing import Union

import xmi
import express

from md import markdown_attribute_parser

import logging
logging.basicConfig(level=logging.WARNING, stream=sys.stdout)

# @todo schema name is hardcoded and not derived from the XMI package name for now
is_iso = os.environ.get('ISO', '0') == '1'
is_package = os.environ.get('PACKAGE', '0') == '1'

if is_package or is_iso:
    SCHEMA_NAME = "IFC4X3_ADD2"
else:
    SCHEMA_NAME = "IFC4X3_DEV"

    try:
        if os.environ.get("REPO_DIR"):
            repo_dir = "-C", os.environ.get("REPO_DIR")
        else:
            repo_dir = []
        sha = subprocess.check_output(["git", *repo_dir, "rev-parse", "--short", "HEAD"]).decode('ascii').strip()
        SCHEMA_NAME += f"_{sha}"
    except: pass

def unescape(s):
    # @todo this is bizarre encoding, what happened here?
    return html.unescape(html.unescape(s.replace('xx38', '&')))

def float_international(s):
    return float(s.replace(',', '.'))
    
association_data = namedtuple("association_data", ("own_end", "type", "other_end", "asssocation"))

def yield_parents(node):
    yield node
    if node.parentNode:
        yield from yield_parents(node.parentNode)
        
def get_path(xmi_node):
    nodes = list(yield_parents(xmi_node.xml))
    def get_name(n):
        if n.attributes:
            v = n.attributes.get('name')
            if v: return v.value
    node_names = [get_name(n) for n in nodes]
    return node_names[::-1]
    
infinity = 1e9

where_pat = re.compile(r"'\w+\.(\w+(\.\w+)?)'")
def fix_schema_name(s, remove=False):
    def repl(x):
        if remove:
            return x.group(1)
        else:
            return "'%s.%s'" % (SCHEMA_NAME, x.group(1))
    return remove_linebreak_before_semi(re.sub(where_pat, repl, s))
    
def remove_linebreak_before_semi(s):
    lines = s.split('\n')
    if lines[-1] == ';':
        lines[-2] += ';'
        lines[-1:] = []
    return '\n'.join(lines)
    

class missing_markdown:
    def __init__(self, reason): self.reason = reason
    def __bool__(self): return False
    def __repr__(self): return self.reason
    def to_json(self):
        logging.warning(self.reason)
        return ''
        
        
class xmi_item:
    id = None
    type = None
    name = None
    definition = None
    node = None
    children = None
    document = None
    parent = None
    
    def __init__(self, type, name, definition, node, children = None, document = None, parent = None, **kwargs):
        self.type, self.name, self.definition, self.node, self.children = type, name.strip(), definition, node, children or []
        self.children = [xmi_item(None, a, None, b, None, parent=self, document=document) for a, b in self.children]        
        self.meta = kwargs
        self.document = document
        self.parent = parent
        if self.node:
            self.id = self.node.id or self.node.xmi_id
            
    def _mdtype(self):
        if self.type == "PSET" and not self.name.startswith("Pset"):
            return "QuantitySets"
            
        return {
            "PT"    : "Types",
            "PSET"  : "PropertySets",
            "TYPE"  : "Types",
            "PENUM" : "PropertyEnumerations",
            "SELECT": "Selects",
            "ENUM"  : "Types",
            "ENTITY": "Entities",
        }.get(self.parent.type if self.parent else self.type, "Unknown")
        
    def __iter__(self):
        return iter(self.children)
        
    def _get_documentation(self):
        if self.node:
            ds = (self.node/"documentation")
            if len(ds) == 1 and self.node.xml.tagName != 'element':
                return ds[0].value
            else:
                ps = (self.node/"properties")
                if ps:
                    return ps[0].documentation


    def _get_package(self):
        return self.parent.path[-2] if self.is_sub_element(strict=True) else self.path[-2]


    def _get_markdown_filename(self):
        md_root = os.path.join(self.repo_root(), 'docs')
        
        if self.parent and self.parent.type == "PSET" and self.type is None:
            return os.path.join(md_root, 'properties', self.name[0].lower(), self.name + ".md")
        else:
            md_root = os.path.join(md_root, 'schemas')
            for category in os.listdir(md_root):
                for module in os.listdir(os.path.join(md_root, category)):
                    if module == self.package:
                        return os.path.join(md_root, category, module, self.mdtype, (self.parent.name if self.is_sub_element() else self.name) + ".md")

    def repo_root(self):
        fn = self.parent.document.filename if self.is_sub_element(strict=True) else self.document.filename
        return os.path.join(os.path.abspath(os.path.dirname(fn)), '..')

    def is_sub_element(self, strict=False):
        """
        used for:
          determining package (strict=True)
          determining location of markdown (strict=False):
            - true: sub-element, definition is in parent markdown under 2nd level heading
            - false: root-element, definition is under 1st level heading in own markdown document
            
            NB: Note that property definitions are always in their own file            
        """
        is_sub = self.parent is not None
        
        if not strict:
            if self.parent and self.parent.type == "PSET" and self.type is None:
                # properties are not encoded into a definition of their pset
                # but rather are listed separately in a directory 
                is_sub = False
            
        return is_sub


    def _get_markdown(self, definition=False, content=False):
        if self.node:

            
            md_fn = self.markdown_filename
                         
            if md_fn is None:
                return missing_markdown("Unable to locate markdown path")                        
            
            p = os.path.relpath(md_fn, start=self.repo_root()).replace(os.sep, '/')
                                    
            if not os.path.exists(md_fn):
                return missing_markdown(REPO_URL + p + " does not exist")
            
            hname = 'Attributes' if not self.is_sub_element() or self.parent.type == "ENTITY" else 'Items'
            
            if not os.path.exists(md_fn):
                return missing_markdown(REPO_URL + p + " failed to parse")
                
            if content and not self.is_sub_element():
                lines = list(open(md_fn, encoding='utf-8'))
                h0 = [set(ln.strip()) in ({'='}, {'-'}) for ln in lines]
                h1 = [ln.startswith("#") for ln in lines]
                for h in (h0, h1):
                    if any(h):
                        lines = lines[h.index(True) + 1:]
                        break
                empty = [len(ln.strip()) == 0 for ln in lines]
                if any(empty):
                    lines = lines[empty.index(True) + 1:]
                return "\n".join(lines)                    
                
            md_parser = markdown_attribute_parser(fn=md_fn, heading_name=hname, short=definition)
            
            if self.is_sub_element():
                attrs = dict(md_parser)
                if md_parser.status.get("ALL") == "NO_HEADING":
                    return missing_markdown(REPO_URL + p + " has no '%s' heading" % sub_item_heading_name)
                    
                st = md_parser.status.get(self.name)
                if st and st[0] == "NO_CONTENT":
                    return missing_markdown(REPO_URL + p + "#L%d has no content" % st[1])
                elif st is None:
                    return missing_markdown(REPO_URL + p + " has no '%s' heading" % self.name)
                
                return attrs[self.name]
            else:
                d = md_parser.definition(short=definition)
                st = md_parser.status.get("DEFINITION")
                if st and st[0] == "NO_CONTENT":
                    return missing_markdown(REPO_URL + p + " has no content")
                else:
                    return d

                        
    def _get_markdown_definition(self):
        return self._get_markdown(definition=True)
        
    def _get_markdown_definition_html(self):
        # pip install Markdown
        import markdown
        
        md = self._get_markdown(definition=True)
        
        if not md: return md
        
        html = markdown.markdown(
            md,
            extensions=['tables', 'fenced_code']
        )
        
        return html
                        
    def _get_path(self):
        if self.node:
            return get_path(self.document.xmi.by_id[self.id])
        
    documentation = property(_get_documentation)
    markdown = property(_get_markdown)
    markdown_definition = property(_get_markdown_definition)
    markdown_definition_html = property(_get_markdown_definition_html)
    path = property(_get_path)
    package = property(_get_package)
    mdtype = property(_mdtype)
    markdown_filename = property(_get_markdown_filename)
    markdown_content = property(lambda s: s._get_markdown(content=True))
    
class xmi_document:

    def __init__(self, fn : Union[str, xmi.doc]):    
        self.dependencies_in = defaultdict(list)
        self.dependencies_out = defaultdict(list)
        self.associations = defaultdict(list)
        self.generalizations_in = defaultdict(list)
        self.generalizations_out = defaultdict(list)
    
        if isinstance(fn, str):
            self.filename = fn
            self.xmi = xmi.doc(fn)
        else:
            self.filename = fn.filename
            self.xmi = fn
            
        self.extract_associations()
        self.extract_dependencies()
        self.extract_generalizations()

        fp = Path(self.filename).parent / "mvd" / "GeneralUsage" / "ObjectTyping.csv"
        self.concepts = {
            "ObjectTyping": list(csv.DictReader(fp.open(encoding='utf-8', newline='')))
        }
        
        self.should_translate_pset_types = True
        
    def skip_by_package(self, element):
        return "Views" in get_path(self.xmi.by_id[element.id or element.xmi_id])
        
        
    def supertypes(self, eid):
        yield self.xmi.by_id[eid].name
        gs = self.xmi.by_id[eid] / "generalization"
        if gs:
            yield from self.supertypes(gs[0].resolve('general'))

    def extract_dependencies(self):
        for dep in self.xmi.by_tag_and_type["packagedElement"]["uml:Dependency"]:
            self.dependencies_in[dep.resolve('client')].append(dep.resolve('supplier'))
            self.dependencies_out[dep.resolve('supplier')].append(dep.resolve('client'))
            
    def extract_generalizations(self):
        for dep in self.xmi.by_tag["generalization"]:
            specific, general = dep.parent.id, dep.resolve('general')
            self.generalizations_in[general].append(specific)
            self.generalizations_out[specific].append(general)
            
    def extract_associations(self, concepts=False):
        for assoc in self.xmi.by_tag_and_type["packagedElement"]["uml:AssociationClass" if concepts else "uml:Association"]:
            ends = [self.xmi.by_id[s] for s in assoc.memberEnd.split(' ')]
            is_source = [e.xml.tagName == "ownedAttribute" for e in ends]
            end_types = [e.resolve('type') for e in ends]
            end_names = [e.name for e in ends]
            end_type_names = list(map(lambda t: self.xmi.by_id[t].name, end_types))

            if sum(is_source) == 0:
                is_suppressed = [(s[0],s[-1]) == ('(',')') for s in end_names]
                assert sum(is_suppressed) == 1
                is_source = is_suppressed
            assert sum(is_source) == 1
            
            c1, c2 = ends
            t1, t2 = end_types
            tv1, tv2 = end_type_names

            if is_source[0]:
                self.associations[tv1].append(association_data(c2, self.xmi.by_id[t2], c1, assoc))
            else:
                self.associations[tv2].append(association_data(c1, self.xmi.by_id[t1], c2, assoc))

    def __iter__(self):
        """
        A generator that yields tuples of <a, b> with
        a: an element in EXPRESS_ORDER
        b: an type/entity/function definition string
        """

        def format_aggr(ag):
            ag_names = ("ARRAY", "LIST", "SET", "BAG")
            m = re.match('(\w)(U)?\[(\d+):(\d+|\?)\]', ag)
            assert m
            t, u, l, h = m.groups()
            unique = ("UNIQUE",) if u else ()
            t = [an for an in ag_names if an.startswith(t)][0]
            return (t, f"[{l}:{h}]", "OF", *unique)
        
        class_by_name = {c.name: c for c in self.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}

        for c in self.xmi.root.traverse():
            if c.xmi_id is None or c.name is None:
                continue

            if c.xmi_type in ("uml:Package", "uml:EnumerationLiteral", "uml:Generalization", "uml:OpaqueExpression", "uml:Property", "uml:Association", "uml:Dependency"):
                continue

            if c.xml.tagName == 'uml:Model':
                continue

            if c.parent.name == "base":
                continue

            if 'PropertyTableValueBase' in self.supertypes(c.id):
                # these are anonymous pairs for the propertyset TableValue properties
                continue
                
            if c.xmi_type == "uml:Constraint":
                if c.parent.type == "uml:Package":
                    # Only top-level constraints in a package are emitted as items, other constraints
                    # are handled by their owning class or datatype.
                    yield xmi_item(
                        (c|"language").text.split('_')[-1], 
                        c.name, 
                        (c|"body").text.strip(), 
                        c, 
                        document=self
                    )
                
            elif '.' in c.name :
                continue

            elif c.name.startswith("Pset") or c.name.startswith("Qto"):                
                refs = self.dependencies_in.get(c.id, [])
                def_type = ((c/"ownedComment")[0]|"body").text.lower()
                    
                # There are several kinds of pset and qset association mechanisms:
                # 
                # - occurrence driven: only applicable to IfcObject subtypes
                # - type driven: only applicable to IfcTypeObject subtypes
                # - type driven override: applicable to both IfcObject and IfcTypeObject
                #                         where the former can override the latter
                # - material driven: applicable to IfcMaterialDefinition, uses IfcMaterialProperties
                # - profile driven: applicable to IfcProfileDef, uses IfcProfileProperties
                # 
                # In UML we associate only to the IfcObject subtype
                # 
                # In this step we make sure that the serialized data corresponds
                # to the association mechanism of the pset.
                is_type_driven_only = "typedrivenonly" in def_type
                is_type_driven_override = "typedrivenoverride" in def_type

                if self.should_translate_pset_types and (is_type_driven_override or is_type_driven_only):
                    get_name = lambda id_: self.xmi.by_id[id_].name
                    ref_names = list(map(get_name, refs))
                    
                    def substitute_predefined_type_with_containing_entity(ref_name):
                        """
                        PQsets can also be associated to a predefined type which is
                        modelled in UML as a class with a DOT in its name, signalling
                        the enum container and predefined type value. We should trace
                        the containment of such a predefined type ot the relevant entity
                        by means of the formal UML association, but we take a shortcut
                        here by looking at the name.                            
                        """
                        
                        if "." in ref_name:
                            type_name, type_value = ref_name.split(".")
                            entity_name = re.sub("(Type)?Enum$", "", type_name)
                            entity = class_by_name[entity_name]
                            return entity.xmi_id, type_value
                    
                    ref_substituted_entities = list(map(substitute_predefined_type_with_containing_entity, ref_names))
                    refs_combined = [b if b else (a,) for a, b in zip(refs, ref_substituted_entities)]
                    
                    # Lookup corresponding object types for the applicable entities
                    object_typing_reversed = {class_by_name[d['ApplicableEntity']].id: class_by_name[d['RelatingType']].id for d in self.concepts['ObjectTyping']}
                    corresponding_types = list(filter(None, map(lambda id_pt: object_typing_reversed.get(id_pt[0], None), refs_combined)))
                    
                    if len(corresponding_types) != len(refs) or set(corresponding_types) & set(refs):
                        ref_names = map(get_name, refs)
                        ref_type_names = map(get_name, corresponding_types)
                        print(f"WARNING: For PQset {c.name} applicability [{', '.join(ref_names)}] results in type associations [{', '.join(ref_type_names)}]")
                    
                    # augment with predefined types again:
                    corresponding_types = [(a,) + b[1:] if b[1:] else a for a, b in zip(corresponding_types, refs_combined)]
                    
                    if is_type_driven_only:
                        refs = corresponding_types
                    else:
                        refs = refs + corresponding_types

                set_definition = []
                for attr in c/"ownedAttribute":
                    nm = attr.name
                    ty = self.xmi.by_id[(attr.resolve("type"))]
                    
                    if c.name.startswith("Pset"):
                        bounds = ((attr|"lowerValue").value or "0", (attr|"upperValue").value or "1")
                        prop_args = {"Type": re.split(r'_\w\[', ty.name)[0]}

                        allowed_reference_types = {"IfcAddress", "IfcAppliedValue", "IfcExternalReference", "IfcMaterialDefinition", "IfcOrganization", "IfcPerson", "IfcPersonAndOrganization", "IfcTable", "IfcTimeSeries"}

                        if 'bounded' in [(c|"body").text.lower() for c in (attr/"ownedComment")]:
                            prop_type = "PropertyBoundedValue"
                        elif ty.type == 'uml:Class' and {a.name for a in ty/"ownedAttribute"} == {'DefinedValue', 'DefiningValue'}:
                            prop_type = "PropertyTableValue"
                            prop_args = {a.name.removesuffix("Value"): self.xmi.by_id[a.resolve('type')].name for a in ty/"ownedAttribute"}
                        elif ty.type == 'uml:Enumeration':
                            prop_type = "PropertyEnumeratedValue"
                        elif set(self.supertypes(ty.id)) & allowed_reference_types:
                            prop_type = "PropertyReferenceValue"
                        elif bounds == ("0", "1"):
                            prop_type = "PropertySingleValue"
                        elif bounds == ('1', '*'):
                            prop_type = "PropertyListValue"
                        else:
                            raise RuntimeError(f"Unexpected property: {attr} with type {ty}")
                        
                        set_definition.append((nm, (prop_type, prop_args)))
                    else:
                        set_definition.append((nm, ty.name))

                yield xmi_item(
                    "PSET", 
                    c.name,
                    set_definition, 
                    c,
                    [(x.name, x) for x in c/("ownedAttribute")],
                    document=self, 
                    refs=refs,
                )
                
            elif c.xmi_type == "uml:DataType":
                name = c.name

                supert = self.xmi.by_id[(c|"generalization").resolve('general')].name
                if self.xmi.by_id[(c|"generalization").resolve('general')].parent.name == "base":
                    # format simple type names as upper case, e.g real -> REAL
                    supert = supert.upper()

                if "_" in c.name:
                    name, *aggr = name.split('_')
                    parts = []
                    for ag in aggr:
                        parts.extend(format_aggr(ag))
                    parts.append(supert)
                    supert = " ".join(parts)
                
                constraints = [(r.name, (r|"body").text) for r in c/"ownedRule" if (r|"language").text == 'EXPRESS_WHERE']
                if ocl := next(((r|"body").text for r in c/"ownedRule" if (r|"language").text == 'OCL'), None):
                    if m := re.match(r'self\.size\(\) (=|<=) (\d+)', ocl):
                        op, sz = m.groups()
                        supert = f"{supert}({sz}){' FIXED' if op == '=' else ''}"

                yield xmi_item("TYPE", name, express.simple_type(name, supert, constraints), c, document=self)
                
            elif c.xmi_type == "uml:Enumeration":
                # There are two options, regular enumerations or PredefinedType enumerations.
                # the later category (in addition to the ownedLiterals) has uml:Class equivalents
                # for every literal in order to make property set associations. It is important
                # for the serialization of the Psets that in that case the xmi:ids are not those
                # of the literal, but those of the classes because otherwise the pset associations
                # cannot be traced back.
                values = [(_.name.split(".")[1], _) for _ in self.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if _.name.startswith(f"{c.name}.")]
                if not values:
                    values = [(lit.name, lit) for lit in c/"ownedLiteral"]

                is_property_enum = c.name.lower().startswith("penum_")

                # alphabetical sort, but the items below always come last
                undefined = ("OTHER", "NOTKNOWN", "UNSET", "USERDEFINED", "NOTDEFINED")
                penalize_undefined = lambda tup: f"z{undefined.index(tup[0]):02d}" if tup[0] in undefined else tup[0]
                
                values = sorted(values, key=penalize_undefined)

                express_definition = ""
                if not is_property_enum:
                    # not that it would fail, but they're just not intended to be written to EXP
                    express_definition = express.enumeration(c.name, [a for a, b in values])
                    
                yield xmi_item(
                    "PENUM" if is_property_enum else "ENUM",
                    c.name,
                    express_definition,
                    c,
                    values,
                    document=self)
            
            elif c.xmi_type == "uml:Class" and c.id in self.dependencies_in:
                values = sorted(self.xmi.by_id[x].name.split('_')[0] for x in self.dependencies_in[c.id])
                yield xmi_item("SELECT", c.name, express.select(c.name, values), c, document=self)
            else:
                assert c.name.startswith("Ifc")

                is_abstract = c.isAbstract == "true"

                attributes, inverses, derived, children = [], [], [], []

                subtypes = [*map(operator.attrgetter('name'), filter(lambda n: n.xmi_type == 'uml:Class', filter(lambda n: '.' not in n.name, (self.xmi.by_id[x] for x in self.generalizations_in.get(c.id, [])))))]
                supertypes = [self.xmi.by_id[x].name for x in self.generalizations_out.get(c.id, [])]
                itm_supertype_names = set(self.supertypes(c.id))
                
                for a in c/"ownedAttribute":
                    if a.isDerived == "true":
                        derive_def = (a|"defaultValue"|"body").text
                        supertype_attribute_lookup = dict(sum([[(a.name, x) for a in class_by_name[x]/"ownedAttribute"] for x in itm_supertype_names - {c.name}], []))
                        a_name = a.name
                        if supertype_defining_attr := supertype_attribute_lookup.get(a_name):
                            a_name = f"SELF\\{supertype_defining_attr}.{a_name}"
                        derived.append((a_name, derive_def))
                    else:
                        name, *aggr = a.name.split('_')
                        parts = []
                        if ((a|'lowerValue').value or "0") == "0":
                            parts.append("OPTIONAL")
                        for ag in aggr:
                            parts.extend(format_aggr(ag))

                        atype = self.xmi.by_id[a.resolve('type')]
                        atype_name = atype.name
                        if atype.parent.name == "base":
                            # format simple type names as upper case, e.g real -> REAL
                            atype_name = atype_name.upper()
                        
                        atype_name = atype_name.split('_')[0]

                        parts.append(atype_name)
                        attributes.append((name, " ".join(parts)))

                for assoc in self.associations[c.name]:
                    if assoc.own_end.name:
                        assert assoc.own_end.name.startswith("INV_")
                        name = assoc.own_end.name[4:]
                        parts = []
                        if '_' in name:
                            parts.extend(format_aggr(name.split('_', 1)[1]))
                        other_name = assoc.other_end.name.removeprefix('(').removesuffix(')').split('_')[0].removesuffix('?')
                        parts.extend((assoc.type.name, "FOR", other_name))
                        inverses.append((name.split('_')[0], " ".join(parts)))

                is_occurrence=itm_supertype_names & {"IfcElement", "IfcSystem", "IfcSpatialStructureElement", "IfcConstructionResource", "IfcProcedure", "IfcProcess", "IfcSpatialZone", "IfcWorkCalendar", "IfcWorkControl"}
                # construction resources don't have a CorrectTypeAssigned rule in earlier 4.3 revisions
                is_occurrence_no_type=itm_supertype_names & {"IfcElement", "IfcSystem", "IfcSpatialStructureElement", "IfcSpatialZone"}
                is_type = itm_supertype_names & {"IfcElementType", "IfcConstructionResourceType", "IfcSpatialStructureElementType", "IfcProcedureType", "IfcEventType", "IfcSpatialZoneType", "IfcTaskType"}
                is_restype = itm_supertype_names & {"IfcConstructionResourceType"}
                is_spacialtype = itm_supertype_names & {"IfcSpatialElementType"}
                is_processtype = itm_supertype_names & {"IfcTypeProcess"}
                # some_hardcoded_ones = {
                #     IfcConstructionEquipmentResource
                #     IfcConstructionEquipmentResourceType
                #     IfcConstructionMaterialResource
                #     IfcConstructionMaterialResourceType
                #     IfcConstructionProductResource
                #     IfcConstructionProductResourceType
                #     IfcCrewResource
                #     IfcCrewResourceType
                #     IfcElementAssembly
                #     IfcEventTime
                #     IfcLaborResource
                #     IfcLaborResourceType
                #     IfcProcedure
                #     IfcProcedureType
                #     IfcSpaceType
                #     IfcSpatialZone
                #     IfcSpatialZoneType
                #     IfcSubContractResource
                #     IfcSubContractResourceType
                #     IfcSystemFurnitureElementType
                #     IfcTaskType
                # }

                generated_whererules = []

                if is_type or is_occurrence: # or c.name in some_hardcoded_ones:
                    attribute_dict = dict(attributes)
                    if "PredefinedType" in attribute_dict:
                        type_attr = attribute_dict["PredefinedType"]
                        type_name = type_attr.split(" ")[-1]
                        type_optional = "OPTIONAL" in type_attr
                        attr = "IfcTypeProcess.ProcessType" if is_processtype else "IfcSpatialElementType.ElementType" if is_spacialtype else "IfcTypeResource.ResourceType" if is_restype else "IfcElementType.ElementType" if is_type else "IfcObject.ObjectType"
                        clause_1 = "NOT(EXISTS(PredefinedType)) OR\n " if type_optional else ''
                        rule = clause_1 + f"(PredefinedType <> {type_name}.USERDEFINED) OR\n ((PredefinedType = {type_name}.USERDEFINED) AND EXISTS (SELF\\{attr}))"
                        generated_whererules.append(("CorrectPredefinedType", rule))

                if is_occurrence_no_type:
                    # @todo should use ObjectTyping.csv
                    if ty_def := class_by_name.get(c.name + "Type"):
                        ty_attr_names = [attr.name for attr in ty_def/"ownedAttribute"]
                        # @todo the inconsistencies are uncountable
                        if "PredefinedType" in ty_attr_names or c.name == "IfcDeepFoundation":
                            generated_whererules.append(
                                ("CorrectTypeAssigned", f"(SIZEOF(IsTypedBy) = 0) OR\n  ('{SCHEMA_NAME}.{c.name.upper()}TYPE' IN TYPEOF(SELF\\IfcObject.IsTypedBy[1].RelatingType))")
                            )

                where_rules = sorted([*((r.name, (r|"body").text) for r in c/"ownedRule" if (r|"language").text == 'EXPRESS_WHERE'), *generated_whererules])
                unique_rules = sorted((r.name, (r|"body").text) for r in c/"ownedRule" if (r|"language").text == 'EXPRESS_UNIQUE')

                express_entity = express.entity(c.name, attributes, 
                    derived, sorted(inverses), where_rules,
                    unique_rules,
                    supertypes, subtypes, is_abstract
                )
                             
                yield xmi_item(
                    "ENTITY", c.name, 
                    express_entity, c, children,
                    document=self,
                    supertypes=subtypes
                )
