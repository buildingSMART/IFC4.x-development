# IfcLiquidTerminal

A liquid terminal is a terminating or origination point for the transfer of liquid between distribution system(s). this is the point where the liquid distribution system interacts with the external environment. An example of this is a loading arm for the transfer of liquid from a docked vessel.
<!-- end of short definition -->

## Attributes

### PredefinedType
Identifies the predefined type of a liquid terminal. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcLiquidTerminalType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcLiquidTerminalType_.
