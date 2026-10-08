# IfcMechanicalFastenerType

The element component type **IfcMechanicalFastenerType** defines commonly shared information for occurrences of mechanical fasteners. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a mechanical fastener type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcMechanicalFastenerType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcMechanicalFastenerType** are represented by instances of _IfcMechanicalFastener_.

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Supertype changed from _IfcFastenerType_ to _IfcElementComponentType_. Attributes _PredefinedType_, _NominalDiameter_, _NominalLength_ added.

Classification Use Definition

Mechanical fasteners, especially bolts, are often standardized. To refer to a formal fastener designation according to a standard (a product norm), _IfcRelAssociatesClassification_ together with _IfcClassificationReference_ should be used.

* _IfcClassificationReference.Identification_ contains a machine-readable form of the formal fastener designation from the norm. Example: 'M16X80-10.9-HV' for a high-strength structural bolting assembly for preloading with hexagon bolt and nut. (On the other hand, _IfcMechanicalFastenerType.Name_ contains a displayable name which may not necessarily be the same as the formal designation.)
* _IfcClassificationReference.Name_ carries the short name of the fastener norm. Example: 'EN 14399-4' as the respective European standard for high-strength hexagon bolts.
* Optionally, the norm can be further described by _IfcClassificationReference.ReferencedSource_, including information like publisher and date of issue of the norm.

Furthermore, _IfcRelAssociatesLibrary_ together with _IfcLibraryReference_ may be used to refer to a library which contains fastener definitions.

## Attributes

### PredefinedType
Subtype of mechanical fastener

### NominalDiameter
The nominal diameter describing the cross-section size of the fastener type.

### NominalLength
The nominal length describing the longitudinal dimensions of the fastener type.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Mechanical Fastener Type Attributes



