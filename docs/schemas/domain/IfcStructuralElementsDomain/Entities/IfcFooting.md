# IfcFooting

A footing is a part of the foundation of a structure that spreads and transmits the load to the soil. A footing is also characterized as shallow foundation, where the loads are transferred to the ground near the surface.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: stepped construction that spreads the load at the foot of a wall or column.

> HISTORY New entity in IFC2x2.

> NOTE Slab foundations, also called slab-on-grade, are not instantiated as _IfcFooting_ but as _IfcSlab_ with a predefined type of _IfcSlabTypeEnum_.BASESLAB. Deep foundations, which transfer the loads to subsurface layers, are represented by _IfcDeepFoundation_ and its subtypes _IfcCaissonFoundation_ and _IfcPile_.

## Attributes

### PredefinedType
The generic type of the footing.

> IFC4 CHANGE Attribute made optional. Type information can be provided by _IfcRelDefinesByType_ and _IfcFootingType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFootingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcFootingType_.

## Concepts

### Axis Geometry



### Body Geometry



### FootPrint Geometry



### Material Set



### Object Typing



### Product Local Placement



### Property Sets for Objects



### Quantity Sets



