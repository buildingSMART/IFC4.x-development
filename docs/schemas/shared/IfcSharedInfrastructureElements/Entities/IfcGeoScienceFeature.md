# IfcGeoScienceFeature

Represents a geological or geotechnical feature as an interpretation of factual data such as observations, measurements and tests.
## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcGeoScienceFeatureType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcGeoScienceFeatureType_.
