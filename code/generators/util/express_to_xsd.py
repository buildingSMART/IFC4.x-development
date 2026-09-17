import argparse
import re
import sys
import itertools
from pathlib import Path

from . import xml_dict

from dataclasses import dataclass

from .append_xmi import namespace
from ifcopenshell.express import express_parser
from .xmi_document import SCHEMA_NAME

X = xml_dict.xml_node

def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))

namespaces = {
    'xs': "http://www.w3.org/2001/XMLSchema",
    'xlink': "http://www.w3.org/1999/xlink",
    'ifc': f"https://standards.buildingsmart.org/IFC/RELEASE/{'/'.join(re.split('_|X', SCHEMA_NAME))}"
}

express_xsd_mapping = {
    'real': 'xs:double',
    'binary': 'ifc:hexBinary',
    'boolean': 'xs:boolean',
    'integer': 'xs:long',
    'number': 'xs:double',
    'string': 'xs:normalizedString',
    'logical': 'ifc:logical',
}

CODE_DIR = Path(__file__).resolve().parents[2]

conf = xml_dict.read(str(CODE_DIR / "IFC4_conf.xml"))
entity_configuration = {
    c.attributes['select']:\
    {cc.attributes['select']:cc.attributes for cc in c.children if cc.tag.endswith('attribute') or cc.tag.endswith('inverse') } \
    for c in conf.children if c.tag.endswith('entity')
}

XS = namespace(namespaces['xs'])
XLINK = namespace(namespaces['xlink'])
IFC = namespace(namespaces['ifc'])

class xml_serializable:
    def to_xml(self):
        return X(getattr(XS, self.__dict__.get('tagname', type(self).__name__)), {k:v for k, v in self.__dict__.items() if v and k != 'tagname'})
    

@dataclass
class attribute(xml_serializable):
    name : str
    type : str = None
    use : str = "optional"


@dataclass
class attribute_ref(xml_serializable):
    ref : str
    fixed : str = None
    use : str = "optional"
    
    tagname : str = "attribute"


@dataclass
class element(xml_serializable):
    name : str
    type : str = None
    abstract : str = None
    minOccurs : str = "0"
    substitutionGroup : str = None
    nillable : str = None
    

@dataclass
class element_ref(xml_serializable):
    ref : str
    minOccurs : str = None
    maxOccurs : str = None
    
    tagname : str = "element"
    

def complex_type(elements, attributes, content=None, **kwargs):
    if content:
        children = [content]
    else:
        children = [
            X(
                XS.sequence,
                children=elements
            )
        ]
    return X(
        XS.complexType,
        kwargs,
        children=children + list(map(attribute.to_xml, attributes))
    )

def do_try(fn):
    try:
        return fn()
    except:
        pass

defined_sequences = []
referenced_wrappers = set()

def literal_bound(b):
    # Numeric bound -> int; '?' or symbolic expression -> None (unbounded). (mirrors IfcOpenShell #8039)
    try:
        return int(b)
    except (TypeError, ValueError):
        return None

def create_attribute(entity, a, name_override=None):
    if isinstance(a, express_parser.AggregationType):
        a_type = a
    else:
        a_type = a.type
    
    is_optional = a.optional
    
    if isinstance(a_type, express_parser.NamedType):
        ty = a_type.type
        
        is_binary = do_try(lambda: isinstance(schema.types[ty].type.type, express_parser.BinaryType))
        
        if ty in schema.entities or is_binary:
            assert isinstance(ty, str)
            return element(a.name, f"ifc:{ty}", nillable=None if is_binary else "true", minOccurs="0" if is_optional else None).to_xml()
        elif ty in schema.selects:
            assert isinstance(ty, str)
            elm = element(a.name, None, nillable="true" if is_optional else None, minOccurs="0" if is_optional else None).to_xml()
            elm.children = [X(
                XS.complexType,
                children=[X(
                    XS.group,
                    {"ref": f"ifc:{ty}"}
                )]
            )]
            return elm
        return attribute(a.name, f"ifc:{ty}", "optional").to_xml()
        
    elif isinstance(a_type, express_parser.SimpleType):
        ty = a_type.type
        simple_type_mapping = {
            'integer': 'xs:long',
            'logical': 'ifc:logical'
        }
        return attribute(a.name, simple_type_mapping[ty], "optional").to_xml()
        
    elif isinstance(a, express_parser.InverseAttribute) or \
        isinstance(a_type, express_parser.AggregationType):

        min_occurs_mult = 1
        max_occurs_mult = 1
        aggregate_type_prefix = ""

        def aggregate_type(at):
            agt = at.aggregate_type
            if at.unique:
                agt += "-unique"
            return agt

        def format_unbounded(v):
            if v in (float("inf"), "?") or literal_bound(v) is None:
                return "unbounded"
            return str(v)
        
        if isinstance(a, express_parser.InverseAttribute):
            a_type = type('_0', (), {'type': type('_1', (), {'type': a.entity}), 'bounds': a.bounds, 'aggregate_type': a.type, 'unique': a.unique})
            is_optional = True

            min_occurs_mult = int(a.bounds.lower)
            max_occurs_mult = float("inf") if literal_bound(a.bounds.upper) is None else int(a.bounds.upper)
        else:
            if isinstance(a_type.type, express_parser.AggregationType):
                # nested lists don't require a lot of special handling, just list list
                min_occurs_mult = int(a_type.bounds.lower)
                max_occurs_mult = float("inf") if literal_bound(a_type.bounds.upper) is None else int(a_type.bounds.upper)
                aggregate_type_prefix = aggregate_type(a_type) + " "
                a_type = a_type.type

        #                                            # v this should probably be enabled, but discussion pending in issue #462
                # if : # and not isinstance(mapping.flatten_type(a_type.type).type, express_parser.StringType):
        
        def undecorate_until_string(x):
            if isinstance(x, str):
                return x
            return undecorate_until_string(x.type)
        
        is_list = undecorate_until_string(a_type) in schema.simpletypes and not (entity and entity_configuration.get(entity.name, {}).get(a.name, {}).get('exp-attribute') == 'double-tag')
        
        is_elem = entity and entity_configuration.get(entity.name, {}).get(a.name, {}).get('exp-attribute') == 'attribute-tag'
            
        if name_override:
            is_elem = False
            is_list = True
        
        if is_elem:

            if aggregate_type_prefix:
                        
                # @todo when length constraint is encoded in the type how to guarantee that the correct length constraint is selected?
                attr = X(XS.element, {'name': f'Seq-{undecorate_until_string(a_type)}-wrapper', 'type': f'ifc:Seq-{undecorate_until_string(a_type)}', 'maxOccurs': format_unbounded(max_occurs_mult)})
                
                inner_type = X(XS.simpleType, {'name': f'Seq-{undecorate_until_string(a_type)}'}, children=[
                    X(XS.restriction, children=[
                        X(XS.simpleType, children=[
                            X(XS.list, {'itemType': f'ifc:{undecorate_until_string(a_type)}'})
                        ])
                    ])
                ])
                
                length_constraint = []
                if int(a_type.bounds.lower) != 1:
                    length_constraint += [X(
                        XS.minLength,
                        {"value": (a_type.bounds.lower)}
                    )]
                if literal_bound(a_type.bounds.upper) is not None:
                    length_constraint += [X(
                        XS.maxLength,
                        {"value": (a_type.bounds.upper)}
                    )]
                    
                inner_type.children[0].children += length_constraint                
                defined_sequences.append(inner_type)
                
                attr = X(
                    XS.element, 
                    {'name': a.name, 'minOccurs': '0'},
                    # why:
                    # **({'minOccurs': min_occurs_mult} if min_occurs_mult != 1 else {})},
                    # 
                    # 'maxOccurs': ("unbounded" if max_occurs_mult == float("inf") else max_occurs_mult)
                    children=[X(
                        XS.complexType,
                        children=[X(
                            XS.sequence,
                            children=[attr]
                        )]
                    )]
                )
            else:
                attr = X(XS.element, {'name': a.name, 'type': f'ifc:{undecorate_until_string(a_type)}', 'nillable': 'true', 'minOccurs': a_type.bounds.lower, 'maxOccurs': format_unbounded(a_type.bounds.upper)})
                
        elif is_list:
        
            length_constraint = []
            
            if a_type.aggregate_type == 'array':
                assert min_occurs_mult == 1
                upper = literal_bound(a_type.bounds.upper)
                if upper is not None:
                    extent = upper - int(a_type.bounds.lower) + 1
                    for c in (XS.minLength, XS.maxLength):
                        length_constraint += [X(
                            c, {"value": str(extent)}
                        )]
                # else: symbolic/expression upper bound -> no fixed extent (unbounded)
            else:                
                if int(a_type.bounds.lower) != 1:
                    length_constraint += [X(
                        XS.minLength,
                        {"value": (a_type.bounds.lower * min_occurs_mult)}
                    )]
                if a_type.bounds.upper != "?" and max_occurs_mult != float("inf"):
                    length_constraint += [X(
                        XS.maxLength,
                        {"value": (a_type.bounds.upper * max_occurs_mult)}
                    )]
                    
            attr = attribute(a.name, None, "optional").to_xml()
            
            xsd_type = undecorate_until_string(a_type)
            xsd_type = express_xsd_mapping.get(xsd_type, f'ifc:{xsd_type}')
            
            attr.children = [X(
                XS.simpleType,               
                children=[X(
                    XS.restriction,
                    children=[X(
                        XS.simpleType,
                        children=[X(
                            XS.list,
                            {"itemType": xsd_type}
                        )]
                    )] + length_constraint  
                )]
            )]
            
            if name_override:
                attr = attr.children[0]
                attr.attributes['name'] = name_override
        else:        
            ty = undecorate_until_string(a_type)
            
            if ty in schema.simpletypes:
                wrapper_postfix = "-wrapper"
            else:
                wrapper_postfix = ""
                
            assert isinstance(ty, str)
            attr = element(a.name, None, nillable="true" if is_optional else None, minOccurs="0" if is_optional else None).to_xml()
            
            min_occurs = str(min_occurs_mult * int(a_type.bounds.lower))
            if min_occurs == "1":
                min_occurs = None
                
            max_occurs = "unbounded"
            try:
                max_occurs = str(int(a_type.bounds.upper) * max_occurs_mult)
            except: pass
            
            if max_occurs == "inf":
                max_occurs = "unbounded"    
                
            array_data = [
                attribute_ref("ifc:itemType", fixed=f"ifc:{ty}{wrapper_postfix}", use=None),
                attribute_ref("ifc:cType", fixed=aggregate_type_prefix + aggregate_type(a_type), use=None),
                attribute_ref("ifc:arraySize", use="optional")
            ]
            
            if ty in schema.selects:
                attr.children = [X(XS.complexType, children=[
                    X(XS.group, {'ref': f"ifc:{ty}", **({'minOccurs': min_occurs} if min_occurs else {}), **{'maxOccurs': max_occurs}}),
                    *(x.to_xml() for x in array_data)
                ])]
            else:
                if wrapper_postfix:
                    referenced_wrappers.add(f"{ty}{wrapper_postfix}")

                attr.children = [complex_type([
                    element_ref(f"ifc:{ty}{wrapper_postfix}", minOccurs=min_occurs, maxOccurs=max_occurs).to_xml()
                ], array_data
                )]
            
        return attr
    else:
        breakpoint()
        

