# IfcVibrationIsolator

A vibration isolator is a device used to minimize the effects of vibration transmissibility in a structure.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcVibrationIsolatorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no vibration isolator type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcVibrationIsolatorType_.

## Concepts

### Material Set

#### Casing

Material from which the casing is constructed.

#### Damping

Material from which the damping element of the vibration isolator is constructed.

### Object Typing


### Property Sets for Objects


### Quantity Sets


