# IfcCartesianTransformationOperator2D

An _IfcCartesianTransformationOperator2D_ defines a geometric transformation in two-dimensional space.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A Cartesian transformation operator 2d defines a geometric transformation in two-dimensional space composed of translation, rotation, mirroring and uniform scaling. The list of normalized vectors u defines the columns of an orthogonal matrix **T**. These vectors are computed from the direction attributes axis1 and axis2 by the base axis function. If **|T|= -1**, the transformation includes mirroring.

> NOTE Entity adapted from **cartesian_transformation_operator_2d** defined in ISO10303-42.

> HISTORY New entity in IFC2x.

## Attributes

### U
The list of mutually orthogonal, normalized vectors defining the transformation matrix T. They are derived from the explicit attributes Axis1 and Axis2 in that order.

## Formal Propositions

### DimEqual2
The coordinate space dimensionality of this entity shall be 2.

### Axis1Is2D
The inherited Axis1 should have (if given) the dimensionality of 2.

### Axis2Is2D
The inherited Axis2 should have (if given) the dimensionality of 2.
