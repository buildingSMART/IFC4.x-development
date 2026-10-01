# IfcBridge

A Bridge is a civil engineering work that affords passage to pedestrians, animals, vehicles, and services above obstacles or between two points at a height above ground.
<!-- end of short definition -->

> NOTE Definition from ISO 6707-1:2014:
> Civil engineering works that affords passage to pedestrians, animals, vehicles, and services above obstacles or between two points at a height above ground.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED or _PredefinedType_.

## Concepts

### Body Geometry

### Object Predefined Type

### Product Local Placement

The local placement for IfcBridge is defined in its supertype _IfcProduct_. It is defined by _IfcLocalPlacement_ or by _IfcLinearPlacement_ which defines the local coordinate system that is referenced by all geometric representations.

* The *PlacementRelTo* relationship of _IfcLocalPlacement_ shall point (if relative placement is used) to the IfcSpatialStructureElement containing the bridge (if available).
* Linear placement can be used to place the bridge at a specific distance along a (alignment) curve.
* If neither relative placement nor linear placement is, the absolute placement is defined within the world coordinate system by means of a local placement PlacementRelTo set to be undefined.

### Property Sets for Objects

### Property Sets for Objects

### Spatial Composition

> NOTE By using the inverse relationship _IfcBridge.Decomposes_ it references _IfcProject_ || _IfcSite_ || _IfcBridge_ through _IfcRelAggregates.RelatingObject_. If it refers to another instance of _IfcBridge_, the referenced _IfcBridge_ needs to have a different and higher *CompositionType*, i.e. COMPLEX (if the other _IfcBridge_ has ELEMENT), or ELEMENT (if the other _IfcBridge_ has PARTIAL).

#### IfcProject

Direct assignment to project, if the bridge is the outermost spatial container, and no site information is provided for bridge projects.

#### IfcSite

Assignment to site, if the bridge is the spatial container for the bridge project with site information.

#### IfcBridge

Assignment to another bridge as spatial container, e.g. if this bridge represents a bridge section.

### Spatial Container

> NOTE If there are building elements and/or other elements directly related to the _IfcBridge_, they are associated with the _IfcBridge_ by using the objectified relationship _IfcRelContainedInSpatialStructure_. The _IfcBridge_ references them by its inverse relationship:
> * _IfcBridge.ContainsElements_ -- referencing any subtype of _IfcProduct_ (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

#### IfcElement

Physical elements that are directly related to the bridge.

#### IfcAnnotation

Annotations that are directly related to the bridge.

#### IfcPositioningElement

Positioning elements that are directly related to the bridge.

### Spatial Decomposition

> NOTE By using the inverse relationship _IfcBridge.IsDecomposedBy_ it references _IfcBridge_ || _IfcBridgePart_ through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of _IfcBridge_, the referenced _IfcBridge_ needs to have a different and lower *CompositionType*, i.e. ELEMENT (if the other _IfcBridge_ has COMPLEX), or PARTIAL (if the other _IfcBridge_ has ELEMENT).

#### IfcBridgePart

Spatial decomposition into bridge parts.

#### IfcBridge

Spatial decomposition into other bridges, e.g. if this bridge represents a complex bridge that is subdivided into bridge sections.


### Spatial Service Connectivity
