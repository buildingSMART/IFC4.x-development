# IfcConstructionEquipmentResourceType

The resource type _IfcConstructionEquipmentResourceType_ defines commonly shared information for occurrences of construction equipment resources. The set of shared information may include:

* common productivities
* common cost rates
* common properties within shared property sets
<!-- end of short definition -->

It is used to define a construction equipment resource specification (the specific resource information that is common to all occurrences of that resource). Resource types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcConstructionEquipmentResourceType_ are represented by instances of _IfcConstructionEquipmentResource_.

> HISTORY New entity in IFC4.

Assignment use definition

In addition to assignments specified at the base class _IfcConstructionResourceType_, a construction equipment resource type may have assignments of its own using _IfcRelAssignsToResource_ where _RelatingResource_ refers to the _IfcConstructionEquipmentResourceType_ and _RelatedObjects_ contains one or more _IfcTypeProduct_ subtypes. Such relationship indicates the type of equipment to be used as input, which is instantiated as an occurrence assigned for each resource occurrence. There may be multiple chains of production where such product type may have its own task and resource types assigned indicating how to assemble such equipment.

## Attributes

### PredefinedType
Defines types of construction equipment resources.

## Formal Propositions

### CorrectPredefinedType

