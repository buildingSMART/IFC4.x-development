# IfcMappedItem

The _IfcMappedItem_ is the inserted instance of a source definition (to be compared with a block / shared cell / macro definition). The instance is inserted by applying a Cartesian transformation operator as the _MappingTarget_.
<!-- end of short definition -->

> NOTE A mapped item is a subtype of representation item. It enables a representation to be used as a representation item in one or more other representations. The mapped item allows for the definition of a representation using other representations.

> EXAMPLE An _IfcMappedItem_ can reuse other mapped items (ako nested blocks), doing so the _IfcRepresentationMap_ is based on an _IfcShapeRepresentation_ including one or more _IfcMappedItem_'s.

> NOTE Definition according to ISO/CD 10303-43:1992
> A mapped item is a type of representation item that specifies the mapping of a representation as an element of the items of a second representation.

> NOTE Entity adapted from **mapped_item** defined in ISO 10303-43.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. A mapped item shall not be self-defining by participating in the definition of the representation being mapped.
2. The dimensionality of the mapping source and the mapping target has to be the same, if the mapping source is a geometric representation item.

## Attributes

### MappingSource
A representation map that is the source of the mapped item. It can be seen as a block (or cell or marco) definition.

### MappingTarget
A representation item that is the target onto which the mapping source is mapped. It is constraint to be a Cartesian transformation operator.
