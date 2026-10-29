# IfcPoint

The _IfcPoint_ is the abstract generalisation of all point representations within a Cartesian coordinate system.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A point is a location in some real Cartesian coordinate space R^m^, for m = 1, 2 or 3.

> NOTE Entity adapted from **point** in ISO 10303-42.

> HISTORY New entity in IFC1.5

## Attributes

### Dim

The space dimensionality of this abstract class, handled by a function specific for concrete subtypes. Determined by the number of coordinate components in case of IfcCartesianPoint or by the dimensionality of the basis curve or surface in other cases.
