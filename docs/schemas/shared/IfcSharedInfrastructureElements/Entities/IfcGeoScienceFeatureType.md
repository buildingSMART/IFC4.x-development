# IfcGeoScienceFeatureType

The _IfcGeoScienceFeatureType_ provides the type information for _IfcGeoScienceFeature_ occurrences.
An _IfcGeoScienceFeature_ represents a geological or geotechnical feature as an interpretation of factual data such as observations, measurements and tests.
## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
