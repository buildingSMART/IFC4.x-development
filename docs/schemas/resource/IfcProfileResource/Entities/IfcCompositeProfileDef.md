# IfcCompositeProfileDef

The _IfcCompositeProfileDef_ defines the profile by composition of other profiles. The composition is given by a set of at least two other profile definitions. Any profile definition (except for another composite profile) can be used to construct the composite.
<!-- end of short definition -->

> HISTORY New entity in IFC2x.

Figure 314 illustrates the composite profile definition. The _IfcCompositeProfileDef_ does not define an own position coordinate system, it is directly defined in the underlying coordinate system. The underlying coordinate system is defined by the swept surface or swept area solid that uses the profile definition. It is the xy plane of either:

* _IfcSweptSurface.Position_
* _IfcSweptAreaSolid.Position_

Or in case of sectioned spines it is the xy plane of each list member of _IfcSectionedSpine.CrossSectionPositions_. The _IfcCompositeProfileDef_ is defined using other profile definitions. Those other profile definitions are directly inserted into the underlying coordinate system.

* In case of parameterized profile definitions, the _Position_ attribute of those standard profiles is used to place the profiles relatively to each other.
* In case of arbitrary profile definitions, each Cartesian coordinate is given directly within the underlying coordinate system.

> NOTE The black coordinate axes show the underlying coordinate system of the swept surface or swept area solid.

![composite](../../../../figures/ifccompositeprofiledef-layout1.gif "Figure 314")

Twin profiles special case

If twin profiles are modeled by profile composition, the base profile should only be specified once. It is then included into the composite profile directly and additionally indirectly via _IfcMirroredProfileDef_. For example, a double angle made of two L100x10 with 10mm air gap between them, i.e. a _| |_ shape, can be modeled as

>
> ```
>
single_L : IfcLShapeProfileDef := IfcLShapeProfileDef(AREA, 'L100X100X10',
>   IfcAxis2Placement2D(IfcCartesianPoint(((.100+.010)/2., .0)), ?),
>   .100, .100, .010, .012, ?, 0., ?, ?);
>
> double_L : IfcCompositeProfileDef := IfcCompositeProfileDef(AREA, 'double angle',
>   (single_L, IfcMirroredProfileDef(AREA, ?, single_L, ?)), 'twin profile');

> ```

## Attributes

### Profiles
The profiles which are used to define the composite profile.

### Label
The name by which the composition may be referred to. The actual meaning of the name has to be defined in the context of applications.

## Formal Propositions

### InvariantProfileType
Either all profiles are areas or all profiles are curves.

### NoRecursion
A composite profile should not include another composite profile, i.e. no recursive definitions should be allowed.
