# IfcAirTerminal

An air terminal is a terminating or origination point for the transfer of air between distribution system(s) and one or more spaces. It can also be used for the transfer of air between adjacent spaces.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAirTerminalType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no air terminal type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAirTerminalType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Air_DIFFUSER_AIRCONDITIONING

Supply air, typically connected from a duct segment or fitting.

#### SOURCE_Air_GRILLE_VENTILATION

Return air, typically connected to a duct segment or fitting.

#### SINK_Air_REGISTER_AIRCONDITIONING

Supply air, typically connected from a duct segment or fitting.

### Property Sets for Objects



### Quantity Sets



