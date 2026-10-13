# IfcProperty

_IfcProperty_ is an abstract generalization for all types of properties that can be associated with IFC objects through the property set mechanism.
<!-- end of short definition -->

> HISTORY New entity in IFC1.0.

## Attributes

### Name
Name for this property. This label is the significant name string that defines the semantic meaning for the property.

### Specification
URI reference to a location with semantic definition or informative text to explain the property.

### PartOfPset
Reference to the _IfcPropertySet_ by which the _IfcProperty_ is referenced.
{ .change-ifc2x4}
> IFC4 CHANGE New inverse attribute to navigate from _IfcProperty_ to _IfcPropertySet_ with upward compatibility for file based exchange.

### PropertyForDependance
The property on whose value that of another property depends.

### PropertyDependsOn
The relating property on which the value of the property depends.

### PartOfComplex
Reference to the _IfcComplexProperty_ in which the _IfcProperty_ is contained.
{ .change-ifc2x4}
> IFC4 CHANGE The cardinality has changed to 0..n to allow reuse of instances of _IfcProperty_ in several _IfcComplexProperty_ with upward compatibility for file based exchange.

### HasConstraints
User-defined constraints for the property.

### HasApprovals
User-defined approvals for the property.

### PartOfMaterialOrProfileProperties
Reference to the IfcMaterialProperties or IfcProfileProperties by which the IfcProperty is referenced.
