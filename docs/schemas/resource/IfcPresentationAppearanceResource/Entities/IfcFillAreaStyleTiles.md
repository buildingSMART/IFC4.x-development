# IfcFillAreaStyleTiles

The _IfcFillAreaStyleTiles_ defines the filling of an _IfcAnnotationFillArea_ by recurring patterns of styled two dimensional geometry, called a tile. The recurrence pattern is determined by two vectors, that multiply the tile in regular form.
<!-- end of short definition -->

The two vectors act as a two dimensional repeat factor that determines eight new positions for the tiles.

> NOTE Definition according to ISO 10303-46:
> The fill area style tiles defines a two dimensional tile to be used for the filling of annotation fill areas or other closed regions. The content of a tile is defined by the tile set, and the placement of each tile determined by the filling pattern which indicates how to place tiles next to each other. Tiles or parts of tiles outside of the annotation fill area or closed region shall be clipped at the of the area or region.

> _I + k~1~\* R~1~ +
k~2~\* R~2~_   _k~1~,k~2~_= -1,0,1 , ![formula](../../../../figures/ifcfillareastyletilesymbolwithstyle_fig1.gif)
>

Figure 1 shows the use of a vector for hatch line distances

![IfcFillAreaStyleTiles_Fig1.gif 12,9 KB](../../../../figures/ifcfillareastyletiles_fig1.gif)

Figure 1 — two vectors as two direction repeat factor

> NOTE Entity adapted from **fill_area_style_tiles** defined in ISO10303-46

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE _TilingPattern_ changed to list of two _IfcVector_, _Tiles_ refer directly to _IfcStyledItem_.

## Attributes

### TilingPattern
A two direction repeat factor defining the shape and relative positioning of the tiles.
> IFC4 CHANGE The attribute type has changed to directly reference two _IfcVector_'s.

### Tiles
A set of constituents of the tile being a styled item that is used as the annotation symbol for tiling the filled area.
> IFC4 CHANGE The data type has been changed to _IfcStyledItem_.

> NOTE Only _IfcStyledItem_'s that refer to a compatible geometric representation item and presentation style shall be used.

### TilingScale
The scale factor applied to each tile as it is placed in the annotation fill area.
