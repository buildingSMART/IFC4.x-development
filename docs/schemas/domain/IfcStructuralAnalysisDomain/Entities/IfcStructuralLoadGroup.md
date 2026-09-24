# IfcStructuralLoadGroup

The entity _IfcStructuralLoadGroup_ is used to structure the physical impacts. By using the grouping features inherited from _IfcGroup_, instances of _IfcStructuralAction_ (or its subclasses) and of _IfcStructuralLoadGroup_ can be used to define load groups, load cases and load combinations. (See also _IfcLoadGroupTypeEnum_.)
<!-- end of short definition -->

> NOTE Important functionality for the description of a load-bearing system is derived from the existing IFC entity _IfcGroup_. This class provides, via the relationship class _IfcRelAssignsToGroup_, the needed grouping mechanism. In this way, instances of _IfcStructuralAction_ belonging to a specific load group can be unambiguously determined.

> NOTE The relationship class _IfcRelAssignsToGroupByFactor_ is used to group load cases into load combinations. The factor provided in this assignment relationship is to applied together with the optional _IfcStructuralLoadGroup.Coefficient_. Unlike this coefficient which always affects the load group, the _IfcRelAssignsToGroupByFactor.Factor_ is specific for a load case—load combination pair. As many instances of _IfcRelAssignsToGroupByFactor_ are used within one load combination as there are different _Factor_s to be applied to load cases in the load combination. On the other hand, a load case may appear in more than one load combination and can have a different _Factor_ in each assignment by _IfcRelAssignsToGroupByFactor_.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Subtype _IfcStructuralLoadCase_ added. Informal propositions and WHERE rule added. Predefined type LOAD_COMBINATION_GROUP made obsolete and removed.

**Informal Propositions**

1. Load groups of type LOAD_GROUP shall only contain instances of _IfcStructuralAction_.
2. Load groups of type LOAD_CASE shall always be instantiated from the subtype _IfcStructuralLoadCase_, not directly from the generic type _IfcStructuralLoadGroup_ itself.
3. Instances of _IfcStructuralLoadCase_ shall only contain instances of _IfcStructuralAction_ or/ and instances of _IfcStructuralLoadGroup_ of type LOAD_GROUP.
4. Load groups of type LOAD_COMBINATION shall only contain instances of _IfcStructuralLoadCase_.

## Attributes

### PredefinedType
Selects a predefined type for the load group. It can be differentiated between load groups, load cases, load combinations, or userdefined grouping levels.

### ActionType
Type of actions in the group. Normally needed if 'PredefinedType' specifies a LOAD_CASE.

### ActionSource
Source of actions in the group. Normally needed if 'PredefinedType' specifies a LOAD_CASE.

### Coefficient
Load factor. If omitted, a factor is not yet known or not specified. A load factor of 1.0 shall be explicitly exported as Coefficient = 1.0.

### Purpose
Description of the purpose of this instance. Among else, possible values of the Purpose of load combinations are 'SLS', 'ULS', 'ALS' to indicate serviceability, ultimate, or accidental limit state.

### SourceOfResultGroup
Results which were computed using this load group.

### LoadGroupFor
Analysis models in which this load group is used.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type, action type, or action source is set to USERDEFINED.

## Concepts

### Group Assignment



#### IfcStructuralLoadCase

Structural load cases applicable to the load group.

