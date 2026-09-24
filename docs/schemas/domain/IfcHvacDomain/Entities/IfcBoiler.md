# IfcBoiler

A boiler is a closed, pressure-rated vessel in which water or other fluid is heated using an energy source such as natural gas, heating oil, or electricity. The fluid in the vessel is then circulated out of the boiler for use in various processes or heating applications.
<!-- end of short definition -->

_IfcBoiler_ is a vessel solely used for heating of water or other fluids. Storage vessels, such as for drinking water storage are considered as tanks and use the _IfcTank_ entity.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBoilerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no boiler type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBoilerType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Gas_STEAM_GAS

Gas inlet for burner.

#### SOURCE_Exhaust_STEAM_EXHAUST

Exhaust sent to outside.

#### SOURCE_Condenser_STEAM_CONDENSERWATER

Water feed such as from condenser.

#### SOURCE_Heating_STEAM_HEATING

Steam sent to heating coils and space heaters.

#### SINK_Gas_WATER_GAS

Gas inlet for burner.

#### SOURCE_Exhaust_WATER_EXHAUST

Exhaust sent to outside.

#### SINK_ColdWater_WATER_DOMESTICCOLDWATER

Cold water to be heated.

#### SOURCE_HotWater_WATER_DOMESTICHOTWATER

Hot water heated.

### Property Sets for Objects



### Quantity Sets



