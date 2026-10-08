# IfcBSplineSurfaceWithKnots

The _IfcBSplineSurfaceWithKnots_ is a general form of rational or polynomial parametric surface in which the knot values are explicitly given.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This is a B-spline surface in which the knot values are explicitly given. This subtype shall be used to represent non-uniform B-spline surfaces, and may also be used for other knot types.
> All knot multiplicities except the first and the last shall be in the range 1,....,_d_; the first and last may have a maximum value of _d_ + 1. In evaluating the basis functions, a knot _u_ of, e.g., multiplicity 3 is interpreted as a sequence _u_, _u_, _u_, in the knot array.

> NOTE Entity adapted from **b_spline_surface_with_knots** defined in ISO10303-42.

> HISTORY New entity in IFC4.

## Attributes

### UMultiplicities
The multiplicities of the knots in the _u_ parameter direction.

### VMultiplicities
The multiplicities of the knots in the _v_ parameter direction.

### UKnots
The list of the distinct knots in the _u_ parameter direction.

### VKnots
The list of the distinct knots in the _v_ parameter direction.

### KnotSpec
The description of the knot type.

### KnotVUpper
The number of distinct knots in the _v_ parameter direction.

### KnotUUpper
The number of distinct knots in the _u_ parameter direction.

## Formal Propositions

### UDirectionConstraints
The function returns TRUE when the parameter constraints are verified for the _u_ direction.

### VDirectionConstraints
The function returns TRUE when the parameter constraints are verified for the _v_ direction.

### CorrespondingULists
The number of _UMultiplicities_ shall be the same as the number of _UKnots_.

### CorrespondingVLists
The number of _VMultiplicities_ shall be the same as the number of _VKnots_.
