# IfcTendon

A tendon is a steel element such as a wire, cable, bar, rod, or strand used to impart compressive strength to concrete when the element is given a tensile stress (prestressed or post-tensioned).
<!-- end of short definition -->

{ .extDef}
> NOTE Definition according to ISO 6707-1: steel bar(s) or groups of bars, strands or wires given a tensile stress that produces a compressive stress in prestressed concrete or masonry.

{ .extDef}
> NOTE To be efficient, the cable follows the deck alignment and moves vertically up on the top of the piers and down in the middle of the span. Therefore the cable axis is defined relatively towards the deck alignment. The ShapeRepresentation should be 'AdvancedSweptSolid' geometry based on SectionedSolidHorizontal description including DistanceExpression, CircleProfileDef and AlignmentCurve, leading to a polyline describing the cable directrix.

{ .extDef}
> NOTE Regarding the Structural Analysis model, the cable has to be transformed into loads applied at each CartesianPoint defining the polyline.

> HISTORY New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute _PredefinedType_ made optional. _NominalDiameter_ and _CrossSectionArea_ made optional and deprecated; this information can now be provided by _IfcTendonType_. Description of _FrictionCoefficient_ corrected.

## Attributes

### PredefinedType
Predefined generic types for a tendon.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute made optional.

### NominalDiameter
The nominal diameter defining the cross-section size of the tendon.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcTendonType_ instead.

### CrossSectionArea
The effective cross-section area of the tendon.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute made optional and deprecated. Use respective attribute at _IfcTendonType_ instead.

### TensionForce
The maximum allowed tension force that can be applied on the tendon.

### PreStress
The prestress to be applied on the tendon.

### FrictionCoefficient
The friction coefficient between tendon and tendon sheet while the tendon is unbonded.

### AnchorageSlip
The deformation of an anchor or slippage of tendons when the prestressing device is released.

### MinCurvatureRadius
The smallest curvature radius calculated on the whole effective length of the tendon where the tension properties are still valid.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTendonType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcTendonType_.

## Concepts

### Body Geometry

### Mapped Geometry

This method of representation allows for several tendons represented by a single instance of IfcTendon. The representation map should contain one IfcSweptDiskSolid.

### Object Typing



### Product Local Placement



### Property Sets for Objects



### Quantity Sets



### Tendon Attributes



