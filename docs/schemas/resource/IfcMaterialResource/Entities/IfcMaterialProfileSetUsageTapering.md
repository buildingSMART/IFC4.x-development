# IfcMaterialProfileSetUsageTapering

_IfcMaterialProfileSetUsageTapering_ specifies dual material profile sets in association with tapered prismatic (beam- or column-like) elements.
<!-- end of short definition -->

> HISTORY  New entity in IFC4

Usage with tapered building elements

The inherited attribute _ForProfileSet_ specifies the profile and material at the start of the member, _ForProfileEndSet_ at its end. Start and end correspond to the extrusion direction in the shape model of the shape representation of the element or element type.

Both material profile sets should refer to the same material, that is, only differ with respect to their profiles.

Usage with structural analysis curve members

_IfcMaterialProfileSetUsageTapering_ may be used with the structural analysis idealization (_IfcStructuralCurveMember_) of uniform members as well as of tapered members.

In case of uniform members, _ForProfileSet_ and _ForProfileEndSet_ refer to the same material profile set. In case of tapered members, _ForProfileSet_ specifies the profile and material at the start of the member, _ForProfileEndSet_ at its end. Start and end correspond to the edge direction in the topological representation of the curve member.

## Attributes

### ForProfileEndSet
The second _IfcMaterialProfileSet_ set to which the usage is applied.

### CardinalEndPoint
Index reference to a significant point in the second section profile. Describes how this section is aligned relative to the axis of the member it is associated with. This parametric specification of profile alignment can be provided redundantly to the explicit alignment defined by ForProfileSet.MaterialProfiles[\*].Profile.
