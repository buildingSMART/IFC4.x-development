# IfcReinforcingElement

A reinforcing element represents bars, wires, strands, meshes, tendons, and other components embedded in concrete in such a manner that the reinforcement and the concrete act together in resisting forces.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: rod(s), bar(s), fabric, fibres, wires and cable(s) added to give additional strength or support to a material or component.

One or several instances of subtypes of _IfcReinforcingElement_ should always be accompanied by a defining instance of a respective subtype of _IfcReinforcingElementType_. The type object holds shape and material information.

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Attribute _SteelGrade_ deprecated.

## Attributes

### SteelGrade
Deprecated.

> IFC4 CHANGE Attribute deprecated. Use material association at _IfcReinforcingElementType_ instead.
