from functools import reduce
import operator
from pathlib import Path
import re
import io
import bisect

from xml.dom import minidom
from collections import defaultdict

class base(object):
    def child_with_tag_recursive(self, other):
        if self.xml.tagName == other:
            yield self
        for x in self.children:
            yield from x.child_with_tag_recursive(other)

    def __truediv__(self, other):
        return list(self.child_with_tag_recursive(other))

    def __or__(self, other):
        li = self/other
        if len(li) != 1:
            raise ValueError("%s has %d childNodes of type %s" % (self, len(li), other))
        return li[0]
    
    def traverse(self):
        if getattr(self.xml, 'tagName', '') == "packageImport":
            ip = self.resolve('importedPackage', keep_prefix=True)
            if '#' in ip:
                fn, hash = ip.split('#')
                if dc := self.doc.imports.get(fn):
                    pass
                else:
                    dc = self.doc.imports[fn] = doc(str(Path(self.doc.filename).parent / fn))
                self = dc.by_id[hash]
        yield self
        for c in self.children:
            yield from c.traverse()

class node(base):
    
    def __init__(self, xmlnode, parent, doc):
        self.xml = xmlnode
        self.parent = parent
        self.doc = doc
        self.children = []

    @property
    def text(self):
        assert len(self.xml.childNodes) == 1
        assert isinstance(self.xml.childNodes[0], minidom.Text)
        return self.xml.childNodes[0].wholeText
        
    def tags(self):    
        return dict(map(lambda t: (t.name, t.value), self/"tag"))
    
    def resolve(self, k, keep_prefix=False):
        v = self.attributes().get(k)
        if v is not None:
            return v
        href = (self | k).href
        return href if keep_prefix else href.split('#')[1]

    def attributes(self):
        return dict((k, getattr(self, k)) for k in self.xml.attributes.keys())
        
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
        
        """
        merge_default_dict = lambda acc, d: defaultdict(list, {k: acc.get(k, []) + d.get(k, []) for k in (acc.keys() | d.keys())})
        merge_nested = lambda acc, d: defaultdict(
            lambda: defaultdict(list),
            {
                k: defaultdict(
                    list,
                    {
                        kk: acc.get(k, {}).get(kk, []) + d.get(k, {}).get(kk, [])
                        for kk in (acc.get(k, {}).keys() | d.get(k, {}).keys())
                    }
                )
                for k in (acc.keys() | d.keys())
            }
        )

        self.by_id = reduce(operator.or_, (i.by_id for i in self.imports), self.by_id)
        self.by_tag = reduce(merge_default_dict, (i.by_tag for i in self.imports), self.by_tag)
        self.by_type = reduce(merge_default_dict, (i.by_type for i in self.imports), self.by_type)
        self.by_tag_and_type = reduce(merge_nested, (i.by_tag_and_type for i in self.imports), self.by_tag_and_type)
        """
    
    def locate(self, node):
        # pat = r'(?<=<)(%s[^\\/]*?xmi:idref="%s"[^\\/]*?)((?= \\/>)|(?=>))' % (node.xml.tagName, node.idref)
        # offset = next(re.finditer(pat, self.text)).span()[0]
        offset = self.text.find('id="' + (node.idref or node.id))
        line_no = bisect.bisect_left(self.linebreaks, offset)
        char = self.linebreaks[line_no] - offset
        line_no += 1
        return (line_no, char)