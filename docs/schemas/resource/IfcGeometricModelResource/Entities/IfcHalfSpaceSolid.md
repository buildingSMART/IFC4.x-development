# IfcHalfSpaceSolid

A half space solid divides the domain into two by a base surface. Normally, the base surface is a plane and divides the infinitive space into two and indicates the side of the half-space by agreeing or disagreeing to the normal of the plane.
<!-- end of short definition -->

Figure 1 illustrates the definition of the _IfcHalfSpaceSolid_ within a given coordinate system. The base surface is given by an unbounded plane, the red boundary is shown for visualization purposes only.

![half space solid](../../../../figures/ifchalfspacesolid-layout1.gif "Figure 1 — Half space solid geometry")

> NOTE Definition according to ISO/CD 10303-42:1992
> A half space solid is defined by the half space which is the regular subset of the domain which lies on one side of an unbounded surface. The side of the surface which is in the half space is determined by the surface normal and the agreement flag. If the agreement flag is TRUE, then the subset is the one the normal points away from. If the agreement flag is FALSE, then the subset is the one the normal points into.
>
> For a valid half space solid the surface shall divide the domain into exactly two subsets. Also, within the domain the surface shall be manifold and all surface normals shall point into the same subset.
>
> NOTE A half space is not a subtype of solid model, half space solids are only useful as operands in Boolean expressions.

> NOTE Entity adapted from **half_space_solid** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5

**Informal Propositions**

1. The base surface shall divide the domain into exactly two subsets. If the half space solid is of subtype boxed half space (_IfcBoxedHalfSpace_), the domain in question is that of the attribute enclosure. In all other cases the domain is all of space and the base surface shall be unbounded.
2. The base surface shall be an unbounded surface (subtype of _IfcElementarySurface_).

## Attributes

### BaseSurface
Surface defining side of half space.

### AgreementFlag
The agreement flag is TRUE if the normal to the BaseSurface points away from the material of the IfcHalfSpaceSolid. Otherwise it is FALSE.

### Dim
The space dimensionality of this class, it is always 3
