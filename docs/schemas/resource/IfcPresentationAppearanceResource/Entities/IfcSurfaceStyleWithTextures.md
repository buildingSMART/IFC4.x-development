# IfcSurfaceStyleWithTextures

The entity _IfcSurfaceStyleWithTextures_ allows to include image textures in surface styles. These image textures can be applied repeating across the surface or mapped with a particular scale upon the surface.
<!-- end of short definition -->

**Informal Propositions**

1. Only one instance of _IfcSurfaceStyleWithTextures_ shall be referenced by an _IfcStyledItem_ and be assigned to an _IfcGeometricRepresentationItem_

> NOTE The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE inverse attribute _HasTextureCoordinates_ deleted.

## Attributes

### Textures
The textures applied to the surface. In case of more than one surface texture is included, the _IfcSurfaceStyleWithTextures_ defines a multi texture.
