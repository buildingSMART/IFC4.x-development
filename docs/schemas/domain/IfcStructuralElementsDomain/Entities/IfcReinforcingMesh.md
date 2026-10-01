# IfcReinforcingMesh

A reinforcing mesh is a series of longitudinal and transverse wires or bars of various gauges, arranged at right angles to each other and welded at all points of intersection; usually used for concrete slab reinforcement. It is also known as welded wire fabric. In scope are plane meshes as well as bent meshes.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC4 CHANGE All attributes are optional now. Several attributes are deprecated; their information is now provided by _IfcReinforcingMeshType_. Attribute _PredefinedType_ added.

Geometry Use Definition

Placement and representation are defined at the supertype _IfcElementComponent_.

The representation map of a mapped 'Outline' representation should contain a representation of type 'Curve3D' which holds an _IfcPolyline_.

The representation map of a mapped 'Body' representation should contain a representation of type 'AdvancedSweptSolid' which holds multiple _IfcSweptDiskSolid_ (including subtype _IfcSweptDiskSolidPolygonal_).

## Attributes

### MeshLength
Deprecated.

> IFC4 CHANGE Attribute deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### MeshWidth
Deprecated.

> IFC4 CHANGE Attribute deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### LongitudinalBarNominalDiameter
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### TransverseBarNominalDiameter
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### LongitudinalBarCrossSectionArea
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### TransverseBarCrossSectionArea
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### LongitudinalBarSpacing
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### TransverseBarSpacing
Deprecated.

> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.

### PredefinedType
Kind of mesh.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcReinforcingMeshType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcReinforcingMeshType_.

## Concepts

### Body Geometry

### Mapped Geometry

The representation map referenced by a 'Body' 'MappedRepresentation' could contain a representation of type 'AdvancedSweptSolid' which holds an IfcSweptDiskSolid (including subtype IfcSweptDiskSolidPolygonal). Multiple IfcMappedItem's can be used to represent the bars within a mesh as one occurrence of IfcReinforcingMesh.

### Object Typing

### Property Sets for Objects

### Quantity Sets

### Reinforcing Mesh Attributes

