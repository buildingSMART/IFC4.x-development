# IfcStructuralSurfaceMemberVarying

This entity describes surface members with varying section properties. The properties are provided by means of _Pset_StructuralSurfaceMemberVaryingThickness_ via _IfcRelDefinesByProperties_, or by means of aggregation: An instance of _IfcStructuralSurfaceMemberVarying_ may be composed of two or more instances of _IfcStructuralSurfaceMember_ with differing section properties. These subordinate members relate to the instance of _IfcStructuralSurfaceMemberVarying_ by _IfcRelAggregates_.
<!-- end of short definition -->

> NOTE It is recommended that structural activities (actions or reactions) are not connected with aggregated _IfcStructuralSurfaceMemberVarying_ but only with the _IfcStructuralSurfaceMember_s in the aggregation. That way, difficulties in interpretation of local coordinates are avoided.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Use definition changed and attributes deleted.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_ and _IfcStructuralSurfaceMember_. The local coordinates of an aggregate are generally undefined since continuity of local coordinates of the parts is not ensured.

****Material Use Definition****

In case of aggregation, only the individual parts (direct instances of _IfcStructuralSurfaceMember_) carry material and thickness information. Otherwise, definitions at _IfcStructuralSurfaceMember_ apply.

## Concepts

### Property Sets for Objects



