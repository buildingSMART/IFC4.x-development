# IfcBorehole

A Borehole is the generalized term for any narrow shaft drilled in the ground, either vertically, horizontally, or inclined. 

> NOTE In the context of ground models, IfcBorehole is mainly used as a space where observations of the ground conditions are made, and results from tests in place (in-situ) or on samples collected from the borehole are located.

> NOTE The IfcBorehole may aggregate other elements such as installations and lining and have IfcGeoScienceObservation instances assigned to represent e.g. intervals and points. Further, the IfcGeoScienceObservation instances can represent the ground classification described by IfcGeoScienceModel, and link a certain part (interval) of the borehole to an IfcGeoScienceFeature like a geotechnical unit. 

> NOTE The assembly may also contain one or more strata. The contained subtypes of _IfcGeotechnicalStratum_ will have shape representations made from straight or bent tubes reflecting the bore diameter, or discs if a 'Yabuki' top surface model is being used.

## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBoreholeType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBoreholeType_.
