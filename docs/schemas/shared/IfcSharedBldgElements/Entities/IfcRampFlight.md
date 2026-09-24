# IfcRampFlight

A ramp comprises a single inclined segment, or several inclined segments that are connected by a horizontal segment, referred to as a landing. A ramp flight is the single inclined segment and part of the ramp construction. In case of single flight ramps, the ramp flight and the ramp are identical.
<!-- end of short definition -->

> NOTE A single flight ramp is represented by an _IfcRamp_ instance without using aggregation and by utilizing the product shape representation directly at _IfcRamp_.

An _IfcRampFlight_ is an aggregated part of an _IfcRamp_ realized through the _IfcRelAggregates_ relationship, the ramp flight is therefore included in the set of _IfcRelAggregates.RelatedObjects_.

An _IfcRampFlight_ connects the floor slab of zero to two different storeys (or partial storeys or landings) within a building. The connection relationship between the _IfcRampFlight_ and the _IfcSlab_ can be expressed using the _IfcRelConnectsElements_ relationship.

> HISTORY New entity in IFC2.0.

## Attributes

### PredefinedType
Predefined generic type for a ramp flight that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcRampFlightType_ is assigned, providing its own _IfcRampFlightType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcRampFlightType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no ramp flight type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcRampFlightType_.

## Concepts

### Axis 2D Geometry

The walking line is represented by a two-dimensional open curve as the axis. The curve is directed into the upward direction (direction has to be interpreted as specified at the subtypes of _IfcCurve_).

Figure 254 illustrates the axis representation which has the following constraints:

* In case of straight flights the curve shall be a single item of type _IfcPolyline_.
* In case of winding flights the curve shall be a single item of type _IfcCompositeCurve_.
* In case of a curved flight or a spiral flight the curve shall be a single item of type _IfcTrimmedCurve_.

![walking line](../../../../figures/ifcstairflight_01-layout1.gif)
Figure 254 — Ramp flight axis

### Body Clipping Geometry



### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation type:

* **Solid**: _IfcExtrudedAreaSolid_ is required,
* **Profile**: _IfcRectangleProfileDef_ and _IfcArbitraryClosedProfileDef_ shall be supported.
* **Extrusion**: The profile shall be extruded in any direction relative to the XY plane of the position coordinate system of the _IfcExtrudedAreaSolid_. Therefore non-perpendicular sweep operation has to be supported. It might be further constrained to be in the direction of the global z-axis in implementers agreements.

Figure 256 illustrates the body representation.

![fig1](../../../../figures/ifcrampflight-layout1.gif)
Figure 256 — Ramp flight body

### FootPrint Geometry

The flight foot print, including the flight boundary is represented by a two-dimensional geometric curve set.

Figure 255 illustrates the footprint representation which has the following constraints:

* In case of straight flights the curve set shall consist of a single item of type _IfcPolyline_.
* In case of winding flights or curved flights the curve set shall consist of a single item of type _IfcCompositeCurve_.
* In case of a spiral flight the curve set shall consist of a single item of type _IfcConic_ or _IfcPolyline_.

![boundary](../../../../figures/ifcstairflight_02-layout1.gif)
Figure 255 — Ramp flight footprint

### Material Single

The material of the _IfcRampFlight_ is defined by the _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcRampFlight_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

> NOTE Model view definitions or implementer agreements may force an IfcRampFlight to be solely used as a part within an _IfcRamp_ container. In this case, no _Spatial containment_ shall be used.

#### IfcBuildingStorey

Default spatial container, if the ramp flight is not used (by default) as a part within a ramp container.

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

