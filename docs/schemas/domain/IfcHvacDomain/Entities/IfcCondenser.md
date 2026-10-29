# IfcCondenser

A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCondenserType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no condenser type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCondenserType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Refrigerant

Refrigerant material.

### Object Typing



### Port Nesting



#### SINK_RefrigerantIn_AIRCOOLED_REFRIGERATION

Vapor refrigerant entering the condenser.

#### SOURCE_RefrigerantOut_AIRCOOLED_REFRIGERATION

Liquid refrigerant leaving the condenser.

#### SINK_CompressedAirIn_AIRCOOLED_COMPRESSEDAIR

Cooler air entering the condenser.

#### SOURCE_CompressedAirOut_AIRCOOLED_COMPRESSEDAIR

Warmer air leaving the condenser.

#### SINK_RefrigerantIn_EVAPORATIVECOOLED_REFRIGERATION

Vapor refrigerant entering the condenser.

#### SOURCE_RefrigerantOut_EVAPORATIVECOOLED_REFRIGERATION

Liquid refrigerant leaving the condenser.

#### SINK_CondenserWaterIn_EVAPORATIVECOOLED_CONDENSERWATER

Makeup water entering the condenser.

#### SOURCE_CondenserWaterOut_EVAPORATIVECOOLED_CONDENSERWATER

Purged water leaving the condenser.

#### SINK_VentilationIn_EVAPORATIVECOOLED_VENTILATION

Air entering the condenser.

#### SOURCE_VentilationOut_EVAPORATIVECOOLED_VENTILATION

Air leaving the condenser.

#### SINK_RefrigerantIn_WATERCOOLED_REFRIGERATION

Vapor refrigerant entering the condenser.

#### SOURCE_RefrigerantOut_WATERCOOLED_REFRIGERATION

Liquid refrigerant leaving the condenser.

#### SINK_CondenserWaterIn_WATERCOOLED_CONDENSERWATER

Cooler water entering the condenser, optionally from cooling tower.

#### SOURCE_CondenserWaterOut_WATERCOOLED_CONDENSERWATER

Warmer water leaving the condenser, optionally to cooling tower.

### Property Sets for Objects



### Quantity Sets



