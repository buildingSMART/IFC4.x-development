# IfcPropertyReferenceValue

The _IfcPropertyReferenceValue_ allows a property value to be of type of an resource level entity. The applicable entities that can be used as value references are given by the _IfcObjectReferenceSelect_.
<!-- end of short definition -->

> HISTORY New entity in IFC1.5. Entity has been renamed from IfcObjectReference in IFC2x.

> IFC4 CHANGE Attribute _PropertyReference_ has been made OPTIONAL with upward compatibility for file based exchange.

## Attributes

### UsageName
Description of the use of the referenced value within the property. It is a descriptive text that may hold an expression or other additional information.

### PropertyReference
Reference to another property entity through one of the select types in the _IfcObjectReferenceSelect_.
> IFC4 CHANGE The attribute has been made optional with upward compatibility for file based exchange.
