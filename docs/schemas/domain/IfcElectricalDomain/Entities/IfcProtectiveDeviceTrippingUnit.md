# IfcProtectiveDeviceTrippingUnit

A protective device tripping unit breaks an electrical circuit at a separate breaking unit when a stated electric current that passes through the unit is exceeded.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcProtectiveDeviceTrippingUnitType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no protective device tripping unit type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcProtectiveDeviceTrippingUnitType_.

## Concepts

### Control Flow



#### IfcProtectiveDevice

The corresponding breaker unit for breaking the circuit.

### Object Typing



### Property Sets for Objects



### Quantity Sets



