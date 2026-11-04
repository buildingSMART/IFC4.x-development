# IfcGeoScienceModelType

The _IfcGeoScienceModelType_ provides the type information for _IfcGeoScienceModel_ occurrences.
An _IfcGeoScienceModel_ represents a model of the geological structure as considered relevant for the project, as a base for the definition of building- and design-related geotechnical models, hydrogeological models and geo hazard models.
## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
