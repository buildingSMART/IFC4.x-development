# IfcUShapeProfileDef

_IfcUShapeProfileDef_ defines a section profile that provides the defining parameters of a U-shape (channel) section to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The centre of the position coordinate system is in the profile's centre of the bounding box.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE All profile origins are now in the center of the bounding box.

> IFC4 CHANGE Type of _FilletRadius_ and _EdgeRadius_ relaxed to allow for zero radius. Trailing attribute _CentreOfGravityInX_ deleted, use respective property in _IfcProfileProperties_ instead.

Figure 1 illustrates parameters of the U-shape profile definition.

![U-shape profile](../../../../figures/ifcushapeprofiledef.gif)

Figure 1 — U-shape profile

<u>Position</u>

The parameterized profile defines its own position coordinate system. The underlying coordinate system is defined by the swept area solid that uses the profile definition. It is the xy plane of:

 * <em>IfcSweptAreaSolid.Position</em>

By using offsets of the position location, the parameterized profile can be positioned centric (using x,y offsets = 0.), or at any position relative to the profile.

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

### EdgeRadius
Edge radius according the above illustration (= r2).

### FlangeSlope
Slope of flange of the profile.

## Formal Propositions

### ValidFlangeThickness
The flange thickness shall be smaller than half of the depth.

### ValidWebThickness
The web thickness shall be smaller than the flange width.
