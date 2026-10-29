# IfcVector

An _IfcVector_ is a geometric representation item having both a magnitude and direction. The magnitude of the vector is solely defined by the _Magnitude_ attribute and the direction is solely defined by the _Orientation_ attribute.
<!-- end of short definition -->

> NOTE The _DirectionRatios_ of the _Orientation_ attribute are not used to define the magnitude.

> NOTE Definition according to ISO/CD 10303-42:1992
> The vector is defined in terms of the direction and magnitude of the vector. The value of the magnitude attribute defines the magnitude of the vector. The magnitude of the vector can not be reliable calculated from the components of the orientation attribute. This form of representation was selected to reduce problems with numerical instability. For example a vector of magnitude 2.0 mm and equally inclined to the coordinate axes could be represented with Orientation attribute of (1.0,1.0,1.0).

> NOTE Entity adapted from **vector** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0

## Attributes

### Orientation
The direction of the vector.

### Magnitude
The magnitude of the vector. All vectors of Magnitude 0.0 are regarded as equal in value regardless of the orientation attribute.

### Dim
The space dimensionality of this class, it is derived from Orientation

## Formal Propositions

### MagGreaterOrEqualZero
The magnitude shall be positive or zero.
