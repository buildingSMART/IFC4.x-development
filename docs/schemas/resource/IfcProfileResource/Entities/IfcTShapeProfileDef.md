# IfcTShapeProfileDef

_IfcTShapeProfileDef_ defines a section profile that provides the defining parameters of a T-shaped section to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The centre of the position coordinate system is in the profile's centre of the bounding box.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE All profile origins are now in the center of the bounding box.

> IFC4 CHANGE Type of _FilletRadius_, _FlangeEdgeRadius_, and _WebEdgeRadius_ relaxed to allow for zero radius. Trailing attribute _CentreOfGravityInY_ deleted, use respective property in _IfcProfileProperties_ instead.

Figure 1 illustrates parameters of the T-shape profile definition.

![T-shape profile](../../../../figures/ifctshapeprofiledef.gif)

Figure 1 — T-shape profile

<u>Position</u>

The parameterized profile defines its own position coordinate system. The underlying coordinate system is defined by the swept area solid that uses the profile definition. It is the xy plane of:

 * IfcSweptAreaSolid.Position

by using offsets of the position location, the parameterized profile can be positioned centric (using x,y offsets = 0.), or at any position relative to the profile.

## Attributes

### Depth
Web lengths, see illustration above (= h).

### FlangeWidth
Flange lengths, see illustration above (= b).

### WebThickness
Constant wall thickness of web (= ts).

### FlangeThickness
Constant wall thickness of flange (= tg).

### FilletRadius
Fillet radius according the above illustration (= r1).

### FlangeEdgeRadius
Edge radius according the above illustration (= r2).

### WebEdgeRadius
Edge radius according the above illustration (= r3).

### WebSlope
Slope of flange of the profile.

### FlangeSlope
Slope of web of the profile.

## Formal Propositions

### ValidFlangeThickness
The flange thickness shall be smaller than the depth.

### ValidWebThickness
The web thickness shall be smaller than the flange width.
