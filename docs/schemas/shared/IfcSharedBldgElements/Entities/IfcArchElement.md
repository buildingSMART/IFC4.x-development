# IfcArchElement

The arch element is a curved structural element typically forming part of a tunnel lining ring, an underground excavation primary support, or other arched constructions. Arch elements are characterised by a sweep along a circular or near-circular arc and a section that may be precast (lining segments), rolled steel (ribs), or built-up assemblies.
<!-- end of short definition -->

{ .extDef}

An _IfcArchElement_ may participate in a tunnel ring assembly via _IfcRelAggregates_ when it is a lining _SEGMENT_, or stand alone as a _STEELRIB_ rib element placed along the tunnel axis. The geometry of an arch element is described by a swept-disk solid (cross-section swept along an arc directrix) or, for parametric placement, by a profile and a curved axis.

> NOTE The placement of an arch element is typically driven by alignment-based positioning (see _IfcRelPositions_) so that the ring or rib spacing follows the underlying tunnel alignment. For ad-hoc placements outside an alignment, use the standard _IfcLocalPlacement_ chain.

> NOTE For ring segments (_SEGMENT_), the longitudinal direction of the arch element is the tunnel axis; for steel ribs (_STEELRIB_), the longitudinal direction is along the rib itself (perpendicular to the tunnel axis). Quantity definitions (_Qto_ArchElementBaseQuantities.Length_) follow this convention.

> HISTORY New entity in IFC4.4.

## Attributes

### PredefinedType
Predefined generic type for an arch element specified as one of the _IfcArchElementTypeEnum_ literals. If the element is assigned an _IfcArchElementType_, the predefined type given on the type takes precedence.

> NOTE The _PredefinedType_ shall only be used if no _IfcArchElementType_ is assigned, providing its own _IfcArchElementType.PredefinedType_.

## Concepts

### Property Set Use Definition

The property sets relating to _IfcArchElement_ are defined by _IfcPropertySet_ and attached by an _IfcRelDefinesByProperties_. The following property set is part of this entity definition:

- _Pset_ArchElementCommon_: common properties applicable to every _IfcArchElement_
- _Pset_ArchElementTypeSegment_: applicable when _PredefinedType_ = _SEGMENT_
- _Pset_ArchElementTypeSteelRib_: applicable when _PredefinedType_ = _STEELRIB_

### Quantity Use Definition

The base quantities relating to _IfcArchElement_ are defined by _Qto_ArchElementBaseQuantities_, attached via _IfcRelDefinesByProperties_:

- _Length_, _Volume_, _CrossSectionArea_, _OuterSurfaceArea_, _InnerSurfaceArea_

### Material Use Definition

The material of an _IfcArchElement_ is defined by _IfcMaterialProfileSetUsage_ (for parametric arched profiles) or by an _IfcMaterial_ attached directly via _IfcRelAssociatesMaterial_ (for as-built segments where the profile is implicit in the geometry).
