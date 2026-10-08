# IfcSurface

An _IfcSurface_ is a 2-dimensional representation item positioned in 3-dimensional space. 2-dimensional means that each point at the surface can be defined by a 2-dimensional coordinate system, usually by u and v coordinates.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A surface can be envisioned as a set of connected points in 3-dimensional space which is always locally 2-dimensional, but need not be a manifold.

> NOTE Entity adapted from **surface** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5

**Informal Propositions**

1. A surface has non zero area.
2. A surface is arcwise connected.

## Attributes

### Dim
The space dimensionality of IfcSurface. It is always a three-dimensional geometric representation item.
> IFC4 CHANGE Derived attribute promoted from subtypes.
