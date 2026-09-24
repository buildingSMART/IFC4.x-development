# IfcCartesianTransformationOperator3D

An _IfcCartesianTransformationOperator_ defines a geometric transformation in three-dimensional space.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A Cartesian transformation operator 3d defines a geometric transformation in three-dimensional space composed of translation, rotation, mirroring and uniform scaling. The list of normalized vectors u defines the columns of an orthogonal matrix **T**. These vectors are computed from the direction attributes axis1, axis2 and axis3 by the base axis function. If |**T**|= -1, the transformation includes mirroring.

> NOTE Entity adapted from **cartesian_transformation_operator_3d** defined in ISO10303-42.

> HISTORY New entity in IFC2x.

## Attributes

### Axis3
The exact direction of U[3], the derived Z axis direction.

### U
The list of mutually orthogonal, normalized vectors defining the transformation matrix T. They are derived from the explicit attributes Axis3, Axis1, and Axis2 in that order.

## Formal Propositions

### DimIs3D
The coordinate space dimensionality of this entity shall be 3.

### Axis1Is3D
The inherited Axis1 should have (if given) the dimensionality of 3.

### Axis2Is3D
The inherited Axis2 should have (if given) the dimensionality of 3.

### Axis3Is3D
The Axis3 should have (if given) the dimensionality of 3.
