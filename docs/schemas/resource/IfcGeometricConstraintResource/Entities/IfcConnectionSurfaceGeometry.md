# IfcConnectionSurfaceGeometry

_IfcConnectionSurfaceGeometry_ is used to describe the geometric constraints that facilitate the physical connection of two objects at a surface or at a face with surface geometry associated. It is envisioned as a control that applies to the element connection relationships.
<!-- end of short definition -->

The _IfcSurface_ (or the _IfcFaceSurface_ with an associated _IfcSurface_) at the _SurfaceOnRelatingElement_ attribute defines the surface where the basic geometry items of the connected elements connects. The surface geometry and coordinates are provided within the local coordinate system of the _RelatingElement_, as specified at the _IfcRelConnects_ subtype that utilizes the _IfcConnectionSurfaceGeometry_. Optionally, the same surface geometry and coordinates can also be provided within the local coordinate system of the _RelatedElement_ by using the _SurfaceOnRelatedElement_ attribute.

> HISTORY New entity in IFC2x.

> IFC2x3 CHANGE The provision of topology with associated geometry, _IfcFaceSurface_, is enabled by using the _IfcSurfaceOrFaceSurface_.

## Attributes

### SurfaceOnRelatingElement
Surface at which related object is aligned at the relating element, given in the LCS of the relating element.

### SurfaceOnRelatedElement
Surface at which the relating element is aligned at the related element, given in the LCS of the related element. If the information is omitted, then the origin of the related element is used.
