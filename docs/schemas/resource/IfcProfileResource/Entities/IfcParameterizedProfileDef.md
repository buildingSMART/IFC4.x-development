# IfcParameterizedProfileDef

The parameterized profile definition defines a 2D position coordinate system to which the parameters of the different profiles relate to. All profiles are defined centric to the origin of the position coordinate system, or more specific, the origin [0.,0.] shall be in the center of the bounding box of the profile.
<!-- end of short definition -->

The _Position_ attribute of _IfcParameterizedProfileDef_ is used to position the profile within the XY plane of the underlying coordinate system of the swept surface geometry, the swept area solid or the sectioned spine. It can be used to position the profile at any point which becomes the origin [0.,0.,0.] of the extruded or rotated surface or solid.

The _Position_ attribute should not be used if the transformation can be specified in a containing object instead. In particular, this applies if the _IfcParameterizedProfileDef_ is referenced as _SweptArea_ in subtypes of _IfcSweptAreaSolid_ or as _CrossSections_ in _IfcSectionedSpine_.

Several subtypes of _IfcParameterizedProfileDef_ provide shape parameters which are optional. Sending systems should always provide values for these parameters if possible. If these parameters are left unspecified, receiving systems may retrieve values for them by external reference (if a reference to an external document or library is given; see guidance at _IfcProfileDef_), or estimate them, or simply assume zero values.

> HISTORY New entity in IFC2x2.

> IFC2x CHANGE The _IfcParameterizedProfileDef_ is introduced as an intermediate new abstract entity that unifies the definition and usage of the position coordinate system for all parameterized profiles. The Position attribute has been removed at all subtypes (like _IfcRectangleProfileDef_, _IfcCircleProfileDef_, etc.).

> IFC2x3 CHANGE All profile origins are now in the center of the bounding box.

> IFC4 CHANGE _Position_ attribute made optional (default: identity transformation).
> Several radius parameters in subtypes have been changed from optional _IfcPositiveLengthMeasure_ (assumed default: 0.) to optional _IfcNonNegativeLengthMeasure_ (default: unspecified). This change allows to explicitly specify zero radius. Sending systems shall export 0. values if parameters are known to be 0.
> Subtypes _IfcCraneRailAShapeProfileDef_ and _IfcCraneRailFShapeProfileDef_ deleted. Rail profiles shall be modeled as _IfcArbitraryClosedProfileDef_ or as _IfcAsymmetricIShapeProfileDef_ together with appropriate external reference.

## Attributes

### Position
Position coordinate system of the parameterized profile definition. If unspecified, no translation and no rotation is applied.
