# IfcWindowPanelProperties

A window panel is a casement, that is, a component, fixed or opening, consisting essentially of a frame and the infilling. The infilling of a window panel is normally glazing. The way of operation is defined in the operation type.
<!-- end of short definition -->

The _IfcWindowPanelProperties_ are used to parametrically describe the shape and operation of window panels. The parametric definition can be added solely or additionally to the explicit shape representation of the window.

The _IfcWindowType_ can define windows consisting of more then one panel. In this case, one instance of _IfcWindowPanelProperties_ has to be included for each window panel. The _PanelPosition_ attribute, in conjunction with the _IfcWindowType_.OperationType attribute, determines to which panel the _IfcWindowPanelProperties_apply. The _IfcWindowPanelProperties_ are included in the list of properties (_HasPropertySets_) of the _IfcWindowType_. More information about the window panel can be included in the same list of the _IfcWindowType_ using the _IfcPropertySet_ for dynamic extensions.

The _IfcWindowPanelProperties_ does not hold an own geometric representation. However it defines parameter, which can be used to create the shape of the _IfcWindowType_ (which is inserted by the _IfcWindow_ into the spatial context of the project). The parameters at the _IfcWindowPanelProperties_ define a standard window panel. The outer boundary of the lining is determined by the 'Profile' shape representation assigned to the _IfcWindow_, which inserts the _IfcWindowType_. It has to take the lining parameter into account as well. The position of the window panel within the overall window is determined by the _PanelPosition_ attribute.

As shown in Figure 1, the panel is applied to the position within the lining as defined by the panel position attribute. The following parameter apply to that panel: _FrameDepth_, _FrameThickness_.

![panel 1](../../../../figures/ifcwindowpanelproperties-fig01.gif "Figure 1 — Window panel properties")

> HISTORY New entity in IFC2.0, it had been renamed from IfcWindowPanel in IFC2x.

> IFC4 CHANGE Supertype changed to new _IfcPreDefinedPropertySet_.

> IFC4.3.2.0 DEPRECATION This entity, and most other subtypes of IfcPredefinedPropertySet, are now deprecated. Use Pset_WindowPanelProperties instead.

## Attributes

### OperationType
Types of window panel operations. Also used to assign standard symbolic presentations according to national building standards.

### PanelPosition
Position of this panel within the overall window style.

### FrameDepth
Depth of panel frame, measured from front face to back face horizontally (i.e. perpendicular to the window (elevation) plane.

### FrameThickness
Width of panel frame, measured from inside of panel (at glazing) to outside of panel (at lining), i.e. parallel to the window (elevation) plane.

### ShapeAspectStyle
Optional link to a shape aspect definition, which points to the part of the geometric representation of the window style, which is used to represent the panel.
> DEPRECATION The attribute is deprecated and shall no longer be used, i.e. the value shall be NIL ($).

## Formal Propositions

### ApplicableToType
The _IfcWindowPanelProperties_ shall only be used in the context of an _IfcDoorType_.
> NOTE The deprecated entity _IfcWindowStyle_ is applicable as well.
