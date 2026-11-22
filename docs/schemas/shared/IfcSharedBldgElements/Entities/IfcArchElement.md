# IfcArchElement

A typically curved structural member spanning an opening and serving as a support.
<!-- end of short definition -->

> NOTE Subtype of _IfcBuiltElement_ — see that entity's documentation for inherited attributes and behavior.

> HISTORY New entity in IFC 4.4.

## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration. This type may associate additional specific property sets.

> NOTE  The _PredefinedType_ shall only be used, if no _IfcArchElementType_ is assigned, providing its own _IfcArchElementType.PredefinedType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcArchElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no arch element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcArchElementType_.
