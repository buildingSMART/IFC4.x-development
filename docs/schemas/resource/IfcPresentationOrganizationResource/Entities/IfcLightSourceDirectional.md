# IfcLightSourceDirectional

<!-- end of short definition -->

> NOTE Definition according to ISO 10303-46:
> The light source directional is a subtype of light source. This entity has a light source direction. With a conceptual origin at infinity, all the rays of the light are parallel to this direction. This kind of light source lights a surface based on the surface's orientation, but not position.

> NOTE Definition according to ISO/IEC 14772-1:1997:
> The directional light node defines a directional light source that illuminates along rays parallel to a given 3-dimensional vector. Directional light nodes do not attenuate with distance. Directional light nodes are specified in the local coordinate system and are affected by ancestor transformations.

> NOTE Corresponding ISO 10303 entity: light_source_directional. Please refer to ISO/IS 10303-46:1994, p. 32 for the final definition of the formal standard.

> NOTE In addition to the attributes as defined in ISO 10303-46 the additional property from ISO/IEC 14772-1:1997 (VRML) _AmbientIntensity_ and _Intensity_ are inherited from the supertype.

> HISTORY New entity in IFC2x, renamed and enhanced in IFC2x2.

## Attributes

### Orientation
Definition from ISO/CD 10303-46:1992: This direction is the direction of the light source.
Definition from VRML97 - ISO/IEC 14772-1:1997: The direction field specifies the direction vector of the illumination emanating from the light source in the local coordinate system. Light is emitted along parallel rays from an infinite distance away.
