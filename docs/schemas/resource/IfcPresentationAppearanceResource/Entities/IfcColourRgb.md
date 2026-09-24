# IfcColourRgb

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-46:1992
> A colour rgb as a subtype of colour specifications is defined by three colour component values for red, green, and blue in the RGB colour model.

> NOTE In contrary to the usual value range of colour components being integer from 0...255, the definition from ISO10303-46 defines the colour components as real from 0.0 ... 1.0. Applications need to execute this conversion before populating the colour RGB values.

> NOTE Corresponding STEP name: colour_rgb. The name attribute has been omitted, the data type for the red, green and blue parts is _IfcNormalisedRatioMeasure_, that already includes the range restrictions for the values. Please refer to ISO/IS 10303-46:1994, p. 138 for the final definition of the formal standard.

> HISTORY New entity in IFC2x2.

## Attributes

### Red
The intensity of the red colour component.
> NOTE The colour component value is given within the range of 0..1, and not within the range of 0..255 as otherwise usual.

### Green
The intensity of the green colour component.
> NOTE The colour component value is given within the range of 0..1, and not within the range of 0..255 as otherwise usual.

### Blue
The intensity of the blue colour component.
> NOTE The colour component value is given within the range of 0..1, and not within the range of 0..255 as otherwise usual.
