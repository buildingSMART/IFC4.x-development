# IfcLShapeProfileDef

_IfcLShapeProfileDef_ defines a section profile that provides the defining parameters of an L-shaped section (equilateral L profiles are also covered by this entity) to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The shorter leg has the same direction as the positive _Position.P[1]_-axis, the longer or equal leg the same as the positive _Position.P[2]_-axis. The centre of the position coordinate system is in the profiles centre of the bounding box.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE All profile origins are now in the center of the bounding box.

> IFC4 CHANGE Types of _FilletRadius_ and _EdgeRadius_ were relaxed to allow for zero values.
> Trailing attributes _CentreOfGravityInX_ and _CentreOfGravityInY_ deleted, use respective properties in _IfcProfileProperties_ instead.
> WHERE rule which required _Width_ <= _Depth_ removed.

Figure 1 and Figure 2 illustrates parameters of equal-sided and non-equal sided L-shaped section definitions.

![non equal sided L-shape](../../../../figures/ifclshapeprofiledef_layout1.gif)

Figure 1 — Non-equal L-shape profile

The parameterized profile defines its own position coordinate system. The underlying coordinate system is defined by the swept area solid that uses the profile definition. It is the xy plane of <em>IfcSweptAreaSolid.Position</em> by using offsets of the position location, the parameterized profile can be positioned centric (using x,y offsets = 0.), or at any position relative to the profile.

In the illustrated example, the 'CentreOfGravityInX' and 'CentreOfGravityInY' properties in <em>IfcProfileProperties</em>, if provided, are both negative.

![equal sided L-shape](../../../../figures/ifclshapeprofiledef_layout2.gif)

Figure 2 — Equal L-shape profile

> NOTE The black coordinate axes show the underlying coordinate system of the swept surface or swept area solid

The profile is inserted into the underlying coordinate system of the swept area solid by using the <em>Position</em> attribute. In this example (cardinal point of gravity) the attribute values of <em>IfcAxis2Placement2D</em> are:

```
Location = IfcCartesianPoint(+|CentreOfGravityInX|, +|CentreOfGravityInY|)
RefDirection = NIL (defaults to 1.,0.)
```

In the illustrated example, the x and y value of <em>Position.Location</em>, i.e. the <u>measures</u> |CentreOfGravityInX| and |CentreOfGravityInY| are both positive. On the other hand, the <u>properties</u> named 'CentreOfGravityInX' and 'CentreOfGravityInY' in <em>IfcProfileProperties</em>, if provided, must both be set to 0 now because the centre of gravity of the resulting profile definition is located in the coordinate origin.

## Attributes

### Depth
Leg length, see illustration above (= h). Same as the overall depth.

### Width
Leg length, see illustration above (= b). Same as the overall width. This attribute is formally optional for historic reasons only. Whenever the width is known, it shall be provided by value.

### Thickness
Constant wall thickness of profile, see illustration above (= ts).

### FilletRadius
Fillet radius according the above illustration (= r1).

### EdgeRadius
Edge radius according the above illustration (= r2).

### LegSlope
Slope of the inner face of each leg of the profile.

## Formal Propositions

### ValidThickness
The thickness shall be smaller than the depth and width.
