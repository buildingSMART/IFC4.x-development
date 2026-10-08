# IfcDiscreteAccessory

A discrete accessory is a representation of different kinds of accessories included in or added to elements.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _PredefinedType_ added.

## Attributes

### PredefinedType
Subtype of discrete accessory. If USERDEFINED, the type is further qualified by means of the inherited attribute _ObjectType_. Refer to _IfcDiscreteAccessoryType_ for a non-exclusive list of userdefined type designations which are applicable to _IfcDiscreteAccessory_ as well.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcDiscreteAccessoryType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcDiscreteAccessoryType_.

## Concepts

### Object Typing



### Property Sets for Objects



