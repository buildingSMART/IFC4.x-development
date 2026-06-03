# IfcAxis2PlacementLinear

The _IfcAxis2PlacementLinear_ provides location and orientation to place items in a three-dimensional space confined to the context of a curve. Relative placement axes (Axis and RefDirection) are relative to the curve used for linear referencing provided in _IfcPlacement_ _Location_ (_IfcPointByDistanceExpression_ _BasisCurve_), maintaining the relationship to the tangent of the curve.
<!-- end of short definition -->

## Attributes

### Axis
The exact direction of the local Z Axis.
If Axis is omitted, the direction is taken from the local coordinate frame of the 3D basis curve.
For example, with _IfcGradientCurve_ the Axis direction is taken perpendicular to the tangent of the basis curve in the plane of the basis curve.
For _IfcSegmentedReferenceCurve_ the Axis direction also includes the 'twist' resulting from a deviating elevation relative to the associated _IfcGradientCurve_.

### RefDirection
The direction used to determine the direction of the local X Axis. In case both Axis and RefDirection are set and not perpendicular an adjustment is necessary to maintain orthogonality to the Axis direction. If RefDirection is omitted, the direction is taken from the curve tangent at _Location_.

## Formal Propositions

### WR1
The _Location_ on parent type _IfcPlacement_ shall be of type _IfcPointByDistanceExpression_

### WR2
The _Axis_ and _RefDirection_ shall not be parallel or anti-parallel.

## Informal Propositions

- _Axis_ and _RefDirection_ shall either both be provided or both be omitted.
