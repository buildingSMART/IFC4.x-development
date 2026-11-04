Excavation Cuttings
==========================

Excavation Cuttings represent a voiding of an existing or constructed earthen element (referred to as the voided element) usually represented by a subtype of _IfcGeoScienceModel_, _IfcGeoScienceFeature_ or an _IfcEarthworksFill_. The _IfcExcavation_ semantically represents the work of removing/excavating material from the voided element, and the associated geometrical representation is the resulting void created. An _IfcExcavation_ may optionally be filled (fully or partially) with another element such as a foundation, earthen fill or foundation utilizing the _IfcRelFillsElement_ relationship.

The resulting geometry of the relationship, when applied, is the result of CSG operations where the _IfcExcavation_ representation is subtracted from the voided element representation.

```
concept {
    IfcElement_0:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcExcavation
    IfcExcavation:FillsVoids -> IfcRelFillsElement:RelatedBuildingElement
    IfcRelFillsElement:RelatedBuildingElement -> IfcElement_1
    IfcElement_0:HasOpenings[binding="HasOpenings"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedEarthworksCut"]
    IfcExcavation:FillsVoids[binding="FillsVoids"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedBuiltElement"]
}
```