# IfcTextStyle

The _IfcTextStyle_ is a presentation style for annotations that place a text in model space. The _IfcTextStyle_ provides the text style for presentation information assigned to _IfcTextLiteral_'s. The style is defined by color, text font characteristics, and text box characteristics.
<!-- end of short definition -->

An _IfcTextStyle_ is instantiated with:

* _TextCharacterAppearance_: _IfcTextStyleForDefinedFont_
* _TextStyle_: _IfcTextStyleTextModel_
* _TextFontStyle_: _IfcTextStyleFontModel_

An _IfcTextStyle_ is assigned to _IfcTextLiteral_ through the _IfcStyledItem_ entity.

> NOTE Entity adopted from font properties (font-family, font-style, font-variant, font-weight, font-size), Color and background properties (color, background-color) and text properties (word-spacing, letter-spacing, text-decoration, text-transform, text-align, text-indent, line-height) defined in [CSS-1](../content/bibliography.htm#CSS1).

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE The _IfcTextStyle_ has been changed by adding _TextFontStyle_ and different data types for _TextStyle_ and _IfcTextCharacterAppearance_.

> IFC4 CHANGE The _IfcTextStyle_ has been simplified by removing old vector based text style definitions.

## Attributes

### TextCharacterAppearance
A character style to be used for presented text.
> IFC4 CHANGE Superfluous select type IfcCharacterStyleSelect has been removed.

### TextStyle
The style applied to the text block for its visual appearance.
> IFC2x3 CHANGE The attribute _TextBlockStyle_ has been changed from SET[1:?] to a non-aggregated optional and renamed into _TextStyles_.

> IFC4 CHANGE The IfcTextStyleWithBoxCharacteristics and the now superfluous select type IfcTextStyleSelect have been removed.

### TextFontStyle
The style applied to the text font for its visual appearance. It defines the font family, font style, weight and size.

> IFC2x2 Add2 CHANGE The attribute _TextFontStyle_ is a new attribute attached to _IfcTextStyle_.

### ModelOrDraughting
Indication whether the length measures provided for the presentation style are model based, or draughting based.
> IFC4 CHANGE New attribute.
