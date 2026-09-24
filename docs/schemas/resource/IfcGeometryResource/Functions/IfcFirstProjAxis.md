# IfcFirstProjAxis

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This function produces a three dimensional direction which is, with fully defined input, the projection of arg onto the plane normal to the z-axis. With arg defaulted the result is the projection of (1.0,0.0,0.0) onto this plane except that if z-axis = (1.0,0.0,0.0) then (0.0,1.0,0.0) is used as initial value of arg. A violation occurs if arg is in the same direction as the input z-axis.

> NOTE Function adapted from **first_proj_axis** defined in ISO 10303-42.

> HISTORY New function in IFC1.5
