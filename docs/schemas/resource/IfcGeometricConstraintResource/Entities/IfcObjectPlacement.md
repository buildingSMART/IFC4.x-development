# IfcObjectPlacement

_IfcObjectPlacement_ is an abstract supertype for the special types defining the object coordinate system. The _IfcObjectPlacement_ has to be provided for each product that has a shape representation.
<!-- end of short definition -->

The object placement can be given:

* absolute: by an axis2 placement, relative to the world coordinate system,
* relative: by an axis2 placement, relative to the object placement of another product,
* by grid reference: by the virtual intersection and reference direction given by two axes of a design grid,
* linear placement: by distance along a curve, with possible offsets.

In any case the object placement has to unambiguously define the object coordinate system as either two-dimensional axis placement (_IfcAxis2Placement2D_) or three-dimensional axis placement (_IfcAxis2Placement3D_). The axis placement may have to be calculated.

> HISTORY New entity in IFC2x.

## Attributes

### PlacesObject
The _IfcObjectPlacement_ shall be used to provide a placement and
an object coordinate system for instances of _IfcProduct_.
{ .note}
> If an _IfcObjectPlacement_ is shared by many instances of _IfcProduct_ it does not apply a semantic meaning of being a shared placement that needs to be maintained. The same instance of _IfcObjectPlacement_ could simply be used to reduce exchange file size.

{ .change-ifc2x3}
> IFC2x3 CHANGE New inverse attribute.

{ .change-ifc2x4}
> IFC4 CHANGE The cardinality has changed to 0..n to allow reuse of instances of _IfcObjectPlacement_ as placement object in one to many products. It takes also into account that it can act as a placement for _IfcStructuralAnalysisModel_.

### PlacementRelTo
Reference to the object placement that establishes the coordinate system in which this object placement is defined. It is optional and may be omitted only for IfcLocalPlacement subtype.
