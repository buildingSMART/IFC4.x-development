# IfcEvaporator

An evaporator is a device in which a liquid refrigerent is vaporized and absorbs heat from the surrounding fluid.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcEvaporatorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no evaporator type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcEvaporatorType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Refrigerant

Refrigerant material.

### Object Typing



### Port Nesting



#### SINK_RefrigerantIn_DIRECTEXPANSION_REFRIGERATION

Liquid refrigerant entering the evaporator.

#### SINK_RefrigerantOut_DIRECTEXPANSION_REFRIGERATION

Liquid refrigerant entering the evaporator.

#### SINK_AirIn_DIRECTEXPANSION_AIRCONDITIONING

Air return entering the evaporator.

#### SOURCE_AirOut_DIRECTEXPANSION_AIRCONDITIONING

Air supply leaving the evaporator.

#### SINK_RefrigerantIn_FLOODEDSHELLANDTUBE_REFRIGERATION

Liquid refrigerant entering the evaporator.

#### SINK_RefrigerantOut_FLOODEDSHELLANDTUBE_REFRIGERATION

Liquid refrigerant entering the evaporator.

#### SINK_ChilledWaterIn_FLOODEDSHELLANDTUBE_CHILLEDWATER

Chilled water return entering the evaporator.

#### SOURCE_ChilledWaterOut_FLOODEDSHELLANDTUBE_CHILLEDWATER

Chilled water supply leaving the evaporator.

#### SINK_RefrigerantIn_SHELLANDCOIL_REFRIGERATION

Liquid refrigerant entering the evaporator.

#### SINK_RefrigerantOut_SHELLANDCOIL_REFRIGERATION

Vapor refrigerant leaving the evaporator.

#### SINK_ChilledWaterIn_FLOODEDSHELLANDTUBE_CHILLEDWATER

Chilled water return entering the evaporator.

#### SOURCE_ChilledWaterOut_FLOODEDSHELLANDTUBE_CHILLEDWATER

Chilled water supply leaving the evaporator.

### Property Sets for Objects



### Quantity Sets



