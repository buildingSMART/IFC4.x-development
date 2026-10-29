# IfcLightIntensityDistribution

_IfcLightIntensityDistribution_ defines the the luminous intensity of a light source that changes according to the direction of the ray. It is based on some standardized light distribution curves, which are defined by the _LightDistributionCurve_ attribute.
<!-- end of short definition -->

> New entity in IFC2x2.

## Attributes

### LightDistributionCurve
Standardized light distribution curve used to define the luminous intensity of the light in all directions.

### DistributionData
Light distribution data applied to the light source. It is defined by a list of main plane angles (B or C according to the light distribution curve chosen) that includes (for each B or C angle) a second list of secondary plane angles (the β or γ angles) and the according luminous intensity distribution measures.
