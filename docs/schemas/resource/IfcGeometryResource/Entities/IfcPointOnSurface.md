# IfcPointOnSurface

The _IfcPointOnSurface_ is a point defined by two parameter value of its defining surface.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A point on surface is a point which lies on a parametric surface. The point is determined by evaluating the surface at a particular pair of parameter values.

> NOTE Entity adapted from **point_on_surface** in ISO 10303-42.

> HISTORY New entity in IFC2x2.

**Informal Propositions**

1. The parametric values specified for u and v shall not be outside the parametric range of the basis surface.

## Attributes

### BasisSurface
The surface to which the parameter values relate.

### PointParameterU
The first parameter value of the point location.

### PointParameterV
The second parameter value of the point location.
