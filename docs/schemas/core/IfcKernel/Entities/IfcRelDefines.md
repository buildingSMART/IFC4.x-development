# IfcRelDefines

_IfcRelDefines_ is a generic and abstract relationship which subtypes are used to:

* assign an object type to an object occurrence
* assign a property set to an object instance
* assign a property set template to a property set
<!-- end of short definition -->

> EXAMPLE  Several instances of windows within the IFC project model may be of the same (catalogue or manufacturer) type. Thereby they share the same properties. This relationship is established by the subtype _IfcRelDefinesByType_ of the _IfcRelDefines_ relationship assigning an _IfcWindowType_ to multiple occurrences of _IfcWindow_.

> EXAMPLE  The (same) property set, e.g.  Pset_ProductManufacturerInfo, keeping the manufacturer name, label and production year of a product, can be assigned to one or many instances of furnishing. This relationship is established by the subtype _IfcRelDefinesByProperties_ of _IfcRelDefines_ relationship assigning an _IfcPropertySet_ to one or more instances of _IfcFurnishingElement_.

> HISTORY New entity in IFC2x.

> IFC4 CHANGE The attribute _RelatedObjects_ has been demoted to the subtypes _IfcRelDefinesByProperties_ and _IfcRelDefinesByType_.
