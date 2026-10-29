# IfcOutlet

An outlet is a device installed at a point to receive one or more inserted plugs for electrical power or communications.
<!-- end of short definition -->

Power outlets are commonly connected within a junction box; data outlets may be directly connected to a wall. For power outlets sharing the same circuit within a junction box, the ports should indicate the logical wiring relationship to the enclosing junction box, even though they may be physically connected to a cable going to another outlet, switch, or fixture.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcOutletType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no outlet type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcOutletType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Conductor

Material from which the conductors are constructed.

#### Surface

Material from which the outer plate is constructed.

### Object Typing



### Port Nesting



#### SINK_Line1_DATAOUTLET_DATA

A data line, connecting to a cable commonly originating from a port on a router.

#### SINK_Line2_DATAOUTLET_DATA

A data line, connecting to a cable commonly originating from a port on a router.

#### SOURCE_Jack1_DATAOUTLET_DATA

Jacks in order of layout, going to the right and then down, which may accept a cable.

#### SOURCE_Jack2_DATAOUTLET_DATA

Jacks in order of layout, going to the right and then down, which may accept a cable.

#### SINK_Line1_POWEROUTLET_ELECTRICAL

The source of power, which may refer to a port on a junction box.

#### SOURCE_Jack1_POWEROUTLET_ELECTRICAL

Upper jack, accepting a plug from an appliance or fixture.

#### SOURCE_Jack1_POWEROUTLET_ELECTRICAL

Lower jack, accepting a plug from an appliance or fixture.

#### SINK_Line1_TELEPHONEOUTLET_TELEPHONE

A telephone line, connecting to a cable originating from a telecommunications distribution board.

#### SINK_Line2_TELEPHONEOUTLET_TELEPHONE

A telephone line, connecting to a cable originating from a telecommunications distribution board.

#### SINK_Jack1_TELEPHONEOUTLET_TELEPHONE

Jacks in order of layout, going to the right and then down, which may accept a cable.

#### SINK_Jack2_TELEPHONEOUTLET_TELEPHONE

Jacks in order of layout, going to the right and then down, which may accept a cable.

### Property Sets for Objects



### Quantity Sets



