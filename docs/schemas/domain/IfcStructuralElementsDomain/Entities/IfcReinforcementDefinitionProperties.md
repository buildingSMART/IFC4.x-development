# IfcReinforcementDefinitionProperties

_IfcReinforcementDefinitionProperties_ defines the cross section properties of reinforcement included in reinforced concrete building elements. The property set definition may be used both in conjunction with insitu and precast structures.
<!-- end of short definition -->

This subtype of _IfcPropertySetDefinition_ is used to define the reinforcement properties in early design stages, such as in requirement definition or scheme design. In later design stages explicit instances of subtypes of _IfcReinforcingElement_ are used. The intended usage may be indicated using the _DefinitionType_ attribute value as a designator: recommended values are 'Reinforcement area requirement' or 'Reinforcement configuration requirement'. Other values may be used according to local standards.

Only one property set definition of this kind is used for each concrete building element in each intended usage indicated by the _DefinitionType_ attribute value. This set then defines a list of cross section properties in a discrete number of longitudinal sections as instances of _IfcSectionReinforcementProperties_ (one for each structural reinforcement bar role), which in turn have a section cross section property defined as a profile and a number of reinforcement properties, one for each steel grade / bar type.

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Supertype changed from _IfcPropertySetDefinition_ to _IfcPreDefinedPropertySet_

## Attributes

### DefinitionType
Descriptive type name applied to reinforcement definition properties.

### ReinforcementSectionDefinitions
The list of section reinforcement properties attached to the reinforcement definition properties.
