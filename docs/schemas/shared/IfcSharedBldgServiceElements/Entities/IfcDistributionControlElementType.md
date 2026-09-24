# IfcDistributionControlElementType

The element type _IfcDistributionControlElementType_ defines a list of commonly shared property set definitions of an element and an optional set of product representations. It is used to define an element specification (the specific product information that is common to all occurrences of that product type).
<!-- end of short definition -->

Distribution control element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcDistributionControlElementType_ are represented by instances of _IfcDistributionControlElement_ or its subtypes.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Ports may now be defined using _IfcRelNests_ to enable definition of ports at type definitions (both forward and backward compatible), provide a logical order, and reduce the number of relationship objects needed. The relationship _IfcRelConnectsPortToElement_ is still supported on occurrence objects, however is now specific to dynamically connected ports.

## Concepts

### Product Type Assignment



#### IfcTaskType

Indicates task types available to purchase, install, renovate, demolish, operate, or otherwise act upon occurrences of the element type. Such task types may be instantiated as task occurrences assigned to occurrences of the element type. Prices (such as for purchasing or shipping) may be established by resource types assigned to task types.

#### IfcProcedureType

Indicates procedure types available to operate occurrences of the element type. Such procedure types may be instantiated as procedure occurrences assigned to occurrences of the element type.

#### IfcEventType

Indicates event types available to be raised by occurrences of the element type, sequenced by procedures to be followed. Such event types may be instantiated as event occurrences assigned to occurrences of the element type.

