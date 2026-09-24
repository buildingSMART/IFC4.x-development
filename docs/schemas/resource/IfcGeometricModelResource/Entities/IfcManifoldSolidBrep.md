# IfcManifoldSolidBrep

The _IfcManifoldSolidBrep_ is a solid represented as a collection of connected surfaces that delimit the solid from the surrounding non-solid.
<!-- end of short definition -->

Instances of type _IfcManifoldSolidBrep_ shall be of type _IfcFacetedBrep_, using only _IfcPolyLoop_ for the bounds of _IfcFaceBound_, or of type _IfcAdvancedBrep_, using only _IfcAdvancedFace_ for the face geometry, and _IfcEdgeCurve_ for the edges.

> NOTE Definition according to ISO/CD 10303-42:1992
> A manifold solid b-rep is a finite, arcwise connected volume bounded by one or more surfaces, each of which is a connected, oriented, finite, closed 2-manifold. There is no restriction on the genus of the volume, nor on the number of voids within the volume.
>
> The Boundary Representation (B-rep) of a manifold solid utilizes a graph of edges and vertices embedded in a connected, oriented, finite, closed two manifold surface. The embedded graph divides the surface into arcwise connected areas known as faces. The edges and vertices, therefore, form the boundaries of the face and the domain of a face does not include its boundaries. The embedded graph may be disconnected and may be a pseudo graph. The graph is labeled; that is, each entity in the graph has a unique identity. The geometric surface definition used to specify the geometry of a face shall be 2-manifold embeddable in the plane within the domain of the face. In other words, it shall be connected, oriented, finite, non-self-intersecting, and of surface genus 0.
>
> Faces do not intersect except along their boundaries. Each edge along the boundary of a face is shared by at most one other face in the assemblage. The assemblage of edges in the B-rep do not intersect except at their boundaries (i.e., vertices). The geometry curve definition used to specify the geometry of an edge shall be arcwise connected and shall not self intersect or overlap within the domain of the edge. The geometry of an edge shall be consistent with the geometry of the faces of which it forms a partial bound. The geometry used to define a vertex shall be consistent with the geometry of the faces and edges of which it forms a partial bound.
>
> The geometry used to define a vertex shall be consistent with the geometry of the faces and edges of which it forms a partial bound.
>
> A B-rep is represented by one or more closed shells which shall be disjoint. One shell, the outer, shall completely enclose all the other shells and no other shell may enclose a shell. The facility to define a B-rep with one or more internal voids is provided by a subtype. The following version of the Euler formula shall be satisfied,
>
>> ![math](../../../../figures/ifcmanifoldsolidbrep-math1.gif)
> where V, E, F, L~l~ and S are the numbers of unique vertices, edges, faces, loop uses and shells in the model and G^s^ is the sum of the genus of the shells.
>


> NOTE Entity adapted from **manifold_solid_brep** defined in ISO 10303-42.

> HISTORY: New entity in IFC Release 1.0



**Informal proposition**:

1. The dimensionality of a manifold solid brep shall be 3.
2. The extent of the manifold solid brep shall be finite and non-zero.
3. All elements of the manifold solid brep shall have defined associated geometry.
4. The shell normals shall agree with the B-rep normal and point away from the solid represented by the B-rep.
5. Each face shall be referenced only once by the shells of the manifold solid brep.
6. The Euler equation shall be satisfied for the boundary representation, where the genus term "shell term" us the sum of the genus values for the shells of the brep.

## Attributes

### Outer
A closed shell defining the exterior boundary of the solid. The shell normal shall point away from the interior of the solid.
