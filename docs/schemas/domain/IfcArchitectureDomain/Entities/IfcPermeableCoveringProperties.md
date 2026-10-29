# IfcPermeableCoveringProperties

This entity is a description of a panel within a door or window (as fillers for opening) which allows for air flow. It is given by its properties (_IfcPermeableCoveringProperties_). A permeable covering is a casement, such as a component, fixed or opening, consisting essentially of a frame and the infilling. The infilling is normally a grill, a louver or a screen. The way of operation is defined in the operation type.
<!-- end of short definition -->

The _IfcPermeableCoveringProperties_ are included in the list of properties (_HasPropertySets_) of the _IfcWindowType_ or the _IfcDoorType_. More information about the permeable covering can be included in the same list of the window or door style using the _IfcPropertySet_ for dynamic extensions. This particularly applies for additional properties for the various operation types

The _IfcPermeableCoveringProperties_ does not hold a geometric representation. However it defines parameters which can be used to create the shape of the _IfcWindowType_ (which is inserted by the _IfcWindow_ into the spatial context of the project), or of the _IfcDoorType_ (which is inserted by the _IfcDoor_).

The parameters at the _IfcPermeableCoveringProperties_ define a standard permeable covering. The outer boundary of the panel is determined by the occurrence parameter assigned to the _IfcWindow_ or _IfcDoor_. It has to take the lining parameter into account as well. The position of the permeable covering within the overall window or door is determined by the _PanelPosition_ attribute.

Figure 1 illustrates the panel applied to the position within the lining, as defined by the panel position attribute. The following parameters apply to that panel: _FrameDepth_, _FrameThickness_.

![covering](../../../../figures/ifcpermeablecoveringproperties.gif "Figure 1 — Permeable covering properties")

> HISTORY New entity in IFC2.0, it had been renamed from _IfcPermeableCovering_ in IFC2x.

> IFC4 CHANGE Supertype changed to new _IfcPreDefinedPropertySet_.

> IFC4.3.2.0 DEPRECATION This entity, and most other subtypes of IfcPredefinedPropertySet, are now deprecated. Use Pset_PermeableCoveringProperties instead.

## Attributes

### OperationType
Types of permeable covering operations. Also used to assign standard symbolic presentations according to national building standards.

### PanelPosition
Position of this permeable covering panel within the overall window or door type.

### FrameDepth
Depth of panel frame (used to include the permeable covering), measured from front face to back face horizontally (i.e. perpendicular to the window or door (elevation) plane.

### FrameThickness
Width of panel frame (used to include the permeable covering), measured from inside of panel (at permeable covering) to outside of panel (at lining), i.e. parallel to the window or door (elevation) plane.

### ShapeAspectStyle
Optional link to a shape aspect definition, which points to the part of the geometric representation of the window style, which is used to represent the permeable covering.
