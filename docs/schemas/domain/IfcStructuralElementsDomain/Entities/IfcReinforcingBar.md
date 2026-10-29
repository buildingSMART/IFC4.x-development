# IfcReinforcingBar

A reinforcing bar is usually made of steel with manufactured deformations in the surface, and used in concrete and masonry construction to provide additional strength. A single instance of this class may represent one or many of actual rebars, for example a row of rebars.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC 2x4 CHANGE All attributes are optional now. Several attributes are deprecated; their information now provided by _IfcReinforcingBarType_. Attribute _BarRole_ renamed to _PredefinedType_.

Geometry Use Definition

Placement and representation are defined at the supertype _IfcElementComponent_.

The representation map of a mapped 'Body' representation should contain a representation of type 'AdvancedSweptSolid' which holds an _IfcSweptDiskSolid_ (including subtype _IfcSweptDiskSolidPolygonal_).

## Attributes

### NominalDiameter
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingBarType_ instead.

### CrossSectionArea
The effective cross-section area of the reinforcing bar or group of bars.

> IFC4 CHANGE Attribute made optional.

### BarLength
Deprecated.

> IFC4 CHANGE Attribute deprecated. Use respective attribute at _IfcReinforcingBarType_ instead.

### PredefinedType
The role, purpose or usage of the bar, i.e. the kind of loads and stresses it is intended to carry.

> IFC4 CHANGE Attribute renamed from _BarRole_ to _PredefinedType_ and made optional. Type changed from _IfcReinforcingBarRoleEnum_ without changes to the range of enumeration items.

### BarSurface
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingBarType_ instead.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcReinforcingBarType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcReinforcingBarType_.

## Concepts

### Body Geometry

### Mapped Geometry

The representation map referenced by a 'Body' 'MappedRepresentation' should contain a representation of type 'AdvancedSweptSolid' which holds an IfcSweptDiskSolid (including subtype IfcSweptDiskSolidPolygonal). Multiple IfcMappedItem's can be used to represent several bars as one occurrence of IfcReinforcingBar.

### Material Set



#### Core

Material from which the rebar is constructed, such as steel.

#### Coating

Outer coating, if applicable.

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Reinforcing Bar Attributes



