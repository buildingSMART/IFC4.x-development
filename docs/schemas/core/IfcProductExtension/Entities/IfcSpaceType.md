# IfcSpaceType

A space represents an area or volume bounded actually or theoretically. Spaces are areas or volumes that provide for certain functions within a building.
<!-- end of short definition -->

The _IfcSpaceType_ defines a list of commonly shared information for occurrences of spaces. The set of shared information may include:

* common properties within shared property sets
* common shape representations

It is used to define an space specification (i.e. the specific space information, that is common to all occurrences of that space type. Space types may be exchanged without being already assigned to occurrences).

> NOTE The space types are often used to represent space catalogues, less so for sharing a common representation map. Space types in a space catalogue share same space classification and a common set of space requirement properties.

The occurrences of _IfcSpaceType_ are represented by instances of _IfcSpace_.

> HISTORY New entity in IFC2x3.

> IFC4 CHANGE The attribute _LongName_ has been added to the end of the entity definition.

## Attributes

### PredefinedType
Predefined types to define the particular type of space. There may be property set definitions available for each predefined type.

### LongName
Long name for a space type, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE In many scenarios the _Name_ attribute refers to the short name or number of a space type, and the _LongName_ refers to the full descriptive name.

> IFC4 CHANGE New attribute added at the end of entity definition.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
