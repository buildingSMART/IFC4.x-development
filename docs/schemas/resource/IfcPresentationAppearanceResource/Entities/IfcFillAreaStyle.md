# IfcFillAreaStyle

An _IfcFillAreaStyle_ provides the style table for presentation information assigned to annotation fill areas or surfaces for hatching and tiling. The _IfcFillAreaStyle_defines hatches as model hatches, that is, the distance between hatch lines, or the curve patterns of hatch lines are given in model space dimensions (that have to be scaled using the target plot scale). The _IfcFillAreaStyle_ allows for the following combinations of defining the style of hatching and tiling:

* Solid fill for areas and surfaces by only assigning _IfcColour_ to the set of _FillStyles_. It then provides the background colour for the filled area or surface.
<!-- end of short definition -->

> NOTE Color information of surfaces for rendering is assigned by using _IfcSurfaceStyle_, not by using _IfcFillAreaStyle_.

* Vector based hatching for areas and surfaces based on a single row of hatch lines by assigning a single instance of _IfcFillAreaStyleHatching_ to the set of _FillStyles_.
  * If an instance of _IfcColour_ is assigned in addition to the set of _FillStyles_, it provides the background colour for the hatching.

* Vector based hatching for areas and surfaces based on two (potentially crossing) rows of hatch lines by assigning two instances of _IfcFillAreaStyleHatching_ to the set of _FillStyles._
  * If an instance of _IfcColour_ is assigned in addition to the set of _FillStyles_, it provides the background colour for the hatching.


>
>> NOTE Assigning more then two instances of _IfcFillAreaStyleHatching_ to define three or more rows of hatch lines is not encouraged.


>
* Tiling for areas and surfaces by assigning a single instance of _IfcFillAreaStyleTiles_ to the set of _FillStyles_.
  * If an instance of _IfcColour_ is assigned in addition to the set of _FillStyles_, it provides the background colour for the tiling.


* Externally defined hatch style by assigning a single instance of _IfcExternallyDefinedHatchStyle_ to the set of _FillStyles_.
  * If an instance of _IfcColour_ is assigned in addition to the set of _FillStyles_, it provides the background colour for the hatching.

Measures given to a hatch or tile pattern are given in global drawing length units.

> NOTE Global units are defined at the single _IfcProject_ instance, given by _UnitsInContext:IfcUnitAssignment_, the same units are used for the geometric representation items and for the style definitions.

The measure values for hatch or tile pattern apply to the model space with a target plot scale provided for the correct appearance in the default plot scale.

> NOTE the target plot scale is given by _IfcGeometricRepresentationSubContext.TargetScale_.

> NOTE Definition according to ISO/CD 10303-46:1992
> The style for filling visible curve segments, annotation fill areas or surfaces with tiles or hatches.

> NOTE Corresponding ISO 10303 name: fill_area_style. Please refer to ISO/IS 10303-46:1994 for the final definition of the formal standard.

> HISTORY New entity in IFC2x2.

> DEPRECATION The use of IfcFillAreaStyleTiles is deprecated, as its definition might change is future releases.

## Attributes

### FillStyles
The set of fill area styles to use in presenting visible curve segments, annotation fill areas or surfaces.

### ModelOrDraughting
Indication whether the length measures provided for the presentation style are model based, or draughting based.
> IFC4 CHANGE New attribute.

## Formal Propositions

### MaxOneColour
There shall be a maximum of one colour assignment to the fill area style.

### MaxOneExtHatchStyle
There shall be a maximum of one externally defined hatch style assignment to the fill area style.

### ConsistentHatchStyleDef
Either the fill area style contains a definition from an externally defined hatch style, or from (one or many) fill area style hatchings or from (one or many) fill area style tiles, but not a combination of those three types.
