# IfcDirection

The _IfcDirection_ provides a direction in two or three dimensional space depending on the number of _DirectionRatio_'s provided. The _IfcDirection_ does not imply a vector length, and the direction ratios does not have to be normalized.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This entity defines a general direction vector in two or three dimensional space. The actual magnitudes of the components have no effect upon the direction being defined, only the ratios X:Y:Z or X:Y are significant.

> NOTE The components of this entity are not normalized. If a unit vector is required it should be normalized before use.

> NOTE Entity adapted from **direction** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0

## Attributes

### DirectionRatios
The components in the direction of X axis (DirectionRatios[1]), of Y axis (DirectionRatios[2]), and of Z axis (DirectionRatios[3])

### Dim
The space dimensionality of this class, defined by the number of real in the list of DirectionRatios.

## Formal Propositions

### MagnitudeGreaterZero
The magnitude of the direction vector shall be greater than zero.
