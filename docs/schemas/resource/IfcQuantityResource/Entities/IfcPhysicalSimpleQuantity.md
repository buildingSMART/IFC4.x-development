# IfcPhysicalSimpleQuantity

The physical quantity, _IfcPhysicalSimpleQuantity_, is an entity that holds a single quantity measure value (as defined at the subtypes of _IfcPhysicalSimpleQuantity_) together with a semantic definition of the usage for the measure value.
<!-- end of short definition -->

> EXAMPLE An element, like a wall, may have several area measures, like footprint area, left wall face area, right wall face area. These areas would be given by three instances of the area quantity subtype, with different _Name_ string values.

A section "Quantity Use Definition" at individual entities as subtypes of _IfcBuiltElement_ gives guidance to the usage of the _Name_ attribute to characterize the individual quantities. If the _Unit_ attribute is given, the value attribute (introduced at the level of subtypes of _IfcPhysicalSimpleQuantity_) are given as quantities of this unit, otherwise the global unit definitions (given by _IfcUnitAssignment_) are used.

> HISTORY New entity in IFC2x2 Addendum 1.

> IFC2x2 ADDENDUM 1 CHANGE The abstract entity _IfcPhysicalSimpleQuantity_ has been added. Upward compatibility for file based exchange is guaranteed.

## Attributes

### Unit
Optional assignment of a unit. If no unit is given, then the global unit assignment, as established at the IfcProject, applies to the quantity measures.
