# IfcTextStyleTextModel

The _IfcTextStyleTextModel_ combines all text style properties, that affect the presentation of a text literal within a given extent. It includes the spacing between characters and words, the horizontal and vertical alignment of the text within the planar box of the extent, decorations (like underline), transformations of the literal (like uppercase), and the height of each text line within a multi-line text block.
<!-- end of short definition -->

> Definition according to W3C for Cascading Style Sheets:
> The properties defined in the text model affect the visual presentation of characters, spaces, words, and paragraphs.

> NOTE Corresponding CSS1 definitions are Text properties (word-spacing, letter-spacing, text-decoration, vertical-align, text-transform, text-align, text-indent, line-height).

> HISTORY New entity in IFC2x3.

## Attributes

### TextIndent
The property specifies the indentation that appears before the first formatted line.

> NOTE It has been introduced for later compliance to full CSS support.

### TextAlign
This property describes how text is aligned horizontally within the element. The actual justification algorithm used is dependent on the rendering algorithm.

### TextDecoration
This property describes decorations that are added to the text of an element.

### LetterSpacing
The length unit indicates an addition to the default space between characters. Values can be negative, but there may be implementation-specific limits. The importing application is free to select the exact spacing algorithm. The letter spacing may also be influenced by justification (which is a value of the _TextAlign_ attribute).
> NOTE The following values are allowed, _IfcDescriptiveMeasure_ with value='normal', _IfcRatioMeasure_, or _IfcLengthMeasure_, where the length unit is globally defined at _IfcUnitAssignment_.

### WordSpacing
The length unit indicates an addition to the default space between words. Values can be negative, but there may be implementation-specific limits. The importing application is free to select the exact spacing algorithm. The word spacing may also be influenced by justification (which is a value of the 'text-align' property).

> NOTE It has been introduced for later compliance to full CSS support.

### TextTransform
This property describes how text characters may transform to upper case, lower case, or capitalized case, independent of the character case used in the text literal.

> NOTE It has been introduced for later compliance to full CSS support.

### LineHeight
The property sets the distance between two adjacent lines' baselines.
When a ratio value is specified, the line height is given by the font size of the current element multiplied with the numerical value. A value of 'normal' sets the line height to a reasonable value for the element's font. It is suggested that importing applications set the 'normal' value to be a ratio number in the range of 1.0 to 1.2.

> NOTE The following values are allowed: _IfcDescriptiveMeasure_ with value='normal', or _IfcLengthMeasure_, with non-negative values, the length unit is globally defined at _IfcUnitAssignment_, or _IfcRatioMeasure_.__
