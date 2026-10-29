# IfcSensor

A sensor is a device that measures a physical quantity and converts it into a signal which can be read by an observer or by an instrument.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSensorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no sensor type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSensorType_.

## Concepts

### Control Flow



#### IfcDistributionFlowElement

Sensors may be connected to a flow element for which an aspect of the fluid or flow is measured.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SOURCE_Output_SIGNAL

Transmits signal.

### Property Sets for Objects



### Quantity Sets



