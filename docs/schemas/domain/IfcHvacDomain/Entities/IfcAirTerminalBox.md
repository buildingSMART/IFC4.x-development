# IfcAirTerminalBox

An air terminal box typically participates in an HVAC duct distribution system and is used to control or modulate the amount of air delivered to its downstream ductwork. An air terminal box type is often referred to as an "air flow regulator".
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAirTerminalBoxType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no air terminal box type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAirTerminalBoxType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Inlet_AIRCONDITIONING

Incoming air.

#### SOURCE_Outlet_AIRCONDITIONING

Outgoing regulated air.

### Property Sets for Objects



### Quantity Sets



