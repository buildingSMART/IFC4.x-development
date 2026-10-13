# IfcTessellatedFaceSet

The _IfcTessellatedFaceSet_ is a boundary representation topological model limited to planar faces and straight edges. It may represent an approximation of an analytical surface or solid that may be provided in addition to its tessellation as a separate shape representation. The _IfcTessellatedFaceSet_ provides a compact data representation of an connected face set using indices into ordered lists of vertices, normals, colours, and texture maps.
<!-- end of short definition -->

> NOTE The compact representation has been chosen to enable small data sets despite potentially large sets of faces, edges and vertices needed to represent tessellations of analytical surfaces and solids, and despite large sets of colour and texture information to annotate the tessellated faces.

The _IfcTessellatedFaceSet_ is an abstract supertype of tessellated face sets each imposing specific constraints on face generation for tessellation, such as triangulation (with or without strip and fans), or quadrilaterals, or polygonal faces (with or without inner loops).

> NOTE Not all different constraints on face sets are included as specific subtypes in this release of the specification.

The following attributes apply to all subtypes:

* The _Coordinates_ are the ordered list of Cartesian points representing the vertices of the tessellated item. An index list, defined at the level of subtypes, uses the points, identified by index position, to construct the polylines that represent the faces.
* The _HasColours_ inverse relation provides an indexed colour map with an corresponding list of indices providing a colour for each face of the tessellated face set.
* The _HasTextures_ inverse relation provides an indexed texture map with an corresponding list of indices providing texture coordinates that map to the geometric coordinates of the polylines representing the faces.

Each face of the tessellated face set shall have:

* at least three non-coincident vertices;
* vertices that define a planar polygon;
* vertices that define a non-self-intersecting polygon.

> NOTE The definition of _IfcTessellatedFaceSet_ is based on the **indexedFaceSet** defined in ISO/IEC 19775-1

> HISTORY New entity in IFC4.

## Attributes

### Coordinates
An ordered list of Cartesian points used by the coordinate index defined at the subtypes of _IfcTessellatedFaceSet_.

### Dim
The space dimensionality of this geometric representation item, it is always 3.

### HasTextures
Reference to the indexed texture map providing the corresponding texture coordinates to the vertices bounding the faces of the subtypes of _IfcTessellatedFaceSet_.
