# IfcBSplineSurfaceForm

The _IfcBSplineSurfaceForm_ represents a part of a surface of some specific form.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This type is used to indicate that the B-spline surface represents a part of a surface of some specific form.

> NOTE Type adapted from **b_spline_surface_form** defined in ISO 10303-42.

> HISTORY New type in IFC4.

## Items

### PLANE_SURF
A bounded portion of a plane represented by a B-spline surface of degree 1 in each parameter.

### CYLINDRICAL_SURF
A bounded portion of a cylindrical surface.

### CONICAL_SURF
A bounded portion of the surface of a right circular cone.

### SPHERICAL_SURF
A bounded portion of a sphere, or a complete sphere, represented by a B-spline surface.

### TOROIDAL_SURF
A torus, or portion of a torus, represented by a B-spline surface.

### SURF_OF_REVOLUTION
A bounded portion of a surface of revolution.

### RULED_SURF
A surface constructed from two parametric curves by joining with straight lines
corresponding points with the same parameter value on each of the curves.

### GENERALISED_CONE
A special case of a ruled surface in which the second curve degenerates to a
single point; when represented by a B-spline surface all the control points along one edge will be coincident.

### QUADRIC_SURF
A bounded portion of one of the class of surfaces of degree 2 in the variables x, y and z.

### SURF_OF_LINEAR_EXTRUSION
A bounded portion of a surface of linear extrusion represented by a B-spline surface of degree 1 in one of the parameters.

### UNSPECIFIED
A surface for which no particular form is specified.
