# IfcConveyorSegment

A conveyor segment defines an occurrence of a flow segment/ continuous run within a conveyor system that joins two sections of the system. these can utilise different carrying methods such as belt, rope, chain, screw etc.
<!-- end of short definition -->

> NOTE Definition according to ISO6707-1: machine that continuously transports material or objects along a gentle slope using an endless belt, rope or chain, or rollers.

## Attributes

### PredefinedType
Identifies the predefined type of a conveyor segment. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcConveyorSegmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcConveyorSegmentType_.
