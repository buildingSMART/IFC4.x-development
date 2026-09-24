# IfcRelConnectsPortToElement

_IfcRelConnectsPortToElement_ is a relationship between a distribution element and dynamically connected ports where connections are realised to other distribution elements.
<!-- end of short definition -->

Ports contained in different elements are connected to each other using the _IfcRelConnectsPorts_ relationship.

> NOTE See _IfcRelNests_ for its usages to represent an ordered collection of ports that are contained by an element and relevant subtypes of _IfcDistributionElement_ for examples and port use definition sections.

> HISTORY New entity in IFC2x2.

> IFC4.3.0.0 DEPRECATION The relationship IfcRelConnectsPortToElement shall not be used anymore, use IfcRelNests instead for specifying the element to which any kind of port belongs.

## Attributes

### RelatingPort
Reference to an Port that is connected by the objectified relationship.

### RelatedElement
Reference to an _IfcDistributionElement_ that has ports assigned.
> IFC4 CHANGE Data type restricted to _IfcDistributionElement_.
