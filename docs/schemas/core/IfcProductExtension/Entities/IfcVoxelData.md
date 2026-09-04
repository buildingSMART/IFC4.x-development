# IfcVoxelData

Abstract class representing voxel data values that is assigned to _IfcProduct_ using the relationship _IfcRelAssignsToProduct_ and to a product representation, as _IfcVoxelGrid_, using _Representation_.
The number of values shall correspond to the number of voxels in the voxel grid.
## Attributes

### ValueType
An optional value type used for the values defined in one of the subtypes. Only the names (as labels) of the types available in the _IfcValue_ select type are allowed.

### GridSize
Derived attribute that represents the total number of voxels in the _IfcVoxelGrid_ that is used as the representation for the _IfcVoxelData_ instance.

## Formal Propositions

### IsAssignedToProduct
_IfcVoxelData_ shall have exactly one assignment relationship of type _IfcRelAssignsToProduct_ to a product.

### VoxelGridRepresentation
_IfcVoxelData_ shall have a product definition shape and there shall be exactly one _IfcShapeRepresentation_ in _IfcProductDefinitionShape_._Representations_ that has exactly one geometric item _IfcVoxelGrid_.

### SameRepresentation
The assigned _IfcProduct_ shall have the same shape representation.
