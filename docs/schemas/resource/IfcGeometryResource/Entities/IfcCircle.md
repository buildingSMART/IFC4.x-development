# IfcCircle

An _IfcCircle_ is a curve consisting of a set of points having equal distance from the center.
<!-- end of short definition -->

> NOTE A circular arc segment is defined by using the _IfcTrimmedCurve_ with _BasisCurve_ being an _IfcCircle_.

Figure 1 illustrates the definition of _IfcCircle_ within a three-dimensional position coordinate system placed within the object coordinate system of an element.

![axis1 placement](../../../../figures/ifccircle-layout1.gif "Figure 1 — Circle layout")



> REFERENCE Definition according to ISO/CD 10303-42:1992

A circle is defined by a radius and the location and orientation of the circle. Interpretation of data should be as follows:

```
C = SELF\IfcConic.Position.Location
x = SELF\IfcConic.Position.P[1]
y = SELF\IfcConic.Position.P[2]
z = SELF\IfcConic.Position.P[3]
R = Radius
```

The circle is parameterized as

$$ \lambda(u) = C + R(\cos(u)x + \sin(u)y) $$

The parameterization range is 0 ≤ _u_ ≤ 2π (0 ≤ _u_ ≤ 360 degree).
In the placement coordinate system defined above, the circle is the equation _C_ = 0, where


$$ C(x,y,z) = x^2 + y^2 - R^2 $$

The positive sense of the circle at any point is in the tangent direction, **T**, to the curve at the point, where

$$ T = (-C_y,C_x,0) $$

> HISTORY New entity in IFC1.0

## Attributes

### Radius
The radius of the circle, which shall be greater than zero.
