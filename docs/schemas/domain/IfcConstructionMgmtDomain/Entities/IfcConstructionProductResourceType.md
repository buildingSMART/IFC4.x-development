# IfcConstructionProductResourceType

The resource type _IfcConstructionProductResourceType_ defines commonly shared information for occurrences of construction product resources. The set of shared information may include:

* common productivities
* common cost rates
* common properties within shared property sets
<!-- end of short definition -->

It is used to define a construction product resource specification (i.e. the specific resource information that is common to all occurrences of that resource). Resource types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcConstructionProductResourceType_ are represented by instances of _IfcConstructionProductResource_.

> HISTORY New entity in IFC4.

Assignment use definition

In addition to assignments specified at the base class _IfcConstructionResourceType_, a construction product resource type may have assignments of its own using _IfcRelAssignsToResource_ where _RelatingResource_ refers to the _IfcConstructionProductResourceType_ and _RelatedObjects_ contains one or more _IfcTypeProduct_ subtypes. Such relationship indicates the type of product to be used as input, which is instantiated as an occurrence assigned for each resource occurrence. There may be multiple chains of production where such product type may have its own task and resource types assigned.

## Attributes

### PredefinedType
Defines types of construction product resources.

## Formal Propositions

### CorrectPredefinedType

