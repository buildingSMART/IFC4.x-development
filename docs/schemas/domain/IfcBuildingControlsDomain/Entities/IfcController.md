# IfcController

A controller is a device that monitors inputs and controls outputs within a building automation system.
<!-- end of short definition -->

A controller may be physical (having placement within a spatial structure) or logical (a software interface or aggregated within a programmable physical controller).

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcControllerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no controller type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcControllerType_.

## Concepts

### Aggregation

Figure 1 illustrates controller composition use.

![Composition Use Definition](../../../../figures/ifccontroller-composition.png "Figure 1 — Controller composition use")

#### PROGRAMMABLE_IfcController

May contain IfcController components. Programmable Logic Controllers may be decomposed into logical elements for values and operations.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Input_FLOATING_SIGNAL

Receives the first parameter.

#### SINK_Modifier_FLOATING_SIGNAL

Receives the second parameter (if applicable).

#### SOURCE_Output_FLOATING_SIGNAL

Sets the output value.

#### SINK_Input_MULTIPOSITION_SIGNAL

Receives the first parameter.

#### SINK_Modifier_MULTIPOSITION_SIGNAL

Receives the second parameter (if applicable).

#### SOURCE_Output_MULTIPOSITION_SIGNAL

Sets the output value.

#### SINK_Power_PROGRAMMABLE_ELECTRICAL

Receives electrical power.

#### SINK_Control_PROGRAMMABLE_CONTROL

Direct communication to the device (e.g. serial port).

#### SOURCE_Data_PROGRAMMABLE_DATA

Network communication to the device (e.g. TCP/IP network).

#### SINK_Input1_PROGRAMMABLE_SIGNAL

Analog or digital inputs.

#### SOURCE_Output1_PROGRAMMABLE_SIGNAL

Analog or digital outputs.

#### SINK_Input_PROPORTIONAL_SIGNAL

Receives the first parameter.

#### SINK_Modifier_PROPORTIONAL_SIGNAL

Receives the second parameter (if applicable).

#### SOURCE_Output_PROPORTIONAL_SIGNAL

Sets the output value.

#### SINK_Input_TWOPOSITION_SIGNAL

Receives the first parameter.

#### SINK_Modifier_TWOPOSITION_SIGNAL

Receives the second parameter (if applicable).

#### SOURCE_Output_TWOPOSITION_SIGNAL

Sets the output value.

### Property Sets for Objects



### Quantity Sets



