# IfcRelReferencedInSpatialStructure

The objectified relationship, _IfcRelReferencedInSpatialStructure_ is used to assign elements in addition to those levels of the project spatial structure, in which they are referenced, but not primarily contained. It is also used to connect a system to the relevant spatial element that it serves.
<!-- end of short definition -->

> NOTE The primary containment relationship between an element and the spatial structure is handled by _IfcRelContainedInSpatialStructure_.

Any element can be referenced to zero, one or several levels of the spatial structure. Whereas the _IfcRelContainedInSpatialStructure_ relationship is required to be hierarchical (an element can only be contained in exactly one spatial structure element), the _IfcRelReferencedInSpatialStructure_ is not restricted to be hierarchical.

> EXAMPLE A curtain wall might span through several stories, in this case it can be contained within the ground floor, but it would be referenced by all additional stories it spans.

Predefined spatial structure elements to which elements can be assigned are

* site as _IfcSite_
* facility as _IfcFacility_ or its subtypes _IfcBridge_, _IfcBuilding_, _IfcMarineFacility_, _IfcRailway_ or _IfcRoad_
* part of facility as _IfcFacilityPart_, or more specifically as _IfcBuildingStorey_ or _IfcSpace_

Elements can also be referenced in a spatial zone that is provided as _IfcSpatialZone_.

Figure 1 shows the use of _IfcRelContainedInSpatialStructure_ and _IfcRelReferencedInSpatialStructure_ to assign an _IfcCurtainWall_ to two different levels within the spatial structure. It is primarily contained within the ground floor, and additionally referenced within the first and second floor.

![reference and containment](../../../../figures/ifcrelreferencedinspatialstructure-fig1.png "Figure 1 — Relationship for spatial structure referencing")


> HISTORY New entity in IFC2x3.

## Attributes

### RelatedElements
Set of objects, which are referenced within this level of the spatial structure hierarchy.

### RelatingStructure
Spatial structure element, within which the objects are referenced. An object can be referenced within multiple elements of the project spatial structure.

## Formal Propositions

### AllowedRelatedElements
The relationship object shall not be used to include other spatial structure elements into a spatial structure element. The hierarchy of the spatial structure is defined using _IfcRelAggregates_. Exception: an _IfcSpace_ can be referenced by another spatial structure element, in particular by an _IfcSpatialZone_.
> IFC4 CHANGE The relaxation to allow _IfcSpace_ has been included.
