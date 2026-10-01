# IfcPhysicalQuantity

The physical quantity, _IfcPhysicalQuantity_, is an abstract entity that holds a complex or simple quantity measure together with a semantic definition of the usage for the single or several measure value.
<!-- end of short definition -->

The _Name_ attribute defines the actual usage or kind of measure. The interpretation of the name label has to be established within the actual exchange context. In addition an informative text may be associated to each quantity by the _Description_ attribute.

> HISTORY New entity in IFC2x. It replaces the calcXxx attributes used in previous IFC Releases.

## Attributes

### Name
Name of the element quantity or measure. The name attribute has to be made recognizable by further agreements.

### Description
Further explanation that might be given to the quantity.

### HasExternalReferences
Reference to an external reference, e.g. library, classification, or document information, that is associated to the quantity.
> IFC4 CHANGE New inverse attribute.

### PartOfComplex
Reference to a physical complex quantity in which the physical quantity may be contained.
