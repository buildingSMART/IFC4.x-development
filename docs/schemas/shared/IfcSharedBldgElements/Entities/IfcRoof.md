# IfcRoof

A roof is the covering of the top part of a building, it protects the building against the effects of weather.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: construction enclosing the building from above.

The _IfcRoof_ shall either be represented:

* as a roof assembly that aggregates all parts (slabs, rafters and purlins, or other included roofs, such as dormers) with own shape representation, or
* as a single roof without decomposition including all shape representations directly at the roof entity.

> NOTE In case of an _IfcRoof_ being the assembly of all parts of the roof the aggregation is handled by the _IfcRelAggregates_ relationship, relating an _IfcRoof_ with the related roof elements, like slabs (represented by _IfcSlab_), rafters and purlins (represented by _IfcBeam_), or other included roofs, such as dormers (represented by _IfcRoof_).

> NOTE Model View Definitions and implementer agreements may restrict the _IfcRoof_ being an assembly to not have an independent shape representation, but to always require that the decomposed parts have a shape representation. In this case, at least the 'Body' geometric representations shall not be provided directly at _IfcRoof_ if it is an assembly. The 'Body' geometric representation of the _IfcRoof_ is then the sum of the 'Body' shape representation of the parts within the decomposition structure.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE Attribute _ShapeType_ renamed to _PredefinedType_.

## Attributes

### PredefinedType
Predefined generic types for a roof that are specified in an enumeration. There may be a property set given for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcRoofType_ is assigned, providing its own _IfcRoofType.PredefinedType_.

> IFC4 CHANGE The attribute has been renamed from _ShapeType_ and changed to be OPTIONAL with upward compatibility for file based exchange.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcRoofType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no roof type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcRoofType_.

## Concepts

### Element Decomposition

_Geometric representation by aggregated elements_

If the _IfcRoof_ has components (referenced by _SELF\IfcObject.IsDecomposedBy_) then no independent geometric representation shall be defined for the _IfcRoof_. The _IfcRoof_ is then geometrically represented by the geometric representation of its components. The components are accessed via _SELF\IfcObject.IsDecomposedBy[1].RelatedObjects_. The geometric representations that are supported for the aggregated elements are defined with each element. See geometric use definition for _IfcSlab_, _IfcBeam_, _IfcColumn_, _IfcBuildingElementPart_ and other subtypes of _IfcBuiltElement_.

Figure 260 illustrates roof placement, with an _IfcRoof_ defining the local placement for all aggregated elements.


![roof](../../../../figures/ifcroof-layout1.gif)
Figure 260 — Roof placement

#### IfcSlab

A roof may be aggregated into slabs for each face.

### Object Typing



### Product Local Placement

The following restriction may be imposed by view definitions or implementer agreements:

* If the _IfcRoof_ establishes an aggregate, then all contained elements shall be placed relative to the _IfcRoof.ObjectPlacement_.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment



#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

