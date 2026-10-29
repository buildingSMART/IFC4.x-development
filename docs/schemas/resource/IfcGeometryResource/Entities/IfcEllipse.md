# IfcEllipse

An _IfcEllipse_ is a curve consisting of a set of points whose distances to two fixed points add to the same constant.
<!-- end of short definition -->

The inherited _SELF\IfcConic.Position.Location_ is the center of the _IfcEllipse_, and the inherited _SELF\IfcConic.Position.P[1]_ is the direction of the _SemiAxis1_.

![ellipse](../../../../figures/ifcellipse-layout1.gif)

Figure 1 — Ellipse placement and parameterization

Definition of the <em>IfcEllipse</em> within the a three-dimensional position coordinate system is shown in Figure 1.

It is placed within the object coordinate system of an element of which it is a
representation.

> NOTE An elliptical arc segment is defined by using the _IfcTrimmedCurve_ with _BasisCurve_ being an _IfcEllipse_.

> REFERENCE Definition according to ISO/CD 10303-42:1992

An ellipse is a conic section defined by the lengths of the semi-major and semi-minor diameters and the position (center or mid point of the line joining the foci) and orientation of the curve. Interpretation of the data shall be as follows:


```
C = SELF\IfcConic.Position.Location
x = SELF\IfcConic.Position.P[1]
y = SELF\IfcConic.Position.P[2]
z = SELF\IfcConic.Position.P[3]
R1 = SemiAxis1
R2 = SemiAxis2
```

The ellipse is parameterized as:

$$ \lambda(u) = C + (R_1\cos(u))x + (R_2\sin(u))y $$

The parameterization range is 0 ≤ _u_ <≤ 2π (0 ≤ _u_ ≤ 360 degree). In the placement coordinate system defined above, the ellipse is the equation _C_ = 0, where

$$ C(x,y,z) = \frac{x^2}{R_1^2} + \frac{y^2}{R_2^2} - 1 $$

The positive sense of the ellipse at any point is in the tangent direction, T, to the curve at the point, where

$$ T = (-C_y,C_x,0) $$

> HISTORY New entity in IFC1.0

## Attributes

### SemiAxis1
The first radius of the ellipse which shall be positive. Placement.Axes[1] gives the direction of the SemiAxis1.

### SemiAxis2
The second radius of the ellipse which shall be positive.
