# IfcRelProjectsElement

The _IfcRelProjectsElement_ is an objectified relationship between an element and one projection element that creates a modifier to the shape of the element. The relationship is defined to be a 1:1 relationship, if an element has more than one projection, several relationship objects have to be used, each pointing to a different projection element. The _IfcRelProjectsElement_ establishes an aggregation relationship between the main element and a sub ordinary addition feature.
<!-- end of short definition -->

> NOTE In contrary the _IfcRelAggregates_ relationship established an aggregation of equal parts to a whole.

The _IfcRelProjectsElement_ implies a Boolean operation of addition for the geometric bodies of the element and the feature element. As with all decomposition relationships it determines:

* existence dependency - the _RelatedFeatureElement_ cannot exist without the _RelatingElement_
* hierarchical and non-cyclical relationship - the _IfcRelProjectsElement_ can only alter a single _IfcElement_
* no spatial containment - the _IfcFeatureElementAddition_ as related element never participates in the hierarchical spatial containment relationship _IfcRelContainedInSpatialStructure_

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Supertype changed to IfcRelDecomposes.

## Attributes

### RelatingElement
Element at which a projection is created by the associated _IfcProjectionElement_.

### RelatedFeatureElement
Reference to the _IfcFeatureElementAddition_ that defines an addition to the volume of the element, by using a Boolean addition operation. An example is a projection at the associated element.
