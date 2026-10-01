# IfcPointOnCurve

The _IfcPointOnCurve_ is a point defined by a parameter value of its defining curve.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A point on curve is a point which lies on a curve. The point is determined by evaluating the curve at a specific parameter value. The coordinate space dimensionality of the point is that of the basis curve.

> NOTE Entity adapted from **point_on_curve** in ISO 10303-42.

> HISTORY New entity in IFC2x2.

**Informal Propositions**

1. The value of the point parameter shall not be outside the parametric range of the curve.

## Attributes

### BasisCurve
The curve to which point parameter relates.

### PointParameter
The parameter value of the point location.
