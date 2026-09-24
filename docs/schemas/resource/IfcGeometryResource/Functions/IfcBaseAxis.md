# IfcBaseAxis

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This function returns normalized orthogonal directions, u[1], u[2] and, if appropriate, u[3]. In the three-dimensional case, with complete input data, u[3] is in the direction of axis3, u[1] is in the direction of the projection of axis1 onto the plane normal to u[3], andu[2] is orthogonal to both u[1] and u[3], taking the same sense as axis2. In the two-dimensional case u[1] is in the direction of axis1 and u[2] is perpendicular to this, taking its sense from axis2. For incomplete input data appropriate default values are derived.

> NOTE Function adapted from **base_axis** defined in ISO 10303-42.

> HISTORY New function in IFC2x
