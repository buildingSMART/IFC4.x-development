# IfcProductDefinitionShape

The _IfcProductDefinitionShape_ defines all shape relevant information about an _IfcProduct_. It allows for multiple geometric shape representations of the same product. The shape relevant information includes:

* the shape representation including geometric representation items (for 3D solids, 2D annotations, etc.) and:
  * associated presentation information (line color, line type, surface rendering properties)
  * assignment to presentation layers (CAD layers for visibility control)
* or the topological representation items for connectivity systems (vertex, edge, face representations) that may include geometric representation items (vertex points, edge curves, face surfaces)
<!-- end of short definition -->

> NOTE The definition of this entity relates to the ISO 10303 entity product_definition_shape. Please refer to ISO/IS 10303-41:1994 for the final definition of the formal standard.

> HISTORY New entity in IFC1.5

## Attributes

### ShapeOfProduct
The _IfcProductDefinitionShape_ shall be used to provide a representation for a one or more instances of _IfcProduct_.
> IFC2x3 CHANGE New inverse attribute.

> IFC4 CHANGE Inverse relationship cardinality relaxed to be 1:N.

### HasShapeAspects
Reference to the shape aspect that represents part of the shape or its feature distinctively.

## Formal Propositions

### OnlyShapeModel
Only representations of type _IfcShapeModel_, i.e. either _IfcShapeRepresentation_ or _IfcTopologyRepresentation_ should be used to represent a product through the _IfcProductDefinitionShape_.__
