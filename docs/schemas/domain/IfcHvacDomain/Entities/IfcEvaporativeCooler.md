# IfcEvaporativeCooler

An evaporative cooler is a device that cools air by saturating it with water vapor.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcEvaporativeCoolerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no evaporative cooler type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcEvaporativeCoolerType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Media

Heat exchanger media material.

### Object Typing



### Port Nesting



#### SINK_WaterIn_DOMESTICCOLDWATER

Incoming water.

#### SINK_AirIn_AIRCONDITIONING

Incoming air.

#### SOURCE_AirOut_AIRCONDITIONING

Outgoing air saturated with vapor.

### Property Sets for Objects



### Quantity Sets



