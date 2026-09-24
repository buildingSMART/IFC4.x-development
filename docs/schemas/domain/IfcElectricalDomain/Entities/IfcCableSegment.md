# IfcCableSegment

A cable segment is a flow segment used to carry electrical power, data, or telecommunications signals.
<!-- end of short definition -->

A cable segment is used to typically join two sections of an electrical network or a network of components carrying the electrical service.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType
Identifies the predefined types of cable segment from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableSegmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable segment type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableSegmentType_.

## Concepts

### Aggregation



#### CORESEGMENT_CABLESEGMENT_IfcCableSegment

Cable segments may be aggregated into cable cores.

#### CONDUCTORSEGMENT_CORESEGMENT_IfcCableSegment

Cable cores may be aggregated into cable conductors.

### Material Set



#### Conductor

Material from which the conductors are constructed, such as Aluminium or Copper.

#### Insulation

The material from which the insulation is constructed such as PVC, PEX, or EPR.

#### Screen

The material from which the screen that covers the sheath is constructed (mantel) such as Aluminium, Copper, Steel, or Lead.

#### Sheath

The outer sheathing of the cable which may be color-coded.

### Object Typing



### Port Nesting



#### SINK_Input_NOTDEFINED

The input end of the cable. While many cables may be bidirectional, port direction is indicated for connectivity purposes.

#### SOURCE_Output_NOTDEFINED

The output end of the cable. While many cables may be bidirectional, port direction is indicated for connectivity purposes.

### Property Sets for Objects



### Quantity Sets



