# IfcSurfaceOfLinearExtrusion

The _IfcSurfaceOfLinearExtrusion_ is a surface derived by sweeping a curve along a vector.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> This surface is a simple swept surface or a generalized cylinder obtained by sweeping a curve in a given direction. The parameterization is as follows where the curve has a parameterization λ(_u_):
>
> V = ExtrusionAxis
>
> ![Image](../../../../figures/ifcsurfaceoflinearextrusion-math1.gif)
> The parameterization range for _v_ is -∞ < _v_ < ∞ and for _u_ it is defined by the curve parameterization.

> NOTE Entity adapted from **surface_of_linear_extrusion** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. The surface shall not self-intersect

## Attributes

### ExtrudedDirection
The direction of the extrusion.

### Depth
The depth of the extrusion, it determines the parameterization.

### ExtrusionAxis
The extrusion axis defined as vector.

## Formal Propositions

### DepthGreaterZero

