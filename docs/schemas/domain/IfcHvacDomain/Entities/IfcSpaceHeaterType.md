# IfcSpaceHeaterType

The flow terminal type **IfcSpaceHeaterType** defines commonly shared information for occurrences of space heaters. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of short definition -->

It is used to define a space heater type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcSpaceHeaterType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcSpaceHeaterType** are represented by instances of _IfcSpaceHeater_. Refer to the documentation at _IfcSpaceHeater_ for supported property sets, materials, composition, and ports.

> IFC4 CHANGE Supertype changed from _IfcEnergyConversionDeviceType_ to _IfcFlowTerminalType_

## Attributes

### PredefinedType
Enumeration of possible types of space heater (e.g., baseboard heater, convector, radiator, etc.).

## Formal Propositions

### CorrectPredefinedType

