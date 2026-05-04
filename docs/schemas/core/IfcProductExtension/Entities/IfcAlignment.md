# IfcAlignment

For the purposes of IFC the English term "alignment" defines three separate but closely interconnected concepts.
<!-- end of short definition -->

1. definition of a reference system for linear positioning
2. safeguarding and optimization of the movement of vehicles - kinematic perspective
3. geometric construction of roads, railway tracks or other linear infrastructure

**Reference system for linear positioning**

An alignment is used to define a reference system to position elements mainly for linear construction works, such as roads, rails, bridges, and others. The relative positioning along the alignment is defined by the linear referencing methodology.

> NOTE See ISO 19148 Geographic information – Linear referencing for general definitions about linear referencing.

**Kinematic perspective**

In the kinematic perspective, the focus is on the safe and optimized movement of a vehicle under the constraints induced by changes in the direction of the horizontal and the vertical layout.

**Geometric perspective**

In the geometric perspective the focus is on the proper placement of horizontal and vertical segments to connect certain points along a proposed path. A huge body of knowledge has been developed over a long period of time, in many aspects predating the availability of modern computers and their software.

Supported shape representations of _IfcAlignment_ are:

* _IfcCompositeCurve_ as a 2D horizontal alignment (represented by its horizontal alignment segments), without a vertical layout.
* _IfcGradientCurve_ as a 3D horizontal and vertical alignment (represented by their alignment segments), without a cant layout.
* _IfcSegmentedReferenceCurve_ as a 3D curve defined relative to an _IfcGradientCurve_ to incorporate the application of cant.
* _IfcOffsetCurveByDistances_ as a 2D or 3D curve defined relative to an _IfcGradientCurve_ or another _IfcOffsetCurveByDistances_.
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 3D alignment by a 3D polyline representation (such as coming from a survey).
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 2D horizontal alignment by a 2D polyline representation (such as in very early planning phases or as a map representation).

**State of the art in contemporary engineering**
Generally, contemporary engineering follows these steps when defining an alignment.

1. First, a horizontal layout in a properly projected plane is established.

2. In a second step, the vertical layout (i.e. sequence of segments with constant gradients, together with smoothing segments showing a variation in gradient) is added.

3. In the rail domain, in most cases a cant layout is added to the horizontal layout to compensate a part of the unwanted lateral acceleration.

4. In a final step, the proposed layout is checked against a defined set of rules, formulas and thresholds to guarantee the conformance against the regulation.

The sequence of steps might change from case to case and might be repeated one or more times to achieve the economic objectives and fulfill regulatory safety requirements.

Contemporary alignment design almost always implements a 2.5 dimension approach. The resulting and documented geometry might be very precise or just good enough to meet safety thresholds. This depends on factors like priorities of the management, date of the design - existing alignments might have been designed more then 50 years ago - or software tools used. Working with legacy data in a high precision BIM model requires a good understanding of these factors.

**Distinction between business logic and geometry definition**

The alignment concept is organised into two parts. These two parts work together, but they can also be used and exchanged independently.

1. *Business logic* of alignment
2. *Geometry definition* of alignment

**Business logic:** the IFC schema allows to describe an alignment using terminology and concepts that are as close as possible to business ones. It allows to describe the layouts that make up the alignment (i.e. horizontal, vertical, cant), their segments' structure and attributes. Also, the *business logic* part provides the anchor point for domain specific properties, such as design speed or cant deficiency.

**Geometry definition:** the IFC schema provides well established IFC geometric entities to represent the business concepts. 

A mapping between the *business logic* and its *geometry definition* in IFC is described by the concept templates related to the alignment geometry.

> NOTE Alignment layouts _IfcAlignmentHorizontal_, _IfcAlignmentVertical_, and _IfcAlignmentCant_ nest _IfcAlignment_ with an _IfcRelNests_ relationship. _IfcRelNests.RelatedObjects_ is an ordered list. The proper order of the alignment layouts is _IfcAlignmentHorizontal_, _IfcAlignmentVertical_, and _IfcAlignmentCant_. When _IfcReferent_ is used to define the start station of the alignment, and it is located within the same _IfcRelNests.RelatedObjects_ list as the alignment layouts, it must precede _IfcAlignmentHorizontal_.

## Attributes

### PredefinedType

## Concepts

### Alignment Aggregation To Project

* Every _IfcAlignment_ must be related to _IfcProject_ using the _IfcRelAggregates_ relationship - either directly or indirectly. The indirect case is when a child alignment is aggregated to a parent alignment. In this case, only the parent alignment must be related to _IfcProject_.
* Instances of _IfcAlignment_ must not be related to spatial elements using _IfcRelContainedInSpatialStructure_.

### Alignment Layouts

A single alignment may be described by one or more of the following layouts:

* a horizontal layout (_IfcAlignmentHorizontal_), defined in the x/y plane of the engineering coordinate system.
* an accompanying vertical layout (_IfcAlignmentVertical_), defined along the horizontal layout in the distance along / z coordinate space.
* an accompanying cant layout (_IfcAlignmentCant_), defined as lateral inclination along the horizontal layout.

These 3 layouts may be used in different configurations. The most common are:

1. Only Horizontal (H) layout
2. Horizontal and Vertical (V) layouts
3. Horizontal, Vertical and Cant (C) layouts
4. Multiple Vertical layouts based on the same Horizontal Layout
5. Multiple Vertical layouts based on the same Horizontal Layout, with a Cant layout applied

(4) and (5) are used in scenarios where multiple alignments re-use the same horizontal layout definition. See **Alignment Layout - Reusing Horizontal Layout** and **Alignment Geometry - Reusing Horizontal Layout** for details on how to relate parent and child alignments in these cases.

![Alignment configurations](../../../../figures/IfcAlignment-possible-configurations.png)

Figure ALCONFIG — Common configurations of alignment layouts

### Alignment Layout - Horizontal, Vertical and Cant

For configurations (1),(2),(3)

### Alignment Layout - Reusing Horizontal Layout

For configurations (4),(5)

### Alignment Geometry - Horizontal

For configuration (1)

### Alignment Geometry - Horizontal and Vertical

For configuration (2)

### Alignment Geometry - Horizontal, Vertical and Cant

For configuration (3)

### Element Decomposition

In scenarios where multiple alignments re-use the same horizontal layout definition, these alignment can be aggregated in a parent-child relationship, to avoid redefining the horizontal layout. This is done using _IfcRelAggregates_.

If the parent alignment has a *geometry definition* for its horizontal layout, then all the children can use this definition as *BaseCurve* to construct their own representations.

### Alignment Geometry - Reusing Horizontal Layout

For configurations (4),(5)

### Alignment Geometry - Segments

### Alignment Spatial Reference

Alignments can be related to a spatial element using _IfcRelReferencedInSpatialStructure_.

### Alignment Grouping

Alignments may be assigned to groups using _IfcRelAssignsToGroup_, where _IfcGroup_ or subtypes may capture information common to multiple alignments.

### Object Nesting

Alignments can nest _IfcReferent_'s, such as stations or mileage points. These can be used as semantic entities holding information about locations along the alignment curve. This is done using the _IfcRelNests_ relationship.

