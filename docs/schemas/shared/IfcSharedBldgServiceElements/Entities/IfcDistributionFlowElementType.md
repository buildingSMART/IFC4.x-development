# IfcDistributionFlowElementType

The element type _IfcDistributionFlowElementType_ defines a list of commonly shared property set definitions of an element and an optional set of product representations. It is used to define an element specification (the specific product information that is common to all occurrences of that product type).
<!-- end of short definition -->

Distribution flow element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcDistributionFlowElementType_ are represented by instances of _IfcDistributionFlowElement_ or its subtypes.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Ports may now be defined using _IfcRelNests_ to enable definition of ports at type definitions (both forward and backward compatible), provide a logical order, and reduce the number of relationship objects needed. The relationship _IfcRelConnectsPortToElement_ is still supported on occurrence objects, however is now specific to dynamically connected ports.

## Concepts

### Type Axis Geometry

This represents the 3D flow path of the item having _IfcShapeRepresentation.RepresentationType_ of 'Curve3D' and containing a single IfcBoundedCurve subtype such as IfcPolyline, IfcTrimmedCurve, or IfcCompositeCurve. For elements containing directional ports (IfcDistributionPort with FlowDirection of SOURCE or SINK), the direction of the curve indicates direction of flow where a SINK port is positioned at the start of the curve and a SOURCE port is positioned at the end of the curve. This representation is most applicable to flow segment types (pipes, ducts, cables), however may be used at other elements to define a primary flow path if applicable.

If an element type is defined parametrically (such as a flow segment type defining common material profile but no particular length or path), then no representations shall be asserted at the type.

> NOTE The product representations are defined as representation maps (at the level of the supertype IfcTypeProduct, which get assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an IfcMappedItem.

### Type Clearance Geometry

This represents the 3D clearance volume of the item having RepresentationType of 'Surface3D'. Such clearance region indicates space that should not intersect with the 'Body' representation between element occurrences, though may intersect with the 'Clearance' representation of other element occurrences. The particular use of clearance space may be for safety, maintenance, or other purposes.

### Type Lighting Geometry

This represents the light emission of the item having _IfcShapeRepresentation.RepresentationType_ of 'LightSource' and containing one or more IfcLightSource subtypes. This representation is most applicable to lamps and light fixtures, however may be used at other elements that emit light.

