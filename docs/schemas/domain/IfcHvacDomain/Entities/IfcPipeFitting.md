# IfcPipeFitting

A pipe fitting is a junction or transition in a piping flow distribution system used to connect pipe segments, resulting in changes in flow characteristics to the fluid such as direction or flow rate.
<!-- end of short definition -->

Pipe fittings include elbows, junctions, manifolds, and plumbing boxes.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPipeFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no pipe fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPipeFittingType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Coating

The outer coating, if applicable.

#### Insulation

The insulating wrapping, if applicable.

#### Lining

The inner lining, if applicable.

### Object Typing



### Port Nesting



#### SINK_Inlet_BEND_NOTDEFINED

The flow inlet.

#### SOURCE_Outlet_BEND_NOTDEFINED

The flow outlet.

#### SINK_Inlet_CONNECTOR_NOTDEFINED

The flow inlet.

#### SOURCE_Outlet_CONNECTOR_NOTDEFINED

The flow outlet.

#### SOURCE_Outlet_ENTRY_NOTDEFINED

The flow outlet.

#### SINK_Inlet_EXIT_NOTDEFINED

The flow inlet.

#### SINK_Inlet_JUNCTION_NOTDEFINED

The flow inlet.

#### SOURCE_Outlet1_JUNCTION_NOTDEFINED

The left flow outlet.

#### SOURCE_Outlet2_JUNCTION_NOTDEFINED

The right flow outlet.

#### SINK_Inlet_OBSTRUCTION_NOTDEFINED

The flow inlet.

#### SOURCE_Outlet_OBSTRUCTION_NOTDEFINED

The flow outlet.

### Property Sets for Objects



### Quantity Sets



