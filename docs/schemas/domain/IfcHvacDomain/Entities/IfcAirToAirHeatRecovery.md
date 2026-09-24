# IfcAirToAirHeatRecovery

An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAirToAirHeatRecoveryType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no air-to-air heat recovery type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAirToAirHeatRecoveryType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Media

The primary media material used for heat transfer.

### Object Typing



### Port Nesting



#### SINK_AirInlet_AIRCONDITIONING

Conditioned air in.

#### SOURCE_AirOutlet_AIRCONDITIONING

Conditioned air out.

#### SINK_ExhaustInlet_AIRCONDITIONING

Exhausted air in.

#### SOURCE_ExhaustOutlet_AIRCONDITIONING

Exhausted air out.

### Property Sets for Objects



### Quantity Sets



