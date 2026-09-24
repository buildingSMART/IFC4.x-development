# IfcBoxedHalfSpace

The _IfcBoxedHalfSpace_ is used (as its supertype _IfcHalfSpaceSolid_) only within Boolean operations. It divides the domain into exactly two subsets, where the domain in question is that of the attribute _Enclosure_.
<!-- end of short definition -->

The purpose of the attribute _Enclosure_ is to provide a search box for the other operand in the Boolean operation. It shall be sufficiently large to fully enclose the resulting solid after the Boolean operation with the half space. It however does not alter the final result. The result of the Boolean operation would be the same, as if executed by the supertype _IfcHalfSpaceSolid_. See Figure 1 below.

![correct use of enclosure](../../../../figures/ifcboxedhalfspace_01.png "Figure 1 — Boxed half space operands")

The _IfcBoundingBox_ that provides the enclosure is given for the convenience of the receiving application to enable the use of size box comparison for efficiency (for example, to check first whether size boxes intersect, if not no calculations has to be done to check whether the solids of the entities intersect).

![boxed half space](../../../../figures/ifcboxedhalfspace-layout1.png)

Figure 2 — Boxed half space geometry

The <em>Enclosure</em> therefore helps to prevent dealing with infinite-size related issues. The enclosure box is positioned within the object coordinate system, established by the <em>ObjectPlacement</em> of the element represented (for example, by <em>IfcLocalPlacement</em>). Figure 2 shows the <em>Enclosure</em> box being sufficiently large to fully enclose the Boolean result.

> NOTE Definition according to ISO/CD 10303-42:1992
> This entity is a subtype of the half space solid which is trimmed by a surrounding rectangular box. The box has its edges parallel to the coordinate axes of the geometric coordinate system.
> The purpose of the box is to facilitate CSG computations by producing a solid of finite size.

> NOTE Entity adapted from **boxed_half_space** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5.1

> IFC4 CHANGE Usage correct, position coordinate system for _Enclosure_ is the object coordinate system.

## Attributes

### Enclosure
The box which bounds the resulting solid of the Boolean operation involving the half space solid for computational purposes only.

## Formal Propositions

### UnboundedSurface
The BaseSurface defining the half space shall not be a bounded surface.
