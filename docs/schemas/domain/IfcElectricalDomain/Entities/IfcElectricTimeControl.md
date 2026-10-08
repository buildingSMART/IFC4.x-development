# IfcElectricTimeControl

An electric time control is a device that applies control to the provision or flow of electrical energy over time.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricTimeControlType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric time control type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricTimeControlType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_ELECTRICAL

Receives electrical power.

#### SOURCE_Drive_ELECTRICAL

Transmits electrical power according to time.

### Property Sets for Objects



### Quantity Sets



