# IfcTunnelTypicalSection

Interval along the alignment/tunnel with similar conditions.
<!-- end of short definition -->

## Attributes

### PredefinedType
Predefined generic type for a tunnel typical section that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcTunnelTypicalSectionType_ is assigned, providing its own _IfcTunnelTypicalSectionType.PredefinedType_.

## Formal Propositions

### HasObjectType
<!-- FILL IN: prose explaining the rule. EXPRESS body: `(PredefinedType <> IfcTunnelTypicalSectionTypeEnum.USERDEFINED) OR EXISTS(SELF\IfcObject.ObjectType)` -->

