# IfcFacetedBrepWithVoids

The _IfcFacetedBrepWithVoids_ is a specialization of a faceted B-rep which contains one or more voids in its interior. The voids are represented as closed shells which are defined so that the shell normal point into the void.
<!-- end of short definition -->

> NOTE Entity adapted from **brep_with_voids** AND **faceted_brep** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0

> IFC4 CHANGE Subtyping changed from _IfcManifoldSolidBrep_ to _IfcFacetedBrep_ with upward compatibility for file based exchange.



**Informal Propositions**

1. Each void shell shall be disjoint from the outer shell and from every other void shell
2. Each void shell shall be enclosed within the outer shell but not within any other void shell. In particular the outer shell is not in the set of void shells
3. Each shell in the _IfcManifoldSolidBrep_ shall be referenced only once.
4. All the bounding loops of all the faces of all the shells in the _IfcFacetedBrep_ shall be of type _IfcPolyLoop_.

## Attributes

### Voids
Set of closed shells defining voids within the solid.
