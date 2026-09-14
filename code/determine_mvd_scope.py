import functools
import itertools
import re

import ifcopenshell
import ifcopenshell.mvd as mvd
from ifcopenshell.express import parse as express_parse

from collections import defaultdict

W = ifcopenshell.ifcopenshell_wrapper


def run(schema_fn, mvdxml_fn, concept_subset=None, additional=None):

    entities = set()
    types = set()
    causes = defaultdict(set)

    def collect_entities(cause, ent):
        entities.add(ent)
        causes[ent].add(cause)

    def collect_entities_mvdxml(cause, rule, parent):
        if rule.tag == "EntityRule":
            collect_entities(cause, rule.attribute)

    def wrap_try(fn, default=None):
        def inner(*args):
            try:
                return fn(*args)
            except:
                return default
        return inner

    def normalize(name):
        return re.sub(r"[^a-zA-Z0-9]", "", name or "")

    # ``parse`` returns immutable concept_root objects; every concept carries
    # its fully parsed (template-reference-resolved) template. Templates are
    # deduplicated because a template may be instantiated by several roots.
    items = mvd.parse(mvdxml_fn)
    templates = []
    seen = set()
    for item in items:
        if not isinstance(item, mvd.concept_root):
            continue
        for concept in item.concepts():
            tpl = concept.template()
            key = tpl.uuid or id(tpl)
            if key in seen:
                continue
            seen.add(key)
            templates.append(tpl)

    builder = express_parse(schema_fn)
    ifcopenshell.register_schema(builder)
    S = ifcopenshell.ifcopenshell_wrapper.schema_by_name(builder.schema_name)

    concept_subset = set(concept_subset or ())

    for t in templates:
        if not t.entity:
            continue
        if normalize(t.name) not in concept_subset:
            continue

        t.traverse(functools.partial(collect_entities_mvdxml, t.name))

        if additional and (bindings := additional.get(normalize(t.name))):
            for x in set(filter(wrap_try(S.declaration_by_name), itertools.chain.from_iterable(b.values() for b in bindings))):
                collect_entities(t.name, x)

    def yield_supertypes(en):
        yield en.name()
        if en.supertype():
            yield from yield_supertypes(en.supertype())

    entities, pass1 = set(), sorted(entities)

    for en in pass1:
        decl = S.declaration_by_name(en)
        if isinstance(decl, W.entity):
            for st in yield_supertypes(decl):
                entities.add(st)
                if st != en:
                    causes[st].add(en)

    def visit_typedecl(ty, cause=None):
        if isinstance(ty, W.named_type):
            visit_typedecl(ty.declared_type(), cause=cause)
        elif isinstance(ty, W.type_declaration):
            types.add(ty.name())
            causes[ty.name()].add(cause)
        elif isinstance(ty, W.aggregation_type):
            visit_typedecl(ty.type_of_element(), cause=cause)
        elif isinstance(ty, W.entity):
            visit_entity(ty, cause=cause)
        elif isinstance(ty, W.enumeration_type):
            types.add(ty.name())
            causes[ty.name()].add(cause)
        elif isinstance(ty, W.simple_type):
            pass
        elif isinstance(ty, W.select_type):
            # @nb this is important, select types do *not* result
            # in broadening the mvd scope. Templates need explicitly
            # incorporate selected subtypes for them to be in scope.

            # causes[ty.name()].add(cause)
            # for dd in ty.select_list():
            #     visit_typedecl(dd, cause=ty.name())
            pass
        else:
            breakpoint()

    visited = set()

    def visit_entity(en, cause=None):
        if en.name() in visited:
            return
        visited.add(en.name())
        entities.add(en.name())
        causes[en.name()].add(cause)
        # print(en.name())
        for attr in en.attributes():
            # print(attr.name())
            visit_typedecl(attr.type_of_attribute(), f"{en.name()}.{attr.name()}")

    for en in list(entities):
        decl = S.declaration_by_name(en)
        visit_entity(decl)

    # for en in sorted(entities):
    #     print(en)

    return {k: sorted(filter(None, v)) for k, v in causes.items()}


if __name__ == "__main__":
    import sys
    import json

    schema_fn, mvdxml_fn = sys.argv[1:]

    with open("xmi_mvd_concepts.json", "r") as f:
        mvds = json.load(f)

    with open("xmi_concepts.json", "r") as f:
        additional = json.load(f)["GeneralUsage"]

    usage = {}
    for nm, concepts in mvds.items():
        usage[nm] = run(schema_fn, mvdxml_fn, concepts, additional)

    with open("mvd_entity_usage.json", "w") as f:
        json.dump(usage, f, indent=1)
