# IfcRelVoidsElement

_IfcRelVoidsElement_ is an objectified relationship between a building element and one opening element that creates a void in the element. It is a one-to-one relationship. This relationship implies a boolean operation of subtraction between the geometric bodies of the element and the opening.
<!-- end of short definition -->

As shown in Figure 1, the insertion of a void into a wall is represented by the relationship _IfcRelVoidsElement_. The opening within the wall is defined by the pattern _IfcWall_ - _IfcRelVoidsElement_ - _IfcOpeningElement_.

![relationships for voiding](../../../../figures/ifcrelvoidselements-fig1.png)

Figure 1 — Relationship for element voiding

> HISTORY New entity in IFC1.0

## Attributes

### RelatingBuildingElement
Reference to the element in which a void is created by the associated feature subtraction element.
> IFC2x CHANGE The data type has been changed from _IfcBuildingElement_ to _IfcElement_ with upward compatibility for file based exchange.

### RelatedOpeningElement
Reference to the feature subtraction element which defines a void in the associated element.
> IFC2x CHANGE The data type has been changed from _IfcOpeningElement_ to _IfcFeatureElementSubtraction_ with upward compatibility for file based exchange.
