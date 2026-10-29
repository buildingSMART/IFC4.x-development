# IfcConnectionPointGeometry

_IfcConnectionPointGeometry_ is used to describe the geometric constraints that facilitate the physical connection of two objects at a point (here _IfcCartesianPoint_) or at an vertex with point coordinates associated. It is envisioned as a control that applies to the element connection relationships.
<!-- end of short definition -->

> EXAMPLE The connection relationship between two path based elements (like a column and a beam) has a geometric constraint which describes the connection points by a _PointOnRelatingElement_ for the column and a _PointOnRelatedElement_ for the beam. The exact usage of the _IfcConnectionPointGeometry_ is further defined in the geometry use sections of the elements that use it.

The _IfcPoint_ (or the _IfcVertexPoint_ with an associated _IfcPoint_) at the _PointOnRelatingElement_ attribute defines the point where the basic geometry items of the connected elements connect. The point coordinates are provided within the local coordinate system of the _RelatingElement_, as specified at the _IfcRelConnects_ subtype that utilizes the _IfcConnectionPointGeometry_. Optionally, the same point coordinates can also be provided within the local coordinate system of the _RelatedElement_ by using the _PointOnRelatedElement_ attribute. If both point coordinates are not identical within a common parent coordinate system (ultimately within the world coordinate system), the subtype _IfcConnectionPointEccentricity_ shall be used.

> NOTE If the point connection has an offset (if the two points or vertex points at the relating and related element do not physically match), the subtype _IfcConnectionPointEccentricity_ shall be used.

> HISTORY New entity in IFC1.5.

> IFC2x CHANGE Renamed from IfcPointConnectionGeometry.

> IFC2x3 CHANGE The provision of topology with associated geometry, _IfcVertexPoint_, is enabled by using the _IfcPointOrVertexPoint_.

## Attributes

### PointOnRelatingElement
Point at which the connected object is aligned at the relating element, given in the LCS of the relating element.

### PointOnRelatedElement
Point at which connected objects are aligned at the related element, given in the LCS of the related element. If the information is omitted, then the origin of the related element is used.
