# IfcCurveBoundedSurface

The _IfcCurveBoundedSurface_ is a parametric surface with boundaries defined by p-curves, that is, a curve which lies on the basis of a surface and is defined in the parameter space of that surface. The p-curve is a special type of a composite curve segment and shall only be used to bound a surface.
<!-- end of short definition -->

The outer boundary shall be either defined by:

* an _IfcOuterBoundaryCurve_ a closed composite curve on surface for the definition of an outer boundary, in this case the attribute _ImplicitOuter_ has to be set to FALSE, or
* an implicit boundary of the bounded surface, e.g. the u1, u2, v1, v2 of _IfcRectangularTrimmedSurface_, in this case the attribute _ImplicitOuter_ has to be set to TRUE.

> NOTE Some surfaces, like _IfcCylindricalSurface_ does not have identifiable implicit boundaries.

> NOTE Definition according to ISO/CD 10303-42:1992
> The curve bounded surface is a parametric surface with curved boundaries defined by one or more boundary curves. One of the boundary curves may be the outer boundary; any number of inner boundaries is permissible. The region of the curve bounded surface in the basis surface is defined to be the portion of the basis surface in the direction of **_N_ x _T_** from any point on the boundary, where **N** is the surface normal and **T** the boundary curve tangent vector at this point. The region so defined shall be arcwise connected.

> NOTE Entity adapted from **curve_bounded_surface** defined in ISO 10303-42.

> HISTORY New entity in IFC4.

**Informal Propositions**

1. Each curve in the set of _Boundaries_ shall be closed.
2. No two curves in the set of _Boundaries_ shall intersect.
3. At most one of the boundary curves may enclose any other boundary curve. If an _IfcOuterBoundaryCurve_ is designated, only that curve may enclose any other boundary curve.

## Attributes

### BasisSurface
The surface to be bounded.

### Boundaries
The outer boundary of the surface.

### ImplicitOuter

