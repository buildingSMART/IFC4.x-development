# IfcPixelTexture

An _IfcPixelTexture_ provides a 2D image-based texture map as an explicit array of pixel values (list of _Pixel_ binary attributes). In contrary to the _IfcImageTexture_ the _IfcPixelTexture_ holds a 2 dimensional list of pixel color (and opacity) directly, instead of referencing to an URL.
<!-- end of short definition -->

The following definitions from ISO/IEC 19775-1 X3D Architecture and base components ([X3D Specification](http://www.web3d.org/x3d/specifications/)) apply:

* The PixelTexture node defines a 2D image-based texture map as an explicit array of pixel values (image field) and parameters controlling tiling repetition of the texture onto geometry.
* Texture maps are defined in a 2D coordinate system (s, t) that ranges from 0.0 to 1.0 in both directions. The bottom edge of the pixel image corresponds to the S-axis of the texture map, and left edge of the pixel image corresponds to the T-axis of the texture map. The lower-left pixel of the pixel image corresponds to s=0.0, t=0.0, and the top-right pixel of the image corresponds to s = 1.0, t = 1.0.
* The Image field specifies a single uncompressed 2-dimensional pixel image. Image fields contain three integers representing the width, height and number of components in the image, followed by width×height hexadecimal values representing the pixels in the image. Pixel values are limited to 256 levels of intensity (that is, 0x00-0xFF hexadecimal).
  1. A one-component image specifies one-byte hexadecimal value representing the intensity of the image. For example, 0xFF is full intensity in hexadecimal (255 in decimal), 0x00 is no intensity (0 in decimal).
  2. A two-component image specifies the intensity in the first (high) byte and the alpha opacity in the second (low) byte.
  3. Pixels in a three-component image specify the red component in the first (high) byte, followed by the green and blue components (for example, 0xFF0000 is red, 0x00FF00 is green, 0x0000FF is blue).
  4. Four-component images specify the alpha opacity byte after red/green/blue (e.g., 0x0000FF80 is semi-transparent blue). A value of 00 is completely transparent, FF is completely opaque, 80 is semi-transparent.
* <font size="-1">Note that alpha equals (1.0 -transparency), if alpha and transparency each range from 0.0 to 1.0.</font>

> HISTORY New entity in IFC2x2.

## Attributes

### Width
The number of pixels in width (S) direction.

### Height
The number of pixels in height (T) direction.

### ColourComponents
Indication whether the pixel values contain a 1, 2, 3, or 4 colour component.

### Pixel
Flat list of hexadecimal values, each describing one pixel by 1, 2, 3, or 4 components.
> IFC2x3 CHANGE The data type has been changed from STRING to BINARY.

## Formal Propositions

### MinPixelInS
The minimum number of pixel in width (S coordinate) direction shall be 1.

### MinPixelInT
The minimum number of pixel in height (T coordinate) direction shall be 1.

### NumberOfColours
The number of color components shall be either 1, 2, 3, or 4.

### SizeOfPixelList
The list of pixel shall have exactly width\*height members.

### PixelAsByteAndSameLength
The binary value provided for each _Pixel_ shall be a multiple of 8 bits. And all pixel shall have the same binary length.
