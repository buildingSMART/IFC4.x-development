# IfcWindowLiningProperties

The window lining is the outer frame which enables the window to be fixed in position. The window lining is used to hold the window panels or other casements. The parameter of the _IfcWindowLiningProperties_ define the geometrically relevant parameter of the lining.
<!-- end of short definition -->

> NOTE The _IfcWindowLiningProperties_ shall only be applied to construct the 3D shape of a window, if the attribute _IfcWindowType_.ParameterTakesPrecedence is set TRUE.

The _IfcWindowLiningProperties_ are included in the set of properties of _IfcWindowType.HasPropertySets_. More information about the window lining can be included in the same set of the _IfcWindowType_ using another _IfcPropertySet_ for dynamic extensions.

The _IfcWindowLiningProperties_ does not hold a geometric representation. However it defines parameters which can be used to create the shape of the window type(which is inserted by the _IfcWindow_ into the spatial context of the project) as shown in Figure 1. The parameters at the _IfcWindowLiningProperties_ define a standard window lining, including (if given) a mullion and a transom (for horizontal and vertical splits). The outer boundary of the lining is determined by the 'Profile' shape representation assigned to the _IfcWindow_, which inserts the _IfcWindowType_.

| Figure | OperationType | Applicable Parameters |
| --- | --- | --- |
| ![lining 5](../../../../figures/ifcwindowliningproperties-fig05.png) | All | LiningDepth, LiningThickness, LiningOffset, LiningToPanelOffsetX, LiningToPanelOffsetY (Note: The inner side is defined as the direction of the window panel opening operation.) |
| ![lining 1](../../../../figures/ifcwindowliningproperties-fig01.png) | DoublePanelVertical (shown), TriplePanelBottom, TriplePanelTop, TriplePanelLeft, TriplePanelRight | MullionThickness, FirstMullionOffset (measured as offset to the Z axis in XZ plane as a normalized ratio measure) |
| ![lining 2](../../../../figures/ifcwindowliningproperties-fig02.png) | DoublePanelHorizontal, TriplePanelBottom, TriplePanelTop, TriplePanelLeft, TriplePanelRight | TransomThickness, FirstTransomOffset (measured as offset to the X axis in XZ plane as a normalized ratio measure) |
| ![lining 3](../../../../figures/ifcwindowliningproperties-fig03.png) | TriplePanelVertical | SecondMullionOffset (measured as offset to the Z axis in XZ plane as a normalized ratio measure) |
| ![lining 4](../../../../figures/ifcwindowliningproperties-fig04.png) | TriplePanelHorizontal | SecondTransomOffset (measured as offset to the X axis in XZ plane as a normalized ratio measure) |

Table 1 — Window lining properties

> HISTORY New entity in IFC2.0. Has been renamed from _IfcWindowLining_ in IFC2x.

> IFC4 CHANGE The following attributes have been added _LiningOffset_, _LiningToPanelOffsetX_, _LiningToPanelOffsetY_. The attribute _ShapeAspectStyle_ is deprecated and shall no longer be used. Supertype changed to new _IfcPreDefinedPropertySet_.

> IFC4.3.2.0 DEPRECATION This entity, and most other subtypes of IfcPredefinedPropertySet, are now deprecated. Use Pset_WindowLiningProperties instead.

## Attributes

### LiningDepth
Depth of the window lining (dimension measured perpendicular to window elevation plane).

### LiningThickness
Thickness of the window lining as explained in the figure above. If _LiningThickness_ value is 0. (zero) it denotes a window without a lining (all other lining parameters shall be set to NIL in this case). If the _LiningThickness_ is NIL it denotes that the value is not available.
> IFC4 CHANGE Data type modified to be _IfcNonNegativeLengthMeasure_.

### TransomThickness
Thickness of the transom (horizontal separator of window panels within a window), measured parallel to the window elevation plane. The transom is part of the lining and the transom depth is assumed to be identical to the lining depth.
If the _TransomThickness_ is set to zero (and the _TransomOffset_ set to a positive length), then the window is divided vertically without a physical divider.
> IFC4 CHANGE Data type changed to _IfcNonNegativeLengthMeasure_.

### MullionThickness
Thickness of the mullion (vertical separator of window panels within a window), measured parallel to the window elevation plane. The mullion is part of the lining and the mullion depth is assumed to be identical to the lining depth.
If the _MullionThickness_ is set to zero (and the _MullionOffset_ set to a positive length), then the window is divided horizontally without a physical divider.
> IFC4 CHANGE Data type changed to _IfcNonNegativeLengthMeasure_.

### FirstTransomOffset
Offset of the transom centerline, measured along the z-axis of the window placement coordinate system. An offset value = 0.5 indicates that the transom is positioned in the middle of the window.

### SecondTransomOffset
Offset of the transom centerline for the second transom, measured along the x-axis of the window placement coordinate system. An offset value = 0.666 indicates that the second transom is positioned at two/third of the window.

### FirstMullionOffset
Offset of the mullion centerline, measured along the x-axis of the window placement coordinate system. An offset value = 0.5 indicates that the mullion is positioned in the middle of the window.

### SecondMullionOffset
Offset of the mullion centerline for the second mullion, measured along the x-axis of the window placement coordinate system. An offset value = 0.666 indicates that the second mullion is positioned at two/third of the window.

### ShapeAspectStyle
Optional link to a shape aspect definition, which points to the part of the geometric representation of the window style, which is used to represent the lining.
> IFC4 CHANGE The attribute is deprecated and shall no longer be used, i.e. the value shall be NIL ($).

### LiningOffset
Offset of the window lining. The offset is given as distance along the y axis of the local placement (perpendicular to the window plane).
> IFC4 CHANGE New attribute added at the end of the entity definition.

### LiningToPanelOffsetX
Offset between the lining and the window panel measured along the x-axis of the local placement. Should be smaller or equal to the _LiningThickness_.
> IFC4 CHANGE New attribute added at the end of the entity definition.

### LiningToPanelOffsetY
Offset between the lining and the window panel measured along the y-axis of the local placement. Should be smaller or equal to the _IfcWindowPanelProperties.PanelThickness_.
> IFC4 CHANGE New attribute added at the end of the entity definition.

## Formal Propositions

### WR31
Either both parameter, _LiningDepth_ and _LiningThickness_ are given, or only the _LiningThickness_, then the _LiningDepth_ is variable. It is not valid to only assert the _LiningDepth_.
> NOTE A _LiningDepth_ with NIL ($) value indicates a window style with a lining equal to the wall thickness.

> IFC4 CHANGE Rule corrected.

### WR32
Either both parameter, _FirstTransomOffset_ and _SecondTransomOffset_ are given, or only the _FirstTransomOffset_, or none of both. It is not valid to only assert the _SecondTransomOffset_.

### WR33
Either both parameter, _FirstMullionOffset_ and _SecondMullionOffset_ are given, or only the _FirstMullionOffset_, or none of both. It is not valid to only assert the _SecondMullionOffset_.

### WR34
The _IfcWindowPanelProperties_ shall only be used in the context of an _IfcDoorType_.
> NOTE The deprecated entity _IfcWindowType_ is applicable as well.
