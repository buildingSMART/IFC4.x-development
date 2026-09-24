# IfcFan

A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFanType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no fan type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcFanType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Wheel

Material from which the fan wheel is constructed.

### Object Typing



### Port Nesting



#### SINK_AirIn_NOTDEFINED

Incoming air.

#### SOURCE_AirOut_NOTDEFINED

Outgoing air.

### Property Sets for Objects



### Quantity Sets



