# IfcAdvancedBrepWithVoids

The _IfcAdvancedBrepWithVoids_ is a specialization of an advanced B-rep which contains one or more voids in its interior. The voids are represented as closed shells which are defined so that the shell normal point into the void.
<!-- end of short definition -->

> NOTE Entity adapted from **advanced_brep_shape_representation** defined in ISO 10303-514.

> HISTORY  New entity in IFC4

**Informal Propositions**

1. Each void shell shall be disjoint from the outer shell and from every other void shell
2. Each void shell shall be enclosed within the outer shell but not within any other void shell. In particular the outer shell is not in the set of void shells
3. Each shell in the _IfcManifoldSolidBrep_ shall be referenced only once.
4. All the faces of all the shells in the _IfcAdvancedBrep_ and the _IfcAdvancedBrepWithVoids.Voids_ shall be of type _IfcAdvancedFace_.

## Attributes

### Voids


## Formal Propositions

### VoidsHaveAdvancedFaces
Each face of the voids within the advanced B-rep with voids shall be of type _IfcAdvancedFace_.
