# IfcCableCarrierFitting

A cable carrier fitting is a fitting that is placed at junction or transition in a cable carrier system.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType
Identifies the predefined types of cable carrier fitting from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableCarrierFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable carrier fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableCarrierFittingType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Head_BEND_NOTDEFINED

Head connection.

#### SOURCE_Tail_BEND_NOTDEFINED

Tail connection.

#### SINK_Head_CROSS_NOTDEFINED

Head connection.

#### SOURCE_Tail_CROSS_NOTDEFINED

Tail connection.

#### SOURCE_Left_CROSS_NOTDEFINED

Left connection.

#### SOURCE_Right_CROSS_NOTDEFINED

Right connection.

#### SINK_Head_REDUCER_NOTDEFINED

Head connection.

#### SOURCE_Tail_REDUCER_NOTDEFINED

Tail connection.

#### SINK_Head_TEE_NOTDEFINED

Head connection.

#### SOURCE_Left_TEE_NOTDEFINED

Left connection.

#### SOURCE_Right_TEE_NOTDEFINED

Right connection.

### Property Sets for Objects



### Quantity Sets



