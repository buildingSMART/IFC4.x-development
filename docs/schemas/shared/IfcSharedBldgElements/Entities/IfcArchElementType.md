# IfcArchElementType

The element type _IfcArchElementType_ defines commonly shared information for occurrences of arch elements. Arch elements are building elements which represent unitary curved structures. The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define an arch element specification that is common to all occurrences of that arch element type. Arch element types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcArchElementType_ within building models are represented by instances of _IfcArchElement_.
<!-- end of short definition -->

> NOTE Subtype of _IfcBuiltElementType_ — see that entity's documentation for inherited attributes and behavior.

> HISTORY New entity in IFC 4.4.

## Attributes

### PredefinedType
Specifies the type for which the value is selected from a predefined type enumeration.

