# IfcSpaceTypeEnum

This enumeration defines the available generic types for _IfcSpace_ and _IfcSpaceType_.
<!-- end of short definition -->

> HISTORY New enumeration in IFC2x3.

{ .change-ifc2x4}
> IFC4 CHANGE The enumerators INTERNAL and EXTERNAL have been added for upward compatibility to replace _InteriorOrExteriorSpace_ usage.

## Items

### SPACE
Any space not falling into another category.

### PARKING
A space dedication for use as a parking spot for vehicles, including access, such as a parking aisle.

### GFA
Gross Floor Area - a specific kind of space for each building story that includes all net area and construction area (also the external envelop). Provision of such a specific space is often required by regulations.

### INTERNAL
A space inside a facility.

> IFC4.3.2.0 DEPRECATION INTERNAL and EXTERNAL are now deprecated. Use Pset_SpaceCommon.IsExternal instead.

### EXTERNAL
A space outside of a facility.

> IFC4.3.2.0 DEPRECATION INTERNAL and EXTERNAL are now deprecated. Use Pset_SpaceCommon.IsExternal instead.

### BERTH
A space dedicated to the berthing of vessels within a port or managed area.

### USERDEFINED


### NOTDEFINED

