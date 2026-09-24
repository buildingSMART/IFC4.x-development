# IfcElectricAppliance

An electric appliance is a device intended for consumer usage that is powered by electricity.
<!-- end of short definition -->

Electric appliances may be fixed in place or may be able to be moved from one space to another. Electric appliances require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricApplianceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric appliance type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricApplianceType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Power_DISHWASHER_ELECTRICAL

Receives electrical power.

#### SINK_HotWater_DISHWASHER_DOMESTICHOTWATER

Hot water used for washing dishes.

#### SOURCE_Drainage_DISHWASHER_DRAINAGE

Drainage from used water.

#### SINK_Power_ELECTRICCOOKER_ELECTRICAL

Receives electrical power.

#### SINK_Power_FREEZER_ELECTRICAL

Receives electrical power.

#### SINK_Power_FRIDGE_FREEZER_ELECTRICAL

Receives electrical power.

#### SINK_ColdWater_FRIDGE_FREEZER_DOMESTICCOLDWATER

Cold water used for icemaking and/or drinking water.

#### SINK_Power_HANDDRYER_ELECTRICAL

Receives electrical power.

#### SINK_Power_MICROWAVE_ELECTRICAL

Receives electrical power.

#### SINK_Power_REFRIGERATOR_ELECTRICAL

Receives electrical power.

#### SINK_Power_TUMBLEDRYER_ELECTRICAL

Receives electrical power.

#### SINK_Gas_TUMBLEDRYER_GAS

Gas source if applicable.

#### SINK_Exhaust_TUMBLEDRYER_EXHAUST

Exhaust air.

#### SINK_Power_WASHINGMACHINE_ELECTRICAL

Receives electrical power.

#### SINK_ColdWater_WASHINGMACHINE_DOMESTICCOLDWATER

Cold water used for washing.

#### SINK_HotWater_WASHINGMACHINE_DOMESTICHOTWATER

Hot water used for washing.

#### SOURCE_Drainage_WASHINGMACHINE_DRAINAGE

Drainage from used water.

### Property Sets for Objects



### Quantity Sets



