# IfcToroidalSurface

The _IfcToroidalSurface_ is a bounded elementary surface. It is constructed by completely revolving a circle around an axis line. The inherited _Position_ attribute defines the _IfcAxis2Placement3D_ and provides:

* _SELF\IfcElementarySurface.Position_: The location and orientation of the axis system for the primitive.
* _SELF\IfcElementarySurface.Position.Location_: The center of the toroidal surface.
* _SELF\IfcElementarySurface.Position.Position[3]:_ The axis of revolution of the toroidal surface
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An _IfcToroidalSurface_ is a type of elementary surface, which could be produced by revolving a circle about a line in its plane. The radius of the circle being revolved is referred to here as the _MinorRadius_ and the _MajorRadius_ is the distance from the centre of this circle to the axis of revolution. A toroidal surface is defined by the major and minor radii and the position and orientation of the surface.
>
> C = Position.Location
> x = Position.P[1]
> y = Position.P[2]
> z = Position.P[3] (axis of toroidal_surface)
> _R_ = MajorRadius
> _r_ = MinorRadius
>
>

_**σ**(u,v)_ = **C** + _(R + r_cos _v_)((cos_u_)**x** + (sin _u_))**y**) + _r_(sin_v_))**z**

where the parametrisation range is _0 ≤ u, v ≤ 360_ degrees. _u_ and _v_ are angular parameters and when numerical values are specified they shall use the current units for plane angle measure.

In the placement coordinate system defined above, the surface is represented by the equation _S_ = 0, where

> _S(x, y, z) = x^2^ + y^2^ + z^2^ -2R√(x^2^+y^2^) - r^2^ + R^2^._

The positive direction of the normal to the surface at any point on the surface is given by

> _( S~x~, S~y~, S~z~ )._

The unit normal is given by

> **N**_(u,v)_ = cos_v_((cos _u_)**x** + (sin _u_)**y**) + (sin _v_)**z**.

The sense of this normal is away from the nearest point on the circle of radius _R_ with centre **C**. A manifold surface will be produced if the major radius is greater than the minor radius. If this condition is not fulfilled, the resulting surface will be self-intersecting.

> NOTE Entity adapted from **toroidal_surface** defined in ISO 10303-42.

> HISTORY New entity in IFC4 Addendum 2.

## Attributes

### MajorRadius
The major radius of the torus.

### MinorRadius
The minor radius of the torus.

## Formal Propositions

### MajorLargerMinor
The attribute value of the MinorRadius shall be smaller then the value of the MajorRadius
