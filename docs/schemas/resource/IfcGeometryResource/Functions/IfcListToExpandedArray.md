# IfcListToExpandedArray

This function converts a generic list to an array with newly determined array bounds. If the array bounds are incompatible with the number of elements in the conditional list (number of elements in the list has to be smaller than the array upper bound and the number of values has to match the number of true values from Condition) a null result is returned. This function is used to construct the array of voxel values in IfcVoxelData based on the its IfcVoxelGrid geometric representation.

> HISTORY  New function in IFC4X4
