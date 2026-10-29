# IfcStructuralItem

The abstract entity _IfcStructuralItem_ is the generalization of structural members and structural connections, that is, analysis idealizations of elements in the building model. It defines the relation between structural members and connections with structural activities (actions and reactions).
<!-- end of short definition -->

Relationships between elements in the building model and structural items as their idealizations can be expressed by instances of _IfcRelAssignsToProduct_.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Use definitions and informal proposition added.

****Coordinate Systems****:

The following coordinate systems are distinguished:

* The so-called global coordinate system is the coordinate system shared by all items and activities which are grouped in a common _IfcStructuralAnalysisModel_. This coordinate system is established by _SELF\IfcProduct.ObjectPlacement_. (This coordinate system is not necessarily the same as the _IfcProject_'s world coordinate system.)
* The so-called local coordinate system is a coordinate system local to a structural item (connection or member). This coordinate system is established by a _Representation_ (attribute inherited from _IfcProduct_) in conjunction with further use definitions and attributes of subtypes of _IfcStructuralItem_.

Representation items in topology representations are always given within the _ObjectPlacement_, i.e. in so-called global coordinates (global with respect to the _IfcStructuralAnalysisModel_ to which this item belongs).

The usage of local coordinate systems is further defined in subtypes.

****Topology Use Definitions****:

Instances of _IfcStructuralItem_ shall have a topology representation. It includes a placement and a product representation. The _IfcProductRepresentation_ shall be given by an item in a _Representation_ of type _IfcTopologyRepresentation_.

**Local Placement**

The local placement for _IfcStructuralItem_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which establishes a global coordinate system which shall be common to all items and activities in an _IfcStructuralAnalysisModel_.

**Topology Representation**

Instances of _IfcStructuralItem_ shall have a topology representation given by an instance of a subtype of _IfcTopologicalRepresentationItem_, which should be the single item of _IfcTopologyRepresentation.Items_. Depending on the dimensionality of the structural item, one of the following types of topological representation items shall be used:

* Point connections shall be represented by an _IfcVertexPoint_ with an underlying _IfcCartesianPoint_. The Cartesian point is the reference point of the connection in the so-called global coordinate system. The following labels are used in the _IfcTopologyRepresentation_:
  * _RepresentationIdentifier_: 'Reference'
  * _RepresentationType_: 'Vertex'
* Curve members and curve connections shall either be represented by an _IfcOrientedEdge_, _IfcEdgeCurve_, or _IfcEdge_. The curve to which the _IfcEdgeCurve_ (or an _IfcOrientedEdge_'s underlying _IfcEdgeCurve_) refers to is the reference curve of the structural item in the global coordinate system. Start and end vertex of the edge shall be _IfcVertexPoint_s with underlying _IfcCartesianPoint_s. The following labels are used in the _IfcTopologyRepresentation_:
  * _RepresentationIdentifier_: 'Reference'
  * _RepresentationType_: 'Edge'
>> NOTE While an _IfcEdge_ (or _IfcOrientedEdge_ with underlying _IfcEdge_) does not provide an explicit underlying curve geometry, it may be used to imply an underlying straight line as reference curve with the origin of the curve parameter at the start vertex point.
* Surface members and surface connections shall be represented by an _IfcFaceSurface_. The underlying surface defines the reference surface of the structural surface item in the global coordinate system. All edges in the bounds of the face shall conform to the rules for edge representations of structural curve item. The following labels are used in the _IfcTopologyRepresentation_:
  * _RepresentationIdentifier_: 'Reference'
  * _RepresentationType_: 'Face'

The reference point, reference curve, or reference surface partially or completely defines the local coordinate system of the represented structural item according to the following rules. In all cases, The local x,y,z directions form a right-handed Cartesian coordinate system.

_Structural point items_

* The reference point in the representation is the origin of the local coordinate system of the structural item.
* The axes of the local coordinate system are either parallel with and directed like the so-called global coordinate axes, or are oriented according to definitions at the respective subtype of _IfcStructuralItem_.

_Structural curve items_

* The u parameter origin of the reference curve in the representation is the origin of the local coordinate system of the structural item.
* The local x axis is parallel with the tangent on the curve and directed like the u parameter direction.
* The local y and z axes are oriented according to definitions at the respective subtypes of _IfcStructuralItem_.

_Structural surface items_

* The u,v parameter origin of the reference surface in the representation is the origin of the local coordinate system of the structural item.
* The local x and y directions follow the tangents on the surface and are in parallel with and directed like u and v respectively.
* The local z direction is in parallel with and directed like the surface normal.

**Informal Propositions**

1. The _ObjectPlacement_s of all structural items which are grouped into the same instance of _IfcStructuralAnalysisModel_ shall refer to the same instance of _IfcObjectPlacement_.

> NOTE This rule is necessary to achieve consistent topology representations. The topology representations of structural items in an analysis model are meant to share vertices and edges und must therefore have the same object placement.

> NOTE A structural item may be grouped into more than one analysis model. In this case, all these models must use the same instance of _IfcObjectPlacement_.

## Attributes

### AssignedStructuralActivity
Inverse relationship to all structural activities (i.e. to actions or reactions) which are assigned to this structural member.
