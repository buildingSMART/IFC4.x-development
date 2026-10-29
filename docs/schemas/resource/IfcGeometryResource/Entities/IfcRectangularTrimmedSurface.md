# IfcRectangularTrimmedSurface

The _IfcRectangularTrimmedSurface_ is a surface created by bounding its _BasisSurface_ along two pairs of parallel curves defined within the parametric space of the referenced surface.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> The trimmed surface is a simple bounded surface in which the boundaries are the constant parametric lines _u_~1~ = u1, _u_~2~ = u2, _v_~1~ = v1 and _v_~2~ = v2. All these values shall be within the parametric range of the referenced surface. Cyclic properties of the parameter range are assumed. The rectangular trimmed surface inherits its parameterization directly from the basis surface and has parameter ranges from 0 to |_u_~2~ - _u_~1~| and 0 to|_v_~2~-_v_~1~|.

> NOTE If the surface is closed in a given parametric direction, the values of _u_~2~ or _v_~2~ may require to be increased by the cyclic range.

> EXAMPLE 370 degrees is equivalent to 10 degrees, for those surfaces whose parametric form is defined using circular functions (sine and cosine).

> NOTE Entity adapted from **rectangular_trimmed_surface** in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. The domain of the trimmed surface shall be within the domain of the surface being trimmed.

## Attributes

### BasisSurface
Surface being trimmed.

### U1
First u parametric value.

### V1
First v parametric value.

### U2
Second u parametric value.

### V2
Second v parametric value.

### Usense
Flag to indicate whether the direction of the first parameter of the trimmed surface agrees with or opposes the sense of u in the basis surface.

### Vsense
Flag to indicate whether the direction of the second parameter of the trimmed surface agrees with or opposes the sense of v in the basis surface.

## Formal Propositions

### U1AndU2Different
U1 and U2 shall have different values.

### V1AndV2Different
V1 and V2 shall have different values.

### UsenseCompatible
With exception of those surfaces closed in the U parameter, direction Usense shall be compatible with the ordered parameter values for U.

### VsenseCompatible
Vsense shall be compatible with the ordered parameter values for V.
