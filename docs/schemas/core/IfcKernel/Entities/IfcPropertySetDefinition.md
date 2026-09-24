# IfcPropertySetDefinition

_IfcPropertySetDefinition_ is a generalization of all individual property sets that can be assigned to an object or type object. The property set definition can be either:

* **Dynamically extendable property sets** - _IfcPropertySet_, a set of properties for which the IFC specification only provides a kind of "meta model", to be further declared by agreement. This means no entity definition of the properties exists within the IFC specification. The declaration is done by assigning a significant string value to the _Name_ attribute of the entity as defined in the entity _IfcPropertySet_ and at each subtype of _IfcProperty_, referenced by the property set. Dynamically defined property sets may have an underlying template provided by _IfcPropertySetTemplate_.
* **Statically defined property sets** - _IfcPreDefinedPropertySet_, a property set entity that exists within the IFC specification. The semantic meaning of each statically defined property set is declared by its entity type and the meaning of the properties is defined by the name and data type of the explicit attribute representing it.
<!-- end of short definition -->

Property set definitions define information that is shared among multiple instances of objects, either object occurrences or object types. _IfcPropertySetDefinition_'s (by their instantiable subtypes) can participate within the following relationships:

* **Assignment to object types** - an _DefinesType_ direct relationship to _IfcTypeObject_ that applies the property set, with all included properties, to the object type. Those properties apply to all object occurrences having the same object type.
* **Assignment to object occurrences** - an _DefinesOccurrence_ relationship to _IfcRelDefinesByProperties_ that applies the property set, with all included properties, to the object occurrence.

> NOTE Properties assigned to object occurrences may override properties assigned to the object type. See _IfcRelDefinesByType_ for further information.

> HISTORY New entity in IFC2x

> IFC4 CHANGE The subtype _IfcPreDefinedPropertySet_ has been added.

## Attributes

### DefinesType
The type object to which the property set is assigned. The property set acts as a shared property set to all occurrences of the type object.
> NOTE The relationship between the _IfcPropertySetDefinition_ and the _IfcTypeObject_ is a direct relationship, not utilizing _IfcRelDefinesByProperties_, for maintaining compatibility with earlier releases of this standard.

> IFC4 CHANGE The cardinality has been changed from 0..1 to 0..n with upward compatibility for file-based exchange.

### IsDefinedBy
Relation to the property set template, via the objectified relationship _IfcRelDefinesByTemplate_, that, if given, provides the definition template for the property set or quantity set and its properties.
> IFC4 CHANGE New inverse relationship, change made with upward compatibility for file-based exchange.

### DefinesOccurrence
Reference to the relation to one or many object occurrences that are characterized by the property set definition. A single property set can be assigned to multiple object occurrences using the objectified relationship _IfcRelDefinesByProperties_.
> IFC4 CHANGE Inverse attribute renamed from _PropertyDefinitionOf_ with upward compatibility for file-based exchange.
