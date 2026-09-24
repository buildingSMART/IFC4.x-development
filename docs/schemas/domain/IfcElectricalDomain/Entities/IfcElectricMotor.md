# IfcElectricMotor

An electric motor is an engine that is a machine for converting electrical energy into mechanical energy.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricMotorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric motor type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricMotorType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_ELECTRICAL

Receives electrical power.

#### SOURCE_Drive_NOTDEFINED

Motor connection to a driven device.

### Property Sets for Objects



### Quantity Sets



