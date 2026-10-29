# IfcLightSource

<!-- end of short definition -->

> NOTE Definition according to ISO 10303-46:
> The light source entity is determined by the reflectance specified in the surface style rendering. Lighting is applied on a surface by surface basis: no interactions between surfaces such as shadows or reflections are defined.

> NOTE Entity adapted from **light_source** defined in ISO 10303-46.

> NOTE In addition to the attributes as defined in ISO10303-46 the following additional properties from ISO/IEC 14772-1:1997 (VRML) are added: _ambientIntensity_ and _Intensity_. The attribute _Name_ has been added as well (as it is not inherited via representation_item).

> HISTORY New entity in IFC2x, renamed and enhanced in IFC2x2.

## Attributes

### Name
The name given to the light source in presentation.

### LightColour
Definition from ISO/CD 10303-46:1992: Based on the current lighting model, the colour of the light to be used for shading.
Definition from VRML97 - ISO/IEC 14772-1:1997: The color field specifies the spectral color properties of both the direct and ambient light emission as an RGB value.

### AmbientIntensity
Definition from VRML97 - ISO/IEC 14772-1:1997: The ambientIntensity specifies the intensity of the ambient emission from the light. Light intensity may range from 0.0 (no light emission) to 1.0 (full intensity).

### Intensity
Definition from VRML97 - ISO/IEC 14772-1:1997: The intensity field specifies the brightness of the direct emission from the light. Light intensity may range from 0.0 (no light emission) to 1.0 (full intensity).
