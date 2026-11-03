Station
==========================

Station for element template. An _IfcElement_ may have a linear referencing measurement attached to it. The _IfcReferent_.Name features a localized form of station measurement encodings and shall be positioned on an _IfcAlignment_ to ensure that a distance along measurement is clearly defined. The _IfcReferent_ should have a placement.

```
concept {
    IfcReferent:Positions -> IfcRelPositions:RelatingPositioningElement
    IfcReferent:ObjectPlacement -> IfcObjectPlacement
    IfcRelPositions:RelatedProducts -> IfcProduct
    IfcProduct:Name -> IfcLabel
    IfcRelPositions:RelatedProducts[binding="RelatedProducts"]
    IfcProduct:Name[binding="ProductName"]
    IfcReferent:ObjectPlacement[binding="HasObjectPlacement"]
}
```