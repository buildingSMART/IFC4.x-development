# IfcBlobTexture

An _IfcBlobTexture_ provides a 2-dimensional distribution of the lighting parameters of a surface onto which it is mapped. The texture itself is given as a single binary blob, representing the content of a pixel format file. The file format of the pixel file is given by the _RasterFormat_ attribute and allowable formats are guided by where rule _SupportedRasterFormat_.
<!-- end of short definition -->

> NOTE Toolbox specific implementations of the binary datatype may restrict the maximum length of the binary blob to capture the raster file content.

For interpretation of the texture nodes see _IfcImageTexture_ definition.

> HISTORY New entity in IFC2x3.

> IFC4 CHANGE Data type of _RasterCode_ has been corrected to BINARY.

## Attributes

### RasterFormat
The format of the _RasterCode_ often using a compression.

### RasterCode
Blob, given as a single binary, to capture the texture within one popular file (compression) format. The file format is provided by the _RasterFormat_ attribute.

## Formal Propositions

### SupportedRasterFormat
Currently the formats of bmp, jpg, gif and pgn, shall be supported.

### RasterCodeByteStream
The size of the raster code shall be a multiple of 8 bits.
