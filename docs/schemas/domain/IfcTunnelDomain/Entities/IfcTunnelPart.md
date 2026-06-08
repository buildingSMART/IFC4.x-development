# IfcTunnelPart

A part of a tunnel.
<!-- end of short definition -->

## Attributes

### PredefinedType
Identifies the predefined type of a tunnel part element. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
