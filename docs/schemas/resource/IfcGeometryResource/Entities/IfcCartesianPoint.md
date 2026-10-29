# IfcCartesianPoint

An _IfcCartesianPoint_ defines a point by coordinates in an orthogonal, right-handed Cartesian coordinate system. For the purpose of this specification only two and three dimensional Cartesian points are used.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A cartesian_point is a point defined by its coordinates in a rectangular Cartesian coordinate system, or in a parameter space. The entity is defined in a one, two or three-dimensional space as determined by the number of coordinates in the list. Depending upon the geometric representation context in which the point is used the names of the coordinates may be (x,y,z), or (u,v), or any other chosen values.

> NOTE Entity adapted from **cartesian_point** defined in ISO 10303-42

> HISTORY New entity in IFC1.0

## Attributes

### Coordinates
The first, second, and third coordinate of the point location. If placed in a two or three dimensional rectangular Cartesian coordinate system, Coordinates[1] is the X coordinate, Coordinates[2] is the Y coordinate, and Coordinates[3] is the Z coordinate.

## Formal Propositions

### CP2Dor3D
Only two or three dimensional points are in scope.
