# IfcPhysicalComplexQuantity

The complex physical quantity, _IfcPhysicalComplexQuantity_, is an entity that holds a set of single quantity measure value (as defined at the subtypes of _IfcPhysicalSimpleQuantity_), that all apply to a given component or aspect of the element.
<!-- end of short definition -->

> EXAMPLE: A layered element, like a wall, may have several material layers, each having individual quantities, like footprint area, side area and volume. An instance of _IfcPhysicalComplexQuantity_ would group these individual quantities (given by a subtype of _IfcPhysicalSimpleQuantity_) and name them according to the material layer name by using the _Name_ attribute. The _Discrimination_ attribute would then be 'layer'.

A section "Quantity Use Definition" at individual entities as subtypes of _IfcBuiltElement_ gives guidance to the usage of the _Name_ and _Discrimination_ attribute to characterize the complex quantities.

> HISTORY New entity in IFC2x2 Addendum 1.

> IFC2x2 ADDENDUM 1 CHANGE The entity _IfcPhysicalComplexQuantity_ has been added. Upward compatibility for file based exchange is guaranteed.

## Attributes

### HasQuantities
Set of physical quantities that are grouped by this complex physical quantity according to a given discrimination.

### Discrimination
Identification of the discrimination by which this physical complex property is distinguished. Examples of discriminations are 'layer', 'steel bar diameter', etc.

### Quality
Additional indication of a quality of the quantities that are grouped under this physical complex quantity.

### Usage
Additional indication of a usage type of the quantities that are grouped under this physical complex quantity.

## Formal Propositions

### NoSelfReference
The _IfcPhysicalComplexQuantity_ should not reference itself within the list of _HasQuantities_.

### UniqueQuantityNames
Every individual _IfcPhysicalQuantity_ within the set _HasQuantities_ shall have a unique _Name_ attribute value.
> HISTORY New rule in IFC4
