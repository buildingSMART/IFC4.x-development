python3 extract_concepts_from_xmi.py ../schemas/ifc4x3_add2.uml
python3 to_pset.py ../schemas/ifc4x3_add2.uml psd
python3 parse_xmi.py ../schemas/ifc4x3_add2.uml
python3 -m generators.express ../schemas/ifc4x3_add2.uml -o IFC.exp
python3 -m generators.xsd IFC.exp IFC.xsd
python3 change_log.py ..
python3 parse_examples.py ..
python3 templates_to_mvdxml.py IFC4.3.mvdxml
python3 determine_mvd_scope.py IFC.exp IFC4.3.mvdxml
python3 translate.py build-cache
