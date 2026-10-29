# IfcGeometricRepresentationItem

An _IfcGeometricRepresentationItem_ is the common supertype of all geometric items used within a representation. It is positioned within a geometric coordinate system, directly or indirectly through intervening items.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An geometric representation item is a representation item that has the additional meaning of having geometric position or orientation or both. This meaning is present by virtue of:
>
> * being a Cartesian point or a direction
> * referencing directly a Cartesian point or direction
> * referencing indirectly a Cartesian point or direction

An indirect reference to a Cartesian point or direction means that a given geometric item references the Cartesian point or direction through one or more intervening geometry or topology items.
>
>> EXAMPLE 1 Consider a circle. It gains its geometric position and orientation by virtue of a reference to axis2_placement (_IfcAxis2Placement_) that is turn references a cartesian_point (_IfcCartesianPoint_) and several directions (_IfcDirection_).
>> EXAMPLE 2 Consider a manifold brep. A manifold_solid_brep (_IfcManifoldSolidBrep_) is a geometric_representation_item (_IfcGeometricRepresentationItem_) that through several layers of topological_representation_item's (_IfcTopologicalRepresentationItem_) references poly loops (_IfcPolyLoop_). Through additional intervening entities poly loops reference cartesian_point's (_IfcCartesianPoint_).


>
> NOTE Entity adapted from **geometric_representation_item** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5
