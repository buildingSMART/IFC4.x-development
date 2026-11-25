# IfcFillElementType

The element type _IfcFillElementType_ defines commonly shared information for occurrences of fill elements. Fill elements are building elements with the purpose of filling gaps between other elements. The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define a fill element specification that is common to all occurrences of that fill element type. Fill element types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcFillElementType_ within building models are represented by instances of _IfcFillElement_.
<!-- end of short definition -->

> HISTORY New entity in IFC4.4.

## Attributes

### PredefinedType
Predefined generic type for a fill element type that is specified in an enumeration. There may be a property set given specifically for the predefined types.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
