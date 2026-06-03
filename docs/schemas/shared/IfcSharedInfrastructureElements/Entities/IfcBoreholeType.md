# IfcBoreholeType

The _IfcBoreholeType_ provides the type information for _IfcBorehole_ occurrences.
A Borehole is the generalized term for any narrow shaft drilled in the ground, either vertically, horizontally, or inclined.

## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
