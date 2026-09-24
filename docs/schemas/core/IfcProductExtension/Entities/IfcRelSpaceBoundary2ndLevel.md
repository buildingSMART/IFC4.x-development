# IfcRelSpaceBoundary2ndLevel

The 2nd level space boundary defines the physical or virtual delimiter of a space by the relationship _IfcRelSpaceBoundary2ndLevel_ to the surrounding elements. 2nd level space boundaries are characterized by:

* 2nd level space boundaries still represent building elements that bound the space, but are more granular in that they are subdivided in any of the following cases:
  * Differences in materials and/or material assemblies (for example, a wainscot or paneling on the lower portion of a wall).
  * Differences in spaces or zones on the other side of the building element (or virtual boundary) represented by the space boundary (for example, two different spaces on the other side of a wall)
* 2nd level space boundaries are differentiated in two ways: virtual or physical and internal or external, whereby any space boundary that is both internal and external has to be split into segments being either internal or external.
* 2nd level space boundaries represent both sides of a heat transfer surface separated by the thickness of the building element. They can be further differentiated in:
  * Type 2a that occurs when there is a space on the opposite side of the building element providing the space boundary
  * Type 2b occurs if there is a building element on the opposite side of the building element providing the space boundary.
* The connection geometry of 2nd level space boundaries is restricted to planar surfaces only. This means that curved surfaces must be segmented.
<!-- end of short definition -->

2nd level space boundaries define the heat transfer surfaces on both sides of building elements that separate spaces. The generation of 2nd level space boundaries has to take building elements and spaces on the other side into account.

> NOTE 2nd level space boundaries are used by many analysis packages that require a surface view of the building that can be transformed into the various simple topological models. Examples of such analysis packages include: (1) energy analysis, (2) lighting analysis, (3) fluid dynamics

> HISTORY New entity in IFC4.

Relationship Use Definitions

As shown in Figure 1, the attribute _ParentBoundary_ with inverse _InnerBoundaries_ is provided to link the space boundaries of doors, windows, and openings to the parent boundary, such as of a wall or slab.

> NOTE The space boundary of the parent is not cut by the inner boundary - both overlap.

The attribute _CorrespondingBoundary_ with inverse _Corresponds_ is provided to link the pair of space boundaries on the opposite sides of the building element.

> NOTE Only 2nd level space boundaries of type A have corresponding boundaries.

![IfcRelSpaceBoundary2ndLevel](../../../../figures/ifcrelspaceboundary2ndlevel-fig1.png "Figure 1 — Space boundary second level relationships")

Geometry Use Definitions

See the definition at the supertype _IfcRelSpaceBoundary_ for guidance on using the connection geometry for second level space boundaries.

## Attributes

### CorrespondingBoundary
Reference to the other space boundary of the pair of two space boundaries on either side of a space separating thermal boundary element.

### Corresponds
Reference to the other space boundary of the pair of two space boundaries on either side of a space separating thermal boundary element.
