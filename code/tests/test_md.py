from generators.util.md import markdown_attribute_parser


def test_sibling_paragraphs_are_separated_by_a_space():
    mdp = markdown_attribute_parser(data="# IfcX\n\nA need.\n\nHISTORY: IFC4 removed it.\n")
    assert mdp.definition() == "A need. HISTORY: IFC4 removed it."
