# IfcChimney

Chimneys are typically vertical, or as near as vertical, parts of the construction of a building and part of the building fabric. Often constructed by pre-cast or insitu concrete, today seldom by bricks. Chimneys are used to evacuate flues from e.g. boilers or fire places.
<!-- end of short definition -->

> NOTE Definition according to ISO 6707-1: construction containing one or more flues.
> Flue: Duct designed to convey the products of combustion to the open air.
> Chimney stack: Part of the chimney that projects above a roof.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Predefined generic type for a chimney that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcChimneyType_ is assigned, providing its own _IfcChimneyType.PredefinedType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcChimneyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no chimney type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcChimneyType_.

## Concepts

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcChimney_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container (in most cases the storey where the base of the chimney is placed)

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

