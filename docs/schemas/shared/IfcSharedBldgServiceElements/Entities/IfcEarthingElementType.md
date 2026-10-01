# IfcEarthingElementType

The flow terminal type _IfcEarthingElementType_ defines commonly shared information for occurrences of earthing elements. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports

It is used to define an earthing element type specification indicating the specific product information that is common to all occurrences of that product type. The _IfcEarthingElementType_ may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of _IfcEarthingElementType_ are represented by instances of _IfcEarthingElement_. Refer to the documentation at _IfcEarthingElement_ for supported property sets, materials, composition, and ports.
<!-- end of short definition -->

## Attributes

### PredefinedType
Identifies the predefined types of earting element from which the type required may be set.

