# IfcBSplineCurve

The _IfcBSplineCurve_ is a spline curve parameterized by spline functions.
<!-- end of short definition -->

Figure 1 illustrates a B-spline curve.

> NOTE Figure quoted from ISO 10303-42.

![control points](../../../../figures/ifcbsplinecurve-fig1.gif "Figure 1 — B-spline curve")

> NOTE Definition according to ISO/CD 10303-42:1992

A B-spline curve is a piecewise parametric polynomial or rational curve described in terms of control points and basis functions. The B-spline curve has been selected as the most stable format to represent all types of polynomial or rational parametric curves. With appropriate attribute values it is capable of representing single span or spline curves of explicit polynomial, rational, Bezier or B-spline type.

![equation1](../../../../figures/ifcbsplinecurve-math1.gif)

Figure 2 - Equation 1

![equation2](../../../../figures/ifcbsplinecurve-math2.gif)

Figure 3 - Equation 2

Variable | Definition
---|---
k+1 | Number of control points
P<sub>i</sub> | Control points
w<sub>i</sub> | Weights
d | Degree

Table 4 - Variable definitions

Interpretation of the data is as follows:

 1. All weights shall be positive and the curve is given by Figure 2, with variables defined in Table 4. The knot array is an array of (<em>k</em>+<em>d</em>+2) real numbers
[<em>u</em><sub>-<em>d</em></sub> ... <em>u</em><sub><em>k</em>+1</sub>], such that for all indices j in
[-<em>d</em>,<em>k</em>], <em>u</em><sub>j</sub> <= <em>u</em><sub>j+1</sub>. This array is obtained from the knot
data list by repeating each multiple knot according to the multiplicity. <em>N <sup>d</sup><sub>i</sub></em>, the
<em>i</em>th normalized B-spline basis function of degree <em>d</em>, is defined on the subset
[<em>u<sub>i-d</sub></em>, ... , <em>u<sub>i+1</sub></em>] of this array.</p>
 2. Let <em>L</em> denote the number of distinct values among the <em>d</em>+<em>k</em>+2
knots in the knot array; <em>L</em> will be referred to as the 'upper index on knots'. Let <em>m<sub>j</sub></em>
denote the multiplicity (number of repetitions) of the <em>j</em>th distinct knot. Then see Figure 3. All knot multiplicities except the first and the last shall be in the range 1 ... degree; the first and last may have a maximum value of degree + 1. In evaluating the basis functions, a knot <em>u</em> of e.g. multiplicity 3 is interpreted as a string <em>u, u, u,</em> in the knot array. The B-spline curve has 3 special
subtypes (<em>Note: only 1, Bezier curve, included in this IFC release</em>) where the knots and knot multiplicities are derived to provide simple default capabilities.</p>
 3. Logical flag is provided to indicate whether the curve self intersects or not.

> NOTE Entity adapted from **b_spline_curve** defined in ISO10303-42.

> HISTORY New entity in IFC2x2.

## Attributes

### Degree
The algebraic degree of the basis functions.

### ControlPointsList
The list of control points for the curve.

### CurveForm
Used to identify particular types of curve; it is for information only.

### ClosedCurve
Indication of whether the curve is closed; it is for information only.

### SelfIntersect
Indication whether the curve self-intersects or not; it is for information only.

### UpperIndexOnControlPoints
The upper index on the array of control points; the lower index is 0.
This value is derived from the control points list.

### ControlPoints
The array of control points used to define the geometry of the curve. This is derived from the list of control points.

## Formal Propositions

### SameDim
All control points shall have the same dimensionality.
