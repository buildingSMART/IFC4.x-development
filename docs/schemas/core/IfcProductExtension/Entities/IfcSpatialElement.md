# IfcSpatialElement

A spatial element is the generalization of all spatial elements that might be used to define a spatial structure or to define spatial zones.
<!-- end of short definition -->

* a hierarchical spatial structure element as _IfcSpatialStructureElement_
  * a spatial structure is a hierarchical decomposition of the project. That spatial structure is often used to provide a project structure to organize a project.
  * a spatial project structure might define as many levels of decomposition as necessary for the project. Some examples of elements within the spatial breakdown can be: site, building, storey, space. And for infrastructure projects also: bridge, railway, road, ports, tunnel and parts of them.
* a spatial zone as _IfcSpatialZone_
  * a spatial zone is a non-hierarchical and potentially overlapping decomposition of the project under some functional consideration.
  * a spatial zone might be used to represent a thermal zone, a lighting zone, a usable area zone.
  * a spatial zone might be used to represent a horizontal spatial structure as used in civil works.
  * a spatial zone might have its independent placement and shape representation.

> HISTORY New entity in IFC4.

## Attributes

### LongName
Long name for a spatial structure element, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE In many scenarios the _Name_ attribute refers to the short name or number of a spatial element, and the _LongName_ refers to the full descriptive name.

### ContainsElements
Set of spatial containment relationships, that holds those elements, which are contained within this element of the project spatial structure.
> NOTE The spatial containment relationship, established by _IfcRelContainedInSpatialStructure_, is required to be an hierarchical relationship, where each element can only be assigned to 0 or 1 spatial structure element.

### ServicedBySystems
Set of relationships to systems, that provides a certain service to the spatial element for which it is defined. The relationship is handled by the objectified relationship _IfcRelServicesBuildings_.
> IFC4 CHANGE The inverse attribute has been promoted to the new supertype _IfcSpatialElement_ with upward compatibility for file based exchange.

### ReferencesElements
Set of spatial reference relationships, that holds those elements, which are referenced, but not contained, within this element of the project spatial structure.
> NOTE The spatial reference relationship, established by _IfcRelReferencedInSpatialStructure_, is not required to be an hierarchical relationship, i.e. each element can be assigned to 0, 1 or many spatial structure elements.

> EXAMPLE A curtain wall maybe contained in the ground floor, but maybe referenced in all floors, it reaches.

> IFC2x3 CHANGE The inverse attribute has been added with upward compatibility for file based exchange.

> Ø\X

### IsInterferedByElements
Reference to the interference relationship to indicate the spatial element that is interfered. The relationship, if provided, indicates that this spatial element has an interference with one or many other spatial elements.
> NOTE There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_. Orientated interference is defined by _IfcRelInterferesElements.ImpliedOrder_ or _IfcRelInterferesElements.InterferenceType_.

> IFC4x3 CHANGE New inverse relationship.

### InterferesElements
Reference to the interference relationship to indicate the spatial element that interferes. The relationship, if provided, indicates that this spatial element has an interference with one or many other spatial elements.
> NOTE There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_. Orientated interference is defined by _IfcRelInterferesElements.ImpliedOrder_ or _IfcRelInterferesElements.InterferenceType_.

> IFC4x3 CHANGE New inverse relationship.

## Concepts

### Body Geometry

A spatial element will not usually provide a body geometry, instead relying on its constituting elements. A body geometry may be provided if it is necessary to expose an independent geometric representation. This geometry is typically expressed by its exterior elements or volume boundary.

### FootPrint GeomSet Geometry



#### FootPrint_IfcGeometricCurveSet_GeometricCurveSet

Set of curves (outer and inner) representing the floor projection,

### Group Spatial Connectivity



### Property Sets for Objects



### Spatial Interference



### Spatial Interference With Zones



