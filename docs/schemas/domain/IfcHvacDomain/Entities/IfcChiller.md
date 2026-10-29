# IfcChiller

A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcChillerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no chiller type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcChillerType_.

## Concepts

### Aggregation



#### IfcDistributionElement

Chillers may aggregate distribution flow elements forming a refrigeration cycle (compressor, condenser, valve, evaporator), as well as control elements.

### Material Set



#### Casing

Material from which the casing is constructed.

#### Refrigerant

Refrigerant material.

### Object Typing



### Port Nesting



#### SINK_Power_AIRCOOLED_ELECTRICAL

Receives electrical power.

#### SINK_Control_AIRCOOLED_CONTROL

Control unit accessing internal sensors and actuators.

#### SINK_ChilledWaterIn_AIRCOOLED_CHILLEDWATER

Chilled water return.

#### SOURCE_ChilledWaterOut_AIRCOOLED_CHILLEDWATER

Chilled water supply.

#### SINK_VentilationIn_AIRCOOLED_VENTILATION

Incoming cooler air.

#### SOURCE_VentilationOut_AIRCOOLED_VENTILATION

Outgoing hotter air.

#### SINK_Power_WATERCOOLED_ELECTRICAL

Receives electrical power.

#### SINK_Control_WATERCOOLED_CONTROL

Control unit accessing internal sensors and actuators.

#### SINK_ChilledWaterIn_WATERCOOLED_CHILLEDWATER

Chilled water return.

#### SOURCE_ChilledWaterOut_WATERCOOLED_CHILLEDWATER

Chilled water supply.

#### SINK_CondenserWaterIn_WATERCOOLED_CONDENSERWATER

Incoming cooler condenser water.

#### SOURCE_CondenserWaterOut_WATERCOOLED_CONDENSERWATER

Outgoing hotter condenser water.

### Property Sets for Objects



### Quantity Sets



