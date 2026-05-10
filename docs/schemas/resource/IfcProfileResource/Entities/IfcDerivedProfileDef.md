AbV

# IfcDerivedProfileDef

_IfcDerivedProfileDef_ defines the profile by transformation from the parent profile. The transformation is given by a two dimensional transformation operator. Transformation includes translation, rotation, mirror and scaling. The latter can be uniform or non uniform. The derived profiles may be used to define swept surfaces, swept area solids or sectioned spines.
<!-- end of short definition -->

The transformation effects the position, rotation, mirroring or scale of the profile at the underlying coordinate system, i.e. the coordinate system defined by the swept surface or swept area solid that uses the profile definition. It is the xy plane of either:

* _IfcSweptSurface.Position_
* _IfcSweptAreaSolid.Position_

or in case of sectioned spines the xy plane of each list member of _IfcSectionedSpine.CrossSectionPositions_. The position and potential rotation of the _ParentProfile_ within the underlying coordinate system is taken into consideration before applying the Cartesian transformation operator.

Note, if only mirroring is required, _IfcMirroredProfileDef_ should be used instead.

> HISTORY New entity in IFC2x.

![Uniform](../../../../figures/ifcderivedprofiledef-layout1.gif)

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em>
is defined using the <em>IfcCartesianTransformationOperator2D</em>
(CTO), which is applied to the parent profile definition. <br>
</p>

<p><u>Example</u><br>
The example shows an uniform scaling and a transformation
of an <em>IfcRectangleProfileDef</em>
to match the lower-left cardinal point. The attributes of the CTO are:<br>
</p>

  Axis1 = NIL (defaults to 1.,0.)
  Axis2 = NIL (defaults to 0.,1.)
  LocalOrigin = IfcCartesianPoint(<1/2 XDim>,<1/2 YDim>)
  Scale = 2.

> NOTE The <em>ParentProfile</em> has a <em>Position</em> = <em>IfcCartesianPoint</em>(<1/2 XDim>,<1/2 YDim>) already.

![Non uniform](../../../../figures/ifcderivedprofiledef-layout2.gif)

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em> is defined using
non uniform transformationsby applying the <em>IfcCartesianTransformationOperator2DnonUniform</em>
as a subtype of the 2D CTO.</p>

<p><u>Example</u><br>
The example shows a non-uniform scaling and a translation of an <em>IfcRectangleProfileDef</em>
to match the lower-left cardinal point. The attributes of the CTO are:</p>

  Axis1 = NIL (defaults to 1.,0.)
  Axis2 = NIL (defaults to 0.,1.)
  LocalOrigin = IfcCartesianPoint(0.,<1/2 YDim>)
  Scale = 1.
  Scale2 = 2.

> NOTE The <em>ParentProfile</em> has a <em>Position</em> = <em>IfcCartesianPoint</em>(<1/2 XDim>,<1/2 YDim>) already.

![mirroring](../../../../figures/ifcderivedprofiledef-layout3.gif)

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em>
is defined using mirroring by applying the <em>IfcCartesianTransformationOperator2D</em>
(CTO) to the parent profile.</p>

<p><u>Example</u><br>
The example shows a mirroring of an <em>IfcLShapeProfileDef</em>
to match the centre cardinal point. The attributes of the CTO are:</p>

  Axis1 = (-1.,0.)
  Axis2 = NIL (defaults to 0.,1.)
  LocalOrigin = IfcCartesianPoint(0.,0.)
  Scale = NIL (defaults to 1.)

> NOTE The <em>ParentProfile</em> has a <em>Position</em> = <em>IfcCartesianPoint</em>(0.,0.).

<p>This example is for illustration only.
If the transformation results only in mirroring like shown in the example, then
<em>IfcMirroredProfileDef</em> should be used instead of <em>IfcDerivedProfileDef</em>.</p>

Note: The following color map applies:

 * black coordinate axes show the underlying coordinate system of the swept surface, swept area solid, or sectioned spine
 * <font color="#ff0000">red coordinate axes</font> show the position coordinate system of the parent profile
 * <font color="#993300">brown coordinate axes</font> show the position coordinate system of the derived profile


## Attributes

### ParentProfile
The parent profile provides the origin of the transformation.

### Operator
Transformation operator applied to the parent profile.

### Label
The name by which the transformation may be referred to. The actual meaning of the name has to be defined in the context of applications.

## Formal Propositions

### InvariantProfileType
The profile type of the derived profile shall be the same as the type of the parent profile, i.e. both shall be either AREA or CURVE.
