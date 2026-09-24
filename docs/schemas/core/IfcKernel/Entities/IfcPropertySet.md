# IfcPropertySet

The _IfcPropertySet_ is a container that holds properties within a property tree. These properties are interpreted according to their name attribute. Each individual property has a significant name string. Some property sets are included in the specification of this standard and have a predefined set of properties indicated by assigning a significant name. These property sets are listed under "property sets" within this specification. Property sets applicable to certain objects are listed in the object specification. The naming convention "Pset_Xxx" applies to all those property sets that are defined as part of this specification and it shall be used as the value of the _Name_ attribute.
<!-- end of short definition -->

In addition any user defined property set can be captured. Property sets that are not declared as part of the IFC specification shall have a _Name_ value not including the "Pset_" prefix.

_IfcPropertySet_ can be assigned to object occurrences and object types. An _IfcPropertySet_ assigned to an object type is shared among all occurrences of the same object type.

> NOTE See _IfcRelDefinesByType_ for how to override property sets assigned to an object type within the object occurrence.

An _IfcPropertySetTemplate_ may define the underlying structure, i.e. the required name, the applicable object or object types to which the property set can be attached, and the individual properties that can be included. Property sets are related to other objects by using the relationship object that refers to the corresponding object:

* **Occurrence Object**: _IfcRelDefinesByProperties_ using the inverse attribute _DefinesOccurrence_.
* **Type Object**: using a direct link by inverse attribute _DefinesType_.
* **Underlying template**: _IfcRelDefinesByTemplate_ using the inverse attribute _IsDefinedBy_.
* **External reference**: subtypes of _IfcRelAssociates_ are used to provide a link to a classification system, or external library providing further reference to the property set. Accessible by inverse attribute _HasAssociations_.

> HISTORY New entity in IFC1.0

> IFC4 CHANGE All statically defined property set entities are no longer subtypes of _IfcPropertySet_.

## Attributes

### HasProperties
Contained set of properties. For property sets defined as part of the IFC Object model, the property objects within a property set are defined as part of the standard. If a property is not contained within the set of predefined properties, its value has not been set at this time.

## Formal Propositions

### ExistsName
The _Name_ attribute has to be provided. The attribute is used to specify the signifier of the property set. The properties that are allowed to be attached to a particular property set may be given within the property set definition part of the IFC specification. Those property set definitions are referenced in the semantic definition section of the individual subtypes of _IfcObjectDefinition_.

### UniquePropertyNames
Every individual subtype of _IfcProperty_ within the property set shall have a unique _Name_ attribute value.
