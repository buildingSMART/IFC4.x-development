from functools import reduce
import operator
from pathlib import Path
import re
import io
import bisect

from xml.dom import minidom
from collections import defaultdict

class base(object):
    children: list

    def __init__(self):
        self.children = []

    def child_with_tag_recursive(self, other):
        if getattr(self.xml, 'tagName', None) == other:
            yield self
        for x in self.children:
            yield from x.child_with_tag_recursive(other)

    def child_with_tag(self, other):
        for ch in self.children:
            if getattr(ch.xml, 'tagName', None) == other:
                yield ch

    def __truediv__(self, other):
        return list(self.child_with_tag_recursive(other))

    def __or__(self, other):
        li = self/other
        if len(li) != 1:
            raise ValueError("%s has %d childNodes of type %s" % (self, len(li), other))
        return li[0]
    
    def traverse(self):
        if getattr(self.xml, 'tagName', '') == "packageImport" and '#' in self.resolve('importedPackage', full=True):
            fn, hash = self.resolve('importedPackage', full=True).split('#')
            if dc := self.doc.imports.get(fn):
                pass
            else:
                dc = self.doc.imports[fn] = doc(str(Path(self.doc.filename).parent / fn))
            self = dc.by_id[hash]
        yield self
        for c in self.children:
            yield from c.traverse()

    def attributes(self):
        return dict((k, getattr(self, k)) for k in (self.xml.attributes or {}).keys())
        
class node(base):
    
    def __init__(self, xmlnode, parent, doc):
        super().__init__()
        self.xml = xmlnode
        self.parent = parent
        self.doc = doc

    @property
    def text(self):
        assert len(self.xml.childNodes) == 1
        assert isinstance(self.xml.childNodes[0], minidom.Text)
        return self.xml.childNodes[0].wholeText
        
    def tags(self):    
        return dict(map(lambda t: (t.name, t.value), self/"tag"))
    
    def resolve(self, k, full=False):
        v = self.attributes().get(k)
        if v is not None:
            return v
        ch = [n for n in self.children if n.xml.tagName == k]
        if len(ch) == 1:
            v = ch[0].href
            if full:
                return v
            else:
                return v.split('#')[1]
        return None

    def __getattr__(self, k):
        di = (self.xml.attributes or {})
        attr = di.get(k, di.get('xmi:'+k))
        if attr: return attr.value
        else:
            if '_' in k:
                return self.__getattr__(k.replace("_", ":"))
            else:
                return None

    def __repr__(self):
        out = io.StringIO()
        self.xml.writexml(out)
        return re.sub(r"^\s+", "", out.getvalue(), flags=re.MULTILINE).split("\n")[0]


def get_encoding(fn):
    from xml.parsers import expat
    p = expat.ParserCreate()
    d = []
    p.XmlDeclHandler = lambda *args: d.extend(args)
    p.Parse(next(iter(open(fn, encoding='ascii'))) + "<dummy/>")
    return d[1]


class doc(base):
    """
    A helper class for easily navigating the DOM.
    
    Examples:
    
    doc/"connector" list of elements with connector tagName
    doc|"start" same as above but single element (this is asserted)
    doc.by_tag_and_type["element"]["uml:DataType"]
    doc.by_id[...] single element by xml:id
    
    """       
    
    def __init__(self, fn):
        self.filename = fn
        self.imports = {}
        self.xml = minidom.parse(fn)
        self.text = open(fn, encoding=get_encoding(fn)).read()
        self.linebreaks = [m.span()[0] for m in re.finditer(r'\n', self.text)]
        
        self.by_id = dict()
        
        self.by_type = defaultdict(list)
        self.by_tag_and_type = defaultdict(lambda: defaultdict(list))
        self.by_tag = defaultdict(list)
        
        def visit(n, parent=None):
            N = node(n, parent=parent, doc=self)
            for c in n.childNodes:
                if c.nodeType == c.ELEMENT_NODE:
                    N.children.append(visit(c, parent=N))
                    
            return N
        
        self.root = visit(self.xml)

        def register_by_xmi_type(n):
            t = n.type
            if t: self.by_type[t].append(n)
            
        def register_by_tag_and_xmi_type(n):
            self.by_tag[n.xml.tagName].append(n)
            t = n.type
            if t: self.by_tag_and_type[n.xml.tagName][t].append(n)
            
        def register_by_xmi_id(n):
            t = n.xmi_id
            if t and t not in self.by_id:
                # note that duplicate xmi:ids do exist e.g. for generalizations
                self.by_id[t] = n

        fns = [register_by_xmi_type,
            register_by_xmi_id,
            register_by_tag_and_xmi_type]
        
        for elem in self.root.traverse():
            if elem.xml.nodeType == elem.xml.ELEMENT_NODE:
                for fn in fns:
                    fn(elem)
                    
        self.children = [self.root]
    
    def locate(self, node):
        # pat = r'(?<=<)(%s[^\\/]*?xmi:idref="%s"[^\\/]*?)((?= \\/>)|(?=>))' % (node.xml.tagName, node.idref)
        # offset = next(re.finditer(pat, self.text)).span()[0]
        offset = self.text.find('id="' + (node.idref or node.id))
        line_no = bisect.bisect_left(self.linebreaks, offset)
        char = self.linebreaks[line_no] - offset
        line_no += 1
        return (line_no, char)