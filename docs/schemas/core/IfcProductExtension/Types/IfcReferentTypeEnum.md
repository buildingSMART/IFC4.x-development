# IfcReferentTypeEnum

This enumeration defines the different types of referents.
<!-- end of short definition -->

## Items

### KILOPOINT
Kilo point.

### MILEPOINT
Mile point.

### STATION
Station.

### REFERENCEMARKER
The reference marker is a notation referent, typically located in the right of way of the road, rail or other transportation system. Usually reference markers are initially spaced at a uniform distance along the linear element being measured, though subsequent re-alignments can result in uneven spacing between the markers.

> NOTE definition from ISO 19148:2021

> NOTE The physical manifestation of the _IfcReferent.REFERENCEMARKER_ can be an _IfcSign.MARKER_ (e.g., a bolt fixed on a post)

### LANDMARK
The referent is the location of a physical landmark visible in the field.

> NOTE definition from ISO 19148:2021

### BOUNDARY
The referent represents where an administrative or maintenance boundary crosses the linear element being measured. This is typically the first time the boundary crosses the linear element. If the boundary runs along the linear element, it would be the point at which they first become collinear. The LRS (linear referencing system) should include specific rules about how boundaries are handled if this type of referent is permitted. If the linear element changes at the boundary as for a county route beginning at the county boundary, then the LRM (linear referencing method) is more correctly categorized as absolute.

> NOTE definition from ISO 19148:2021

### INTERSECTION
The referent is the location of an intersection specified by the referent name. The intersection location is typically taken as the location of the intersection of the reference lines of the streets comprising the intersection and is, therefore, not necessarily precise or deterministic. Physical markers can be installed to remedy this. The LRS (linear referencing system) should include specific rules about how intersection locations are determined if this type of referent is permitted.

> NOTE definition from ISO 19148:2021

### POSITION
Used to fully describe a linearly referenced location given by the linear element being measured (the _IfcAlignment_ into which the _IfcReferent_ is nested), the method of measurement (_Pset_LinearReferencingMethod_) and a measure value (_Pset_Stationing_). If a linear referencing method is specified for the position, it overrides any linear referencing method specified for the alignment.

### WIDTHEVENT
A kind of event that specifies the width at a specific location along a road alignment, and the type of transition from the previous location. The locations are specified using an IfcLinearPlacement measured along the alignment axis curve.
The element(s) that are affected by the width event is currently proposed to be specified by containing the event in a specific lateral breakdown element of the road spatial structure (e.g. a Lane or the entire carriageway).

### SUPERELEVATIONEVENT
A kind of event that specifies the superelevation (cross slope) at a specific location along a road alignment, and the type of transition from the previous location. The locations are specified using an IfcLinearPlacement measured along the alignment axis curve.

The element(s) that are affected by the superelevation event is currently proposed to be specified by containing the event in a specific lateral breakdown element of the road spatial structure (e.g. a Lane).

### USERDEFINED
User defined.

### NOTDEFINED
Undefined.
