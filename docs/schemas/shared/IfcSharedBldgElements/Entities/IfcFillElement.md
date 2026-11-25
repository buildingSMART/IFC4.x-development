# IfcFillElement

An element with the purpose of filling gaps between other elements.
<!-- end of short definition -->

> HISTORY New entity in IFC4.4.

## Attributes

### PredefinedType
Predefined generic type for a fill element that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcFillElementType_ is assigned, providing its own _IfcFillElementType.PredefinedType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFillElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no fill element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcFillElementType_.
