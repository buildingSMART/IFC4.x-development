# IfcValve

A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcValveType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no valve type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcValveType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Operation

Material from which the operating mechanism (such as gate, globe, plug, needle, or clack) of the valve is constructed.

### Object Connectivity



#### IfcRelFlowControlElements_IfcActuator

Indicates an actuator operating on the valve.

### Object Typing



### Port Nesting



#### SINK_Inlet_AIRHANDLER_NOTDEFINED

Incoming fluid.

#### SOURCE_Outlet_ANTIVACUUM_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_CHANGEOVER_NOTDEFINED

Incoming fluid.

#### SINK_Outlet1_CHANGEOVER_NOTDEFINED

Switched outgoing fluid.

#### SINK_Outlet2_CHANGEOVER_NOTDEFINED

Switched outgoing fluid.

#### SINK_Inlet_CHECK_NOTDEFINED

Incoming fluid.

#### SINK_Outlet_CHECK_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_COMMISSIONING_NOTDEFINED

Incoming fluid.

#### SOURCE_Outlet_COMMISSIONING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_DIVERTING_NOTDEFINED

Incoming fluid.

#### SINK_Outlet1_DIVERTING_NOTDEFINED

Outgoing fluid.

#### SINK_Outlet2_DIVERTING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_DOUBLECHECK_NOTDEFINED

Incoming fluid.

#### SINK_Outlet_DOUBLECHECK_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_DOUBLEREGULATING_NOTDEFINED

Incoming fluid.

#### SINK_Outlet_DOUBLEREGULATING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_DRAWOFFCOCK_NOTDEFINED

Incoming fluid.

#### SINK_Inlet_FAUCET_NOTDEFINED

Incoming fluid.

#### SINK_Inlet_FLUSHING_NOTDEFINED

Incoming fluid.

#### SINK_Outlet_FLUSHING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_GASCOCK_GAS

Incoming fluid.

#### SINK_Inlet_GASTAP_GAS

Incoming fluid.

#### SINK_Inlet_ISOLATING_GAS

Incoming fluid.

#### SOURCE_Outlet_ISOLATING_GAS

Outgoing fluid.

#### SINK_Inlet1_MIXING_NOTDEFINED

Incoming fluid to be mixed.

#### SINK_Inlet2_MIXING_NOTDEFINED

Incoming fluid to be mixed.

#### SOURCE_Outlet_MIXING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_PRESSUREREDUCING_NOTDEFINED

Incoming fluid.

#### SOURCE_Outlet_PRESSUREREDUCING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_PRESSURERELIEF_NOTDEFINED

Incoming fluid.

#### SINK_Inlet_REGULATING_NOTDEFINED

Incoming fluid.

#### SOURCE_Inlet_REGULATING_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_SAFETYCUTOFF_NOTDEFINED

Incoming fluid.

#### SOURCE_Outlet_SAFETYCUTOFF_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_STEAMTRAP_NOTDEFINED

Incoming fluid.

#### SOURCE_Outlet_STEAMTRAP_NOTDEFINED

Outgoing fluid.

#### SINK_Inlet_STOPCOCK_NOTDEFINED

Incoming fluid.

### Property Sets for Objects



### Quantity Sets



