# IfcCurtainWall

A curtain wall is a wall of a building which is an assembly of components, hung from the edge of the floor/roof structure rather than bearing on a floor. Curtain wall is represented as a building element assembly and implemented as a subtype of _IfcBuiltElement_ that uses an _IfcRelAggregates_ relationship. A curtain wall is often external, but using _Pset_CurtainWallCommon.IsExternal_ can be used to define interior curtain walls.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: non load bearing wall positioned on the outside of a building and enclosing it.

> HISTORY New entity in IFC2.0

The geometric representation of _IfcCurtainWall_ is given by the _IfcProductDefinitionShape_, allowing multiple geometric representations. Independent 'Body' geometric representation, as described below, should only be used when the _IfcCurtainWall_ is not defined as an aggregate. If defined as an aggregate, the geometric representation is the sum of the representations of the components within the aggregate.

The geometric representation of _IfcCurtainWall_ is defined using the following multiple shape representations for its definition:

* Axis: A two-dimensional open curve (for restrictions see below) defining the axis for the curtain wall.
  * This is an optional representation for curtain walls.
* Body: A surface model or boundary representation model representation defining the 3D shape of the curtain wall.
  * If the _IfcCurtainWall_ has components (referenced by _SELF\IfcObject.IsDecomposedBy_) then no independent shape representation with _RepresentationType_ = 'Body' shall be defined. The body of _IfcCurtainWall_ is then geometrically represented by the shape representation of its components. The components are accessed via _SELF\IfcObject.IsDecomposedBy[1].RelatedObjects_.
  * If the _IfcCurtainWall_ has no components defined (empty set of _SELF\IfcObject.IsDecomposedBy_) then the _IfcCurtainWall_ may be represented by a shape representation with the _RepresentationIdentifier_ ='Body'.

## Attributes

### PredefinedType
Predefined generic type for a curtain wall that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcCurtainWallType_ is assigned, providing its own _IfcCurtainWallType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCurtainWallType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no curtain wall type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCurtainWallType_.

## Concepts

### Axis 2D Geometry

The following additional constraints apply to the 'Axis' representation:

* **Geometry** : _IfcPolyline_ having two Points, or _IfcTrimmedCurve_ with _BasisCurve_ of type _IfcLine_ or _IfcCircle_.

### Object Typing



### Product Local Placement

The following restriction may be imposed by view definitions or implementer agreements:

* If the _IfcCurtainWall_ establishes an aggregate, then all contained elements shall be placed relative to the _IfcCurtainWall.ObjectPlacement_.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment



#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey - curtain wall facades may be assigned directly to the building

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

