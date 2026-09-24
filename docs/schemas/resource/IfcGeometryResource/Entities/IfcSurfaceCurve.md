# IfcSurfaceCurve

An _IfcSurfaceCurve_ is a 3-dimensional curve that has additional representations provided by one or two pcurves.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A surface curve is a type of curve, that is a curve on a surface. The curve is represented as a curve (curve_3d) in three-dimensional space and possibly as a curve, corresponding to a pcurve, in the two-dimensional parametric space of a surface. The ability of this curve to reference a list of 1 or 2 pcurves enables this entity to define either a curve on a single surface, or an intersection curve which has two distinct surface associations. A `seam' on a closed surface can also be represented by this entity; in this case each associated_geometry will be a pcurve lying on the same surface. Each pcurve shall be parametrised to have the same sense as curve_3d. The surface curve takes its parametrisation directly from either curve_3d or pcurve as indicated by the attribute master representation.

> NOTE Entity adapted from **surface_curve** defined in ISO 10303-42.

> HISTORY New entity in IFC4 Add2.

**Informal Propositions**

1. Where _Curve3D_ and one or two pcurves exist they shall represent the same mathematical point set. (i.e., they shall coincide geometrically but may differ in parametrisation.)
2. The _Curve3D_ and any associated pcurves shall agree with respect to their senses.

## Attributes

### Curve3D
The curve which is the three-dimensional representation of the surface curve.

### AssociatedGeometry
A list of one or two pcurves which define the surface or surfaces associated with the surface curve. Two elements in this list indicate that the curve has two surface associations which need not be two distinct surfaces. Being a pcurve, it also associates a basis curve in the parameter space of this surface as an alternative representation of the surface curve.

### MasterRepresentation
The <em<MasterRepresentation defines the curve used to determine the unique parametrisation of the _IfcSurfaceCurve_.
The master_representation takes one of the values _Curve3D_, _PCurve_S1_ or _PCurve_S2_ to indicate a preference for the 3D curve, or the first or second pcurve, in the associated geometry list, respectively. Multiple representations provide the ability to communicate data in more than one form, even though the data is expected to be geometrically identical.

>NOTE The master representation attribute acknowledges the impracticality of ensuring that multiple forms are indeed identical and allows the indication of a preferred form. This would probably be determined by the creator of the data. All characteristics, such as parametrisation, domain, and results of evaluation, for an entity having multiple representations, are derived from the master representation. Any use of the other representations is a compromise for practical considerations.

### BasisSurface
The surface, or surfaces on which the _IfcSurfaceCurve_ lies. This is determined from the _AssociatedGeometry_ list.

## Formal Propositions

### CurveIs3D
The _Curve2D_ shall be defined in three-dimensional space.

### CurveIsNotPcurve
The _Curve3D_ shall not be a pcurve.
