# IfcMapConversion

The map conversion deals with transforming the local engineering coordinate system, often called world coordinate system, into the coordinate reference system of the underlying map.
<!-- end of short definition -->

> NOTE The _IfcMapConversion_ does not handle the projection of a map from the geodetic coordinate reference system.

For this transformation, _IfcMapConversion_ data are used for:

* a scaling of the three axes (x,y,z), by the same _IfcMapConversion.Scale_
* followed by an **anti-clockwise** rotation about the z-axis of *θ*, where:

$$
\theta=arctan\left(\frac{XAxisOrdinate}{XAxisAbscissa}\right)
$$

* and then a translation in (x,y,z) of _IfcMapConversion.Eastings_, _IfcMapConversion.Northings_, _IfcMapConversion.OrthogonalHeight_

With _IfcMapConversion_, **one scale** is applied equally to x, y and z, **to convert units**.
With _IfcMapConversionScaled_, additional **different factors** multiply x, y and z, to **scale coordinates** - not units.

> NOTE The z-axis of the local engineering coordinate system is always parallel to the z-axis of the map coordinate system.

> NOTE The *Scale* can be used when the length unit for the 3 axes of the map coordinate system are not identical with the length unit established for this project (see _IfcProject.UnitsInContext_) - for example to convert feet into metres. If omitted, the scale factor 1.0 is assumed.

> HISTORY New entity in IFC4

## Attributes

### Eastings
Specifies the location along the easting of the coordinate system of the target map coordinate reference system.
> NOTE for right-handed Cartesian coordinate systems this would establish the location along the x axis.

### Northings
Specifies the location along the northing of the coordinate system of the target map coordinate reference system.
> NOTE for right-handed Cartesian coordinate systems this would establish the location along the y axis

### OrthogonalHeight
Orthogonal height relative to the vertical datum specified.
> NOTE for right-handed Cartesian coordinate systems this would establish the location along the z axis

### XAxisAbscissa
Specifies the value along the easting axis of the end point of a vector indicating the position of the local x axis of the engineering coordinate reference system.
> NOTE for right-handed Cartesian coordinate systems this would establish the location along the x axis

> NOTE together with the _XAxisOrdinate_ it provides the direction of the local x axis within the horizontal plane of the map coordinate system

### XAxisOrdinate
Specifies the value along the northing axis of the end point of a vector indicating the position of the local x axis of the engineering coordinate reference system.
> NOTE for right-handed Cartesian coordinate systems this would establish the location along the y axis

_XAxisAbscissa_ it provides the direction of the local x axis within the horizontal plane of the map coordinate system.

### Scale
Scale to be used, when the units of the CRS are not identical to the units of the engineering coordinate system.
If omitted, the value of 1.0 is assumed.
If the units of the referenced source location engineering coordinate system are different from the units of the referenced target coordinate system,
then this attribute must be included and must have the value of the scale from the source to the target units.