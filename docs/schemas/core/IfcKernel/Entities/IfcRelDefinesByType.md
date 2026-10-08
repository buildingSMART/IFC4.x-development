# IfcRelDefinesByType

The objectified relationship _IfcRelDefinesByType_ defines the relationship between an object type and its object occurrences. The _IfcRelDefinesByType_ is a 1-to-N relationship, as it allows one type definition to be assigned to one or many objects. Those objects then share the same object type, and the property sets and properties assigned to the object type.
<!-- end of short definition -->

The _IfcRelDefinesByType_ links the object type definition with the object occurrence. Both the object type and the object occurrence may define properties by assigning an _IfcPropertySet_, including one or many subtypes of _IfcProperty_ to either the object type or object occurrence, as shown in Figure 1.

There are several scenarios to define the same property set on the object type definition and object occurrence side:

1. All properties for all object occurrences of a common object type have the same value - then only the object type definition has a property set assigned.
2. All properties for all object occurrences are different, that is there are no common property values for the object type definition - then each of the object occurrences has a property set assigned.
3. Some properties within the same property set have common values and are assigned to the object type definition and some are occurrence specific and assigned (with potentially different values) to the object occurrences - then:
  * The sum of all properties within a given property set applicable to an object occurrence is the union of properties assigned to the object type definition, plus the properties assigned to the object occurrence.
  * If the object occurrence has a property with the same _IfcProperty.Name_ in an _IfcPropertySet_, as the corresponding object type definition, then the property value defined at the occurrence overrides the value defined at the type.

![instance diagram](../../../../figures/ifcreldefinesbytype_fig-1.png)
Figure 1 — Type definition relationships

The following table provides an example of property assignments and how occurrence values may override type values.

Properties assigned to _IfcWallType_ | Property assigned to _IfcWall_ | Resulting property value for individual wall
--- | --- | ---
- | ExtendToStructure = TRUE | ExtendToStructure = TRUE
ThermalTransmittance = 0.375 | - | ThermalTransmittance = 0.375
ExtendToStructure = TRUE | ExtendToStructure = FALSE | ExtendToStructure = FALSE

> HISTORY New entity in IFC2x.

> IFC4 CHANGE The attribute _RelatedObjects_ had been demoted from the supertype _IfcRelDefines_ to _IfcRelDefinesByType_.

## Attributes

### RelatedObjects


### RelatingType
Reference to the type (or style) information for that object or set of objects.
