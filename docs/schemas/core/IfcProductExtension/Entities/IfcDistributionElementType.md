# IfcDistributionElementType

The _IfcDistributionElementType_ defines a list of commonly shared property set definitions of an element and an optional set of product representations. It is used to define an element specification (i.e. the specific product information, that is common to all occurrences of that product type).
<!-- end of short definition -->

> NOTE The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

A distribution element type is used to define the common properties of a certain type of a distribution element that may be applied to many instances of that feature type to assign a specific style. Distribution element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcDistributionElementType_ are represented by instances of _IfcDistributionElement_ (or its subtypes).

> HISTORY New entity in IFC2x2.

> IFC2x3 CHANGE The entity has been made non-abstract

> IFC4 CHANGE The entity is marked as deprecated for instantiation - will be made ABSTRACT in future releases.
