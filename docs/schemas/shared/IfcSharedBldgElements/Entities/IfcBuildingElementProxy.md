# IfcBuildingElementProxy

The _IfcBuildingElementProxy_ is a proxy definition that provides the same functionality as subtypes of _IfcBuiltElement_, but without having a predefined meaning of the special type of building element it represents.
<!-- end of short definition -->

_IfcBuildingElementProxy_ may be used:

* To exchange special types of building elements for which the current specification does not yet provide a semantic definition.
* To represent building elements for which the participating applications can not provide a semantic definition.

> HISTORY  New entity in IFC2x.

> IFC4.3.0.0 CHANGE _IfcBuildingElementProxy_ should no longer be used as spatial placeholders or provisions. Use _IfcVirtualElement_ instead.

> NOTE  It is advised not to use _IfcBuildingElementProxy_ to represent an arbitrary built element, but to use a direct instantiation of _IfcBuiltElement_ instead.


## Attributes

### PredefinedType
Predefined generic type for a building element proxy that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE The _PredefinedType_ shall only be used, if no _IfcBuildingElementProxyType_ is assigned, providing its own _IfcBuildingElementProxyType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute _CompositionType_ has been replaced by _PredefinedType_, being a superset of the enumerators.

## Formal Propositions

### HasObjectName
A _Name_ attribute should be asserted for a building element proxy.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBuildingElementProxyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no building element proxy type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBuildingElementProxyType_.

## Concepts

### Object Typing

> NOTE The _IfcBuildingElementProxyType_ can be used to share common information among many occurrences of the same proxy without establishing a particular semantic meaning of the type.

If no _IfcBuildingElementProxyType_ is attached (i.e. if only occurrence information is available) the _PredefinedType_ should be provided. If set to USERDEFINED a user defined value has to be provided by the _ObjectType_ attribute.

### Property Sets for Objects



### Spatial Containment

The _IfcBuildingElementProxy_, as any subtype of _IfcBuiltElement_, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

