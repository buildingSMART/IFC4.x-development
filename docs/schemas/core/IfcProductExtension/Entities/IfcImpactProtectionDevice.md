# IfcImpactProtectionDevice

An impact protection device is a component used to protect other built elements from kinetic damage. Impact protection devices currently come in different varieties:
<!-- end of short definition -->

- A vibration damper used to minimize the effects of vibration in a structure by dissipating kinetic energy. The damper may be passive (elastic, frictional, inertia) or active (in a system using sensors and actuators).
- A vibration isolator is a device used to minimize the effects of vibration transmissibility in a structure.
- Impact devices that dissipate kinetic energy from impacting elements (such as vehicles) by deformation or elastic mechanics.

## Attributes

### PredefinedType

Identifies the predefined type of an impact device. This type may associate additional specific property sets.


## Formal Propositions

### CorrectPredefinedType

Either the _PredefinedType_ attribute is unset (e.g. because an _IfcImpactProtectionDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to _USERDEFINED_.

### CorrectTypeAssigned

Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcImpactProtectionDeviceType_.
