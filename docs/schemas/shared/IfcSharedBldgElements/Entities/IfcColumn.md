# IfcColumn

An _IfcColumn_ is a vertical structural or architectural member which often is aligned with a structural grid intersection. In most cases it represents a vertical, or nearly vertical, structural member that transmits, through compression, the weight of the structure above to other structural elements below. It may also represent such a member from an architectural point of view in which case it may represent a non load bearing element.
<!-- end of short definition -->

 Whether it is a structural load bearing element or a non-load bearing element is determined by the _Pset\_ColumnCommon.LoadBearing_ property.


There are two main representations for column occurrences:

 * _IfcColumn_ with _IfcMaterialProfileSetUsage_ is used for all occurrences of columns, that have a profile defined that is swept along a directrix. The profile might change uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These columns are always represented geometricly by an 'Axis' and a 'SweptSolid' or 'AdvancedSweptSolid' shape representation (or by a 'Clipping' geometry based on the swept solid), if a 3D geometric representation is assigned.
 * _IfcColumn_ is used for all other occurrences of columns, particularly for columns with changing profile sizes along the extrusion, or columns defined by non-linear extrusion, or columns having only 'Brep', or 'SurfaceModel' geometry, if a more parametric representation is not intended.


For any longitudial structural member, not constrained to be predominately horizontal nor vertical, or where this semantic information is irrelevant, the entity _IfcMember_ exists.

> REFERENCE Definition according to ISO 6707-1 structural member of slender form, usually vertical, that transmits to its base the forces, primarily in compression, that are applied to it.

> NOTE The entity _IfcColumnStandardCase_ has been deleted, _IfcColumn_ with _IfcMaterialProfileSetUsage_ is used instead.

> NOTE The representation of a column in a structural analysis model is provided by _IfcStructuralCurveMember_ being part of an _IfcStructuralAnalysisModel_.

> HISTORY New entity in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a column that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcColumnType_ is assigned, providing its own _IfcColumnType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcColumnType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no column type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcColumnType_.

## Concepts

### Axis 3D Geometry

The axis representation can be used to represent the fundamental orientation and extents of a column's body.

If an _IfcMaterialProfileSetUsage_ is used, the axis representation is used to locate the profile. In addition:

 * For a body representation using an _IfcExtrudedAreaSolid_, the axis may be an _IfcPolyline_ having two Points, or _IfcTrimmedCurve_ with _BasisCurve_ of type _IfcLine_. The axis curve lies on the z axis of the object coordinate system.
 * For a body representation using an _IfcRevolvedAreaSolid_, the axis may be an _IfcTrimmedCurve_ with _BasisCurve_ of type _IfcCircle_. The axis curve lies on the x/z plane of the object coordinate system, the tangent at the start is along the positive z-axis.

As shown in Figure COLAXREP, the axis shall be defined along the z axis of the object coordinate system.

![Axis](../../../../figures/ifccolumnstandardcase_axis-01.png)

Figure COLAXREP — Column axis representation

As shown in Figure CALAXCARPOINT, the axis representation must be positioned at the _IfcMaterialProfileSetUsage_._CardinalPoint_, and parallel to the _IfcExtrudedAreaSolid_._ExtrudedDirection_. This offset between the axis line and the _IfcExtrudedAreaSolid_._Position_ must correlate with the chosen _IfcMaterialProfileSetUsage_._CardinalPoint_.

![Axis](../../../../figures/ifccolumnstandardcase_axis-02.png)

Figure CALAXCARPOINT — Column axis cardinal point

#### Axis_IfcBoundedCurve_Curve3D

Three-dimensional reference curve for the column.

### Body AdvancedSweptSolid Geometry

* _IfcSurfaceCurveSweptAreaSolid_, _IfcFixedReferenceSweptAreaSolid_, _IfcExtrudedAreaSolidTapered_, _IfcRevolvedAreaSolidTapered_ shall be supported.
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported

### Body Clipping Geometry

* _IfcExtrudedAreaSolid_, _IfcRevolvedAreaSolid_ shall be supported
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported
* All extrusion directions shall be supported
* The _IfcBooleanClippingResult_ shall be supported, allowing for Boolean differences between the swept solid (here _IfcExtrudedAreaSolid_) and one or several _IfcHalfSpaceSolid_.

Figure COLCLIP illustrates a 'Clipping' geometric representation with use of _IfcBooleanClippingResult_ between an _IfcExtrudedAreaSolid_ and an _IfcHalfSpaceSolid_ to create a clipped body.

![advanced column](../../../../figures/ifccolumn_advanced-2-layout1.png)

Figure COLCLIP — Column clipping

### Body SweptSolid Geometry

* _IfcExtrudedAreaSolid_, _IfcRevolvedAreaSolid_ shall be supported
* All subtypes of _IfcProfileDef_ (with exception of _IfcArbitraryOpenProfileDef_) shall be supported
* All extrusion directions shall be supported

Figure COLSWEEP illustrates a 'SweptSolid' geometric representation. There are no restrictions or conventions on how to use the object placement (black), extrusion placement (red) and profile placement (green).


![standard column](../../../../figures/ifccolumn_standard-layout1.gif)

Figure COLSWEEP — Column swept solid

Figure COLEXI illustrates use of a special profile type (here _IfcIShapeProfileDef_) for the definition of the _IfcExtrudedAreaSolid_.

![advanced column](../../../../figures/ifccolumn_advanced-1-layout1.png)

Figure COLEXI — Column extrusion of I-Shape

### Material Profile Set Usage

Figure COLPROFUS illustrates assignment of _IfcMaterialProfileSetUsage_ and _IfcMaterialProfileSet_ to the _IfcColumnType_ and the _IfcColumn_ occurrence. Both the _IfcMaterialProfileSet_ and _IfcProfileDef_ is shared between all occurrences.

![Material profile set and usage](../../../../figures/ifccolumn-01.png)

Figure COLPROFUS — Column profile usage

Figure COLCARPOINTS illustrates cardinal point alignment. The use of _IfcCardinalPointEnum_ must be consistent with the placement of the extrusion body provided by _IfcExtrudedAreaSolid_._Position_.

![Cardinal point usage](../../../../figures/ifccolumn_cardinalpoint.png)

Figure COLCARPOINTS — Column cardinal points

Figure COLCOMPPROF illustrates assignment of a composite profile by using _IfcCompositeProfileDef_ for geometric representation and several _IfcMaterialProfile_ entities within the _IfcMaterialProfileSet_.

![Material profile set and usage](../../../../figures/ifccolumn-02.png)

Figure COLCOMPPROF — Column composite profiles

### Object Typing

### Product Assignment

#### IfcStructuralCurveMember

An idealized structural member corresponding to the column.

#### IfcTask

A task for operating on the column.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcColumn_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)
