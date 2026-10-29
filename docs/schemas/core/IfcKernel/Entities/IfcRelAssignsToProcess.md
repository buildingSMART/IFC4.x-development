# IfcRelAssignsToProcess

The objectified relationship _IfcRelAssignsToProcess_ handles the assignment of one or many objects to a process or activity. An object can be a product on which the process operates. Processes and activities can operate on things other than products, and can operate in ways other than input and output.
<!-- end of short definition -->

> EXAMPLE It may be common to define processes during estimating or scheduling that describe design tasks (resulting in documents), procurement tasks (resulting in construction materials), planning tasks (resulting in processes), etc. Furthermore, the ways in which a process can operate on something might include "installs", "finishes", "transports", "removes", etc. The ways are described as operation types.

The inherited attribute _RelatedObjects_ gives the references to the objects, or object type, which the process operates on. The _RelatingProcess_ is the process or process type, that operates on the object. The operation types are captured in the inherited attribute _Name_.

> NOTE The agreement on valid and recognizable values for the _Name_ attribute is part of view definitions and implementer agreements.

> HISTORY New entity in IFC1.5. Has been renamed from _IfcRelProcessOperatesOn_ in IFC2x.

> IFC4 CHANGE The data type _RelatingProcess_ has been extended to cover also _IfcTypeProcess_

## Attributes

### RelatingProcess
Reference to the process to which the objects are assigned.
> IFC4 CHANGE Datatype expanded to include _IfcProcess_ and _IfcTypeProcess_.

### QuantityInProcess
Quantity of the object specific for the operation by this process.

## Formal Propositions

### NoSelfReference
The instance to which the relation points as provided by _RelatingProcess_ shall not be contained in the set of _RelatedObjects_.
