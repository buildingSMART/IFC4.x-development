# IfcOffsetCurve3D

An _IfcOffsetCurve3D_ is a curve defined by an offset in 3D space from its _BasisCurve_.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An offset curve 3d is a curve at a constant distance from a basis curve in three-dimensional space. The underlying curve shall have a well-defined tangent direction at every point. In the case of a composite curve the transition code between each segment shall be cont same gradient or cont same gradient same curvature. The offset curve at any point (parameter) on the basis curve is in the direction _V x T_ where _V_ is the fixed reference direction and _T_ is the unit tangent to the basis curve. For the offset direction to be well defined, _T_ shall not at any point of the curve be in the same, or opposite, direction as _V_.
>> NOTE The offset curve 3d may differ in nature from the basis curve; the offset of a non self- intersecting curve can be self-intersecting. Care should be taken to ensure that the offset to a continuous curve does not become discontinuous.
> The offset curve 3d takes its parameterization from the basis curve. The offset curve 3d is parameterized as:
>> ![Math](../../../../figures/ifcoffsetcurve3d-math1.gif)
> **T** is the unit tangent vector to the basis curve **C**(_u_) at parameter value _u_, and _d_ is distance. The underlying curve shall be three-dimensional.

> NOTE Entity adapted from **offset_curve_3d** defined in ISO 10303-42

> HISTORY New entity in IFC2x

**Informal Propositions**

1. At no point on the curve shall ref direction be parallel, or opposite to, the direction of the tangent vector.

## Attributes

### Distance
The distance of the offset curve from the basis curve. The distance may be positive, negative or zero.

### SelfIntersect
An indication of whether the offset curve self-intersects, this is for information only.

### RefDirection
The direction used to define the direction of the offset curve 3d from the basis curve.

## Formal Propositions

### DimIs2D
The underlying curve shall be defined in three-dimensional space.
