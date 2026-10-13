# IfcFillElementTypeEnum

This enumeration defines the different predefined types of a fill element that can further specify an _IfcFillElement_ or _IfcFillElementType_.
<!-- end of short definition -->

> HISTORY New enumeration in IFC4.4.

## Items

### INVERTFILL
The fill element used to fill the tunnel invert, i.e. the lowest section of a tunnel, i.e., the floor.

### ANNULARGAPFILL
The fill element used to fill the annular gap, e.g. between the tunnel lining and the surrounding ground.

### USERDEFINED
User-defined fill element type. When set, an _ObjectType_ (on the occurrence) or _ElementType_ (on the type) must be provided to convey the specific intent.

### NOTDEFINED
Undefined fill element type.
