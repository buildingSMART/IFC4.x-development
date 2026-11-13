import os
import re
import sys
import html
import shutil
import operator

from collections import namedtuple, defaultdict

import html2text
import tabulate

from generators.util.xmi_document import xmi_document

try:
    fn = sys.argv[1]
    output = sys.argv[2]
except:
    print("Usage: python to_markdown.py <schema.xml> <output_dir>", file=sys.stderr)
    exit()

if os.path.exists(output):
    shutil.rmtree(output)
    
os.makedirs(output)

xdoc = xmi_document(fn)

def format(s, cell=False):
    h2t = html2text.HTML2Text()
    S = s.replace('\n', '<br>').replace("$inet://", "").replace("../../../../../../", "../")
    if cell:
        h2t.body_width = 0
        S = S.replace('<br>', '')
    return h2t.handle(S)

for item in xdoc:
    if item.type not in {"PSET", "FUNCTION", "RULE"}:
        mdfn = os.path.join(output, item.name[3], item.name + ".md")
        if not os.path.exists(os.path.dirname(mdfn)):
            os.makedirs(os.path.dirname(mdfn))
        
        with open(mdfn, 'w', encoding='utf-8') as f:
    
            print(item.name, file=f)
            print('=' * len(item.name), file=f)
            if item.documentation is not None:
                print(format(item.documentation), file=f)
                
            if item.children:
            
                attrs = [(c.name, format(c.documentation or '', cell=True)) for c in item.children]
            
                print("Attribute definitions", file=f)
                print("---------------------", file=f)
                print(tabulate.tabulate(attrs, headers=['Attribute', 'Description'], tablefmt="github"), file=f)
                print(file=f)
