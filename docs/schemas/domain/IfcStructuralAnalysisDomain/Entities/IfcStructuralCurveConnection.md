# IfcStructuralCurveConnection

Instances of _IfcStructuralCurveConnection_ describe edge 'nodes', i.e. edges where two or more surface members are joined, or edge supports. Edge curves may be straight or curved.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _Axis_ added, allowing for skewed supports. Use definitions added.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_. The local coordinate system is established by the reference curve given by topology representation and by the attribute _Axis_. The local x axis is parallel with the tangent on the reference curve. The local z axis is located in the surface which is created by sweeping _Axis_ along the reference curve and is directed according to _Axis_. The local y axis is directed such that x,y,z form a right-handed Cartesian coordinate system.

## Attributes

### Axis
Direction which is used in the definition of the local z axis. _Axis_ is specified relative to the so-called global coordinate system, i.e. the _SELF\IfcProduct.ObjectPlacement_.

> NOTE It is desirable and usually possible that many instances of _IfcStructuralCurveConnection_ and _IfcStructuralCurveMember_ share a common instance of _IfcDirection_ as their _Axis_ attribute.

## Concepts

### Reference Topology



