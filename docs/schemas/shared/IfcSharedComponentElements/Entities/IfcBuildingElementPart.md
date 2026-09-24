# IfcBuildingElementPart

_IfcBuildingElementPart_ represents major components as subordinate parts of a building element. Typical usage examples include precast concrete sandwich walls, where the layers may have different geometry representations. In this case the layered material representation does not sufficiently describe the element. Each layer is represented by an own instance of the _IfcBuildingElementPart_ with its own geometry description.
<!-- end of short definition -->

The kind of building element part is further specified by a corresponding instance of _IfcBuildingElementPartType_, referred to by _IfcRelDefinesByType_.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Moved from _IfcStructuralElementsDomain_ schema to _IfcSharedComponentElements_ schema, compatible change of supertype, attribute _PredefinedType_ added.

## Attributes

### PredefinedType
Subtype of building element part

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBuildingElementPartType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcBuildingElementPartType_.

## Concepts

### Object Typing



