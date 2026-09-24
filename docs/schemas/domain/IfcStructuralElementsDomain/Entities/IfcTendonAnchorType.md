# IfcTendonAnchorType

The reinforcing element type **IfcTendonAnchorType** defines commonly shared information for occurrences of tendon anchors. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a tendon anchor type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcTendonAnchorType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcTendonAnchorType** are represented by instances of _IfcTendonAnchor_.

> HISTORY New entity in IFC4.

Material Use Definition

A material or material constituent set may be associated.

Geometry Use Definition

The _IfcTendonAnchorType_ may define the shared geometric representation for many tendon anchor occurrences. The _RepresentationMaps_ attribute refers to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations.

## Attributes

### PredefinedType
Subtype of tendon anchor.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.
