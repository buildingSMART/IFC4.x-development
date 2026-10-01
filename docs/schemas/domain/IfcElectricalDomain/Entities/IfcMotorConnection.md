# IfcMotorConnection

A motor connection provides the means for connecting a motor as the driving device to the driven device.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcMotorConnectionType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no motor connection type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcMotorConnectionType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Motor_NOTDEFINED

Connection from the motor.

#### SOURCE_Motor_NOTDEFINED

Connection to the driven device.

### Property Sets for Objects



### Quantity Sets