def convert(e, name_override=None, excluded_attributes=(), restriction=None, include_inherited=False):

    subGroup = supertype = e.supertypes[0] if e.supertypes else "Entity"
    abstract_if_abstract = {"abstract": "true"} if e.abstract or (name_override and "-temp" in name_override) else {}
    
    derived = mapping.derived_in_supertype(e)
    
    def get_attributes(ent):
        e_cfg = entity_configuration.get(ent.name, {})
        keep_fwd = lambda a: e_cfg.get(a.name, {}).get('keep') != 'false' and a.name not in excluded_attributes
        keep_inv = lambda a: a.name in e_cfg
        
        inherited = []
        if include_inherited and ent.supertypes:
            inherited = get_attributes(mapping.schema.entities[ent.supertypes[0]])
        
        return inherited + list(filter(keep_fwd, ent.attributes)) + list(filter(keep_inv, ent.inverse))
    
    attributes = get_attributes(e)
    
    derived_with_additional_attributes = derived and attributes
    derived_without_additional_attributes = derived and not attributes
    
    if derived:
        yield from convert(mapping.schema.entities[e.supertypes[0]],
            name_override = e.name + ("-temp" if attributes else ""), 
            excluded_attributes = set(derived),
            restriction = e.supertypes[0],
            include_inherited = True
        ) 
        supertype = f"{e.name}-temp"
        
    if derived_without_additional_attributes:
        return

    if not name_override:
        yield element(e.name, f"ifc:{e.name}", substitutionGroup=f"ifc:{subGroup}", nillable="true", minOccurs=None, **abstract_if_abstract).to_xml()    
    
    attrs = [create_attribute(e, a) for a in attributes]
    elems = [e for e in attrs if e.tag == XS.element]
    attrs = [e for e in attrs if e.tag == XS.attribute]
    
    if elems:
        elems = [X(
            XS.sequence,
            children=elems
        )]
    
    children = elems + attrs
    
    yield complex_type([], [], content=X(
        XS.complexContent,
        children=[
            X(
                XS.restriction,
                {"base": f"ifc:{restriction}"},
                children=children
            ) \
            if restriction
            else \
            X(
                XS.extension,
                {"base": f"ifc:{supertype}"},
                children=children
            )            
        ]
    ), name=name_override or e.name, **abstract_if_abstract)


