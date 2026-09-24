# IfcPlane

The planar surface is an unbounded surface in the direction of _x_ and _y_. Bounded planar surfaces are defined by using a subtype of _IfcBoundedSurface_ with _BasisSurface_ being a plane.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A plane is an unbounded surface with a constant normal. A plane is defined by a point on the plane and the normal direction to the plane. The data is to be interpreted as follows: <pre>
  C = Position.Location
  x = Position.P[1]
  y = Position.P[2]
  z = Position.P[3] => normal to plane
</pre> and the surface is parameterized as:
>> ![formula](../../../../figures/ifcplane-math1.gif.gif)
> where the parametric range is -∞ < _u,v_ < ∞. In the above parameterization the length unit for the unit vectors **x** and **y** is derived from the context of the plane.

> NOTE A rectangular bounded planar surface can be defined by an _IfcRectangularTrimmedSurface_ with _BasisSurface_ being the plane and _U1_ = left bound in **x**, _U2_ = right bound in **x**, _V_1 = lower bound in **y**, _V2_ = upper bound in **y** if viewed into the direction of the negative normal. (assuming the _Usense_ and _Vsense_ agree to the sense of the basis surface).

The inherited attributes are interpreted as

* _SELF\IfcElementarySurface.Position_ defines the location and orientation of the planar surface.
* _SELF\IfcElementarySurface.Position.Location_ defines a point on the planar surface.
* _SELF\IfcElementarySurface.Position.P[3]_ defines the normal of the planar surface.

> NOTE Entity adapted from **plane** in ISO 10303-42.

> HISTORY New entity in IFC1.5
