# IfcLightSourcePositional

<!-- end of short definition -->

> NOTE Definition according to ISO 10303-46:
> The light source positional entity is a subtype of light source. This entity has a light source position and attenuation coefficients. A positional light source affects a surface based on the surface's orientation and position.

> NOTE Definition according to ISO/IEC 14772-1:1997:
> The Point light node specifies a point light source at a 3D location in the local coordinate system. A point light source emits light equally in all directions; that is, it is omnidirectional. Point light nodes are specified in the local coordinate system and are affected by ancestor transformations.

> Point light node's illumination falls off with distance as specified by three attenuation coefficients. The attenuation factor is
>> 1/max(attenuation[0] + attenuation[1] × r + attenuation[2] × r 2 , 1),
> where r is the distance from the light to the surface being illuminated. The default is no attenuation. An attenuation value of (0, 0, 0) is identical to (1, 0, 0). Attenuation values shall be greater than or equal to zero.

> NOTE Corresponding ISO 10303 entity: light_source_positional. Please refer to ISO/IS 10303-46:1994, p. 32 for the final definition of the formal standard.

> NOTE In addition to the attributes as defined in ISO10303-46 the additional property from ISO/IEC 14772-1:1997 (VRML) _Radius_ and _QuadricAttenuation_ are added to this subtype and the _AmbientIntensity_ and _Intensity_ are inherited from the supertype.

> HISTORY New entity in IFC2x, renamed and enhanced in IFC2x2.

## Attributes

### Position
Definition from ISO/CD 10303-46:1992: The Cartesian point indicates the position of the light source.
Definition from VRML97 - ISO/IEC 14772-1:1997: A Point light node illuminates geometry within radius of its location.

### Radius
The maximum distance from the light source for a surface still to be illuminated.
Definition from VRML97 - ISO/IEC 14772-1:1997: A Point light node illuminates geometry within radius of its location.

### ConstantAttenuation
Definition from ISO/CD 10303-46:1992: This real indicates the value of the attenuation in the lighting equation that is constant.

### DistanceAttenuation
Definition from ISO/CD 10303-46:1992: This real indicates the value of the attenuation in the lighting equation that proportional to the distance from the light source.

### QuadricAttenuation
This real indicates the value of the attenuation in the lighting equation that proportional to the square value of the distance from the light source.
