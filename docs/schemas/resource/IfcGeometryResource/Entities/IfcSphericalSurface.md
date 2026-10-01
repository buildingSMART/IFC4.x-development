# IfcSphericalSurface

The _IfcSphericalSurface_ is a bounded elementary surface. The inherited _Position_ attribute defines the _IfcAxis2Placement3D_ and provides:

* _SELF\IfcElementarySurface.Position_: The location and orientation of the axis system for the primitive.
* _SELF\IfcElementarySurface.Position.Location_: The center of the spherical surface.
* _SELF\IfcElementarySurface.Position.Position[3]:_ The z axis points at its positive direction towards the north pole, and by its negative directions towards the south pole.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An _IfcSphericalSurface_ is a type of an elementary surface, which is at a constant distance (the **radius**) from a central point. A spherical surface is defined by the radius and the location and orientation of the surface.
>
> The data is to be interpreted as follows:
>
>> C = Position.Location
>> x = Position.P[1]
>> y = Position.P[2]
>> z = Position.P[3] (axis of spherical surface)
>> _R_ = Radius
> and the surface is parametrised as
>
>> _**σ**(u,v)_ = **C** + R cos _v_ ((cos _u_) **x** + (sin _u_) **y**) + R(sin _v_) **z**
> where the parametrisation range is _0 ≤ u ≤ 360_ degrees and _-90 ≤ v ≤ 90_ degrees. _u_ and _v_ are angular parameters and when numerical values are specified they shall use the current units for plane angle measure.
>
> In the placement coordinate system defined above, the surface is represented by the equation _S_ = 0, where
>
>> _S(x, y, z) = x^2^ + y^2^ + z^2^ - R^2^._
> The positive direction of the normal to the surface at any point on the surface is given by
>
>> _(S~x~, S~y~, S~z~ )._
> The unit normal is given by
>
>> **N**_(u,v)_ = cos _v_((cos _u_)**x** + (sin _u_)**y**) + (sin _v_)**z**,


>
> NOTE Entity adapted from **spherical_surface** defined in ISO 10303-42.

> HISTORY New entity in IFC4 Addendum 2.

## Attributes

### Radius
The radius of the sphere.
