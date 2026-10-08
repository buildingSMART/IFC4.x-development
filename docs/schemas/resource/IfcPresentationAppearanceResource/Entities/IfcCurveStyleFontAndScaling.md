# IfcCurveStyleFontAndScaling

The _IfcCurveStyleFontAndScaling_ allows for the reuse of the same curve style definition in several sizes. The definition of the _CurveFontScale_ is the scaling of a base curve style pattern to be used as a new or derived curve style pattern.
<!-- end of short definition -->

> NOTE The _CurveFontScale_ should not be mixed up with the target plot scale.

An example for _IfcCurveStyleFontAndScaling_ is the sizing of a basic curve style dash pattern 'dash' (visible 0.01m, invisible 0.005m) into 'dash large' with _CurveFontScale_ = 2 (resulting in visible 0.02m, invisible 0.01m), and into 'dash small' with _CurveFontScale_ = 0.5 (resulting in visible 0.005m, invisible 0.0025m).

> NOTE Definition according to ISO/CD 10303-46:1992
> A curve style font and scaling is a curve style font and a scalar factor for that font, so that a given curve style font may be applied at various scales.

> NOTE Corresponding ISO 10303 name: curve_style_font_and_scaling. Please refer to ISO/IS 10303-46:1994 for the final definition of the formal standard.

> HISTORY New entity in IFC2x2.

## Attributes

### Name
Name that may be assigned with the scaling of a curve font.

### CurveFont
The curve font to be scaled.

### CurveFontScaling
The scale factor.
