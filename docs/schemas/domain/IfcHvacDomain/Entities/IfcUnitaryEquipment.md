# IfcUnitaryEquipment

Unitary equipment typically combine a number of components into a single product, such as air handlers, pre-packaged rooftop air-conditioning units, heat pumps, and split systems.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcUnitaryEquipmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no unitary equipment type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcUnitaryEquipmentType_.

## Concepts

### Aggregation



#### IfcDistributionElement

Unitary equipment (air handlers in particular) may elaborate contained elements such as dampers, fans, coils, sensors, actuators, and controllers. Such breakdown provides access to component information and tracking of performance history for embedded elements.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_ReturnAirIn_AIRHANDLER_AIRCONDITIONING

Return air entering mixture or exhausted.

#### SOURCE_SupplyAirOut_AIRHANDLER_AIRCONDITIONING

Chilled supply air.

#### SINK_OutsideAirIn_AIRHANDLER_VENTILATION

Outside air entering mixture.

#### SOURCE_ExhaustAirOut_AIRHANDLER_EXHAUST

Exhaust air leaving to outside.

#### SINK_ChilledWaterIn_AIRHANDLER_CHILLEDWATER

Chilled water entering cooling coil.

#### SOURCE_ChilledWaterOut_AIRHANDLER_CHILLEDWATER

Chilled water leaving cooling coil.

#### SINK_HeatingIn_AIRHANDLER_HEATING

Steam entering heating coil.

#### SOURCE_HeatingOut_AIRHANDLER_HEATING

Steam leaving heating coil.

#### SINK_Power_AIRHANDLER_ELECTRICAL

Electrical power source.

#### SINK_Control_AIRHANDLER_CONTROL

Control system communication.

### Property Sets for Objects



### Quantity Sets



