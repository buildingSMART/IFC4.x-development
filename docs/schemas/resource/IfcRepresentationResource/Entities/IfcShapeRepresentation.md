# IfcShapeRepresentation

The _IfcShapeRepresentation_ represents the concept of a particular geometric representation of a product or a product component within a specific geometric representation context. The inherited attribute _RepresentationType_ is used to define the geometric model used for the shape representation (e.g. 'SweptSolid', or 'Brep'), the inherited attribute _RepresentationIdentifier_ is used to denote the kind of the representation captured by the _IfcShapeRepresentation_ (e.g. 'Axis', 'Body', etc.).
<!-- end of short definition -->

Several representation identifiers for shape representation are included as predefined values for _RepresentationIdentifier_. Table 1 indicates the defined list of values for _RepresentationIdentifier_.

> IFC4.3.2.0 DEPRECATION Representation type 'PointCloud' is now deprecated as other representation types also didn't differentiate between one or multiple geometries. Use 'Point' instead.

| Identifier    | Description                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CoG           | Point to identify the center of gravity of an element. This value can be used for validation purposes.                                                                                                                            |
| Box           | Bounding box as simplified 3D box geometry of an element                                                                                                                                                                          |
| Annotation    | 2D or 3D annotations                                                                                                                                                                                                              |
| Axis          | 2D or 3D Axis, or single line, representation of an element                                                                                                                                                                       |
| FootPrint     | 2D Foot print, or double line, representation of an element, projected to ground view                                                                                                                                             |
| Profile       | 3D line representation of a profile being planar, e.g. used for door and window outlines                                                                                                                                          |
| Surface       | 3D Surface representation (an analytical surface of an element plane)                                                                                                                                                             |
| Reference     | 3D representation that is not part of the Body representation. This is used, e.g., for opening geometries, if there are to be excluded from an implicit Boolean operation.                                                        |
| Body          | 3D Body representation, e.g. as wireframe, surface, or solid model, of an element                                                                                                                                                 |
| Body-FallBack | 3D Body representation, e.g. as tessellation, or other surface, or boundary representation, added in addition to the solid model (potentially involving Boolean operations) of an element                                         |
| Clearance     | 3D clearance volume of the element. Such clearance region indicates space that should not intersect with the 'Body' representation of other elements, though may intersect with the 'Clearance' representation of other elements. |
| Lighting      | Representation of emitting light as a light source within a shape representation                                                                                                                                                  |

Table 1 — Representation identifiers

Several representation types for shape representation are included as predefined values for _RepresentationType_. Table 2 indicates the defined list of values for _RepresentationType_.

| Type                 | Description                                                                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Point                | 2 or 3 dimensional point(s). Points can be represented by a point list                                                                                                                                                                                |
| PointCloud           | 3 dimensional points represented by a point list. DEPRECATED. Use 'Point' instead.                                                                                                                                                                    |
| Curve                | 2 or 3 dimensional curve(s)                                                                                                                                                                                                                           |
| Curve2D              | 2 dimensional curve(s)                                                                                                                                                                                                                                |
| Curve3D              | 3 dimensional curve(s)                                                                                                                                                                                                                                |
| Segment              | partial geometry of curves that shall not be rendered separately from the main curve                                                                                                                                                                  |
| Surface              | 2 or 3 dimensional surface(s)                                                                                                                                                                                                                         |
| Surface2D            | 2 dimensional surface(s) (a region on ground view)                                                                                                                                                                                                    |
| Surface3D            | 3 dimensional surface(s)                                                                                                                                                                                                                              |
| SectionedSurface     | swept surface(s) created by sweeping open profiles along a directrix                                                                                                                                                                                  |
| FillArea             | 2D region(s) represented as a filled area (hatching)                                                                                                                                                                                                  |
| Text                 | text defined as text literals                                                                                                                                                                                                                         |
| AdvancedSurface      | 3 dimensional b-spline surface(s)                                                                                                                                                                                                                     |
| Annotation2D         | points, curves (2 or 3 dimensional), hatches and text (2 dimensional)                                                                                                                                                                                 |
| GeometricSet         | points, curves, surfaces (2 or 3 dimensional)                                                                                                                                                                                                         |
| GeometricCurveSet    | points, curves (2 or 3 dimensional)                                                                                                                                                                                                                   |
| Tessellation         | Tessellated surface representation(s) only                                                                                                                                                                                                            |
| SurfaceOrSolidModel  | Tessellated surface model(s), shell based surface model(s), face based surface model(s), or solid model(s)                                                                                                                                            |
| SurfaceModel         | face based and shell based surface model(s), or tessellated surface model(s)                                                                                                                                                                          |
| SolidModel           | including swept solid, Boolean results and Brep bodies                                                                                                                                                                                                |
| SweptSolid           | swept area solids, by extrusion and revolution, excluding tapered sweeps                                                                                                                                                                              |
| AdvancedSweptSolid   | swept area solids created by sweeping a profile along a directrix, and tapered sweeps                                                                                                                                                                 |
| CSG                  | Boolean results of operations between solid models, half spaces and Boolean results                                                                                                                                                                   |
| Clipping             | Boolean differences between swept area solids, half spaces and Boolean results                                                                                                                                                                        |
| Brep                 | Faceted Brep's with and without voids                                                                                                                                                                                                                 |
| AdvancedBrep         | Brep's based on advanced faces, with b-spline surface geometry, with and without voids                                                                                                                                                                |
| BoundingBox          | simplistic 3D representation by a bounding box                                                                                                                                                                                                        |
| SectionedSpine       | cross section based representation of a spine curve and planar cross sections. It can represent a surface or a solid and the interpolations of the between the cross sections is not defined                                                          |
| LightSource          | light source with (depending on type) position, orientation, light colour, intensity and attenuation                                                                                                                                                  |
| MappedRepresentation | representation based on mapped item(s), referring to a representation map. Note: it can be seen as an inserted block reference. The shape representation of the mapped item has a representation type declaring the type of its representation items. |

Table 2 — Representation types

> NOTE The definition relates to **shape_representation** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.

> IFC4 CHANGE The _RepresentationType_'s 'Point', 'PointCloud', 'Curve', 'Curve3D', 'Surface', 'Surface2D', 'Surface3D', 'FillArea', 'Text', 'Tessellation', 'AdvancedBrep', 'LightSource', and the _RepresentationIdentifier_ 'Body-FallBack', 'Profile', 'Clearance', 'Lighting' have been added.

## Formal Propositions

### CorrectContext
The context to which the IfcShapeRepresentation is assign, shall be of type IfcGeometricRepresentationContext.

### NoTopologicalItem
No topological representation item shall be directly used for shape representations, with the exception of IfcVertexPoint, IfcEdgeCurve, IfcFaceSurface.

### HasRepresentationType
A representation type should be provided for the shape representation.

### HasRepresentationIdentifier
A representation identifier should be provided for the shape representation.

### CorrectItemsForType
Checks the proper use of _Items_ according to the _RepresentationType_.
