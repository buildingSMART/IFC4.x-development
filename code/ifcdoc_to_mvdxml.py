import os
import re
import glob
import functools

import ifcopenshell
from ifcopenshell.mvd.mvdxml_expression import parse as parse_mvd_expr

from generators.util import xml_dict

class DependencyError(BaseException): pass  
  
def make_transform_tag_renamer(target, attribute_mapping={}):
    def inner(di, parent):
        return xml_dict.xml_node(
            target,
            {attribute_mapping.get(k, k): v for k, v in di.attributes.items()}
        )
    return inner

def make_transform_identity():
    def inner(di, parent):
        return make_transform_tag_renamer(di.tag)(di, parent)
    return inner
    
def do_transform_skip(di, parent):
    return None
       
def transform_uuid(v):
    if len(v) == 36:
        return v
    return ifcopenshell.guid.split(ifcopenshell.guid.expand(v))[1:-1]
    
transform_DocModelView = make_transform_tag_renamer("ModelView")
transform_ConceptRoots = make_transform_tag_renamer("Roots")
transform_Concepts = make_transform_identity()
transform_References = make_transform_identity()
transform_DocModelRuleAttribute = make_transform_tag_renamer("AttributeRule", attribute_mapping={"Name": "AttributeName", "Identification": "RuleID"})

# not sufficient anymore, because an entity rule can contain an href
transform_DocModelRuleEntity_nonhref = make_transform_tag_renamer("EntityRule", attribute_mapping={"Name": "EntityName", "Identification": "RuleID"})

templates = {}
used_template_ids = {}

def parse_templates(pt):
    queue = glob.glob(os.path.join(pt, "**", "DocTemplateDefinition.xml"), recursive=True)
    while queue:
        fn = queue.pop(0)
        try:
            tmpl_defs = transform(xml_dict.read(fn))
        except DependencyError as e:
            print("x", e, fn)
            queue.append(fn)
            continue
            
        if not tmpl_defs:
            continue
            
        tmpl_def = tmpl_defs[0]
            
        if "id" in tmpl_def.attributes:
            href = tmpl_def.attributes["id"]
            templates[href] = tmpl_def
            
            print("v", href)
            
            
def transform_DocModelRuleConstraint(di, parent):
    v = di.child_with_tag("Expression").child_with_tag("Value").attributes["Literal"].replace("'", "")
    return xml_dict.xml_node(
        "Constraint", {"Expression": f"[Value]='{v}'"}
    )

            
def transform_DocTemplateDefinition(di, parent):
    if di.attributes.get("href"):
        if di.attributes["href"] not in templates:
            raise DependencyError(di.attributes["href"])
        ref = templates[di.attributes["href"]].attributes["uuid"]
        return xml_dict.xml_node(
            "Template",
            {'ref': ref}
        )
    elif di.attributes.get("Type") and di.attributes.get("id"):
        return xml_dict.xml_node(
            "ConceptTemplate",
            {
                'id': di.attributes["id"],
                'uuid': transform_uuid(di.attributes["UniqueId"]),
                'name': di.attributes["Name"],
                'applicableEntity': di.attributes["Type"]
            }
        )
        
entity_rule_by_id = {}
        
def transform_DocModelRuleEntity(di, parent):
    if di.attributes.get("href"):
        return entity_rule_by_id[di.attributes["href"]]
    else:
        node = transform_DocModelRuleEntity_nonhref(di, parent)
        if di.attributes.get('id'):
            entity_rule_by_id[di.attributes.get('id')] = node
        return node

def transform_DocConceptRoot(di, parent):
    return xml_dict.xml_node(
        "ConceptRoot",
        {
            'uuid': transform_uuid(di.attributes["UniqueId"]),
            'name': di.child_with_tag("ApplicableEntity").attributes["href"],
            'applicableRootEntity': di.child_with_tag("ApplicableEntity").attributes["href"]
        }
    )
    
