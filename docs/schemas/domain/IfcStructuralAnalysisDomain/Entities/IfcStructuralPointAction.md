# IfcStructuralPointAction

This entity defines an action which acts on a point. A point action is typically connected with a point connection. It may also be connected with a curve member or curve connection, or surface member or surface connection.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attributes in the supertypes _IfcStructuralActivity_ and _IfcStructuralAction_ changed. Use definitions changed, informal propositions added.

****Coordinate Systems****:

See definitions at _IfcStructuralActivity_.

****Topology Use Definitions****:

Standard Case:
If connected with a point item, instances of _IfcStructuralPointAction_ shall not have an _ObjectPlacement_ nor a _Representation_. It is implied that the placement and representation of the action is the same as the structural item.

Special Case 1:
If connected with a curve item or surface item, instances of _IfcStructuralPointAction_ shall have an _ObjectPlacement_ and _Representation_, containing an _IfcVertexPoint_. See _IfcStructuralActivity_ for further definitions.

> NOTE In order to model concentrated actions on a curve or surface item, _IfcStructuralCurveAction_ or _IfcStructuralSurfaceAction_ of type DISCRETE is preferable since they do not require an extra topology representation in this case. An _IfcStructuralPointAction_ should be used for a concentrated action on a curve or surface item only when an explicit vertex point representation is actually desired.

Special Case 2:
If not connected with a structural item (which may happen in an incomplete or conceptual model), a point action should have an _ObjectPlacement_ and _Representation_, containing an _IfcVertexPoint_. See _IfcStructuralActivity_ for further definitions.

## Formal Propositions

### SuitableLoadType
A structural point action shall place either a single force or a single displacement.

## Concepts

### Structural Activity



#### IfcStructuralLoadSingleForce_IfcStructuralCurveConnection

Point force and moment at a point connection.

#### IfcStructuralLoadSingleForce_IfcStructuralCurveMember

Point force and moment positioned within a curve member.

#### IfcStructuralLoadSingleForce_IfcStructuralSurfaceMember

Point force and moment positioned within a surface member.

