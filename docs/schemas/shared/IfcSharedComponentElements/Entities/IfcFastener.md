# IfcFastener

Representations of fixing parts which are used as fasteners to connect or join elements with other elements. Excluded are mechanical fasteners which are modeled by a separate entity (_IfcMechanicalFastener_).
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Attribute _PredefinedType_ added.

## Attributes

### PredefinedType
Subtype of fastener

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFastenerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcFastenerType_.

## Concepts

### Object Typing



### Property Sets for Objects



