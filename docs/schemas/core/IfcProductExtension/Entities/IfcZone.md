# IfcZone

A zone is a group of spaces, partial spaces or other zones. These spaces may or may not be adjacent. A zone does not have its own shape representation. Zone structures may not be hierarchical (in contrary to the spatial structure of a project - see _IfcSpatialStructureElement_), i.e. one individual _IfcSpace_ may be associated with zero, one, or several _IfcZone_'s. _IfcSpace_'s are grouped into an _IfcZone_ by using the objectified relationship _IfcRelAssignsToGroup_ as specified at the supertype _IfcGroup_. For example, a zone might be used to represent an apartment as a group of spaces.
<!-- end of short definition -->

> NOTE  Certain use cases may restrict the freedom of non hierarchical relationships. In some building service use cases the zone denotes a view based delimited volume for the purpose of analysis and calculation. This type of zone cannot overlap with respect to that analysis, but may overlap otherwise.

> HISTORY New entity in IFC1.0

> IFC4 CHANGE The entity is now subtyped from _IfcSystem_ (not its supertype _IfcGroup_) with upward compatibility for file based exchange.

## Attributes

### LongName
Long name for a zone, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE In many scenarios the _Name_ attribute refers to the short name or number of a zone, and the _LongName_ refers to the full name.


> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### WR1
An _IfcZone_ is grouped by the objectified relationship _IfcRelAssignsToGroup_. Only objects of type _IfcSpace_, _IfcZone_ and _IfcSpatialZone_ are allowed as _RelatedObjects_.

## Concepts

### Group Assignment

An IfcZone is a spatial system under which individual IfcSpace's (and other IfcZone's) are grouped. In contrary to the IfcSpatialZone entity, IfcZone is a mere grouping, it can not define an own geometric representation and placement. Therefore it cannot be used for spatial zones having a different shape and size compared to the shape and size of aggregated spaces.

> NOTE The IfcZone is regarded as the spatial system (as compared to the building service, electrical, or analytical system), the name remains IfcZone for compatibility reasons, instead of using a proper naming convention, like IfcSpatialSystem.

> NOTE  One of the purposes of a zone is to define a fire compartmentation. In this case it defines the geometric information about the fire compartment (through the contained spaces) and information, whether this compartment is ventilated or sprinkler protected. In addition the fire risk code and the hazard type can be added, the coding is normally defined within a national fire regulation. All that information is available within the relevant property sets. Again, if an independent shape has to be provided to the fire compartment, then the entity IfcSpatialZone shall be used.

In case of a zone denoting a (fire) compartment, the following types should be used, if applicable, as values of the ObjectType attribute:

* **'FireCompartment'**: a zone of spaces, collected to represent a single fire compartment.
* **'ElevatorShaft'**: a collection of spaces within an elevator, potentially going through many storeys.
* **'RisingDuct'**: A collection of vertical airspaces.
* **'RunningDuct'**: A collection of horizontal airspaces.

### Property Sets for Objects



