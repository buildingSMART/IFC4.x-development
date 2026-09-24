# IfcTendonAnchor

A tendon anchor is the end connection for tendons in prestressed or posttensioned concrete.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _PredefinedType_ added.

## Attributes

### PredefinedType
Kind of tendon anchor.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTendonAnchorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcTendonAnchorType_.

## Concepts

### Body Geometry



### Object Typing



### Product Local Placement



### Property Sets for Objects



### Quantity Sets