def convert_select(nm_def):
    nm, defn = nm_def
    
    def items(s=None):
        def inner(v):
            v = v.type
            if v in schema.selects:
                yield from items(schema.selects[v])
            else: yield v
        yield from itertools.chain.from_iterable(map(inner, (s or defn).values))
    
    def make_ref(s):
        if not s in schema.entities:
            s += '-wrapper'
        return f'ifc:{s}'
    
    for s in items():
        if make_ref(s).endswith("-wrapper"):
            referenced_wrappers.add(make_ref(s).split(':')[1])
               
    make_elem = lambda s: X(XS.element, {'ref': make_ref(s)})
    children = list(map(make_elem, sorted(set(items()))))
    
    yield X(
        XS.group, 
        {'name': nm},
        children=[X(
            XS.choice,
            children=children
        )]
    )
    
    
def convert_enum(nm_def):
    nm, defn = nm_def
    
    make_elem = lambda s: X(XS.enumeration, {'value': s.lower()})
    children = list(map(make_elem, defn.values))
    
    yield X(
        XS.simpleType, 
        {'name': nm},
        children=[X(
            XS.restriction,
            {'base': 'xs:string'},
            children=children
        )]
    )
    

def convert_simple(nm_def):
    nm, defn = nm_def

    def convert_base(d):
        if isinstance(d, express_parser.SimpleType):
            return express_xsd_mapping[str(defn.type).split(' ')[0]]
        elif d in schema.simpletypes or d in schema.entities:
            return f'ifc:{d}'
        else:
            return 'unsupported'
    
    if isinstance(defn, express_parser.AggregationType):
        
        base = convert_base(defn.type)
        attrs = [
            X(XS.attribute, {"ref": "ifc:itemType", "fixed": base}),
            X(XS.attribute, {"ref": "ifc:cType", "fixed": defn.aggregate_type}),
            X(XS.attribute, {"ref": "ifc:arraySize", "use": "optional"})
        ]
        
        if defn.type in schema.entities:
        
            yield X(XS.complexType, {"name": nm}, children=[
                X(XS.sequence, children=[X(XS.element,
                    {"ref": base, 'maxOccurs': defn.bounds.upper if literal_bound(defn.bounds.upper) is not None else "unbounded"}
                )])]+attrs
            )
            
        else:
        
            
            yield X(XS.complexType, {"name": nm},
                children=[X(XS.simpleContent, children=[
                    X(XS.extension, {"base": f"ifc:List-{nm}"}, children=attrs)
                ])]
            )
            
            # due to name_override not actually an attribute, but simpleType directly
            yield create_attribute(None, defn, name_override=f'List-{nm}')
    else:
    
        base = convert_base(defn)
    
        if base == "ifc:hexBinary":
            yield X(
                XS.complexType,
                {'name': nm},
                children = [X(
                    XS.simpleContent,
                    children = [X(
                        XS.extension,
                        {'base': base}
                    )]
                )]
            )
        else:
            x = X(
                XS.simpleType,
                {'name': nm},
                children = [X(
                    XS.restriction,
                    {'base': base}
                )]
            )
            
            try:
                has_width = defn.type.width.width
                is_fixed = bool(defn.type.width.FIXED)
                
                if is_fixed:
                    x.children[0].children = [
                        X(XS.minLength, {"value": str(has_width)}),
                        X(XS.maxLength, {"value": str(has_width)})
                    ]
                    
                elif has_width:
                    x.children[0].children = [
                        X(XS.maxLength, {"value": str(has_width)})
                    ]
                    
            except:
                pass
                
            yield x
            
