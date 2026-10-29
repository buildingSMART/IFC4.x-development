import os
import re

import itertools

from dataclasses import dataclass, field

import markdown

import bs4
def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features='lxml')

@dataclass
class markdown_section:
    level : int
    heading : str
    content : str
    first_node_content : str
    children : list = field(default_factory=list)
    
def parse_document(*, fn=None, data=None, linesep="", as_text=True):
    if fn:
        data = open(fn, encoding="utf-8").read()
    else:
        assert data

    soup = BeautifulSoup(
        markdown.markdown(data,
        extensions=['tables', 'fenced_code', 'sane_lists'])
    )

    if not soup.h1:
        # In a recent PR most of the top-level headings were removed
        # from the Markdown documents, but the code here still relies
        # on them for building the document tree, because parsing
        # happens based on the various headings and their number.
        if soup.body is None:
            return markdown_section(1, '', '', '', [])
        first = next(soup.body.children)
        first.insert_before(soup.new_tag('h1', 'DocumentRoot'))

    
    headings = soup.find_all(re.compile(r"h\d"))
    next_heading = headings[1:] + [None]
    
    root = None
    stack = [None]

    for h, next_h in zip(headings, next_heading):
        nodes = (n for n in h.nextSiblingGenerator())
        selected = itertools.takewhile(lambda n: next_h is None or n != next_h, nodes)
        concat = ""
        first = ""
        if as_text:
            strings = list(filter(None, map(lambda n: getattr(n, 'text', '').strip(), selected)))
            concat = linesep.join(strings)
            first = strings[0] if strings else ""
        else:
            selected = list(selected)
            if selected:
                concat = "".join(map(str, selected))
                first = str(selected[0])
        
        section = markdown_section(int(h.name[1:]), h.text, concat, first)
        if section.level == len(stack):
            stack.append(None)
        elif section.level == len(stack) - 1:
            pass
        else:
            stack[section.level:] = [None]
            
        stack[-1] = section
        try:
            if stack[-2] is not None:
                stack[-2].children.append(section)
        except:
            print(fn)
            return None
        
        if root is None:
            root = section
            
    return root

class markdown_attribute_parser:
    def __init__(self, *, fn=None, data=None, as_text=True, heading_name="Attributes", short=False, linesep=""):
    
        self.heading_name = heading_name
        self.root = parse_document(fn=fn, data=data, as_text=as_text, linesep=linesep)
        self.children = {}
        self.status = {}
        self.short = short
        
    def definition(self, short=False):
        if self.root is None:
            self.status["DEFINITION"] = ("NO_CONTENT", -1)
            return
            
        return self.root.first_node_content if short else self.root.content
        
    def __iter__(self):
        children = self.root.children if self.root else []
        cs = [c for c in children if c.heading == self.heading_name]
        if len(cs) != 1:
            self.status["ALL"] = ("NO_HEADING", -1)
            return
        
        for section in cs[0].children:
            name = section.heading

            if len(section.content.strip()) == 0:
                self.status[name] = ("NO_CONTENT", 0)
            else:
                self.status[name] = ("OK", 0)

            m = re.search(r"\[([\w\- ]+)\]", name)
            if m:
                mvd = m.group(1)
                li = [c for c in name]
                li[slice(*m.span())] = []
                name = (mvd, "".join(li).strip())
                
            self.children[name] = section.children
                
            yield name, section.first_node_content if self.short else section.content

    def get_children(self, name):
        children = self.root.children if self.root else []
        cs = [c for c in children if c.heading == self.heading_name]
        if len(cs) != 1:
            return
        for section in cs[0].children:
            section_name = section.heading
            if section_name == name:
                return {c.heading: c.content for c in section.children}
            
if __name__ == "__main__":
    import tabulate
    fn = os.path.join(os.path.dirname(__file__), "../docs/schemas/resource/IfcActorResource/Entities/IfcActorRole.md")
    mdp = markdown_attribute_parser(fn=fn, as_text=True, short=True)
    print(mdp.definition(short=True))
    print(tabulate.tabulate(list(mdp)))
    
    
