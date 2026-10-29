# IfcCoordinateOperation

_IfcCoordinateOperation_ is an abstract supertype to handle any operation (transformation or conversion) between two coordinate reference systems (CRSs).
<!-- end of short definition -->

By convention, a coordinate operation is given between a **source CRS**, being the more local (or child) CRS; and **target CRS**, being the more remote (or parent) CRS.

> EXAMPLE A common coordinate operation is the one between the local engineering coordinate system of a construction project and any map or other coordinate reference system.

An _IfcCoordinateOperation_ allows to connect:
- an _IfcGeometricRepresentationContext_ – a reference system of a virtual model
- to an _IfcCoordinateReferenceSystem_ – the coordinate system which is related to the real world by datums.

> EXAMPLE This can is done by setting:
> - the _IfcCoordinateOperation.SourceCRS_ to _IfcGeometricRepresentationContext_
> - the _IfcCoordinateOperation.TargetCRS_ either to:
>  -	_IfcProjectedCRS_, for defined easting, northing and orthogonal height
>  -	_IfcGeographicCRS_, for defined latitude, longitude and ellipsoidal height

> NOTE _IfcProjectedCRS_ can be used to represent a projected CRS or a compound CRS, comprising of a projected CRS with a vertical CRS. See _IfcProjectedCRS_ for further details.

> NOTE Definition from OpenGIS Abstract Specification, Topic 2:
> If the relationship between any two coordinate reference systems is known, coordinates can be transformed or converted to another coordinate reference system. Coordinate operations are divided into two subtypes:
>
> * _Coordinate conversion_ – mathematical operation on coordinates that does not include any change of datum. The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters.
>
> * _Coordinate transformation_ – mathematical operation on coordinates that usually includes a change of datum. The parameters of a coordinate transformation are empirically derived from data containing the coordinates of a series of points in both coordinate reference systems. This computational process is usually ‘over-determined’, allowing derivation of error (or accuracy) estimates for the transformation. Also, the stochastic nature of the parameters may result in multiple (different) versions of the same coordinate transformation. Because of this several transformations may exist for a given pair of coordinate reference systems, differing in their transformation method, parameter values and accuracy characteristics.

There are three types of _IfcCoordinateOperation_. The one to be used depends on the specific use case:

* _IfcMapConversion_ and _IfcMapConversionScaled_ involve a **transformation**. These coordinate operations convey that the local engineering coordinate system of the virtual model (which is a topocentric CRS) is put in place in the referenced _IfcProjectedCRS_. 

* _IfcRigidOperation_ involves a **translation** in the 3D space. This coordinate operation convey that the whole virtual model is translated in the same way. For example, using lengths to translate along x,y,z; or using angles for a 2D translation (e.g., lambda, phi), plus a change in height.

![Coordinate operations](../../../../figures/ifccoordinateoperation.png)
Figure COORDOPS — Possible coordinate operations between coordinate reference systems

> HISTORY New entity in IFC4.

## Attributes

### SourceCRS
Source coordinate reference system for the operation.

### TargetCRS
Target coordinate reference system for the operation.