def transform_Documentation(di, parent):
    if parent.tag == "DocTemplateUsage":
        try:
            text = di.text.strip()
        except:
            text = None
        
        if text:
            return xml_dict.xml_node(
                "Definitions",
                children=[xml_dict.xml_node(
                    "Definition",
                    children=[xml_dict.xml_node(
                        "Body",
                        # is already being escaped
                        # text=f"<![CDATA[{text}]]>"
                        text=text                        
                    )]
                )]
            )
        
    
def transform_DocTemplateUsage(di, parent):
    children = []
    if di.child_with_tag("Definition").child_with_tag("Items") is None:
        # for non-parametrized usages we need to take care of the definition
        ref = templates[di.child_with_tag("Definition").attributes["href"]].attributes["uuid"]
        children.append(
            xml_dict.xml_node("Template", {"ref": ref})
        )
         
    href = di.child_with_tag("Definition").attributes["href"]
    if href not in used_template_ids:
        used_template_ids[href] = 1
    return xml_dict.xml_node(
        "Concept",
        {
            'uuid': transform_uuid(di.attributes["UniqueId"]),
            'name': templates[href].attributes["name"],
            'status': "sample",
            'override': "false"
        },
        children=children
    )
    
class failure: pass
failure = failure()

def do_try(fn, do_except=None):
    try:
        return fn()
    except:
        if do_except:
            do_except()
        return failure
    
def transform_DocTemplateItem(di, parent):
    if "RuleParameters" in di.attributes:       
        params = [p for p in di.attributes.get("RuleParameters", "").split(";") if p and do_try(lambda: parse_mvd_expr(p), lambda: print(f"Failed to parse {p}")) is not failure]
        params = ";".join(params)
        if params:
            params += ";"
            
        try:
            description = [("Description", di.child_with_tag("Documentation").text)]
        except:
            description = []
            
        return xml_dict.xml_node(
            "TemplateRule",
            dict([
                *description,
                ("Parameters", params)
            ])
        )

def transform_Items(di, parent):
    href = parent.child_with_tag("Definition").attributes["href"]
    ref = templates[href].attributes["uuid"]
    return [
        xml_dict.xml_node("Template", {"ref": ref}),
        xml_dict.xml_node("TemplateRules", {"operator": "and"})
    ]
    
def transform_Rules(di, parent):
    if parent.tag == "DocTemplateDefinition":
        tag = "Rules"
    elif parent.tag == "DocModelRuleAttribute":
        tag = "EntityRules"
    else:
        if 'DocModelRuleConstraint' in [c.tag for c in di.children]:
            tag = "Constraints"
            assert len(di.children) == 1
        else:
            tag = "AttributeRules"        
    return xml_dict.xml_node(tag)
    
def transform(di, parent=None):
    F = globals().get(f"transform_{di.tag}", do_transform_skip)
    di2 = F(di, parent)
    children = sum(map(functools.partial(transform, parent=di), di.children), [])
    if di2 is None:
        return children
    elif isinstance(di2, xml_dict.xml_node):
        # @nb changed to += still need to verify
        di2.children += children
        di2 = [di2]
    elif isinstance(di2, list):
        di2[-1].children = children
    elif children:
        # nested templates aren't supported in mvdXML, or how?
        # raise ValueError("Should be leaf")
        pass
    return di2
    
    
def create_mvd(roots):
    return [xml_dict.xml_node(
        "mvdXML",
        {
            "uuid": transform_uuid(ifcopenshell.guid.new()),
            "name": "",
            "status": "sample",
        },
        children=[xml_dict.xml_node(
            "Templates",
            children=[templates[t] for t in used_template_ids.keys()]
        ),xml_dict.xml_node(
            "Views",
            children=roots
        )]
    )]
    
    
def strip_child_rules(d):
    def inner(di):
        if di.tag == "TemplateRule" and di.children:
            di.children[:] = []
        else:
            for c in di.children:
                inner(c)
        return di
    return [inner(d[0])]
    
if __name__ == "__main__":
    import sys
    parse_templates(os.path.join(sys.argv[1], "..", "..", "..", "Templates", "Partial Templates"))
    parse_templates(os.path.join(sys.argv[1], "..", "..", "..", "Templates"))
    xml_dict.serialize(create_mvd(strip_child_rules(transform(xml_dict.read(sys.argv[1])))), sys.argv[2])