def convert_simple_wrapper(nm_def):
    nm, defn = nm_def
    
    def undecorate_type(t):
        if hasattr(t, 'type'):
            return undecorate_type(t.type)
        else:
            return t
        
    if undecorate_type(defn) in schema.entities:
        ty = XS.complexContent
    else:
        ty = XS.simpleContent
    
    if f"{nm}-wrapper" in referenced_wrappers:
        yield X(XS.element, {'name': f"{nm}-wrapper", 'nillable': "true"}, children=[
            X(XS.complexType, children=[
                X(ty, children=[
                    X(XS.extension, {'base': f"ifc:{nm}"}, children=[
                        X(XS.attributeGroup, {'ref': "ifc:instanceAttributes"})
                    ])
                ])
            ])
        ])
    
def baseschema():
    yield X(XS.element, {'name': 'Entity', 'type': 'ifc:Entity', 'abstract': 'true', 'nillable': 'true'})
    
    yield X(XS.complexType, {'name': 'Entity', 'abstract': 'true'}, children=[
		X(XS.attribute, {'name': 'href', 'type': 'xs:anyURI', 'use': 'optional'}),
		X(XS.attribute, {'name': 'ref', 'type': 'xs:IDREF', 'use': 'optional'}),
		X(XS.attributeGroup, {'ref': 'ifc:instanceAttributes'})
    ])
    
    yield X(XS.attributeGroup, {'name': 'instanceAttributes'}, children=[
		X(XS.attribute, {'name': 'id', 'type': 'xs:ID', 'use': 'optional'}),
		X(XS.attribute, {'name': 'path', 'type': 'xs:NMTOKENS', 'use': 'optional'}),
		X(XS.attribute, {'name': 'pos', 'use': 'optional'}, children=[
			X(XS.simpleType, children=[
				X(XS.restriction, children=[
					X(XS.simpleType, children=[
						X(XS.list, {'itemType': 'xs:integer'})
                    ]),
					X(XS.minLength, {'value': '1'})
                ])
            ])
        ])
    ])
    
    yield X(XS.attribute, {'name': 'arraySize'}, children=[
		X(XS.simpleType, children=[
			X(XS.restriction, children=[
				X(XS.simpleType, children=[
					X(XS.list, {'itemType': 'xs:integer'})
                ]),
				X(XS.minLength, {'value': '1'})
            ])
        ])
    ])
    
    yield X(XS.attribute, {'name': 'itemType'}, children=[
		X(XS.simpleType, children=[
			X(XS.list, {'itemType': 'xs:QName'})
        ])
    ])
    
    yield X(XS.attribute, {'name': 'cType'}, children=[
		X(XS.simpleType, children=[
			X(XS.list, {'itemType': 'ifc:aggregateType'})
        ])
    ])
    
    yield X(XS.simpleType, {'name': 'aggregateType'}, children=[
		X(XS.restriction, {'base': 'xs:normalizedString'}, children=[
			X(XS.enumeration, {'value': 'array'}),
			X(XS.enumeration, {'value': 'list'}),
			X(XS.enumeration, {'value': 'set'}),
			X(XS.enumeration, {'value': 'bag'}),
			X(XS.enumeration, {'value': 'array-unique'}),
			X(XS.enumeration, {'value': 'array-optional'}),
			X(XS.enumeration, {'value': 'array-optional-unique'}),
			X(XS.enumeration, {'value': 'list-unique'})
        ])
    ])
    
    yield X(XS.complexType, {'name': 'hexBinary'}, children=[
		X(XS.simpleContent, children=[
			X(XS.extension, {'base': 'xs:hexBinary'}, children=[
				X(XS.attribute, {'name': 'extraBits', 'type': 'xs:integer', 'use': 'optional'})
            ])
        ])
    ])
    
    yield X(XS.simpleType, {'name': 'logical'}, children=[
		X(XS.restriction, {'base': 'xs:normalizedString'}, children=[
			X(XS.enumeration, {'value': 'false'}),
			X(XS.enumeration, {'value': 'true'}),
			X(XS.enumeration, {'value': 'unknown'})
        ])
    ])
   
    
