# IfcRelConnectsWithEccentricity

The entity _IfcRelConnectsWithEccentricity_ adds the definition of eccentricity to the connection between a structural member and a structural connection (representing either a node or support).
<!-- end of short definition -->

> NOTE Another eccentricity model is available independently of eccentric connection specification: The section profile of a curve member may be inserted eccentrically with respect to the member's reference curve, see definitions at _IfcStructuralCurveMember_. Whether one or the other or both eccentricity models may be used is subject to information requirements and local agreements.

> HISTORY New entity in IFC2x3.

> IFC4 CHANGE Use definitions changed to always require two topology items.

**Use Definition**

_Point Connection_
_ConnectionConstraint_ shall be of type _IfcConnectionPointGeometry_ and shall refer to two instances of _IfcVertexPoint_.

_Curve Connection_
_ConnectionConstraint_ shall be of type _IfcConnectionCurveGeometry_ and shall refer to two instances of _IfcEdge_ or subtypes.

_Surface Connection_
_ConnectionConstraint_ shall be of type _IfcConnectionSurfaceGeometry_ and shall refer to two instances of _IfcFaceSurface_.

## Attributes

### ConnectionConstraint
The connection constraint explicitly states the eccentricity between a structural member and a structural connection by means of two topological objects (vertex and vertex, or edge and edge, or face and face).
