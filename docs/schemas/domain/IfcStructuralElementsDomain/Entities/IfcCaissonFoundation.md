# IfcCaissonFoundation

CaissonFoundation essentially is a hollow box that can be either open or closed.
<!-- end of short definition -->

(NOTE: corresponding predefined type is deprecated from IfcFootingTypeEnum).

## Attributes

### PredefinedType
Predefined generic type for a caisson foundation that is specified in an enumeration. There may be a property set given specifically for the predefined types.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCaissonFoundationType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no caisson foundation type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCaissonFoundationType_.
