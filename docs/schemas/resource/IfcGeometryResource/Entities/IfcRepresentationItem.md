# IfcRepresentationItem

The _IfcRepresentationItem_ is used within an _IfcRepresentation_ (directly or indirectly through other _IfcRepresentationItem_'s) to represent an _IfcProductRepresentation_. Most commonly these _IfcRepresentationItem_'s are geometric or topological representation items, that can (but not need to) have presentation style information assigned.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-43:1992
> A representation item is an element of product data that participates in one or more representations or contributes to the definition of another representation item. A representation item contributes to the definition of another representation item when it is referenced by that representation item.

> NOTE The assignment of a style is only applicable to the subtypes _IfcGeometricRepresentationItem_, _IfcMappedItem_ and some selected subtypes of _IfcTopologicalRepresentationItem_ (_IfcVertexPoint_, _IfcEdgeCurve_, _IfcFaceSurface_).

In case that presentation style information is applied, it can be either applied by an _IfcStyledItem_, or by an assignment to an _IfcPresentationLayerWithStyle_. If both are present, and both style assignments include the same subtype of _IfcPresentationStyle_, then the style assigned by _IfcStyledItem_ takes priority.

Figure 1 shows an instance diagram explaining the use of _IfcStyledItem_ and _IfcPresentationLayerWithStyle_ to apply presentation styles.

> EXAMPLE The assignment of style information by a styled item and a presentation layer with style. Since the presentation styles are different, _IfcCurveStyle_ and _IfcSurfaceStyle_, both are applied to the geometric representation item.

![styles assigned by layer and styled item](../../../../figures/ifcrepresentationitem_style-1.png)

Figure 1 — Representation item style

Figure 2 shows in instance diagram explaining the override of _IfcPresentationLayerWithStyle_ by _IfcStyledItem_ to apply presentation styles.

> EXAMPLE The assignment of style information by a styled item and a presentation layer with style. Since the presentation styles for curve style are aprovided by both, the _IfcCurveStyle_ provided by the _IfcStyledItem_ overrides the _IfcCurveStyle_ provided by the _IfcPresentationLayerWithStyle_

![styles assigned by layer and styled item](../../../../figures/ifcrepresentationitem_style-2.png)

Figure 2 — Representation item style override

> NOTE Entity adapted from **representation_map** defined in ISO 10303-43.

> HISTORY New entity in IFC2x.

> IFC2x3 CHANGE The inverse attributes _StyledByItem_ and _LayerAssignments_ have been added. Upward compatibility for file based exchange is guaranteed.

## Attributes

### LayerAssignment
Assignment of the representation item to a single or multiple layer(s). The _LayerAssignments_ can override a _LayerAssignments_ of the _IfcRepresentation_ it is used within the list of _Items_.
> IFC2x3 CHANGE The inverse attribute _LayerAssignments_ has been added.

> IFC4 CHANGE The inverse attribute _LayerAssignment_ has been restricted to max 1. Upward compatibility for file based exchange is guaranteed.

### StyledByItem
Reference to the _IfcStyledItem_ that provides presentation information to the representation, e.g. a curve style, including colour and thickness to a geometric curve.

> IFC2x3 CHANGE The inverse attribute _StyledByItem_ has been added.
