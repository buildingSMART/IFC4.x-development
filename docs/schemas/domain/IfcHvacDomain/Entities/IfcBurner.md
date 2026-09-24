# IfcBurner

A burner is a device that converts fuel into heat through combustion. It includes gas, oil, and wood burners.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBurnerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no burner type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBurnerType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Fuel

Material designed to be burned.

### Object Typing



### Port Nesting



#### SINK_Gas_GAS

Gas inlet for burner.

### Property Sets for Objects



### Quantity Sets



