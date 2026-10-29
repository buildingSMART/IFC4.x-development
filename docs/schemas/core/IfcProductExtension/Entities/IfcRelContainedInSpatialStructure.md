# IfcRelContainedInSpatialStructure

This objectified relationship, _IfcRelContainedInSpatialStructure_, is used to assign elements to a certain level of the spatial project structure. Any element can only be assigned once to a certain level of the spatial structure. The question, which level is relevant for which type of element, can only be answered within the context of a particular project and might vary within the various regions.
<!-- end of short definition -->

> EXAMPLE A multi-storey space is contained (or belongs to) the building storey at which its ground level is, but it is referenced by all the other building storeys, in which it spans. A lift shaft might be contained by the basement, but referenced by all storeys, through which it spans.

The containment relationship of an element within a spatial structure has to be a hierarchical relationship; an element can only be contained within a single spatial structure element. The reference relationship between an element and the spatial structure need not be hierarchical; that is, an element can reference many spatial structure elements.

> NOTE The reference relationship is expressed by _IfcRelReferencedInSpatialStructure_.

Occurrences of the same element type can be assigned to different spatial structure elements depending on the context of the occurrence.

> EXAMPLE A wall might be normally assigned to a storey, however the curtain wall might be assigned to the building and the retaining wall in the terrain might be assigned to the site.

Figure 1 shows the use of _IfcRelContainedInSpatialStructure_ to assign a stair and two walls to two different levels within the spatial structure.

![fig1](../../../../figures/ifcrelcontainedinspatialstructure-fig1.png "Figure 1 — Relationship for spatial structure containment")

> HISTORY New entity in IFC2x.

> IFC2x CHANGE The data type of the attribute _RelatedElements_ has been changed from _IfcElement_ to its supertype _IfcProduct_ with upward compatibility for file based exchange.

## Attributes

### RelatedElements
Set of products, which are contained within this level of the spatial structure hierarchy.
> IFC2x CHANGE The data type has been changed from _IfcElement_ to _IfcProduct_ with upward compatibility

### RelatingStructure
Spatial structure element, within which the element is contained. Any element can only be contained within one element of the project spatial structure.
> IFC4 CHANGE The attribute _RelatingStructure_ as been promoted to the new supertype _IfcSpatialElement_ with upward compatibility for file based exchange.

## Formal Propositions

### WR31
The relationship object shall not be used to include other spatial structure elements into a spatial structure element. The hierarchy of the spatial structure is defined using _IfcRelAggregates_.
