# IfcCoil

A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.
<!-- end of short definition -->

Coils may also be used for non-airflow cases such as embedded in a floor slab.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCoilType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no coil type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCoilType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_RefrigerantIn_DXCOOLINGCOIL_REFRIGERATION

Refrigerant entering the coil.

#### SOURCE_RefrigerantOut_DXCOOLINGCOIL_REFRIGERATION

Refrigerant leaving the coil.

#### SINK_AirIn_DXCOOLINGCOIL_AIRCONDITIONING

Air entering the surface of the coil.

#### SOURCE_AirOut_DXCOOLINGCOIL_AIRCONDITIONING

Air leaving the surface of the coil.

#### SINK_ChilledWaterIn_WATERCOOLINGCOIL_CHILLEDWATER

Chilled water entering the coil.

#### SOURCE_ChilledWaterOut_WATERCOOLINGCOIL_CHILLEDWATER

Chilled water leaving the coil.

#### SINK_AirIn_WATERCOOLINGCOIL_AIRCONDITIONING

Air entering the surface of the coil.

#### SOURCE_AirOut_WATERCOOLINGCOIL_AIRCONDITIONING

Air leaving the surface of the coil.

#### SINK_HeatingIn_WATERHEATINGCOIL_HEATING

Heated water entering the coil.

#### SOURCE_HeatingOut_WATERHEATINGCOIL_HEATING

Heated water leaving the coil.

#### SINK_AirIn_WATERHEATINGCOIL_AIRCONDITIONING

Air entering the surface of the coil.

#### SOURCE_AirOut_WATERHEATINGCOIL_AIRCONDITIONING

Air leaving the surface of the coil.

### Property Sets for Objects



### Quantity Sets



