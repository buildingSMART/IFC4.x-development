# IfcEarthingElement

An element that connects the conductive parts of an electrical installation to the ground or earth.
<!-- end of short definition -->

## Attributes

### PredefinedType
Identifies the predefined types of earthing element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcEarthingElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no earthing element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcEarthingElementType_.
