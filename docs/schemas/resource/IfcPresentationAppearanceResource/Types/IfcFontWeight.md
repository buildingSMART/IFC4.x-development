# IfcFontWeight

The _IfcFontWeight_ type defines the weight of the font. Values are:

* normal
* bold
* 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900
<!-- end of short definition -->

> NOTE Definition according to Cascading Style Sheets, level 1
> The values '100' to '900' form an ordered sequence, where each number indicates a weight that is at least as dark as its predecessor. The keyword 'normal' is synonymous with '400', and 'bold' is synonymous with '700'. Keywords other than 'normal' and 'bold' have been shown to be often confused with font names and a numerical scale was therefore chosen for the 9-value list.

> Fonts (the font data) typically have one or more properties whose values are names that are descriptive of the "weight" of a font. There is no accepted, universal meaning to these weight names. Their primary role is to distinguish faces of differing darkness within a single font family. Usage across font families is quite variant; for example a font that you might think of as being bold might be described as being _Regular, Roman, Book, Medium, Semi-_ or _DemiBold, Bold,_ or _Black,_ depending on how black the "normal" face of the font is within the design. Because there is no standard usage of names, the weight property values in CSS1 are given on a numerical scale in which the value '400' (or 'normal') corresponds to the "normal" text face for that family. The weight name associated with that face will typically be _Book, Regular, Roman, Normal_ or sometimes _Medium_.

> The association of other weights within a family to the numerical weight values is intended only to preserve the ordering of darkness within that family. However, the following heuristics tell how the assignment is done in typical cases: > * If the font family already uses a numerical scale with nine values (such as with _OpenType_), the font weights should be mapped directly.
> * If there is both a face labeled _Medium_ and one labeled _Book, Regular, Roman_ or _Normal,_ then the _Medium_ is normally assigned to the '500'.
> * The font labeled "Bold" will often correspond to the weight value '700'.
> * If there are fewer then 9 weights in the family, the default algorithm for filling the "holes" is as follows. If '500' is unassigned, it will be assigned the same font as '400'. If any of the values '600', '700', '800' or '900' remains unassigned, they are assigned to the same face as the next darker assigned keyword, if any, or the next lighter one otherwise. If any of '300', '200' or '100' remains unassigned, it is assigned to the next lighter assigned keyword, if any, or the next darker otherwise.

> The following two examples illustrate the process. Assume four weights in the "Example1" family, from lightest to darkest: _Regular, Medium, Bold, Heavy._ And assume six weights in the "Example2" family: _Book, Medium, Bold, Heavy, Black, ExtraBlack._ Note how in the second example it has been decided _not_ to assign "Example2 ExtraBlack" to anything. <pre>Available faces    | Assignments  | Filling the holes<br>----------------------+---------------+-------------------<br>"Example1 Regular"  | 400      | 100, 200, 300<br>"Example1 Medium"   | 500      |<br>"Example1 Bold"    | 700      | 600<br>"Example1 Heavy"   | 800      | 900<br></pre><pre>Available faces    | Assignments  | Filling the holes<br>----------------------+---------------+-------------------<br>"Example2 Book"    | 400      | 100, 200, 300<br>"Example2 Medium"   | 500      |<br>"Example2 Bold"    | 700      | 600 <br>"Example2 Heavy"   | 800      |<br>"Example2 Black"   | 900      |<br>"Example2 ExtraBlack" | (none)    |<br></pre>

> NOTE Type adopted from **font-weight** defined in [CSS-1](../content/bibliography.htm#CSS1).

> HISTORY New type in IFC2x2 Add2.

## Formal Propositions

### WR1

