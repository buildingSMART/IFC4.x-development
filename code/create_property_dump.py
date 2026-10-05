import glob
import operator

from generators.util import xml_dict

from generators.util.xmi_document import xmi_document

NS_QTO = "http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd"

def format_TypePropertySingleValue(prop):
    try:
        return prop.children[0].attributes["type"]
    except KeyError as e:
        return ""

def format_TypePropertyEnumeratedValue(prop):
    return " ".join(map(operator.attrgetter("text"), prop.children[0].children))

def format_TypePropertyTableValue(prop):
    return "/".join((
        prop.child_with_tag("DefinedValue").children[0].attributes["type"],
        prop.child_with_tag("DefiningValue").children[0].attributes["type"]
    ))

def format_TypePropertyReferenceValue(prop):
    return prop.attributes["reftype"]

def format_TypePropertyListValue(prop):
    return prop.children[0].children[0].attributes["type"]

def format_TypeComplexProperty(prop):
    return " ".join(map(lambda n: n.child_with_tag("Name").text, prop.children))

format_TypePropertyBoundedValue = format_TypePropertySingleValue

def get_property_definitions():
    for fn in glob.glob("../reference_schemas/psd/Pset_*.xml"):
        xd = xml_dict.read(fn)
        pset = xd.child_with_tag("Name").text
        
        for prop in xd.child_with_tag("PropertyDefs").children:
            pname = prop.child_with_tag("Name").text
            
            try:
                pdef = prop.child_with_tag("Definition").text
            except:
                pdef = "-"
            
            proptypenode = prop.child_with_tag('PropertyType').children[0]
            proptype = proptypenode.tag
            proptypeargs = globals()[f"format_{proptype}"](proptypenode)
            proptypeifc = f"Ifc{proptype[4:]}"
            
            yield pname, pset, proptypeifc, proptypeargs, pdef

    for fn in glob.glob("../reference_schemas/psd/Qto_*.xml"):
        xd = xml_dict.read(fn)
        qset = xd.child_with_tag(f'{{{NS_QTO}}}Name').text
        
        for prop in xd.child_with_tag(f'{{{NS_QTO}}}QtoDefs').children:
            qname = prop.child_with_tag(f'{{{NS_QTO}}}Name').text
            qtype = prop.child_with_tag(f'{{{NS_QTO}}}QtoType').text
            try:
                qdef = prop.child_with_tag(f'{{{NS_QTO}}}Definition').text
            except:
                qdef = "-"
        
            yield qname, qset, "Quantity", qtype, qdef

    xmi_doc = xmi_document("../schemas/IFC.xml")
    for item in xmi_doc:
        if item.type == "ENTITY":
            for nm, df in item.definition.attributes:
                yield nm, item.name, 'ATTRIBUTE', df, ''

if __name__ == "__main__":
    import xlsxwriter
    
    workbook = xlsxwriter.Workbook("properties_by_name.xlsx")
    header_format = workbook.add_format({'bg_color': 'black', 'font_color': 'white'})
    
    worksheet = workbook.add_worksheet("Properties")
    
    worksheet.write(0, 0, "name", header_format)
    worksheet.write(0, 1, "pset name / entity", header_format)
    worksheet.write(0, 2, "type", header_format)
    worksheet.write(0, 3, "type arguments", header_format)
    worksheet.write(0, 4, "definition", header_format)
    
    for i, row in enumerate(sorted(get_property_definitions())):
        for j, cell in enumerate(row):
            worksheet.write(i+1, j, cell)
            
    workbook.close()