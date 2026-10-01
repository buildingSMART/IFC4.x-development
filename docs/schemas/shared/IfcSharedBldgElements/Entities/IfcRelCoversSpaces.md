# IfcRelCoversSpaces

The objectified relationship, _IfcRelCoversSpace_, relates a space object to one or many coverings, which faces (or is assigned to) the space.
<!-- end of short definition -->

> NOTE Particularly floorings, ceilings and wall coverings, such as claddings or tiling are often considered as space coverings, rather then wall or slab coverings. In some life cycle phases, such as the operation phase, the relationship is always made to the space.

The IFC specification provides two relationships:

* _IfcRelCoversBldgElements_ to assign coverings to elements.
>> NOTE This relationship is now deprecated and replaced by _IfcRelAggregates_.
* _IfcRelCoversSpaces_ to assign coverings to spaces
>> NOTE This relationship is now deprecated and replaced by _IfcRelContainedInSpatialStructure_.

Whether the relationship between the covering and the space, or between the covering and the element, is regarded as primary, has to be determined within the context of a model view definition.

> HISTORY New entity in IFC2x3.

> IFC4 DEPRECATION The relationship _IfcRelCoversSpace_ shall not be used anymore, use _IfcRelContainedInSpatialStructure_ instead.

## Attributes

### RelatingSpace
Relationship to the space object that is covered.
> IFC4 CHANGE The attribute name has been changed from _RelatedSpace_ to _RelatingSpace_ with upward compatibility for file based exchange.

### RelatedCoverings
Relationship to the set of coverings that cover surfaces of this space.
