# IfcFootingTypeEnum

Enumeration defining the generic footing type.
<!-- end of short definition -->

> HISTORY New type in IFC2x2

> IFC 2x4 CHANGE: Item CAISSON_FOUNDATION added.

## Items

### CAISSON_FOUNDATION
A foundation construction type used in underwater construction.

> IFC4x2 CHANGE Enum made optional and deprecated. Use the dedicated class _IfcCaissonFoundation_ instead.

### FOOTING_BEAM
Footing elements that are in bending and are supported clear of the ground. They will normally span between piers, piles or pile caps. They are distinguished from beams in the building superstructure since they will normally require a lower grade of finish. They are distinguished from _STRIP_FOOTING_ since they are clear of the ground surface and hence require support to the lower face while the concrete is curing.

### PAD_FOOTING
An element that transfers the load of a single column (possibly two) to the ground.

### PILE_CAP
An element that transfers the load from a column or group of columns to a pier or pile or group of piers or piles.

### STRIP_FOOTING
A linear element that transfers loads into the ground from either a continuous element, such as a wall, or from a series of elements, such as columns.

### USERDEFINED
Special types of footings which meet specific local requirements.

### NOTDEFINED
The type of footing is not defined.
