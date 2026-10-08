# IfcStructuralResultGroup

Instances of the entity _IfcStructuralResultGroup_ are used to group results of structural analysis calculations and to capture the connection to the underlying basic load group. The basic functionality for grouping inherited from _IfcGroup_ is used to collect instances from _IfcStructuralReaction_ or its respective subclasses.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE WHERE rule added.

## Attributes

### TheoryType
Specifies the analysis theory used to obtain the respective results.

### ResultForLoadGroup
Reference to an instance of IfcStructuralLoadGroup for which this instance represents the result.

### IsLinear
This value allows to easily recognize whether a linear analysis has been applied (allowing the superposition of analysis results).

### ResultGroupFor
Reference to an instance of IfcStructuralAnalysisModel for which this instance captures a result.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the analysis theory type is set to USERDEFINED.

## Concepts

### Group Assignment



#### IfcStructuralReaction

Structural reactions of the result group.

