import sys

from generators.util import xml_dict
from generators.util.append_xmi import XMI

fn, ofn = sys.argv[1:]
content = xml_dict.read(fn)

def recurse(fn, nd=None, stack=None):
    if nd is None: nd = content
    if stack is None: stack = []
    
    r = fn(nd, stack)
    if r is not None:
        return r

    for ch in nd.children:
        r = recurse(fn, ch, stack + [nd])
        if r is not None:
            return r

def remove_ext(nd, stack):
    tags = [c.tag for c in nd.children]
    if XMI.Extension in tags:
        nd.children = [c for c in nd.children if c.tag != XMI.Extension]
        return 0

recurse(remove_ext)

xml_dict.serialize([content], ofn)

