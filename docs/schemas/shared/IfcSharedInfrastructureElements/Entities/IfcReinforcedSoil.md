# IfcReinforcedSoil

Soil reinforced or stabilized by some mechanical or chemical method.
<!-- end of short definition -->

> DEPRECATION The entity _IfcReinforcedSoil_ shall not be used anymore, use the more generic _IfcImprovedGround_ instead.

## Attributes

### PredefinedType
Identifies the predefined type of a reinforced soil elements. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
