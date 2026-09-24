# IfcResourceConstraintRelationship

An _IfcResourceConstraintRelationship_ is a relationship entity that enables a constraint to be related to one or more resource level objects.
<!-- end of short definition -->

An _IfcResourceConstraintRelationship_ allows for the specification of a constraint to be applied to many entity types. An important case is to apply constraints to properties. The constraints applied therefore enable a property to carry values identifying requirements as well as those identifying the fulfillment of those requirements.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Renamed from IfcResourceConstraintRelationship and extended to apply to all resource level entities. Subtyped from _IfcResourceLevelRelationship_.

## Attributes

### RelatingConstraint
The constraint that is to be related.

### RelatedResourceObjects
The properties to which a constraint is to be related.
