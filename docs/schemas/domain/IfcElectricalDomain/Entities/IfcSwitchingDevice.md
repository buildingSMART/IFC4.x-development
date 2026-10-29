# IfcSwitchingDevice

A switch is used in a cable distribution system (electrical circuit) to control or modulate the flow of electricity.
<!-- end of short definition -->

Switches include those used for electrical power, communications, audio-visual, or other distribution system types as determined by the available ports.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSwitchingDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no switching device type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSwitchingDeviceType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Conductor

Material from which the conductors are constructed.

#### Surface

Material from which the switch surface is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_ELECTRICAL

The supply line.

#### SOURCE_Load_ELECTRICAL

The load controlled by the switch.

### Property Sets for Objects



### Quantity Sets



