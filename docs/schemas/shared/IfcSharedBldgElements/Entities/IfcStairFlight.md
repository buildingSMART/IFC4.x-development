# IfcStairFlight

A stair flight is an assembly of building components in a single "run" of stair steps (not interrupted by a landing). The stair steps and any stringers are included in the stair flight. A winder is also regarded a part of a stair flight.
<!-- end of short definition -->

An _IfcStairFlight_ is normally aggregated by an _IfcStair_ through the _IfcRelAggregates_ relationship, the stair flight is then included in the set of _IfcRelAggregates.RelatedObjects_. An _IfcStairFlight_ normally connects the floor slab of zero to two different storeys (or partial storeys, or landings) within a building. The connection relationship between the _IfcStairFlight_ and the _IfcSlab_ can be expressed using the _IfcRelConnectsElements_ relationship.

> HISTORY New entity in IFC2.0.

## Attributes

### NumberOfRisers
Number of the risers included in the stair flight
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfRisers_ instead.

### NumberOfTreads
Number of treads included in the stair flight.
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfTreads_ instead.

### RiserHeight
Vertical distance from tread to tread. The riser height is supposed to be equal for all stairs in a stair flight.

> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.RiserHeight_ instead.

### TreadLength
Horizontal distance from the front to the back of the tread. The tread length is supposed to be equal for all steps of the stair flight.

> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.TreadLength_ instead.

### PredefinedType
Predefined generic type for a stair flight that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcStairFlightType_ is assigned, providing its own _IfcStairFlightType.PredefinedType_.

> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcStairFlightType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no stair flight type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcStairFlightType_.

## Concepts

### Axis 2D Geometry

The walking line is represented by a two-dimensional open curve as the axis. The curve is directed into the upward direction (direction has to be interpreted as specified at the subtypes of _IfcCurve_).

Figure 273 illustrates the axis representation which has the following constraints:

* In case of straight flights the curve shall be a single item of type _IfcPolyline_.
* In case of winding flights the curve shall be a single item of type _IfcCompositeCurve_.
* In case of a curved flight or a spiral flight the curve shall be a single item of type _IfcTrimmedCurve_.

![walking line](../../../../figures/ifcstairflight_01-layout1.gif)
Figure 273 — Stair flight axis

### Body SweptSolid Geometry

Figure 275 illustrates the 'Body' geometric representation using a 'SweptSolid' representation type.


![3D](../../../../figures/ifcstairflight_03-layout1.gif)
Figure 275 — Stair flight body

### FootPrint Geometry

The flight foot print, including the flight boundary is represented by a two-dimensional geometric curve set.

Figure 274 illustrates the footprint representation which has the following constraints:

* In case of straight flights the curve set shall consists of a single item of type _IfcPolyline_.
* In case of winding flights or curved flights the curve set shall consists of a single item of type _IfcCompositeCurve_.
* In case of a spiral flight the curve set shall consists of a single item of type _IfcConic_ or _IfcPolyline_.

![boundary](../../../../figures/ifcstairflight_02-layout1.gif)
Figure 274 — Stair flight footprint

### Material Single

The material of the _IfcStairFlight_ is defined by the _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcStairFlight_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

> NOTE Model view definitions or implementer agreements may force an _IfcStairFlight_ to be solely used as a part within an _IfcStair_ container. In this case, no _Spatial containment_ shall be used.

#### IfcBuildingStorey

Default spatial container, if the stair flight is not used (by default) as a part within a stair container.

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey.

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

