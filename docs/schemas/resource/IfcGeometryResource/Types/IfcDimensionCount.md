# IfcDimensionCount

The _IfcDimensionCount_ defines the dimensionality of the coordinate space. It is restricted to have the dimensionality of either 1, 2, or 3 for the purpose of this specification.
<!-- end of short definition -->

> NOTE The shape representations assigned to a geometric representation context may include geometric representation items of lower dimensionality, particularly when defining the boundary of planar surfaces as 2D cross sections for the purpose of 3D swept areas.

> NOTE Definition according to ISO/CD 10303-42:1992
> A dimension count is a positive integer used to define the coordinate space dimensionality.

> NOTE Type adapted from **dimension_count** defined in ISO 10303-42.

> HISTORY New Type in IFC1.5

## Formal Propositions

### WR1
The dimension count should be an integer between 1 and 3 NOTE: This is a further constraint by IFC, the upper limit does not exist in STEP.
