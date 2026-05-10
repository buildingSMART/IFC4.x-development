![image](https://github.com/user-attachments/assets/d496b421-29d2-435b-8210-2d395f883c82)

# IfcTextLiteral

The text literal is a geometric representation item which describes a text string using a string literal and additional position and path information. The text size and appearance is determined by the _IfcTextStyle_ that is associated to the _IfcTextLiteral_ through an _IfcStyledItem_.
<!-- end of short definition -->

The text string is placed within the planar extent (the box) defined within the subtype _IfcTextLiteralWithExtent_.

> NOTE Entity adapted from **text_literal** defined in ISO10303-46

> HISTORY New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE The _IfcTextLiteral_ has been changed by removing _Font_ and _Alignment_.

{ .deprecated}
> DEPRECATION The use of _IfcTextLiteral_ is deprecated and it will be made abstract.

## Attributes

### Literal
The text literal to be presented.

### Placement
An _IfcAxis2Placement_ that determines the placement and orientation of the presented string.

### Path
The writing direction of the text literal.
