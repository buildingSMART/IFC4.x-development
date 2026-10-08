# IfcRepresentationMap

An _IfcRepresentationMap_ defines the base definition (also referred to as block, cell or macro) called _MappedRepresentation_ within the _MappingOrigin_. The _MappingOrigin_ defines the coordinate system in which the _MappedRepresentation_ is defined.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-43:1992
> A representation map is the identification of a representation and a representation item in that representation for the purpose of mapping. The representation item defines the origin of the mapping. The representation map is used as the source of a mapping by a mapped item.

The _RepresentationMap_ is used through an _IfcMappedItem_ in one or several _IfcShapeRepresentation_'s. An Cartesian transformation operator can be applied to transform the _MappedRepresentation_ into the placement coordinate system of the shape representation. The transformation of the representation map is restricted to be a Cartesian transformation mapping (translation, rotation, mirroring and scaling).

> NOTE The definition of a mapping which is used to specify a new representation item comprises a representation map and a mapped item entity. Without both entities, the mapping is not fully defined. Two entities are specified to allow the same source representation to be mapped into multiple new representations.

> NOTE Entity adapted from **representation_map** defined in ISO 10303-43.

> HISTORY New entity in IFC2x.

## Attributes

### MappingOrigin
An axis2 placement that defines the position about which the mapped
representation is mapped.

### MappedRepresentation
A representation that is mapped to at least one mapped item.

### HasShapeAspects
Reference to the shape aspect that represents part of the shape or its feature distinctively.
> IFC4 CHANGE Inverse attribute added.

### MapUsage


## Formal Propositions

### ApplicableMappedRepr
Only representations of type _IfcShapeRepresentation_, or _IfcTopologyRepresentation_ are allowed as _MappedRepresentation_.
