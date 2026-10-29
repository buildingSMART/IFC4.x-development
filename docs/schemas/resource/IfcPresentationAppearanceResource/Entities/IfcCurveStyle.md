# IfcCurveStyle

An _IfcCurveStyle_ provides the style table for presentation information assigned to geometric curves. The style is defined by a color, a font and a width. The _IfcCurveStyle_ defines curve patterns as model patterns, that is, the distance between visible and invisible segments of curve patterns are given in model space dimensions (that have to be scaled using the target plot scale).
<!-- end of short definition -->

Styles are intended to be shared by multiple _IfcStyledItem_'s, assigning the style to occurrences of (subtypes of) _IfcGeometricRepresentationItem_'s. Measures given to a font pattern or a curve width are given in global drawing length units.

> NOTE global units are defined at the single _IfcProject_ instance, given by _UnitsInContext:IfcUnitAssignment_, the same units are used for the geometric representation items and for the style definitions.

The measure values for font pattern and curve width apply to the model space with a target plot scale provided for the correct appearance in the default plot scale.

> NOTE the target plot scale is given by _IfcGeometricRepresentationSubContext.TargetScale_.

An _IfcCurveStyle_ can be assigned to _IfcGeometricRepresentationItem_'s via the _IfcStyledItem_.

> NOTE Definition according to ISO/CD 10303-46:1992
> A curve style specifies the visual appearance of curves.

> NOTE Corresponding ISO 10303 name: curve_style. Please refer to ISO/IS 10303-46:1994 for the final definition of the formal standard.

> HISTORY New entity in IFC2x2.

## Attributes

### CurveFont
A curve style font which is used to present a curve. It can either be a predefined curve font, or an explicitly defined curve font. Both may be scaled. If not given, then the curve font should be taken from the layer assignment with style, if that is not given either, then the default curve font applies.

### CurveWidth
A positive length measure in units of the presentation area for the width of a presented curve. If not given, then the style should be taken from the layer assignment with style, if that is not given either, then the default style applies.

### CurveColour
The colour of the visible part of the curve. If not given, then the colour should be taken from the layer assignment with style, if that is not given either, then the default colour applies.

### ModelOrDraughting
Indication whether the length measures provided for the presentation style are model based, or draughting based.
> IFC4 CHANGE New attribute.

## Formal Propositions

### MeasureOfWidth
The curve width, if provided, shall be given by an _IfcPositiveLengthMeasure_ representing the curve width in the default measure unit, or by an _IfcDescriptiveMeasure_ with the value 'by layer' representing the curve width by the default curve width at the associated layer.

### IdentifiableCurveStyle
At minimum one of the three attribute values have to be provided, _CurveFont_, _CurveWidth_, _CurveColour_.
