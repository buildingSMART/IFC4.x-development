# IfcStructuralCurveMemberVarying

This entity describes edge members with varying profile properties. Each instance of _IfcStructuralCurveMemberVarying_ is composed of two or more instances of _IfcStructuralCurveMember_ with differing profile properties. These subordinate members relate to the instance of _IfcStructuralCurveMemberVarying_ by _IfcRelAggregates_.
<!-- end of short definition -->

> NOTE A curve member whose variation of profile properties can be sufficiently described by a start profile and an end profile (e.g. tapers) shall be modeled as a single direct instance of the supertype _IfcStructuralCurveMember_.

> NOTE It is recommended that structural activities (actions or reactions) are not connected with aggregated _IfcStructuralCurveMemberVarying_ but only with the _IfcStructuralCurveMember_s in the aggregation. That way, difficulties in interpretation of local coordinates are avoided.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Use definition changed.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_ and _IfcStructuralCurveMember_. The local coordinates of the aggregate are derived from those of its parts. Length measures in local x direction of the aggregate depend on continuity and lengths of the parts. The _Axis_ of the aggregate shall be the same as the _Axis_ of the part at the start of the aggregate.

****Material Use Definition****

Only the individual parts (direct instances of _IfcStructuralCurveMember_) carry material and profile information.
