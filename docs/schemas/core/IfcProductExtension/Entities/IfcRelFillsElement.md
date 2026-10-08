# IfcRelFillsElement

_IfcRelFillsElement_ is an objectified relationship between an opening element and an element that fills (or partially fills) the opening element. It is an one-to-one relationship.
<!-- end of short definition -->

> NOTE View definitions or implementer agreements may restrict an opening to be filled by one filling element only.

As shown in Figure 1, the insertion of a door into a wall is represented by two separate relationships. First the door opening is created within the wall by _IfcWall_ <-- _IfcRelVoidsElement_ --> _IfcOpeningElement_, then the door is inserted within the opening by _IfcOpeningElement_ <-- _IfcRelFillsElement_ --> _IfcDoor_. The red mark in the figure indicates that there shall be no _IfcRelContainedInSpatialStructure_ relationship that connects the opening to the spatial container of the wall.

![relationships for filling](../../../../figures/ifcrelfillselements-fig1.png "Figure 1 — Relationships for element filling")

> HISTORY New entity in IFC1.0

## Attributes

### RelatingOpeningElement
Opening Element being filled by virtue of this relationship.

### RelatedBuildingElement
Reference to element that occupies fully or partially the associated opening.
> IFC2x CHANGE The data type has been changed from _IfcBuildingElement_ to _IfcElement_ with upward compatibility for file based exchange.