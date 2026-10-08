# IfcIShapeProfileDef

_IfcIShapeProfileDef_ defines a section profile that provides the defining parameters of an 'I' or 'H' section. The I-shape profile has values for its overall depth, width and its web and flange thicknesses. Additionally a fillet radius, flange edge radius, and flange slope may be given. This profile definition represents an I-section which is symmetrical about its major and minor axes; top and bottom flanges are equal and centred on the web.
<!-- end of short definition -->

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Type of _FilletRadius_ relaxed to allow for zero radius. Attributes _FlangeEdgeRadius_ and _FlangeSlope_ added.

Figure 1 illustrates parameters of the I-shape profile definition.

![I-shape profile](../../../../figures/ifcishapeprofiledef-layout1.gif)

<u>Position</u>

The parameterized profile defines its own position coordinate system. The underlying coordinate system is defined by the swept area solid that uses the profile definition. It is the xy plane of:

 * IfcSweptAreaSolid.Position

by using offsets of the position location, the parameterized profile can be positioned centric (using x,y offsets = 0.), or at any position relative to the profile. Explicit coordinate offsets are used to define cardinal points (e.g. upper-left bound).

<u>Parameter</u>

The parameterized profile is defined by a set of parameter attributes, see attribute definition below.

![I shape with fillet](../../../../figures/ifcishapeprofiledef-layout2.gif)

Figure 1 — I-shape profile

> NOTE The black coordinate axes show the underlying coordinate system of the swept surface or swept area solid

<u>Position</u>

The profile is inserted into the underlying coordinate system of the swept area solid by using the <em>Position</em> attribute. In this example (cardinal point of lower left corner) the attribute values of <em>IfcAxis2Placement2D</em> are:

```
Location = IfcCartesianPoint(<1/2 OverallWidth>,<1/2 OverallDepth>)
RefDirection = NIL (defaults to 1.,0.)
```

<u>Parameter</u>
If the <em>FilletRadius</em>
is given, it is equally applied to all four corners created by the web
and flanges.

## Attributes

### OverallWidth
Total extent of the width, defined parallel to the x axis of the position coordinate system.

### OverallDepth
Total extent of the depth, defined parallel to the y axis of the position coordinate system.

### WebThickness
Thickness of the web of the I-shape. The web is centred on the x-axis and the y-axis of the position coordinate system.

### FlangeThickness
Flange thickness of the I-shape. Both, the upper and the lower flanges have the same thickness and they are centred on the y-axis of the position coordinate system.

### FilletRadius
The fillet between the web and the flange. 0 if sharp-edged, omitted if unknown.

### FlangeEdgeRadius
Radius of the lower edges of the top flange and the upper edges of the bottom flange. 0 if sharp-edged, omitted if unknown.

### FlangeSlope
Slope of the lower faces of the top flange and of the upper faces of the bottom flange. Non-zero in case of tapered flanges, 0 in case of parallel flanges, omitted if unknown.

## Formal Propositions

### ValidFlangeThickness
The sum of flange thicknesses shall be less than the overall depth.

### ValidWebThickness
The web thickness shall be less then the flange width.

### ValidFilletRadius
The FilletRadius, if given, shall be within the range of allowed values.
