# IfcCableFitting

A cable fitting is a fitting that is placed at a junction, transition or termination in a cable system.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType
Identifies the predefined types of cable fitting from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableFittingType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Conductor

Material from which the conductors are constructed, such as Aluminium or Copper.

### Object Connectivity



#### ENTRY_IfcRelConnectsElements_IfcPipeSegment

For equipotential bonding, may represent a clamp that is attached from a pipe or other conducting element of an earthing system.

#### EXIT_IfcRelConnectsElements_IfcPipeSegment

For equipotential bonding, may represent a clamp that is attached from a pipe or other conducting element of an earthing system.

### Object Typing



### Port Nesting



#### SINK_Input_CONNECTOR_NOTDEFINED

The input of the connector.

#### SOURCE_Output_CONNECTOR_NOTDEFINED

The output of the connector.

#### SOURCE_Output_ENTRY_NOTDEFINED

The output of the connector.

#### SINK_Input_EXIT_NOTDEFINED

The input of the connector.

#### SINK_Input_JUNCTION_NOTDEFINED

The input of the connector.

#### SOURCE_Output1_JUNCTION_NOTDEFINED

An output of the connector.

#### SOURCE_Output2_JUNCTION_NOTDEFINED

An output of the connector.

#### SINK_Input_CONNECTOR_NOTDEFINED

The input of the connector.

#### SOURCE_Output_CONNECTOR_NOTDEFINED

The output of the connector.

### Property Sets for Objects



### Quantity Sets



