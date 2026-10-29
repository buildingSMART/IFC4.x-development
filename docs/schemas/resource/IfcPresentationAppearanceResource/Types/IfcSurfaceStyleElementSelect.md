# IfcSurfaceStyleElementSelect

The _IfcSurfaceStyleElementSelect_ provides a selection between different surface styles, including _IfcSurfaceStyleRendering_ for rendering properties, _IfcSurfaceStyleLighting_, which holds the exact physically based lighting properties for lighting based calculation algorithms (as the opposite to the rendering based calculation), the _IfcSurfaceStyleRefraction_ (for more advanced refraction indices) and _IfcSurfaceStyleWithTextures_ to allow for image textures applied to surfaces. In addition an _IfcExternallyDefinedSurfaceStyle_ can be selected that points into an external rendering material library.
<!-- end of short definition -->

> NOTE The _IfcSurfaceStyleLighting_ are needed for exact lighting calculation, because physically based lighting calculation algorithms need exact physically based parameters. The factors in _IfcSurfaceStyleRendering_ lack the physical base, they are intended for rendering calculations, but a lighting calculation based software cannot use these values.

> NOTE Definition according to ISO/CD 10303-46:1992
> The surface style element select is a selection of the different surface styles to use in the presentation of the side of a surface.

> NOTE Type adapted from **surface_style_element_select** defined in ISO10303-46.

> HISTORY New select type in IFC2x2.
