# IfcStructuralActivity

The abstract entity _IfcStructuralActivity_ combines the definition of actions (such as forces, displacements, etc.) and reactions (support reactions, internal forces, deflections, etc.) which are specified by using the basic load definitions from the _IfcStructuralLoadResource_.
<!-- end of short definition -->

The differentiation between actions and reactions is realized by instantiating objects either from subclasses of _IfcStructuralAction_ or _IfcStructuralReaction_ respectively. They inherit commonly needed attributes from the abstract superclass _IfcStructuralActivity_, notably the relationship which connects actions or reactions with connections, analysis members, or elements (subtypes of _IfcStructuralItem_ or _IfcElement_).

> NOTE Instances of _IfcStructuralActivity_ which are connected with an _IfcElement_ are subject to agreements outside the scope of this specification.

> NOTE The semantics of _IfcStructuralActivity_ are only fully defined if an activity instance is connected with exactly one structural item. The inverse attribute _AssignedToStructuralItem_ can only be empty in incomplete models or in conceptual models which are not yet ready for analysis.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Cardinality of attribute _AssignedToStructuralItem_ relaxed from 1 to 0..1 in order to allow for schema-compliant incomplete models as well as conceptual models without load—item relationships.

****Coordinate Systems****:

The following coordinate systems are distinguished:

