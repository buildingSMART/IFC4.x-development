# IfcDistributionControlElement

The distribution element _IfcDistributionControlElement_ defines occurrence elements of a building automation control system that are used to impart control over elements of a distribution system.
<!-- end of short definition -->

_IfcDistributionControlElement_ defines elements of a building automation control system. These are typically used to control distribution system elements to maintain variables such as temperature, humidity, pressure, flow, power, or lighting levels, through the modulation, staging or sequencing of mechanical or electrical devices. The three general functional categories of control elements are as follows:

* Impart control over flow control elements (_IfcFlowController_) in a distribution system such as dampers, valves, or relays, typically through the use of actuation (_IfcActuator_).
* Sensing elements (_IfcSensor_) that measure changes in the controlled variable such as temperature, humidity, pressure, or flow.
* Controllers (_IfcController_) typically classified according to the control action they seek to perform and generally responsible for making decisions about the elements under control.

Since _IfcDistributionControlElement_ and its subtypes typically relate to many different distribution flow elements (_IfcDistributionFlowElement_), the objectified relationship _IfcRelFlowControlElements_ has been provided to relate control and flow elements as required.

The key distinction between _IfcDistributionFlowElement_ and _IfcDistributionControlElement_ is whether it is internal or external to the flow system, respectively. For example, the distinction between _IfcFlowMeter_ (subtype of _IfcDistributionFlowElement_ measuring a flow quantity) and _IfcFlowInstrument_ (subtype of _IfcDistributionControlElement_ measuring a flow quality), is based on this principal. A physical device that connects within the flow system in which it measures (having inlet/outlet pipes for the measured substance) follows the _IfcDistributionFlowElement_ hierarchy (and therefore _IfcFlowMeter_ which measures the flow internally). Otherwise, if it monitors/controls but does not connect inline within the flow system (it is external or is a component of another device), then it follows the _IfcDistributionControlElement_ hierarchy (and therefore _IfcFlowInstrument_ which may display various attributes through connected sensors).

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE Attribute _ControlElementId_ attribute deleted; replaced by classification usage. Ports are now primarily defined using _IfcRelNests_ to enable definition of ports at type definitions (both forward and backward compatible), provide a logical order, and reduce the number of relationship objects needed. The relationship _IfcRelConnectsPortToElement_ is still supported, however is now specific to dynamically connected ports.

## Attributes

### AssignedToFlowElement
Reference through the relationship object to related distribution flow elements.

## Concepts

### Library Association

A distribution system may be associated with an external Building Automation System or similar system. Library references can be used to indicate a device address or other key which can identify the IFC control element within the external system.

```
digraph dot_neato {
  IfcDistributionSystem[pos="0,0!"];
  IfcRelAssignsToGroup[pos="200,0!"];
  IfcController[pos="400,0!"];
  IfcRelAssociatesLibrary[pos="0,-70!"];
  IfcLibraryInformation[pos="0,-140!"];
  IfcRelAssociatesLibrary2 [label="IfcRelAssociatesLibrary", pos="400,-70!"];
  IfcLibraryReference[pos="400,-140!"]

  IfcRelAssignsToGroup -> IfcController [taillabel="RelatedObjects", labelangle=90, labeldistance=3];
  IfcRelAssignsToGroup -> IfcDistributionSystem [headlabel="RelatingGroup", labelangle=90, labeldistance=3];
  IfcRelAssociatesLibrary -> IfcDistributionSystem [label="RelatedObjects"];
  IfcRelAssociatesLibrary -> IfcLibraryInformation [label="RelatingLibrary"];
  IfcRelAssociatesLibrary2 -> IfcController [label="RelatedObjects"];
  IfcRelAssociatesLibrary2 -> IfcLibraryReference [label="RelatingLibrary"];
  IfcLibraryReference -> IfcLibraryInformation [label="ReferencedLibrary"];
}
```

> IFC4.3.0.0 CHANGE Library references are now to be used instead of a classification system references for referencing external systems such as Building Automation Systems.

### Object Typing



### Product Assignment

The **IfcDistributionControlElement** may be assigned to the following entities using relationships as indicated:

* IfcDistributionSystem (IfcRelAssignsToGroup): Indicates a system containing interconnected devices, where control elements are typically part of a control system having _PredefinedType=CONTROL_.
* IfcPerformanceHistory (IfcRelAssignsToControl): Indicates realtime or historical information captured for the device.

#### IfcTask

Indicates tasks used to purchase, install, renovate, demolish, operate, or otherwise act upon the element. If the element has a type, available task types are assigned to the element type.

#### IfcProcedure

Indicates procedures used to operate the element. If the element has a type, available procedure types are assigned to the element type.

#### IfcEvent

Indicates events to be handled by the element, sequenced by procedures to be followed. If the element has a type, available event types are assigned to the element type.

