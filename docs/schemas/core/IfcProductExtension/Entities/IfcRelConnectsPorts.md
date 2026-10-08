# IfcRelConnectsPorts

An _IfcRelConnectsPorts_ relationship defines the relationship that is made between two ports at their point of connection. It may include the connection geometry between two ports.
<!-- end of short definition -->

The objectified relationship _IfcRelConnectsPorts_ is required for defining how two instances of _IfcPort_ connect together. Each of the ports is logically contained within the _IfcDistributionElement_ by using the ordered collection _IfcRelNests_.

> HISTORY New entity in IFC2.0, modified in IFC2x.

> IFC4 CHANGE Previously the containment of the _IfcPort_ within the _IfcDistributionElement_ had been realized using the _IfcRelConnectsPortToElement_ relationship.

## Attributes

### RelatingPort
Reference to the first port that is connected by the objectified relationship.

### RelatedPort
Reference to the second port that is connected by the objectified relationship.

### RealizingElement
Defines the element that realizes a port connection relationship.

## Formal Propositions

### NoSelfReference
The instance of the _RelatingPort_ shall not be the same instance as the _RelatedPort_.
