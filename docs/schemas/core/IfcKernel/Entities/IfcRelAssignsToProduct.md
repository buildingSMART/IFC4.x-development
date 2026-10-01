# IfcRelAssignsToProduct

The objectified relationship _IfcRelAssignsToProduct_ handles the assignment of objects (subtypes of _IfcObject_) to a product (subtypes of _IfcProduct_). The _Name_ attribute should be used to classify the usage of the _IfcRelAssignsToProduct_ objectified relationship. The following _Name_ values are proposed:

* 'Context' : Assignment of a context specific representation, such as of structural members to a different context representation (with potentially different decomposition breakdown) such as of building elements for a specific context specific representation. 
* 'View' : Assignment of a product (via _RelatingProduct_) that is decomposed according to a discipline view, to another product (via _RelatedObjects_) that is decomposed according to a different discipline view. An example is the assignment of the architectural slab to a different decomposition of the pre manufactured sections of a slab (under a precast concrete discipline view).
<!-- end of short definition -->

> HISTORY New entity in IFC2x

> IFC2x3 CHANGE  The reference of a product within a spatial structure is now handled by a new relationship object _IfcRelReferencedInSpatialStructure_. The _IfcRelAssignsToProduct_ shall not be used to represent this relation from IFC2x3 onwards.

## Attributes

### RelatingProduct
Reference to the product or product type to which the objects are assigned.
> IFC4 CHANGE Datatype expanded to include _IfcProduct_ and _IfcTypeProduct_.

## Formal Propositions

### NoSelfReference
The instance to which the relation points, as provided by _RelatingProduct_, shall not be contained in the set of _RelatedObjects_.
