# IfcSanitaryTerminal

A sanitary terminal is a fixed appliance or terminal usually supplied with water and used for drinking, cleaning or foul water disposal or that is an item of equipment directly used with such an appliance or terminal.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType


### CorrectTypeAssigned
Either there is no sanitary terminal type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSanitaryTerminalType_.

## Concepts

### Element Nesting

> EXAMPLE A faucet mounted to sink that provides cold and/or hot water can be nested.

> IFC4 ADD1 CHANGE Element nesting is now used for attaching faucets. Hot and cold water ports have been removed from subtypes that use attached faucets.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SOURCE_Drainage_BATH_DRAINAGE

Drainage.

#### SINK_ColdWater_BIDET_DOMESTICCOLDWATER

Cold water supply.

#### SINK_HotWater_BIDET_DOMESTICHOTWATER

Hot water supply.

#### SOURCE_Drainage_BIDET_DRAINAGE

Drainage.

#### SINK_ColdWater_CISTERN_DOMESTICCOLDWATER

Cold water supply.

#### SINK_HotWater_CISTERN_DOMESTICHOTWATER

Hot water supply.

#### SOURCE_Drainage_CISTERN_DRAINAGE

Drainage.

#### SINK_ColdWater_SANITARYFOUNTAIN_DOMESTICCOLDWATER

Cold water supply.

#### SINK_HotWater_SANITARYFOUNTAIN_DOMESTICHOTWATER

Hot water supply.

#### SOURCE_Drainage_SANITARYFOUNTAIN_DRAINAGE

Drainage.

#### SOURCE_Drainage_SHOWER_DRAINAGE

Drainage.

#### SOURCE_Drainage_SINK_DRAINAGE

Drainage.

#### SINK_ColdWater_TOILETPAN_DOMESTICCOLDWATER

Cold water supply.

#### SOURCE_Drainage_TOILETPAN_DRAINAGE

Drainage.

#### SINK_ColdWater_URINAL_DOMESTICCOLDWATER

Cold water supply.

#### SOURCE_Drainage_URINAL_DRAINAGE

Drainage.

#### SINK_ColdWater_WASHHANDBASIN_DOMESTICCOLDWATER

Cold water supply.

#### SINK_HotWater_WASHHANDBASIN_DOMESTICHOTWATER

Hot water supply.

#### SOURCE_Drainage_WASHHANDBASIN_DRAINAGE

Drainage.

### Property Sets for Objects



### Quantity Sets



