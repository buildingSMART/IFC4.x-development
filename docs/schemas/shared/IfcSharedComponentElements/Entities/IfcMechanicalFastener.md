# IfcMechanicalFastener

A mechanical fasteners connecting building elements or parts mechanically. A single instance of this class may represent one or many of actual mechanical fasteners, for example an array of bolts or a row of nails.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC4 CHANGE Supertype changed from _IfcFastener_ to _IfcElementComponent_. Attribute _PredefinedType_ added. Attributes _NominalDiameter_ and _NominalLength_ deprecated.

## Attributes

### NominalDiameter
The nominal diameter describing the cross-section size of the fastener type.

> IFC4 CHANGE Deprecated; the respective attribute of _IfcMechanicalFastenerType_ should be used instead.

### NominalLength
The nominal length describing the longitudinal dimensions of the fastener type.

> IFC4 CHANGE Deprecated; the respective attribute of _IfcMechanicalFastenerType_ should be used instead.

### PredefinedType
Subtype of mechanical fastener

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcMechanicalFastenerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcMechanicalFastenerType_.

## Concepts

### Mechanical Fastener Attributes



### Object Typing



### Property Sets for Objects



### Quantity Sets



