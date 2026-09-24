# IfcDistributionFlowElement

The distribution element _IfcDistributionFlowElement_ defines occurrence elements of a distribution system that facilitate the distribution of energy or matter, such as air, water or power.
<!-- end of short definition -->

> EXAMPLE Examples of distribution flow elements are ducts, pipes, wires, fittings, and equipment.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE Ports are now primarily defined using _IfcRelNests_ to enable definition of ports at type definitions (both forward and backward compatible), provide a logical order, and reduce the number of relationship objects needed. The relationship _IfcRelConnectsPortToElement_ is still supported, however is now specific to dynamically connected ports.

## Attributes

### HasControlElements
Reference to the relationship object that relates control elements.

## Concepts

### Axis Geometry

This represents the 3D flow path of the item having _IfcShapeRepresentation.RepresentationType_ of 'Curve3D' and containing a single IfcBoundedCurve subtype such as IfcPolyline, IfcTrimmedCurve, or IfcCompositeCurve. For elements containing directional ports (IfcDistributionPort with FlowDirection of SOURCE or SINK), the direction of the curve indicates direction of flow where a SINK port is positioned at the start of the curve and a SOURCE port is positioned at the end of the curve. This representation is most applicable to flow segments (pipes, ducts, cables), however may be used at other elements to define a primary flow path if applicable.

### Clearance Geometry

This represents the 3D clearance volume of the item having RepresentationType of 'Surface3D'. Such clearance region indicates space that should not intersect with the 'Body' representation of other elements, though may intersect with the 'Clearance' representation of other elements. The particular use of clearance space may be for safety, maintenance, or other purposes.

### Object Typing



### Property Sets for Objects



