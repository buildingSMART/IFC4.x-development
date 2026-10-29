# IfcProductRepresentation

_IfcProductRepresentation_ defines a representation of a product, including its (geometric or topological) representation. A product can have zero, one or many geometric representations, and a single geometric representation can be shared among various products using mapped representations.
<!-- end of short definition -->

> NOTE The definition of this entity relates to the ISO 10303 entity property_definition. The use of the term ‘property’ was avoided since it conflicts with the property, property type, and property set definitions elsewhere in the IFC model.

> HISTORY New entity in IFC2.0

> IFC2x3 NOTE  Users should not instantiate the entity from IFC2x3 onwards.

> IFC4 CHANGE Entity made abstract.

## Attributes

### Name
The word or group of words by which the product representation is known.

### Description
The word or group of words that characterize the product representation. It can be used to add additional meaning to the name of the product representation.

### Representations
Contained list of representations (including shape representations). Each member defines a valid representation of a particular type within a particular representation context.
