# imports the deprecation status from IfcDoc dump

import os
import sys
import glob
import json

from generators.util import xml_dict

dr = sys.argv[1]
xmls = os.path.join(dr, "IFC4x3", "Sections", "**", "*.xml")

statusses = set()
deprecated = []

for xml in glob.glob(xmls, recursive=True):
    doc = xml_dict.read(xml)
    st = doc.attributes.get("Status", None)
    statusses.add(st)
    if st == "Deprecated":
        deprecated.append(doc.attributes["Name"])
    
print("Available status types")
print("----------------------")

print(*statusses)
print()

print("Deprecated types")
print("----------------")

print(json.dumps(deprecated))
print()
