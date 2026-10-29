import hashlib
import html
import os
import re
import shutil
import subprocess

import markdown
import pydot

import bs4
def BeautifulSoup(*args, as_xml=False):
    return bs4.BeautifulSoup(*args, features='lxml-xml' if as_xml else 'lxml')

class markdown_mixin:
    structure : dict

    def get_node_type(self, n):
        try:
            n = n.replace("<br />", "")
            n = re.findall(r'Ifc\w+', n)[0]
        except:
            return "attribute"

        if n not in self.structure['entity_definitions']:
            return "attribute"

        def is_relationship(ty=n):
            if ty == "IfcRelationship" or ty == "IfcResourceLevelRelationship":
                return True
            ty = self.structure['entity_supertype'].get(ty)
            if ty:
                return is_relationship(ty)
            return False

        return "relationship" if is_relationship() else "entity"

    def transform_graph(self, current_entity, graph_data, only_urls=False):
        graphs = pydot.graph_from_dot_data(graph_data)

        # collect all node names to see if we need to insert args in cluster

        all_nodes = set()

        def collect_nodes(g):
            all_nodes.update(n.get_name() for n in g.get_nodes())
            for sg in g.get_subgraphs():
                collect_nodes(sg)

        for graph in graphs:
            collect_nodes(graph)

        # now visit graph and decorate nodes

        def visit_graph(g):
            names_seen = {}

            edge_nodes_in_cluster = set()

            for e in g.get_edges():
                edge_nodes_in_cluster.add(e.get_source())
                edge_nodes_in_cluster.add(e.get_destination())

            # add nodes to cluster that aren't explicitly declared
            # in the graph
            for n in edge_nodes_in_cluster - all_nodes:
                g.add_node(pydot.Node(n))

            for n in list(g.get_nodes()):
                nm = n.get_label() or n.get_name()

                if nm == '"\\n"':
                    # not sure where this comes from, some artefact
                    # of the pydot parsing, but it can't be reproduced
                    # consistently
                    g.del_node(n)
                    continue

                if nm in {"graph", "edge", "node"}:
                    continue

                if not only_urls:

                    if n.get_name() in names_seen:
                        # rank=same groupings otherwise cause
                        # node names to be listed twice
                        args = names_seen[n.get_name()]
                    else:
                        node_type = self.get_node_type(nm)
                        args = {
                            "shape": "box",
                            "style": "filled",
                            "penwidth": 0.2,
                            "width": 2,
                            "height": 0.5,
                            "color": "#000000",
                        }
                        if node_type == "entity":
                            args["fillcolor"] = "#1976d2"
                        elif node_type == "relationship":
                            args["fillcolor"] = "#E9D758"
                        else:
                            args["style"] = ""
                            args["shape"] = "plain"

                        # A pipe is the symbol for a table
                        if "|" in nm:
                            # Experimenting with "Mrecord" incase it looks nicer
                            args["shape"] = "record"

                        if nm.strip('"').split(" ")[0] == current_entity:
                            args["fillcolor"] = "#1976d2"
                            args["penwidth"] = "1"


                        names_seen[n.get_name()] = args

                    for kv in args.items():
                        n.set(*kv)

                if nm.startswith("Ifc"):
                    n.set("URL", self.url_for("resource", resource=nm, _external=True))

            for sg in g.get_subgraphs():
                visit_graph(sg)

        for graph in graphs:
            visit_graph(graph)

        return graph.to_string()


    def process_graphviz(self, current_entity, md):
        def is_figure(s):
            if "dot_figure" in s:
                return 1
            elif "dot_inheritance" in s:
                return 2
            elif "dot_neato" in s:
                return 3
            else:
                return 0

        is_markdown = True
        graphviz_code = list(filter(is_figure, re.findall("```(.*?)```", md or "", re.S)))
        # This is a hack to allow markdown that is already in HTML to still get diagrams generated.
        if not graphviz_code:
            is_markdown = False
            graphviz_code = filter(is_figure, re.findall("<pre><code>(.*?)</code></pre>", md or "", re.S))

        for c in graphviz_code:
            if not is_markdown:
                escaped_c = c
                c = html.unescape(c)

            layout_engine = "dot"
            if is_figure(c) == 3:
                layout_engine = "neato"

            hash = hashlib.sha256(c.encode("utf-8")).hexdigest()
            fn = os.path.join("svgs", current_entity + "_" + hash + ".dot")
            c2 = self.transform_graph(current_entity, c, only_urls=is_figure(c) == 2)
            with open(fn, "w") as f:
                f.write(c2)
            if is_markdown:
                md = md.replace("```%s```" % c, "![dot_diagram](/svgs/%s_%s.svg)" % (current_entity, hash))
            else:
                md = md.replace("<pre><code>%s</code></pre>" % escaped_c, "![](/svgs/%s_%s.svg)" % (current_entity, hash))
            subprocess.call([
                shutil.which("dot") or "dot",
                f"-K{layout_engine}",
                "-O",
                "-Tsvg",
                "-n2",
                #"-Gsize=10,8",
                "-Gbgcolor=#ffffff00",
                "-Earrowsize=0.5",
                "-Earrowhead=dot",
                fn
            ])

        return md or ""

    def process_markdown(self, resource, mdc, process_quotes=True, number_headings=False, chapter=None):
        html = markdown.markdown(self.process_graphviz(resource, mdc), extensions=["tables", "fenced_code"])

        soup = BeautifulSoup(html)

        # First h1 is handled by the template
        try:
            soup.find("h1").decompose()
        except:
            # only entities have H1?
            pass

        # Change svg img references to embedded svg because otherwise URLS are not interactive
        for img in soup.findAll("img"):
            if img["src"].endswith(".svg"):
                entity, hash = img["src"].split("/")[-1].split(".")[0].split("_")
                try:
                    svg = BeautifulSoup(open(os.path.join("svgs", entity + "_" + hash + ".dot.svg")), as_xml=True)
                    img.replaceWith(svg.find("svg"))
                    img = svg
                except FileNotFoundError:
                    # There are now also .svg figure references from markdown,
                    # these do not need to be embedded for link interactivity.
                    pass
            elif img["src"].startswith("http"):
                pass
            else:
                if img["src"] and img["src"].startswith("../../figures/examples/"):
                    img["src"] = self.url_for('get_example_figure', fig=img["src"].replace("../../figures/examples/", ""))
                else:
                    img["src"] = img["src"][9:]

        if number_headings:
            assert chapter

            headings = soup.find_all(('h3', 'h4', 'h5'))
        
            stack = list(chapter)
            orig_length = len(stack) - 2

            for h in headings:         
                level = int(h.name[1:]) + orig_length
                if level == len(stack):
                    stack[-1] += 1
                elif len(stack) < level:
                    stack += [1] * (level - len(stack))
                else:
                    stack = stack[0:level]
                    stack[-1] += 1
                
                span1 = soup.new_tag('div')
                span1['class'] = 'number'
                span1.string = ".".join(map(str, stack))

                span2 = soup.new_tag('div')
                span2.string = h.text

                h.contents = [span1, span2]

        for svg in soup.findAll("svg"):
            # Graphviz diagrams use pt, a hackish way to isolate them
            if "pt" in svg.attrs["width"]:
                svg.attrs["width"] = "%dpx" % (int(svg.attrs["width"][0:-2]) * 1)
                svg.attrs["height"] = "%dpx" % (int(svg.attrs["height"][0:-2]) * 1)

        # Tag all special notes separately. In markdown they are all lumped in a single block quote.
        for blockquote in soup.findAll("blockquote"):
            has_aside = False
            non_aside_ps = []

            for p in blockquote.findAll("p"):
                try:
                    keyword, contents = p.text.split(" ", 1)
                    keyword = keyword.strip()
                except:
                    continue
                valid_keywords = ["HISTORY", "IFC", "EXAMPLE", "NOTE", "REFERENCE"]
                has_valid_keyword = any(v in keyword for v in valid_keywords)
                if not has_valid_keyword:
                    non_aside_ps.append(p)
                    continue

                has_aside = True

                css_class = keyword.lower()
                if css_class == "ifc":
                    try:
                        keyword_2 = p.text.split(" ", 2)[1].lower()
                    except:
                        pass
                    if keyword_2 in ("addendum", "change"):
                        css_class = "change"
                    elif keyword_2 in ("deprecation",):
                        css_class = "deprecation"

                new_p = soup.new_tag('aside', attrs={'class': [f"aside-{css_class}"]})
                new_p.extend(p.contents)
                p.replace_with(new_p)
                p = new_p

                if process_quotes:
                    if keyword.startswith("IFC"):
                        # This is typically something like "IFC4 CHANGE" denoting a historic change reason
                        keyword, keyword2, contents = p.text.split(" ", 2)
                        p.contents = BeautifulSoup(str(p).replace(keyword + " " + keyword2, "")).html.body.aside.contents
                        keyword = keyword.strip()
                        keyword2 = keyword2.strip()
                        keyword = "-".join((keyword, keyword2))
                    else:
                        p.contents = BeautifulSoup(str(p).replace(keyword, "")).html.body.aside.contents

                mark = soup.new_tag("mark")
                mark.string = keyword
                
                if "deprecation" in css_class:
                    anchor = soup.new_tag("a", href=f"{self.base}/content/terms_and_definitions.html#deprecation")
                    icon = soup.new_tag("i")
                    icon["data-feather"] = "link"
                    anchor.append(icon)
                    mark.append(anchor)

                if process_quotes:
                    p.insert(0, mark)
                blockquote.insert_before(p)

            if has_aside:
                if not non_aside_ps:
                    blockquote.decompose()

        html = str(soup).replace("{{ base }}", self.base)

        return html
