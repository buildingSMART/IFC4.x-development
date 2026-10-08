# IfcConstraintsParamBSpline

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This function checks the parametrisation of a B-spline curve or (one of the directions of) a B-spline surface and returns TRUE if no inconsistencies are found. These constraints are: > 1. Degree ≤ 1.
> 2. Upper index on knots ≤ 2.
> 3. Upper index on control points ≤ degree.
> 4. Sum of knot multiplicities = degree + (upper index on control points) + 2.
> 5. For the first and last knot the multiplicity is bounded by 1 and (degree+1).
> 6. For all other knots the knot multiplicity is bounded by 1 and degree.
> 7. The consecutive knots are increasing in value.

> NOTE Function adapted from **constraints_param_b_spline** defined in ISO 10303-42.

> HISTORY New function in IFC4
