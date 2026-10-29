# IfcCoolingTower

A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCoolingTowerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cooling tower type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCoolingTowerType_.

## Concepts

### Aggregation



#### MECHANICALFORCEDDRAFT_IfcFan

May contain fan components for forcing air into the cooling tower.

#### MECHANICALINDUCEDDDRAFT_IfcFan

May contain fan components for inducing air into the cooling tower.

### Material Set



#### Casing

Material from which the casing is constructed.

#### Fill

Fill material.

### Object Typing



### Port Nesting



#### SINK_CondenserWaterIn_CONDENSERWATER

Warmer water entering the cooling tower.

#### SOURCE_CondenserWaterOut_CONDENSERWATER

Cooler water leaving the cooling tower.

### Property Sets for Objects



### Quantity Sets



