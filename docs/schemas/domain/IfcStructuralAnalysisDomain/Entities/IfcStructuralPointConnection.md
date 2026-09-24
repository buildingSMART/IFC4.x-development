# IfcStructuralPointConnection

Instances of _IfcStructuralPointConnection_ describe structural nodes or point supports.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _ConditionCoordinateSystem_ added, allowing for skewed supports. Use definitions added.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_. The local coordinate system is established by the reference point given by topology representation and by the attribute _ConditionCoordinateSystem_.

## Attributes

### ConditionCoordinateSystem
Defines a coordinate system used for the description of the support condition properties in _SELF\IfcStructuralConnection.SupportCondition_, specified relative to the global coordinate system (global to the structural analysis model) established by _SELF.\IfcProduct.ObjectPlacement_. If left unspecified, the placement _IfcAxis2Placement3D_((x,y,z), ?, ?) is implied with x,y,z being the coordinates of the reference point of this _IfcStructuralPointConnection_ and the default axes directions being in parallel with the global axes.

## Concepts

### Reference Topology

Instances of IfcStructuralPointConnection shall have a topology representation which consists of one IfcVertexPoint, representing the reference point of the point connection. See definitions at IfcStructuralItem for further specifications.

