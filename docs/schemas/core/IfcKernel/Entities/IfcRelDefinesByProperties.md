# IfcRelDefinesByProperties

The objectified relationship _IfcRelDefinesByProperties_ defines the relationships between property set definitions and objects. Properties are aggregated in property sets. Property sets can be either directly assigned to occurrence objects using this relationship, or assigned to an object type and assigned via that type to occurrence objects. The assignment of an _IfcPropertySet_ to an _IfcTypeObject_ is not handled via this objectified relationship, but through the direct relationship _HasPropertySets_ on the _IfcTypeObject_.
<!-- end of short definition -->

The _IfcRelDefinesByProperties_ is an N-to-N relationship, as it allows for the assignment of one or more property sets to one or more objects. Those objects then share the same property definition.

> HISTORY New entity in IFC2.0. Has been renamed from _IfcRelAssignsProperties_ in IFC2x.

> IFC4 CHANGE The attribute _RelatedObjects_ has been demoted from the supertype _IfcRelDefines_ to _IfcRelDefinesByProperties_. This relationship has been modified to support multiple property sets referenced by a single relationship.

## Attributes

### RelatedObjects
Reference to the objects (or single object) to which the property definition applies.
> IFC4 CHANGE Data type promoted from subtype _IfcObject_.

### RelatingPropertyDefinition
Reference to the property set definition for that object or set of objects.

## Formal Propositions

### NoRelatedTypeObject
There shall be no related object being of type _IfcTypeObject_.
> NOTE The relationship between a _IfcTypeObject_ and a _IfcPropertySet_ is handled through the direct relationship _HasPropertySets_ on the _IfcTypeObject_.
