# IfcZShapeProfileDef

_IfcZShapeProfileDef_ defines a section profile that provides the defining parameters of a Z-shape section to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The centre of the position coordinate system is in the profile's centre of the bounding box.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Type of _FilletRadius_ and _EdgeRadius_ relaxed to allow for zero radius.

Figure 1 illustrates parameters of the Z-shape profile definition.

![Z-shape profile](../../../../figures/ifczshapeprofiledef.gif)

Figure 1 — Z-shape profile

<u>Position</u>

The parameterized profile defines its own position coordinate system.
The underlying coordinate system is defined by the swept area solid
that uses the profile definition. It is the xy plane of:

 * IfcSweptAreaSolid.Position

By using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile.


## Attributes

### Depth
Web length, see illustration above (= h).

### FlangeWidth
Flange length, see illustration above (= b).

### WebThickness
Constant wall thickness of web, see illustration above (= ts).

### FlangeThickness
Constant wall thickness of flange, see illustration above (= tg).

### FilletRadius
Fillet radius according the above illustration (= r1).

### EdgeRadius
Edge radius according the above illustration (= r2).

## Formal Propositions

### ValidFlangeThickness
The flange thickness shall be smaller than half of the depth.
