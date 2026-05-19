# IfcRelNests

The nesting relationship _IfcRelNests_ is a special type of the general composition/decomposition (or whole/part) relationship _IfcRelDecomposes_. The nesting relationship can be applied to all subtypes of objects and object types, such as processes, controls (e.g., cost items), and resources. It can also be applied to alignment, nesting its different layouts; and to physical subtypes of object and object types, such as elements having ports. The nesting implies an order among the nested parts.
<!-- end of short definition -->

> EXAMPLE A nesting of cost items in an _IfcCostSchedule_ is the composition of complex cost items from other cost items. The order of the nested cost items underneath the parent cost item is determined by the order of the list of _RelatedObjects_.

> EXAMPLE A nesting of _IfcTask_ entities within a work schedule is the composition of a parent work task from more specific sub work tasks. The order of the sub tasks underneath the parent task is determined by the order of the list of _RelatedObjects_.

> EXAMPLE A series of _IfcDistributionPort_ entities can be nested within an _IfcDistributionElement_. They decompose the distribution element and have an implied order.

> EXAMPLE A series of _IfcCableSegment_ entities can be nested within an _IfcCableCarrierSegment_.

Decompositions imply a dependency, i.e. the definition of the whole depends on the definition of the parts and the parts depend on the existence of the whole. The behaviour that is implied from the dependency has to be established inside the applications.

> HISTORY New entity in IFC2.0

{ .change-ifc2x4}
> IFC4 CHANGE The attributes _RelatingObject_ and _RelatedObjects_ are demoted from the supertype _IfcRelDecomposes_, and _RelatedObjects_ is refined to be a list. The use of _IfcRelNests_ is repurposed to be a nesting of an ordered collection of parts.

## Attributes

### RelatingObject
The object definition, either an object type or an object occurrence, that represents the nest. It is the whole within the whole/part relationship.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been demoted from the supertype _IfcRelDecomposes_ and defines the ordered nesting relationship.

### RelatedObjects
The object definitions, either object type or object occurrence, that are being nested. They are defined as the parts in the ordered whole/part relationship - i.e. there is an implied order among the parts expressed by the position within the list of _RelatedObjects_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been demoted from the supertype _IfcRelDecomposes_ and defines the ordered set of parts within the nest.

## Formal Propositions

### NoSelfReference
The instance to which the relation points as provided by _RelatingObject_ shall not be contained in the list of _RelatedObjects_.
