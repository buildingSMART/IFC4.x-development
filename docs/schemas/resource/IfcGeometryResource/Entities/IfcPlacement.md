# IfcPlacement

An _IfcPlacement_ is an abstract supertype of placement subtypes that define the location of an item, or an entire shape representation, and provide its orientation. All placement subtypes define right-handed Cartesian coordinate systems and do not allow mirroring.
<!-- end of short definition -->

> NOTE Cartesian transformations including mirroring and scaling are supported by _IfcCartesianTransformationOperator_

> NOTE Definition according to ISO/CD 10303-42:1992
> A placement locates a geometric item with respect to the coordinate system of its geometric context. It locates the item to be defined and, in the case of the axis placement subtypes, gives its orientation.

> NOTE Entity adapted from **placement** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0

## Attributes

### Location
The geometric position of a reference point, such as the center of a circle, of the item to be located.

### Dim
The space dimensionality of this class, derived from the dimensionality of the location.
