# IfcTransformer

A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.
<!-- end of short definition -->

_IfcTransformer_ is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: _IfcController_ converts arbitrary signals, _IfcAudioVisualAppliance_ converts signals for audio or video streams, and _IfcCommunicationsAppliance_ converts signals for data or other communications usage.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTransformerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no transformer type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcTransformerType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_ELECTRICAL

Line to be transformed.

#### SOURCE_Load_ELECTRICAL

Transformed load.

### Property Sets for Objects



### Quantity Sets



