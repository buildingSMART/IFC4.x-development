# IfcMaterialList

_IfcMaterialList_ is a list of the different materials that are used in an element.
<!-- end of short definition -->

> NOTE The class _IfcMaterialList_ will normally be used where an element is described at a more abstract level. For example, for an architectural specification writer, the only information that may be needed about a concrete column is that it contains concrete, reinforcing steel and mild steel ligatures. It shall not be used for elements consisting of material layers when the different layers can be defined and the class _IfcMaterialLayerSet_ can be used. Also, _IfcMaterialList_ shall not be used for elements consisting of a single identifiable material (for example, to represent anisotropic material).

> IFC4 CHANGE  The entity _IfcMaterialList_ is deprecated and shall no longer be used. Use _IfcMaterialConstituentSet_ instead.

## Attributes

### Materials
Materials used in a composition of substances.
