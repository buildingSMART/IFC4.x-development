# IfcBSplineSurface

The _IfcBSplineSurface_ is a general form of rational or polynomial parametric surface.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A b_spline_surface is a general form of rational or polynomial parametric surface which is represented by control points, basis functions, and possibly, weights. As with the corresponding curve entity it has some special subtypes where some of the data can be derived.

The symbology used here is:

Variable | Definition
--- | ---
<em>K</em>1 | upper_index_on_u_control_points
<em>K</em>2 | upper_index_on_v_control_points
<b>P</b><sub>ij</sub> | control_points
w<sub>ij</sub> | weights
<em>d</em>1 | u_degree
<em>d</em>2</td> | v_degree

The control points are ordered as: P<sub>00</sub>, P<sub>01</sub>, P<sub>02</sub>, ..., P<sub><em>K</em>1(<em>K</em>2-1)</sub>, P<sub><em>K</em>1<em>K</em>2</sub>

The weights, in the case of the rational subtype, are ordered similarly.

For each parameter, <em>s</em> = <em>u</em> or <em>v</em>, if <em>k</em> is the upper
index on the control points and <em>d</em> is the degree for <em>s</em>, the knot array is an array of (<em>k</em> +
<em>d</em> + 2) real numbers [s<sub>-d</sub>, ...., s<sub><em>k</em>+1</sub>], such that for all indices j in
[-<em>d</em>, <em>k</em>]; <em>s</em><sub><em>j</em></sub> ≤ <em>s</em><sub><em>j</em>+1</sub>. This array is
obtained from the appropriate u_knots or v_knots list by repeating each multiple knot according to the
multiplicity.<br>
<br>
N<sub><em>i</em></sub><sup><em>d</em></sup>, the <em>i</em>th normalised B-spline basis function of degree <em>d</em>,
is defined on the subset [<em>s</em><sub>i-<em>d</em></sub>, ...., <em>s</em><sub><em>i</em>+1</sub>] of this
array.

Let <em>L</em> denote the number of distinct values amongst the knots in the knot list;
<em>L</em> will be referred to as the ‘upper index on knots’. Let <em>m</em><sub><em>j</em></sub> denote
the multiplicity (i.e., number of repetitions) of the <em>j</em>th distinct knot value. Then:

![formula](../../../../figures/ifcbsplinecurve-math2.gif)

All knot multiplicities except the first and the last shall be in the range 1, ...., <em>d</em>; the first and last may have a maximum value of <em>d</em>+1. In evaluating the basis functions, a knot <em>u</em> of, e.g., multiplicity 3 is interpreted as a sequence <em>u</em>, <em>u</em>, <em>u</em>, in the knot array.

The surface form is used to identify specific quadric surface types (which shall have degree two), ruled surfaces and surfaces of revolution. As with the b-spline curve, the surface form is informational only and the spline data takes precedence.

The surface is to be interpreted as follows: In the polynomial case the surface is
given by the equation:

![formula](../../../../figures/ifcbsplinesurface-math1.gif)

In the rational case the surface equation is:

![formula](../../../../figures/ifcbsplinesurface-math2.gif)

> NOTE Entity adapted from **b_spline_surface** defined in ISO10303-42.

> HISTORY New entity in IFC4.

## Attributes

### UDegree
Algebraic degree of basis functions in _u_.

### VDegree
Algebraic degree of basis functions in _v_.

### ControlPointsList
This is a list of lists of control points.

### SurfaceForm
Indicator of special surface types.

### UClosed
Indication of whether the surface is closed in the _u_ direction; this is for information only.

### VClosed
Indication of whether the surface is closed in the _v_ direction; this is for information only.

### SelfIntersect
Flag to indicate whether, or not, surface is self-intersecting; this is for information only.

### UUpper
Upper index on control points in _u_ direction.

### VUpper
Upper index on control points in _v_ direction.

### ControlPoints
Array (two-dimensional) of control points defining surface geometry. This array is constructed from the control points list.
