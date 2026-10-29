# IfcTransitionCode

_IfcTransitionCode_ indicates the continuity between consecutive segments of a curve or surface.
<!-- end of short definition -->

> EXAMPLE In ContSameGradient the tangent vectors of successive segments will have the same direction, but may have different magnitude.

Figure 1 illustrates transition types

> NOTE The figure is quoted from ISO 10303-42.

![transition code](../../../../figures/ifctransitioncode.gif "Figure 1 — Transition code")

> NOTE Definition according to ISO/CD 10303-42:1992
> This type conveys the continuity properties of a composite curve or surface. The continuity referred to is geometric, not parametric continuity.

> NOTE Type adapted from **transition_code** defined in ISO 10303-42.

> HISTORY New Type in IFC1.0

## Items

### DISCONTINUOUS
The segments do not join. This is permitted only at the boundary of the curve or
surface to indicate that it is not closed.

### CONTINUOUS
The segments join but no condition on their tangents is implied.

### CONTSAMEGRADIENT
The segments join and their tangent vectors or tangent planes are parallel and
have the same direction at the joint: equality of derivatives is not required.

### CONTSAMEGRADIENTSAMECURVATURE
For a curve, the segments join, their tangent vectors are parallel and in the same direction and their curvatures are equal at the joint: equality of derivatives is not required. For a surface this implies that the principle curvatures are the same and the principle directions are coincident along the
common boundary.
