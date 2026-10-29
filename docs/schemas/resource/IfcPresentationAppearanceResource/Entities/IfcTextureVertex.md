# IfcTextureVertex

An _IfcTextureVertex_ is a list of 2 (S, T) texture coordinates.
<!-- end of short definition -->

> NOTE Definition according to ISO/IEC 19775-1 :
>
> Each vertex-based geometry node uses a set of 2D texture coordinates that map textures to vertices. Texture map values ( ImageTexture, PixelTexture) range from [0.0, 1.0] along the S-axis and T-axis. However, texture coordinate values may be in the range (-∞,∞). Texture coordinates identify a location (and thus a colour value) in the texture map. The horizontal coordinate S is specified first, followed by the vertical coordinate T. If the texture map is repeated in a given direction (S-axis or T-axis), a texture coordinate C (s or t) is mapped into a texture map that has N pixels in the given direction as follows: <pre style=" font-size:larger;">
<b>Texture map location = (C - floor(C)) × N</b>
</pre>

> If the texture map is not repeated, the texture coordinates are clamped to the 0.0 to 1.0 range as follows: <pre style=" font-size:larger;">
<b>Texture map location = N,   if C > 1.0,
<br>           = 0.0,  if C < 0.0,
<br>           = C × N, if 0.0 ≤ C ≤ 1.0.</b>
</pre>

> NOTE Texture coordinates may be transformed (scaled, rotated, translated) by supplying a TextureTransform as a component of the texture's definition.

> HISTORY New entity in IFC2x2.

## Attributes

### Coordinates
The first Coordinate[1] is the S, the second Coordinate[2] is the T parameter value.
