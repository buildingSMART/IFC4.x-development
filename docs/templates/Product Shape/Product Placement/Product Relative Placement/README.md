Product Relative Placement
==========================

Relative placement to positioning element.

Any _IfcProduct_ may have a direct reference to the _IfcAlignment_ on which it is placed. This is an exception where no measurements in the form of stationing values are required. The placement is always relative to the underlying _IfcAlignment_.Representation (allowed geometric items are certain types of curves) with an absolute measurement from the start of the representing curve at zero parameter length.

```
concept {
    IfcProduct:ObjectPlacement -> IfcObjectPlacement_0
    IfcObjectPlacement_0:PlacementRelTo -> IfcObjectPlacement_1
    IfcObjectPlacement_1:PlacesObject -> IfcPositioningElement:ObjectPlacement
    IfcPositioningElement:Name -> IfcLabel
    IfcProduct:ObjectPlacement[binding="HasPlacement"]
    IfcObjectPlacement_1:PlacesObject[binding="RelativeToElement"]
    IfcPositioningElement:Name[binding="PositioningElementName"]
}
```