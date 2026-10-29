# IfcRelAssignsToResource

The objectified relationship _IfcRelAssignsToResource_ handles the assignment of objects (as subtypes of _IfcObject_), acting as a resource usage or consumption, to a resource (as subtypes of _IfcResource_).
<!-- end of short definition -->

> EXAMPLE The assignment of a resource usage to a construction resource is an application of this generic relationship. It could be an actor, such as a person or organization, assigned to a labor resource, or a raw product assigned to a construction product or material resource.

> HISTORY New entity in IFC2x.

## Attributes

### RelatingResource

Reference to the resource to which the objects are assigned.

> IFC4 CHANGE Datatype expanded to include _IfcResource_ and _IfcTypeResource_.

## Formal Propositions

### NoSelfReference

The instance to which the relation points shall not be contained in the set of _RelatedObjects_.
