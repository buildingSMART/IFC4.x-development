# IfcSurfaceOfRevolution

The IfcSurfaceOfRevolution is a surface derived by rotating a curve about an axis.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A surface of revolution is the surface obtained by rotating a curve one complete revolution about an axis. The data shall be interpreted as below.
>
> The parameterization is as follows where the curve has a parameterization λ(_u_):
>> **C** = AxisPosition.Location
>> **V** = AxisPosition.Z
>>
>> ![Image](../../../../figures/ifcsurfaceofresolution-math1.gif)
> In order to produce a single-valued surface with a complete revolution, the curve shall be such that when expressed in a cylindrical coordinate system (_r,φ ,z_) centred at **C** with an axis **V**, no two distinct parametric points on the curve shall have the same values for (_r, z_). For a surface of revolution the parametric range is 0 < _u_ < 360 degree. The parameterization range for _v_ is defined by referenced curve.

> NOTE Entity adapted from **surface_of_revolution** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. The surface shall not self-intersect
2. The swept curve shall not be coincident with the axis line for any finite part of its length.

## Attributes

### AxisPosition
A point on the axis of revolution and the direction of the axis of revolution.

### AxisLine
The line coinciding with the axis of revolution.
