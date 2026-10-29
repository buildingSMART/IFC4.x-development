# IfcTextureCoordinateGenerator

The _IfcTextureCoordinateGenerator_ describes a procedurally defined mapping function with input parameter to map 2D texture coordinates to 3D geometry vertices.
<!-- end of short definition -->

The TextureCoordinateGenerator supports the automatic generation of texture coordinates for geometric shapes.

> NOTE The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.

> HISTORY New entity in IFC2x2.

> IFC2x2 Add2 CHANGE The attribute Texture has been deleted.

## Attributes

### Mode
The _Mode_ attribute describes the algorithm used to compute texture coordinates. The following modes are recommended:

 * COORD: use vertex coordinates
 * COORD-EYE: use vertex coordinates transformed to camera space

### Parameter
The parameters used as arguments by the function as specified by _Mode_.
> IFC4 CHANGE : Data type restricted to REAL.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used.
