# IfcUnitaryControlElement

A unitary control element combines a number of control components into a single product, such as a thermostat or humidistat.
<!-- end of short definition -->

A unitary control element provides a housing for an aggregation of control or electrical distribution elements that, in combination, perform a singular (unitary) purpose. Each item in the aggregation may have its own geometric representation and location.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcUnitaryControlElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no unitary control element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcUnitaryControlElementType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SOURCE_Control_CONTROL

Receives power (typically 24V), and closes the circuit for Fan, Heat, and Cool. Port may be aggregated into sub-ports: 'Fan'(SIGNAL,SOURCE), 'Heat'(SIGNAL,SOURCE), and 'Cool'(SIGNAL,SOURCE)

### Property Sets for Objects



### Quantity Sets



