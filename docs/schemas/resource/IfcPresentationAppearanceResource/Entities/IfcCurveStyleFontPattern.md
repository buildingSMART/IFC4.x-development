# IfcCurveStyleFontPattern

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-46:1992
> A curve style font pattern is a pair of visible and invisible curve segment length measures in presentation area units.

> NOTE Corresponding ISO 10303 name: curve_style_font_pattern. Please refer to ISO/IS 10303-46:1994 for the final definition of the formal standard.

> HISTORY New entity in IFC2x2.

## Attributes

### VisibleSegmentLength
The length of the visible segment in the pattern definition.
> NOTE For a visible segment representing a point, the value 0. should be assigned.

> IFC2x3 CHANGE The datatype has been changed to IfcLengthMeasure with upward compatibility for file-based exchange.

### InvisibleSegmentLength
The length of the invisible segment in the pattern definition.

## Formal Propositions

### VisibleLengthGreaterEqualZero
The value of a visible pattern length shall be equal or greater then zero.