* The so-called global coordinate system is the coordinate system shared by all items and activities which are grouped in a common _IfcStructuralAnalysisModel_. This coordinate system is established by an _ObjectPlacement_. (This coordinate system is not necessarily the same as the _IfcProject_'s world coordinate system.)
* The so-called local coordinate system is a coordinate system local to a structural item (connection or member). This coordinate system is established by a _Representation_ in conjunction with further use definitions and attributes of subtypes of _IfcStructuralItem_.

Representation items in topology representations are always given within the _ObjectPlacement_, i.e. in so-called global coordinates (global with respect to the _IfcStructuralAnalysisModel_ to which this activity belongs).

Locations of the load objects in the _AppliedLoad_ attribute (if of type _IfcStructuralLoadConfiguration_) are always given in local coordinates.

Directions of the load objects in the _AppliedLoad_ attribute refer to global or local coordinates according to the _GlobalOrLocal_ attribute.

The _ObjectPlacement_ and _Representation_ are sometimes not explicitly instantiated; instead they may be implied as described below. Global and local coordinate systems are then determined in the same way as with explicit placement and representation.

****Topology Use Definitions****:

Instances of _IfcStructuralActivity_ which are connected with a structural item of same dimensionality, i.e.

* a point action or reaction connected with a point item (_IfcStructuralPointConnection_),
* a curve action or reaction connected with a curve item (_IfcStructuralCurveConnection_, _IfcStructuralCurveMember_), or
* a surface action or reaction connected with a surface item (_IfcStructuralSurfaceConnection_, _IfcStructuralSurfaceMember_) and which acts on the entire surface of the item and is not specified by isocontours

shall not have an _ObjectPlacement_ nor a _Representation_. It is implied that the placement and representation of the _IfcStructuralActivity_ is the same as the ones of the _IfcStructuralItem_.

Instances of _IfcStructuralActivity_ which are connected with

* a curve item (_IfcStructuralCurveConnection_, _IfcStructuralCurveMember_) and act on a point of the item
* a surface item (_IfcStructuralSurfaceConnection_, _IfcStructuralSurfaceMember_) and act on a point or on a curve or on a part of the surface of the item

shall have a topology representation as specified below. It includes a placement and a product representation. The _IfcProductRepresentation_ shall be given by an item in a _Representation_ of type _IfcTopologyRepresentation_.

Instances of _IfcStructuralActivity_ which are connected with

* a surface item (_IfcStructuralSurfaceConnection_, _IfcStructuralSurfaceMember_) and are specified by isocontours

shall have a shape representation as specified below. It includes a placement and a product representation. The _IfcProductRepresentation_ shall be given by items in a _Representation_ of type _IfcShapeRepresentation_. Shape representation and topology representation may be combined.

**Local Placement**

The local placement for _IfcStructuralActivity_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which establishes a global coordinate system which shall be common to all items and activities in an _IfcStructuralAnalysisModel_.

**Topology Representation**

Instances of _IfcStructuralActivity_ which act on parts of a surface item shall have a topology representation given by a face with underlying surface geometry, _IfcFaceSurface_, which should be the single item of _IfcTopologyRepresentation.Items_. The surface establishes a local coordinate system of the activity:

* The origin of surface parameters u,v is the origin of the local coordinate system.
* The local x and y directions follow the tangents on the surface and are in parallel with and directed like u and v respectively.
* The local z direction is in parallel with and directed like the surface normal.

> * _RepresentationIdentifier_: 'Reference'
> * _RepresentationType_: 'Face'

Instances of _IfcStructuralActivity_ which act on a curve on a surface item shall have a topology representation given by an edge (_IfcEdge_ or subtype), which should be the single item of _IfcTopologyRepresentation.Items_. The curve geometry shall be compatible with the surface geometry of the connected item. In conjunction with this surface, the curve establishes a local coordinate system of the activity:

* The origin of the curve parameter u is the origin of the local coordinate system.
* The local x direction follows the tangent on the curve and is directed like u.
* The local z direction is in parallel with and directed like the surface normal of the connected surface item.
* The local x,y,z directions form a right-handed Cartesian coordinate system.

> * _RepresentationIdentifier_: 'Reference'
> * _RepresentationType_: 'Edge'

> NOTE While an _IfcEdge_ (or _IfcOrientedEdge_ with underlying _IfcEdge_) does not provide an explicit underlying curve geometry, it may be used to imply an underlying straight line as reference curve with the origin of the curve parameter at the start vertex point.

Instances of _IfcStructuralActivity_ which act on a single point on a curve or surface item shall have a topology representation given by an _IfcVertexPoint_, which should be the single item of _IfcTopologyRepresentation.Items_. The point geometry shall be compatible with the curve or surface geometry of the connected item. The local coordinate system of the activity is oriented by the curve or surface geometry of the connected item as described above for activities with edge or face topology.

> * _RepresentationIdentifier_: 'Reference'
> * _RepresentationType_: 'Vertex'

**Shape Representation**

Instances of _IfcStructuralActivity_ which act on a surface item and are specified by isocontours (level sets) shall have a shape representation given by a set of curves on a surface, _IfcPcurve_. The basis surface shall comply with or preferably be identical with the surface of the structural item to which the activity is connected. The representation identifier and type of this geometric representation is:

> * _RepresentationIdentifier_: 'Level set'
> * _RepresentationType_: 'GeometricCurveSet'

## Attributes

### AppliedLoad
Load or result resource object which defines the load type, direction, and load values.

In case of activities which are variably distributed over curves or surfaces, _IfcStructuralLoadConfiguration_ is used which provides a list of load samples and their locations within the load distribution, measured in local coordinates of the curve or surface on which this activity acts. The contents of this load or result distribution may be further restricted by definitions at subtypes of _IfcStructuralActivity_.

### GlobalOrLocal
Indicates whether the load directions refer to the global coordinate system (global to
the analysis model, i.e. as established by _IfcStructuralAnalysisModel.SharedPlacement_)
or to the local coordinate system (local to the activity or connected item, as established by
an explicit or implied representation and its parameter space).

> NOTE , the informal definition of _IfcRepresentationResource.IfcGlobalOrLocalEnum_ doe s not distinguish between "global coordinate system" and "world coordinate system". On the other hand, this distinction is necessary in the _IfcStructuralAnalysisDomain_ where the shared "global" coordinate system of an analysis model may very well not be the same as the project-wide world coordinate system.

> NOTE In the scope of _IfcStructuralActivity.GlobalOrLocal_, the meaning of GLOBAL_COORDS is therefore not to be taken as world coordinate system but as the analysis model specific shared coordinate system. In contrast, LOCAL_COORDS is to be taken as coordinates which are local to individual structural items and activities, as established by subclass-specific geometry use definitions.

### AssignedToStructuralItem
Reference to the _IfcRelConnectsStructuralActivity_ relationship by which activities are connected with structural items.
