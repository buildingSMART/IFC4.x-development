# IfcMember

An _IfcMember_ is a structural member designed to carry loads between or beyond points of support. It is not required to be load bearing. The orientation of the member (being horizontal, vertical or sloped) is not relevant to its definition (in contrary to _IfcBeam_ and _IfcColumn_). An _IfcMember_ represents a linear structural element from an architectural or structural modeling point of view and shall be used if it cannot be expressed more specifically as either an _IfcBeam_ or an _IfcColumn_.
<!-- end of short definition -->

There are two main representations for member occurrences:

 * _IfcMember_ with _IfcMaterialProfileSetUsage_ is used for all occurrences of members, that have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These members are always represented geometricly by an 'Axis' and a 'SweptSolid' or 'AdvancedSweptSolid' shape representation (or by a 'Clipping' geometry based on the swept solid), if a 3D geometric representation is assigned.
 * _IfcMember_ without _IfcMaterialProfileSetUsage_ is used for all other occurrences of members, particularly for members with changing profile sizes along the extrusion, or members defined by non-linear extrusion, or members having only 'Brep', or 'SurfaceModel' geometry, or if a more parametric representation is not intended.

> NOTE The representation of a member in a structural analysis model is provided by _IfcStructuralCurveMember_ being part of an _IfcStructuralAnalysisModel_.

> HISTORY New entity in IFC2x2 Addendum 1.

## Attributes

### PredefinedType
Predefined generic type for a member that is specified in an enumeration. There may be a property set given for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcMemberType_ is assigned, providing its own _IfcMemberType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcMemberType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no member type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcMemberType_.

## Concepts

### Axis 3D Geometry

The axis representation can be used to represent the fundamental orientation and extents of a member's body.

If an _IfcMaterialProfileSetUsage_ is used, the axis representation is used to locate the profile. In addition:

 * For a body representation using an _IfcExtrudedAreaSolid_, the axis may be an _IfcPolyline_ having two Points, or _IfcTrimmedCurve_ with BasisCurve of type _IfcLine_. The axis curve lies on the z axis of the object coordinate system.
 * For a body representation using an _IfcRevolvedAreaSolid_, the axis may be an _IfcTrimmedCurve_ with BasisCurve of type _IfcCircle_. The axis curve lies on the x/z plane of the object coordinate system, the tangent at the start is along the positive z-axis.

As shown in Figure 235, the axis representation can be used to represent the system length of a member that may extend past the body length of the member.

![Axis](../../../../figures/ifcmemberstandardcase_axis-01.png)

Figure 235 — Member axis representation

As shown in Figure 236, the axis representation must be positioned at the _IfcMaterialProfileSetUsage_._CardinalPoint_, and parallel to the _IfcExtrudedAreaSolid_._ExtrudedDirection_. This offset between the axis line and the _IfcExtrudedAreaSolid_._Position_ must correlate with the chosen _IfcMaterialProfileSetUsage_.CardinalPoint.

![Axis](../../../../figures/ifcmemberstandardcase_axis-02.png)

Figure 236 — Member axis cardinal point

#### Axis_IfcBoundedCurve_Curve3D

Three-dimensional reference curve for the member.

### Body AdvancedSweptSolid Geometry

* _IfcSurfaceCurveSweptAreaSolid_, _IfcFixedReferenceSweptAreaSolid_, _IfcExtrudedAreaSolidTapered_, _IfcRevolvedAreaSolidTapered_ shall be supported.
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported

### Body Clipping Geometry

* _IfcExtrudedAreaSolid_, _IfcRevolvedAreaSolid_ shall be supported
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported
* All extrusion directions shall be supported.
* The _IfcBooleanClippingResult_ shall be supported, allowing for Boolean differences between the swept solid (here _IfcExtrudedAreaSolid_) and one or several _IfcHalfSpaceSolid_ (or its subtypes).

Figure 238 illustrates a 'Clipping' geometric representation with use of _IfcBooleanClippingResult_ between an _IfcExtrudedAreaSolid_ and an _IfcHalfSpaceSolid_ to create a clipped body.

![clipped member](../../../../figures/ifcmember_clipping-01.png)

Figure 238 — Member clipping

When an _IfcMaterialProfileSetUsage_ is applied, Figure 239 illustrates an advanced geometric representation with use of _IfcBooleanClippingResult_ between an _IfcExtrudedAreaSolid_ and an _IfcHalfSpaceSolid_ to create a clipped body, with cardinal point applied as 4 (mid-depth left).

![clipped beam](../../../../figures/ifcbeamstandardcase_clipping-01.png)

Figure 239 — Member body clipping

### Body SweptSolid Geometry

* _IfcExtrudedAreaSolid_, _IfcRevolvedAreaSolid_ shall be supported
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported
* All extrusion directions shall be supported.

When an _IfcMaterialProfileSetUsage_ is assigned to the _IfcMember_:

* For all single profiles, the _IfcParameterizedProfileDef.Position_ shall be NIL, or having _Location_ = 0.,0. and _RefDirection_ = 1.,0.
* The extrusion shall be perpendicular to the profile direction.
* The y-axis of the profile, as determined by _IfcSweptAreaSolid.Position.P[2]_ shall point to the Z-Axis. It indicates the "role" of the column, a role=0° means y-axis of profile = Z-axis of reference coordinate system. In the exception of a vertical member, the y-axis shall point to the Y-axis.

Figure 236 illustrates a 'SweptSolid' geometric representation with cardinal point applied as 1 (bottom left).

If parametric profiles are used, the parameters may be interpreted to be the dimensions of the beam:

* _IfcRectangleProfileDef.YDim_ interpreted as member width
* _IfcRectangleProfileDef.XDim_ interpreted as member depth
* _IfcCircleProfileDef.Radius_ interpreted as member radius.

![standard member](../../../../figures/ifcbeamstandardcase_sweptsolid-01.png)

Figure 236 — Member body extrusion

### Material Profile Set Usage

Figure 233 illustrates assignment of _IfcMaterialProfileSetUsage_ and _IfcMaterialProfileSet_ to the _IfcMemberType_ and the _IfcMember_ occurrence. Both the _IfcMaterialProfileSet_ and _IfcProfileDef_ is shared between all occurrences.

![Material profile set and usage](../../../../figures/ifcmember-01.png)

Figure 233 — Member profile usage

Figure 234 illustrates assignment of a composite profile by using _IfcCompositeProfileDef_ for geometric representation and several _IfcMaterialProfile_ entities within the _IfcMaterialProfileSet_.


![Material profile set and usage](../../../../figures/ifcmember-02.png)

Figure 234 — Member composite profiles

### Object Typing

### Product Assignment

#### IfcStructuralCurveMember

An idealized structural member corresponding to the member.

#### IfcTask

A task for operating on the member.

### Property Sets for Objects

### Quantity Sets

### Spatial Containment

The _IfcMember_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)
