# IfcPile

A pile is a slender timber, concrete, or steel structural element, driven, jetted, or otherwise embedded on end in the ground for the purpose of supporting a load. A pile is also characterized as deep foundation, where the loads are transferred to deeper subsurface layers.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: slender structural member, substantially underground, intended to transmit force(s) into loadbearing strata below the surface of the ground.

> NOTE Shallow foundations, which transfer the loads to the ground near its surface, are represented by _IfcFooting_.

> HISTORY New entity in IFC2x2.

## Attributes

### PredefinedType
The predefined generic type of the pile according to function.

> IFC4 CHANGE Attribute made optional. Type information can be provided by _IfcRelDefinesByType_ and _IfcPileType_.

### ConstructionType
Deprecated.

> IFC4 CHANGE Material profile association capability by means of _IfcRelAssociatesMaterial_ has been added. The attribute _ConstructionType_ should not be used whenever its information can be provided by a material profile set, either associated with the _IfcPile_ object or, if present, with a corresponding instance of _IfcPileType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPileType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcPileType_.

## Concepts

### Axis Geometry



### Body Geometry



### FootPrint Geometry



### Material Set



### Object Typing



### Product Local Placement



### Property Sets for Objects



### Quantity Sets



