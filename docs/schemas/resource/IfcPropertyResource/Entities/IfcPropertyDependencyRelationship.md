# IfcPropertyDependencyRelationship

An _IfcPropertyDependencyRelationship_ describes an identified dependency between the value of one property and that of another.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Made subtype of _IfcResourceLevelRelationship_ (attribute order changed).

Use Definition

Whilst the _IfcPropertyDependencyRelationship_ may be used to describe the dependency, and it may do so in terms of the expression of how the dependency operates, it is not possible through the current IFC model for the value of the related property to be actually derived from the value of the relating property. The determination of value according to the dependency is required to be performed by an application that can then use the Expression attribute to flag the form of the dependency.

## Attributes

### DependingProperty
The property on which the relationship depends.

### DependantProperty
The dependant property.

### Expression
Expression that further describes the nature of the dependency relation.

## Formal Propositions

### NoSelfReference
The _DependingProperty_ shall not point to the same instance as the _DependantProperty_.
