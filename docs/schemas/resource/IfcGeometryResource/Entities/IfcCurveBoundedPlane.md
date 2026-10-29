# IfcCurveBoundedPlane

The _IfcCurveBoundedPlane_ is a parametric planar surface with curved boundaries defined by one or more boundary curves. The bounded plane is defined to be the portion of the basis surface in the direction of N x T from any point on the boundary, where N is the surface normal and T the boundary curve tangent vector at this point. The region so defined shall be arcwise connected.
<!-- end of short definition -->

The _BasisSurface_ is an _IfcPlane_ that establishes the position coordinate system by _SELF\IfcElementarySurface.Position_. The _OuterBoundary_ and the _InnerBoundaries_ (if provided) shall lie on the surface of _IfcPlane_. The outer and inner boundary curves shall be defined using the _u_, and _v_ values provided by parameterization of the _BasisSurface_ as their _x_, and _y_ coordinate values.

> NOTE Entity defined in analogy to **curve_bounded_surface** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5

> IFC2x CHANGE The data type of the attribute _OuterBoundary_ and _InnerBoundaries_ has been changed from _Ifc2DCompositeCurve_ to supertype _IfcCurve_.

## Attributes

### BasisSurface
The surface to be bound.

### OuterBoundary
The outer boundary of the surface.

### InnerBoundaries
A potentially empty set of inner boundaries. They shall not intersect each other or the outer boundary.
