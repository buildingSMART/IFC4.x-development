# IfcAxis1Placement

The _IfcAxis1Placement_ provides location and direction of a single axis.
<!-- end of short definition -->

![axis1 placement](../../../../figures/ifcaxis1placement-layout1.gif)

Figure 1 — Axis1 placement

Figure 1 illustrates the definition of the <em>IfcAxis1Placement</em> within the parent three-dimensional coordinate system.

> NOTE Definition according to ISO/CD 10303-42:1992
> The direction and location in three dimensional space of a single axis. An axis1_placement is defined in terms of a locating point (inherited from placement supertype) and an axis direction: this is either the direction of axis or defaults to (0.0,0.0,1.0). The actual direction for the axis placement is given by the derived attribute z.

> NOTE Entity adapted from **axis1_placement** defined in ISO10303-42.

> HISTORY New entity in IFC1.5

## Attributes

### Axis
The direction of the local Z axis.

### Z
The normalized direction of the local Z axis. It is either identical with the Axis value, if given, or it defaults to [0.,0.,1.]

## Formal Propositions

### AxisIs3D
The Axis when given should only reference a three-dimensional IfcDirection.

### LocationIs3D
The Cartesian point defining the Location shall have the dimensionality of 3.

### LocationIsCP

