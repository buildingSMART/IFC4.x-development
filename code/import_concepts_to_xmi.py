import os
import sys
import glob
import operator
import itertools

from generators.util import xmi_document
from generators.util import xml_dict
from generators.util import append_xmi
import concept_extractor
import concept_interpretation

from generators.util.append_xmi import XMI

def norm(v):
    return v.lower().replace(" ", "").replace("_", "")
    

class xmi_concept_writer:

    def __init__(self, xmi, xmi_items, extractor):
        self.xmi = xmi
        self.xmi_items = xmi_items
        self.extractor = extractor
        
        try:
            self.gu_package = self.xmi.package_by_name("GeneralUsage")
        except:
            ifc_package = self.xmi.package_by_name("IFC4X3_ADD2")
            views_package = self.xmi.insert(ifc_package, append_xmi.uml_package("Views"))
            self.gu_package = self.xmi.insert(views_package, append_xmi.uml_package("GeneralUsage"))
        
        # As part of the concept enumerations we want to establish uml:Realizations
        # between uml:Enumeration and designated classes for the literals. We do
        # create these individual classes for enum literals so that we can make
        # associations between them and the concept usage nodes.
        self.realizations = set()
        def v(nd, _):
            if nd.attributes.get(XMI.type) == "uml:Realization":
                self.realizations.add(frozenset((nd.attributes["supplier"], nd.attributes["client"])))
        self.xmi._recurse(v)

    def _create_package(self, key):
        """
        Returns `true` when package does not exist yet
        """
        
        concept_name = key[0]
        self.concept_name_short = concept_name.replace(" ", "")
        self.concept_package = self.xmi.package_by_name(self.concept_name_short)
        if self.concept_package:
            return False
        else:
            self.concept_package = self.xmi.insert(self.gu_package, append_xmi.uml_package(self.concept_name_short))
            return True

    def write_as_directional_binary(self, key, values):
        columns = list(zip(*values))
        non_empty_columns = [col for col in columns if any(cell for cell in col)]
        rows = zip(*non_empty_columns)
        
        for appl, param in rows:
            try:
                nodes = [self.xmi.to_node[("uml:Class", v)] for v in [appl, param]]
            except KeyError as e:
                print(f"Non existent class {e.args[0][1]} in concept {key[0]}")
                continue
            assoc = append_xmi.uml_assoc_class(
                f"{appl}{self.concept_name_short}Usage",
                [n.attributes[XMI.id] for n in nodes],
                owners = [None, nodes[0]]
            )
            self.xmi.insert(self.concept_package, assoc)

    def write_as_directional_grouped(self, key, values):
        mapping = dict([(g, frozenset([vv[1] for vv in vs])) for g, vs in itertools.groupby(sorted([v[0:2] for v in values]), key=operator.itemgetter(0))])
        options = set(mapping.values())
        option_to_class = {}
        
        for opt in options:
            nm = "".join(o[3:] for o in sorted(opt))
            opt_class = append_xmi.uml_class(nm)
            option_to_class[opt] = opt_class
            self.xmi.insert(self.concept_package, opt_class)
            for entity in opt:
                self.xmi.insert(self.concept_package, append_xmi.uml_association(
                    [opt_class.id, self.xmi.to_id("uml:Class", entity)],
                    owners = [None, opt_class.xml]
                ))
                
        for appl, opt in mapping.items():
            ent_class = self.xmi.to_node[("uml:Class", appl)]
            self.xmi.insert(self.concept_package, append_xmi.uml_association(
                [ent_class.attributes[XMI.id], option_to_class[opt].id],
                owners = [None, ent_class]
            ))

    def write_as_nary(self, key, values):
        parameters = key[1:]
        parameter_id_mapping = [{} for _ in parameters]
        
        for column_id, ((rule_id, (entity_name, attribute_name)), pmap) in enumerate(zip(parameters, parameter_id_mapping), start=1):
            
            def get_attrs_from_class(nd):
                def get_type_id(attr):
                    return [ch for ch in attr.children if ch.tag == "type"][0].attributes[XMI.idref]
                
                # First have a peak at the child uml:Properties
                attrs = [get_type_id(ch) for ch in nd.children if ch.attributes[XMI.type] == "uml:Property" and ch.attributes.get('name') == attribute_name]
                
                if not attrs:
                    # If not we take a look at the associations as interpreted by the xmi_document
                    xi = [i for i in self.xmi_items if i.name == nd.attributes['name']][0]
                    attrs = [c.node for c in xi.children if c.name == attribute_name]
                    if attrs:
                        a = attrs[0]
                        assoc_types = set(x.idref for x in a/"type")
                        assert len(assoc_types) == 2
                        attrs = list(assoc_types - {nd.attributes[XMI.id]})
                        assert len(attrs) == 1
                        
                return attrs

            # From the RuleIDs we have (entity_name, attribute_name). We lookup the type of
            # this attribute in the XMI schema. Taking into account inheritance as the
            # attribute may be defined on a more abstract entity.
            nd = self.xmi.to_node[entity_name]
            while True:                
                attrs = get_attrs_from_class(nd)
                
                if attrs:
                    attr_type_ids = [attrs[0]]
                    break
                else:
                    gens = [ch for ch in nd.children if ch.tag == "generalization"]
                    if gens:
                        nd = self.xmi.to_node[gens[0].attributes['general']]
                    else:
                        attr_type_ids = None
                        break
                   
            # If not found on the entity or supertype, we also need to look at subtypes.
            # e.g PredefinedType is only introduced at concrete leaf classes, but is
            # still referenced as part of more generic IfcObject for example in the
            # case of the Property Sets for Objects concept.
            if attr_type_ids is None:
            
                def subclasses(x):
                    yield x
                    for s in self.xmi.subclasses[x]:
                        yield from subclasses(s)
                        
                scs = list(subclasses(entity_name))
                
                attr_type_ids = []
                
                for sc in scs:
                    attrs = get_attrs_from_class(self.xmi.to_node[sc])
                    if attrs:
                        attr_type_ids.append(attrs[0])            
            
            for attr_type_id in attr_type_ids:
                
                attr_type = self.xmi.to_node[attr_type_id]
                attr_type_name = attr_type.attributes['name']
                
                if attr_type.attributes[XMI.type] == "uml:DataType":
                
                    # For data types we create an enumeration as part of the concept
                    # package to hold all values that are used within the parametrization.
                    
                    assert len(attrs) == 1
                
                    column = sorted(set(v[column_id] for v in values))
                    new_enum = append_xmi.uml_enumeration(f"{self.concept_name_short}{rule_id}Values", column)
                    self.xmi.insert(self.concept_package, new_enum)
                    for col in column:
                        full_name = f"{self.concept_name_short}{rule_id}Values.{col}"
                        enum_value_class = append_xmi.uml_class(full_name)
                        self.xmi.insert(self.concept_package, enum_value_class)
                        self.xmi.insert(self.concept_package, append_xmi.uml_realization(enum_value_class.id, new_enum.id))
                        pmap[norm(col)] = enum_value_class.id
                        
                elif attr_type.attributes[XMI.type] == "uml:Enumeration":
                    
                    # Enumeration: check if a node exists already
                    # for the literal.
                    
                    enum_values = [ch.attributes['name'] for ch in attr_type.children if ch.tag == "ownedLiteral"]
                    for ev in enum_values:
                        full_name = f"{attr_type_name}.{ev}"
                        if full_name in self.xmi.to_node:
                            vid = pmap[norm(ev)] = self.xmi.to_node[full_name].attributes[XMI.id]
                            eid = attr_type.attributes[XMI.id]
                            ids = (vid, eid)
                            if frozenset(ids) not in self.realizations:
                                self.realizations.add(frozenset(ids))
                                self.xmi.insert(attr_type.parent, append_xmi.uml_realization(*ids))
                        else:
                            assert attr_type.parent.attributes[XMI.type] == "uml:Package"
                            enum_value_class = append_xmi.uml_class(full_name)
                            self.xmi.insert(attr_type.parent, enum_value_class)
                            ids = (enum_value_class.id, attr_type.attributes[XMI.id])
                            self.realizations.add(frozenset(ids))
                            self.xmi.insert(attr_type.parent, append_xmi.uml_realization(*ids))
                            pmap[norm(ev)] = enum_value_class.id
                
                else:
                    
                    # express select or entity, recursively fill
                    # with specializations and substitutions
                    
                    def visit_type_id(nd_id):
                        name = self.xmi.to_node[nd_id].attributes['name']
                        pmap[norm(name)] = nd_id
                        for ch in self.xmi.substitutions.get(nd_id, []):
                            visit_type_id(ch)
                        for ch_name in self.xmi.subclasses.get(name, []):
                            ch_id = self.xmi.to_node[ch_name].attributes[XMI.id]
                            visit_type_id(ch_id)
                            
                    visit_type_id(attr_type_id)
                    

        def lookup_and_warn(i, pmap, p):
            v = pmap.get(norm(p))
            if v is None:
                breakpoint()
                print(f"Not valid: '{p}' for type {parameters[i][1][0]}.{parameters[i][1][1]} on parameter '{parameters[i][0]}'")
            return v
                    
        for row in values:
            entity = row[0]
            params = row[1:]
            ids = list(filter(None, [lookup_and_warn(i, pmap, p) for i, (pmap, p) in enumerate(zip(parameter_id_mapping, params)) if p]))
            ids = [self.xmi.to_id("uml:Class", entity)] + ids
            # @todo why is this set to Association?
            assoc = append_xmi.uml_assoc_class(f"{entity}{self.concept_name_short}Usage", ids, type="uml:Association")
            self.xmi.insert(self.concept_package, assoc)

    def write_as_no_parametrization(self, key, values):
        pass

    def write_as_property_or_quantity_set(self, key, values):
        # @nb values are ignored, but read from xmls
        
        if "Property" in key[0]:
            desc, ns, filepat = ("Property",
                "",
                "Pset_*.xml")
        else:
            desc, ns, filepat = ("Quantity",
                "{http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd}",
                "Qto_*.xml")
            
        for fn in glob.glob(os.path.join("../reference_schemas/psd/", filepat)):
            xd = xml_dict.read(fn)
            set_name = xd.child_with_tag(f"{ns}Name").text
            appl = [n.text for n in xd.child_with_tag(f"{ns}ApplicableClasses").children]
            
            try:
                set_id = self.xmi.to_id("uml:Class", set_name)
            except KeyError as e:
                print(f"Undefined (p|q)set {set_name}")
                continue
                
            for entity in appl:
        
                if "/" in entity:
                    if "(" in entity:
                        type_enum = entity.split("/")[1].replace(".)", "").replace("(", "")
                        if type_enum.startswith("."):
                            type_enum2 = entity.split("/")[0] + type_enum
                            try:
                                self.xmi.to_id("uml:Class", type_enum2)
                                type_enum = type_enum2
                            except:
                                type_enum = entity.split("/")[0] + "TypeEnum" + type_enum
                    else:
                        parts = entity.split("/")
                        for Type in ("Type", ""):
                            type_enum_type = f"{parts[0]}{Type}Enum"
                            try:
                                self.xmi.to_id("uml:Enumeration", type_enum_type)
                                break
                            except:
                                type_enum_type = parts[0]
                                continue
                        type_enum = f"{type_enum_type}.{parts[1]}"

                    try:
                        self.xmi.to_id("uml:Class", type_enum)
                        entity = type_enum
                    except KeyError as e:
                        print(f"Undefined type enum {type_enum}")
                        entity = entity.split("/")[0]
        
                try:
                    entity_id = self.xmi.to_id("uml:Class", entity)
                except KeyError as e:
                    print(f"Undefined entity {entity}")
                    continue
                
                assoc = append_xmi.uml_assoc_class(f"{entity}{self.concept_name_short}{set_name}", (entity_id, set_id))
                self.xmi.insert(self.concept_package, assoc)
            
        pass

    def write_as_object_typing(self, key, values):
        # tfk: The where rules are not complete wrt abstract classes so instead we simply
        #      look at the classes where a class exists as well with 'Type' appended to the
        #      name.
        # 
        # # Code below uses the express schema to feed the template parametrizations
        # get_typename = lambda S: re.findall(r"'ifc4x3\w+\.(\w+)' in typeof\(self\\IfcObject\.IsTypedBy", S)
        # get_typerule = lambda En: dict(En.where).get('CorrectTypeAssigned', '')
        # import ifcopenshell.express
        # schema = ifcopenshell.express.express_parser.parse("IFC.exp").schema
        # for en in schema.entities.values():
        #     print(en.name, get_typename(get_typerule(en)))
        # 
        
        def get_type_classes(IfcClass):
            tys = []
            for Postfix in ("Type", "Style"):
                try:
                    self.xmi.to_id("uml:Class", f"{IfcClass}{Postfix}")
                    tys.append(f"{IfcClass}{Postfix}")
                except: pass
            return tys

        class_names = [(k[1], get_type_classes(k[1])) for k,v in self.xmi.to_node.items() \
            \
            if k[0] == 'uml:Class' and \
            v.parent.parent.attributes.get('name') != 'GeneralUsage' and \
            v.parent.attributes.get('name') != 'propertytypes' and \
            not '.' in k[1] and \
            get_type_classes(k[1])
        ]
        
        for IfcClass, tys in class_names:
            for ty in tys:
                ids = [self.xmi.to_id("uml:Class", v) for v in [IfcClass, ty]]
                assoc = append_xmi.uml_assoc_class(f"{IfcClass}{self.concept_name_short}Usage", ids)
                self.xmi.insert(self.concept_package, assoc)

    def write_as_simple_unary(self, key, values):
        concept_class = append_xmi.uml_class(self.concept_name_short)
        self.xmi.insert(self.concept_package, concept_class)
        
        for entity in set(v[0] for v in values):
            ids = [concept_class.id, self.xmi.to_id("uml:Class", entity)]
            assoc = append_xmi.uml_assoc_class(f"{entity}{self.concept_name_short}Usage", ids)
            self.xmi.insert(self.concept_package, assoc)
      
    def __call__(self, key):
        values = self.extractor.grouping[key]
        xmi_mechanism = concept_interpretation.concepts[key]
        if not self._create_package(key):
            print(f"Concept package for {key[0]} already present, skipping")
        else:
            method = getattr(self, f"write_as_{xmi_mechanism.name.lower()}")
            method(key, values)

if __name__ == "__main__":
    
    xmi_items = list(xmi_document.xmi_document("..\schemas\IFC.xml"))
    xmi = append_xmi.context("..\schemas\IFC.xml")
    concepts = concept_extractor.extractor(sys.argv[1])
    writer = xmi_concept_writer(xmi, xmi_items, concepts)
    for key in concepts.grouping.keys():
        writer(key)
    
    xmi.write("..\schemas\IFC_with_concepts.xml")