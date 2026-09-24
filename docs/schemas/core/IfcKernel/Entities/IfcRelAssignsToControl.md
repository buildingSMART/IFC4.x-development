# IfcRelAssignsToControl

The objectified relationship _IfcRelAssignsToControl_ handles the assignment of a control (represented by subtypes of _IfcControl_) to other objects (represented by subtypes of _IfcObject_, with the exception of controls).
<!-- end of short definition -->

> EXAMPLE The assignment of a performance history (as a subtype of _IfcControl_) for a building service element (as a subtype of _IfcObject_) is an application of this generic relationship.

> HISTORY New entity in IFC2.0.

> IFC2x CHANGE Entity has been renamed from _IfcRelControls_.

## Attributes

### RelatingControl
Reference to the _IfcControl_ that applies a control upon objects.

## Formal Propositions

### NoSelfReference
The instance to which the relation points shall not be contained in the set of _RelatedObjects_.
