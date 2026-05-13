# IfcArchElementTypeEnum

This enumeration defines the different predefined types of an arch element that can further specify an _IfcArchElement_ or _IfcArchElementType_.
<!-- end of short definition -->

> HISTORY New enumeration in IFC4.4.

## Items

### LINING
A continuous arched lining placed in-situ (cast or sprayed), or a segment whose extents cover the full arch span without circumferential joints. Distinguished from _SEGMENT_ in that the lining is monolithic at the cross-section level.

### SEGMENT
A precast or pre-fabricated lining segment forming one element of a tunnel ring. Multiple _SEGMENT_ instances are aggregated by _IfcRelAggregates_ into a ring assembly. Segments have explicit longitudinal and radial joint properties documented in _Pset_ArchElementTypeSegment_.

### STEELRIB
A steel rib (typically a rolled section such as HEB, IPE, or specialised tunnel-rib profiles like TH/T) installed as an arched primary support. Common in NATM (New Austrian Tunnelling Method) and sequential excavation applications. Spacing between consecutive ribs is documented in _Pset_ArchElementTypeSteelRib_.

### USERDEFINED
User-defined arch element type. When set, an _ObjectType_ (on the occurrence) or _ElementType_ (on the type) must be provided to convey the specific intent.

### NOTDEFINED
Undefined arch element type.