def run(express_path, xsd_path):
    global mapping, schema, entities, selects, enums, simpletypes

    defined_sequences.clear()
    referenced_wrappers.clear()

    mapping = express_parser.parse(str(express_path))
    schema = mapping.schema
    entities = list(schema.entities.values())
    selects = list(schema.selects.items())
    enums = list(schema.enumerations.items())
    simpletypes = list(schema.simpletypes.items())

    header = complex_type(
        [
            X(
                XS.element,
                {"name": "header", "minOccurs": "0"},
                children=[complex_type(
                    [
                        element("name", "xs:string", minOccurs="0").to_xml(),
                        element("time_stamp", "xs:dateTime", minOccurs="0").to_xml(),
                        element("author", "xs:string", minOccurs="0").to_xml(),
                        element("organization", "xs:string", minOccurs="0").to_xml(),
                        element("preprocessor_version", "xs:string", minOccurs="0").to_xml(),
                        element("originating_system", "xs:string", minOccurs="0").to_xml(),
                        element("authorization", "xs:string", minOccurs="0").to_xml(),
                        element("documentation", "xs:string", minOccurs="0").to_xml(),
                    ],
                    []
                )],
            )
        ],
        [
            attribute("id", "xs:ID"),
            attribute("express", "ifc:Seq-anyURI"),
            attribute("configuration", "ifc:Seq-anyURI")
        ],
        name="uos", abstract="true"
    )

    content = X(
        XS.schema,
        {
            "targetNamespace": namespaces['ifc'],
            "elementFormDefault": "qualified",
            "attributeFormDefault": "unqualified"
        },
        namespaces=namespaces,
        children=[
            X(XS.element,
                {
                    "name": "uos",
                    "type": "ifc:uos",
                    "abstract": "true"
                },
            ),
            X(XS.simpleType,
                {
                    "name": "Seq-anyURI",
                },
                children=[
                    X(XS.list,
                        {
                            "itemType": "xs:anyURI",
                        }
                    )
                ]
            ),
            header,
            element("ifcXML", "ifc:ifcXML", minOccurs=None, substitutionGroup="ifc:uos").to_xml(),
            complex_type([], [], content=X(
                XS.complexContent,
                children=[X(
                    XS.extension,
                    {"base": "ifc:uos"},
                    children = [X(
                        XS.choice,
                        {"minOccurs": "0", "maxOccurs": "unbounded"},
                        children=[(
                            X(XS.element, {"ref": "ifc:Entity"})
                        )]
                    )]

                )]
            ),name="ifcXML")
        ] + list(flatmap(convert, entities)) + \
            list(flatmap(convert_select, selects)) + \
            list(flatmap(convert_enum, enums)) + \
            list(flatmap(convert_simple, simpletypes)) + \
            list(baseschema()) + \
            defined_sequences +\
            list(flatmap(convert_simple_wrapper, sorted(simpletypes + enums)))
    )

    xml_dict.serialize([content], str(xsd_path))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate IFC XSD from an EXPRESS schema.")
    parser.add_argument("express", type=Path, help="Path to the input EXPRESS schema.")
    parser.add_argument("output", type=Path, help="Path to the generated XSD file.")
    args = parser.parse_args(argv)
    run(args.express, args.output)


if __name__ == "__main__":
    main()
