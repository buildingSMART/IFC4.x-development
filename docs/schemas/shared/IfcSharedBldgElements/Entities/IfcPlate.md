# IfcPlate

An _IfcPlate_ is a planar and often flat part with constant thickness. A plate may carry loads between or beyond points of support, or provide stiffening. The location of the plate (being horizontal, vertical or sloped) is not relevant to its definition.
<!-- end of short definition -->

Plates are normally made of steel, other metallic material, or by glass panels. However the definition of _IfcPlate_ is material independent and specific material information shall be handled by using _IfcRelAssociatesMaterial_ to assign a material specification to the _IfcPlate_.

Plates are often add-on parts. This is represented by the _IfcRelAggregates_ decomposition mechanism used to aggregate parts, such as _IfcPlate_, into a container element such as _IfcElementAssembly_ or _IfcCurtainWall_.

An instance of _IfcPlate_ should preferably get its geometric representation and material assignment through the type definition by _IfcPlateType_ assigned using the _IfcRelDefinesByType_ relationship. This allows identical plates in a construction to be represented by the same instance of _IfcPlateType_.

A plate may have openings, such as voids or recesses. They are defined by an _IfcOpeningElement_ attached to the plate using the inverse relationship _HasOpenings_ pointing to _IfcRelVoidsElement_. The position number of a plate as often used in steel construction is assigned through the attribute _IfcElement.Tag_

There are two main representations for plate occurrences:

 * _IfcPlate_ with _IfcMaterialLayerSetUsage_ is used for all occurrences of plates, that are prismatic and where the thickness parameter can be fully described by the _IfcMaterialLayerSetUsage_. These plates are always represented geometrically by a 'SweptSolid' geometry (or by a 'Clipping' geometry based on 'SweptSolid'), if a 3D geometric representation is assigned.
 * _IfcPlate_ without _IfcMaterialLayerSetUsage_ is used for all other occurrences of plates, particularly for plates with changing thickness, or plates with non planar surfaces, and plates having only 'SurfaceModel' or 'Brep' geometry or if a more parametric representation is not intended.

> REFERENCE Definition according to ISO 6707-1: thin, rigid, flat, metal product, of a thickness greater than that of a sheet.

> NOTE The representation of a plate in a structural analysis model is provided by _IfcStructuralSurfaceMember_ being part of an _IfcStructuralAnalysisModel_.

> HISTORY New entity in IFC2x2

## Attributes

### PredefinedType
Predefined generic type for a plate that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcPlateType_ is assigned, providing its own _IfcPlateType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPlateType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no plate type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPlateType_.

## Concepts

### Body Clipping Geometry

* _IfcExtrudedAreaSolid_ is required,
* _IfcArbitraryClosedProfileDef_, _IfcArbitraryProfileDefWithVoids_, _IfcRectangleProfileDef_, _IfcCircleProfileDef_, _IfcEllipseProfileDef_ shall be supported.
* The profile can be extruded perpendicularly or non-perpendicularly to the plane of the swept profile.
* The definition of the _IfcMaterialLayerSetUsage_, particularly of the _OffsetFromReferenceLine_ and the _ForLayerSet.TotalThickness_, has to be consistent to the 'SweptSolid' representation.
* The _IfcBooleanClippingResult_ shall be supported, allowing for Boolean differences between the swept solid (here _IfcExtrudedAreaSolid_) and one or several _IfcHalfSpaceSolid_.

Figure 248 illustrates a 'Clipping' geometric representation with definition of a plate using advanced geometric representation. The profile is extruded non-perpendicular and the plate body is clipped at the eave.

![advanced plate](../../../../figures/ifcslab_advanced-layout1.gif)

Figure 248 — Plate body clipping

### Body SweptSolid Geometry

* _IfcExtrudedAreaSolid_ is required,
* _IfcArbitraryClosedProfileDef_, _IfcArbitraryProfileDefWithVoids_, _IfcRectangleProfileDef_, _IfcCircleProfileDef_, _IfcEllipseProfileDef_ shall be supported.
* The profile can be extruded perpendicularly or non-perpendicularly to the plane of the swept profile.

Figure 247 illustrates a 'SweptSolid' geometric representation. The following interpretation of dimension parameter applies for polygonal plates (in ground floor view): _IfcArbitraryClosedProfileDef.OuterCurve_ being a closed bounded curve is interpreted as area (or foot print) of the plate.

![standard plate](../../../../figures/ifcslab_standard-layout1.gif)

Figure 247 — Plate body extrusion

### Material Layer Set Usage

Figure 277 illustrates assignment of _IfcMaterialLayerSetUsage_ and _IfcMaterialLayerSet_ to the _IfcPlateType_ and the _IfcPlate_ occurrence.

![Material layer set and usage](../../../../figures/ifcplate_materialusage-01.png) 

Figure 277 — Plate type definition

Figure 247 illustrates material layer usage, where:

* The reference coordinate system is the coordinate system established by the _IfcExtrudedAreaSolid.Position_.
* The reference plane is the plane defined by the extruded profile of _IfcExtrudedAreaSolid.SweptSolid_. The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is given as a distance from this plane.
* The _IfcMaterialLayerSetUsage.DirectionSense_ defines how the _IfcMaterialLayer_'s are assigned to the reference plane. POSITIVE means in direction to the positive z-axis of the reference coordinate system.
* The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is the distance parallel to the reference plane and always perpendicular to the base (XY) plane of the reference coordinate system. This is independent of a potential non-perpendicular extrusion given by _IfcExtrudedAreaSolid.ExtrudedDirection_ <> 0.,0.,1. A positive value of _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ would then point into the positive z-axis of the reference coordinate system.
* The _Thickness_ of each _IfcMaterialLayer_ shall be the parallel distance (measured perpendicular to the base plane). The _TotalThickness_ of the _IfcMaterialLayerSet_ is the sum of all layer thicknesses and in case of a perpendicular extrusion identical with _IfcExtrudedAreaSolid.Depth_
* The _IfcMaterialLayerSetUsage.LayerSetDirection_ is always AXIS3.
* The local placement of the wall uses the the x/y plane for the profile, and the z-axis as the extrusion direction for the wall body.

![plate material layer set](../../../../figures/ifcmateriallayersetusage_slab-01.png)

Figure 247 — Plate material layers


### Object Typing



### Product Assignment



#### IfcStructuralSurfaceMember

An idealized structural member corresponding to the plate.

#### IfcTask

A task for operating on the plate.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcPlate_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

### Surface 3D Geometry

The 'Surface' can be used to define a surfacic model of the building (e.g. for analytical purposes, or for reduced Level of Detail representation).

