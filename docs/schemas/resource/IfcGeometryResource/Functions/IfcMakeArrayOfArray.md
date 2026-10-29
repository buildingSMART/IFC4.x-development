# IfcMakeArrayOfArray

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This function make array of array builds an array of arrays from a list of lists. The function first checks that the specified array dimensions are compatible with the sizes of the lists, and in particular, verifies that all the sub-lists contain the same number of elements. A null result is returned if the input data is incompatible with the dimensions. This function is used to construct the arrays of control points and weights for a B-spline surface.

> NOTE Function adapted from **make_array_of_array** defined in ISO 10303-42.

> HISTORY New function in IFC4
