# IfcConstructionMaterialResourceType

The resource type _IfcConstructionMaterialResourceType_ defines commonly shared information for occurrences of construction material resources. The set of shared information may include:

* common productivities
* common cost rates
* common properties within shared property sets
<!-- end of short definition -->

It is used to define a construction material resource specification (the specific resource information that is common to all occurrences of that resource). Resource types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcConstructionMaterialResourceType_ are represented by instances of _IfcConstructionMaterialResource_.

> HISTORY New entity in IFC4.

Assignment Use Definition

In addition to assignments specified at the base class _IfcConstructionResourceType_, a construction material resource type may have assignments of its own using _IfcRelAssignsToResource_ where _RelatingResource_ refers to the _IfcConstructionMaterialResourceType_ and _RelatedObjects_ contains one or more _IfcTypeProduct_ subtypes. Such relationship indicates material specifications to be used as input, which is instantiated as an occurrence assigned for each resource occurrence. The _IfcGeographicElementType_ product type may be used to hold the material representation (via _IfcRelAssociatesMaterial_. There may be multiple chains of production where such product type may have its own task and resource types assigned indicating how to transport or extract such material.

## Attributes

### PredefinedType
Defines types of construction material resources.

## Formal Propositions

### CorrectPredefinedType

