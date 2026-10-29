# IfcGroup

_IfcGroup_ is a generalization of any arbitrary group. A group is a logical collection of objects. It does not have its own position, nor can it hold its own shape representation. Therefore a group is an aggregation under some non-geometrical / topological grouping aspects.
<!-- end of short definition -->

> EXAMPLE An example for a group is a system, since it groups elements under the aspect of their role, regardless of their position in a building. One of the most important usages of a group representing a system is the _IfcDistributionSystem_, that groups distribution components, such as space heaters and valves into a heating system.

A group can hold any collection of objects, the relationship _IfcRelAssignsToGroup_ is used to establish the group collection. Objects within a group are products, processes, controls, resources, actors or other groups, thus groups can be nested. An object can be part of zero, one, or many groups. Grouping relationships are not required to be hierarchical nor do they imply a dependency.

A group can be referenced in a spatial structure using the relationship _IfcRelReferencedInSpatialStructure_, such as a mechanical distribution system that refers to a building.

Groups are assigned to other objects (such as a process or a resource) by the relationship object that refers to the corresponding object:

* Process: assigned using _IfcRelAssignsToProcess_
* Resource: assigned using _IfcRelAssignsToResource_
* Controls: affecting the group using _IfcRelAssignsToControl_

A group can be exchanged without having already objects within the group collection.

_IfcGroup_ does not define an own object coordinate system, nor does it have an independent shape representation.

> NOTE Use _IfcRelAggregates_ together with the appropriate subtypes of _IfcProduct_ to define an aggregation of products that may have its own position and shape representation. This relationship shall be used to create a product breakdown structure.

> HISTORY New entity in IFC1.0.

> IFC4 CHANGE The inverse _IsGroupedBy_ relationship is set to 0..n

## Attributes

### IsGroupedBy
Reference to the relationship _IfcRelAssignsToGroup_ that assigns the one to many group members to the _IfcGroup_ object.
> IFC4 CHANGE The cardinality has been changed from 1..1 to 0..n in order to allow the exchange of a group concept without having already group members assigned. It now also allows the use of many instances of _IfcRelAssignsToGroup_ to assign the group members. The change has been done with upward compatibility for file based exchange.

### ReferencedInStructures
Reference to the relationship _IfcRelReferencedInSpatialStructure_ that relates the group to a spatial element.

## Concepts

### Group Assignment

The IfcGroup establishes an arbitrary collection of objects through utilizing this concept.
