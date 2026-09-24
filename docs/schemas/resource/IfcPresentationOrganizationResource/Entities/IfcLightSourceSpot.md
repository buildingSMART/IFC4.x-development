# IfcLightSourceSpot

<!-- end of short definition -->

> NOTE Definition according to ISO 10303-46:
> The light source spot entity is a subtype of light source. Spot light source entities have a light source colour, position, direction, attenuation coefficients, concentration exponent, and spread angle. If a point lies outside the cone of influence of a light source of this type as determined by the light source position, direction and spread angle its colour is not affected by that light source.

> NOTE The _IfcLightSourceSpot_ adds the _BeamWidthAngle_ which defines the inner cone in which the light source emits light at uniform full intensity. The light source's emission intensity drops off from the inner solid angle (_BeamWidthAngle_) to the outer solid angle (_SpreadAngle_).

> NOTE Definition according to ISO/IEC 14772-1:1997:
> The Spot light node defines a light source that emits light from a specific point along a specific direction vector and constrained within a solid angle. Spot lights may illuminate geometry nodes that respond to light sources and intersect the solid angle defined by the Spot light. Spot light nodes are specified in the local coordinate system and are affected by ancestors' transformations. Figure 1 shows the definition of spot light. ![spot light](../../../../figures/ifclightsourcespot_fig1.gif "Figure 1 — Light source spot")

> NOTE Corresponding ISO 10303 entity: light_source_spot. Please refer to ISO/IS 10303-46:1994, p. 33 for the final definition of the formal standard.

> NOTE In addition to the attributes as defined in ISO10303-46 the additional property from ISO/IEC 14772-1:1997 (VRML) _Radius_, _BeamWidth_, and _QuadricAttenuation_ are added to this subtype and the _AmbientIntensity_ and _Intensity_ are inherited from the supertype.

> HISTORY New entity in IFC2x, renamed and enhanced in IFC2x2.

## Attributes

### Orientation
Definition from ISO/CD 10303-46:1992: This is the direction of the axis of the cone of the light source specified in the coordinate space of the representation being projected..
Definition from VRML97 - ISO/IEC 14772-1:1997: The direction field specifies the direction vector of the light's central axis defined in the local coordinate system.

### ConcentrationExponent
Definition from ISO/CD 10303-46:1992: This real is the exponent on the cosine of the angle between the line that starts at the position of the spot light source and is in the direction of the orientation of the spot light source and a line that starts at the position of the spot light source and goes through a point on the surface being shaded.
>NOTE This attribute does not exists in ISO/IEC 14772-1:1997.

### SpreadAngle
Definition from ISO/CD 10303-46:1992: This planar angle measure is the angle between the line that starts at the position of the spot light source and is in the direction of the spot light source and any line on the boundary of the cone of influence.
Definition from VRML97 - ISO/IEC 14772-1:1997: The cutOffAngle (name of spread angle in VRML) field specifies the outer bound of the solid angle. The light source does not emit light outside of this solid angle.

### BeamWidthAngle
Definition from VRML97 - ISO/IEC 14772-1:1997: The beamWidth field specifies an inner solid angle in which the light source emits light at uniform full intensity. The light source's emission intensity drops off from the inner solid angle (beamWidthAngle) to the outer solid angle (spreadAngle).
