# IfcResource

_IfcResource_ contains the information needed to represent the costs, schedule, and other impacts resulting from the use of a thing in a process. It is not intended to use _IfcResource_ to model the general properties of the things themselves, while an optional linkage from _IfcResource_ to the things being used can be specified (specifically, the relationship from subtypes of _IfcResource_ to _IfcProduct_ through the _IfcRelAssignsToResource_ relationship).
<!-- end of short definition -->

There are two basic intended uses of _IfcResource_. First, if the attributes of the thing are not needed for the purpose of the use of _IfcResource_, or the types of things are not explicitly modeled in IFC yet, then the linkage between the resource and the thing doesn't have to be instantiated in the system. That is, the attributes of _IfcResource_ (or its subtypes) alone are sufficient to represent the use of the thing as a resource for the purpose of the project.

> EXAMPLE Construction equipment such as earth-moving vehicles or tools are not currently modeled within the IFC. For the purpose of estimating and scheduling, these can be represented using subtypes of _IfcResource_ alone.

Second, if the attributes of the thing are needed for the use of _IfcResource_ objects, and they are modeled explicitly as objects, then the _IfcResource_ instances can be linked to the instances of the type of the things being referenced. Things that might be used as resources and that are already modeled in the IFC include physical products, people and organizations, and materials. The relationship object _IfcRelAssignsToResource_ is provided for this approach.

The inherited attribute _ObjectType_ is used as a textual code that identifies the resource type.

> HISTORY New entity in IFC1.0

> IFC2x CHANGE The attributes BaseUnit and ResourceConsumption have been removed from the abstract entity; they are reintroduced at a lower level in the hierarchy.

## Attributes

### Identification
An identifying designation given to a resource at the occurrence level.

> IFC4 CHANGE Attribute promoted from subtype _IfcConstructionResource_.

### LongDescription
A detailed description of the resource (e.g. the skillset for a labor resource).
> IFC4 CHANGE The attribute _LongDescription_ has been added, replacing the _ResourceGroup_ attribute at subtype _IfcConstructionResource_.

### ResourceOf
Set of relationships to other objects, e.g. products, processes, controls, resources or actors, for which this resource object is a resource.
