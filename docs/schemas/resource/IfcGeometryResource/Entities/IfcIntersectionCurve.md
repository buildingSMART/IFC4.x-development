# IfcIntersectionCurve

An _IfcIntersectionCurve_ is a 3-dimensional curve that has two additional representations provided by two pcurves defined within two distinct and intersecting surfaces.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An intersection curve is a type of surface curve, which results from the intersection of two surfaces. It is represented as a special subtype of the surface curve entity having two distinct surface associations defined via the associated geometry list.

> NOTE Entity adapted from **intersection_curve** defined in ISO 10303-42.

> HISTORY New entity in IFC4 Add2.

## Formal Propositions

### TwoPCurves
The intersection curve shall have precisely two associated geometry elements.

### DistinctSurfaces
The two associated geometry elements shall be related to distinct surfaces. These are the surfaces which define the intersection curve.
