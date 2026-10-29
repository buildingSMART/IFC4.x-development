# IfcStructuralSurfaceAction

This entity defines an action which is distributed over a surface. A surface action may be connected with a surface member or surface connection.
<!-- end of short definition -->

> HISTORY New entity in IFC4.

> IFC4 CHANGE Former entity _IfcStructuralPlanarActionVarying_ from IFC2x2 has been removed and are replaced by this entity.

****Coordinate Systems****:

See definitions at _IfcStructuralActivity_.

****Topology Use Definitions****:

Standard Case:
If connected with a surface item and acting on its entirety, instances of _IfcStructuralCurveAction_ shall not have an _ObjectPlacement_ nor a _Representation_. It is implied that the placement and representation of the _IfcStructuralActivity_ is the same as the ones of the member or connection.

Special Case 1:
If connected with a surface item but acting only on a part of it, instances of _IfcStructuralSurfaceAction_ shall have an _ObjectPlacement_ and _Representation_, containing an _IfcFaceSurface_ which topologically defines the loaded part of the surface. See _IfcStructuralActivity_ for further definitions.

Special Case 2:
If not connected with a structural item (which may happen in an incomplete or conceptual model), a surface action should have an _ObjectPlacement_ and _Representation_, containing an _IfcFaceSurface_. See _IfcStructuralActivity_ for further definitions.

**Informal Propositions**

1. If the surface action is of the predefined type CONST, _SELF\IfcStructuralActivity.AppliedLoad_ must not be of type _IfcStructuralLoadConfiguration_.
2. If the surface action is of the predefined type BILINEAR, _SELF\IfcStructuralActivity.AppliedLoad_ shall be of type _IfcStructuralLoadConfiguration_ and shall contain three items with two-dimensional _IfcStructuralLoadConfiguration.Locations_, defining the location of the load samples in local coordinates of the surface action.
3. If the surface action is of the predefined type DISCRETE, _SELF\IfcStructuralActivity.AppliedLoad_ shall be of type _IfcStructuralLoadConfiguration_ and shall contain two or more items with two-dimensional locations.
4. Point loads must be of type DISCRETE, thus contain two or more load points. (Single point loads are modeled by _IfcStructuralLoadSingleForce_.)
5. All items in _SELF\IfcStructuralActivity.AppliedLoad\IfcStructuralLoadConfiguration.Values_ shall be of the same entity type.

## Attributes

### ProjectedOrTrue
Defines whether load values are given per true lengths of the surface on which they act, or per lengths of the projection of the surface in load direction. The latter is only applicable to loads which act in global coordinate directions.

### PredefinedType
Type of action according to its distribution of load values.

## Formal Propositions

### ProjectedIsGlobal
A load can only be related to projected lengths if it was specified in global coordinate directions (i.e. in analysis model coordinate directions). If a load was specified in local coordinate directions, it can only relate to true lengths.

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Structural Activity



#### IfcStructuralLoadPlanarForce_IfcStructuralSurfaceMember

Force and moment within a surface member.

