# IfcCableCarrierSegment

A cable carrier segment is a flow segment that is specifically used to carry and support cabling.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType
Identifies the predefined types of cable carrier segment from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableCarrierSegmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable carrier segment type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableCarrierSegmentType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Head_NOTDEFINED

Head connection.

#### SOURCE_Tail_NOTDEFINED

Tail connection.

### Property Sets for Objects



### Quantity Sets



