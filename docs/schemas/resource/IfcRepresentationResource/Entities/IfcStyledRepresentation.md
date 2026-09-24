# IfcStyledRepresentation

The _IfcStyledRepresentation_ represents the concept of a styled presentation being a representation of a product or a product component, like material. within a representation context. This representation context does not need to be (but may be) a geometric representation context.
<!-- end of short definition -->

> NOTE Current usage of _IfcStyledRepresentation_ is restricted to the assignment of presentation information to an material. The _IfcStyledRepresentation_ includes only presentation styles (_IfcCurveStyle_, _FillAreaStyle_, _IfcSurfaceStyle_) that define how a material should be presented within a particular (eventually view and scale dependent) representation context. All instances of _IfcStyledRepresentation_ are referenced by _IfcMaterialDefinitionRepresentation_, and assigned to _IfcMaterial_ by _IfcMaterialDefinitionRepresentation.RepresentedMaterial_.

A styled representation has to include one or several styled items with the associated style information (curve, symbol, text, fill area, or surface styles). It shall not contain the geometric representation items that are styled.

> HISTORY New entity in IFC2x2.

## Formal Propositions

### OnlyStyledItems
Only _IfcStyledItem_'s (or subtypes) are allowed as members in the list of _Items_, inherited from _IfcRepresentation_.
> IFC2x3 CHANGE New where rule to ensure the usage for material definition representations, and other non-shape representations
