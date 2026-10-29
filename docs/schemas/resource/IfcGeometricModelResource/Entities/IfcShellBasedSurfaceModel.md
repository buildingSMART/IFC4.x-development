# IfcShellBasedSurfaceModel

An _IfcShellBasedSurfaceModel_ represents the shape by a set of open or closed shells. The connected faces within the shell have a dimensionality 2 and are placed in a coordinate space of dimensionality 3.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A shell based surface model is described by a set of open or closed shells of dimensionality 2. The shells shall not intersect except at edges and vertices. In particular, distinct faces may not intersect. A complete face of one shell may be shared with another shell. Coincident portions of shells shall both reference the same faces, edges and vertices defining the coincident region. There shall be at least one shell. A shell may exist independently of a surface model.

> NOTE Entity adapted from **shell_based_surface_model** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. The dimensionality of the shell based surface model is 2.
2. The shells shall not overlap or intersect except at common faces, edges or vertices.

## Attributes

### SbsmBoundary


### Dim
The space dimensionality of this class, it is always 3.
