# IfcSectionedSpine

An _IfcSectionedSpine_ is a representation of the shape of a three dimensional object composed by a number of planar cross sections, and a spine curve. The shape is defined between the first element of cross sections and the last element of the cross sections. A sectioned spine may be used to represent a surface or a solid but the interpolation of the shape between the cross sections is not defined.
<!-- end of short definition -->

All cross sections have to define areas by a closed profile to allow for the representation of a solid. All cross sections have to define curves by an open or closed profile to allow for the representation of a surface. The cross sections are defined by subtypes of _IfcProfileDef_, where the consecutive profiles may be derived by a transformation of the start profile or the previous consecutive profile.

The spine curve shall be of type _IfcCompositeCurve_, each of its segments represented by _IfcCompositeCurveSegment_ shall correspond to the part between exactly two consecutive cross-sections.

Figure 1 illustrates an example of an _IfcSectionedSpine_.

* The _SpineCurve_ is given by an _IfcCompositeCurve_ with two _Segments_. The _Segments[1]_ has a _ParentCurve_ of type _IfcPolyline_ and a _Transition_ = CONTSAMEGRADIENT. The _Segments[2]_ has a _ParentCurve_ of type _IfcTrimmedCurve_ and a _Transition_ = DISCONTINUOUS.
* Each _CrossSectionPosition_ lies at a start or end point of the _Segments_.
* Each _CrossSections_ are inserted by the _CrossSectionPositions_. The first two cross sections are of type _IfcRectangleProfileDef_, the third is of type _IfcDerivedProfileDef_.

![spine 1](../../../../figures/ifcsectionedspine-layout1.gif)

Figure 1 — Sectioned spine geometry

Figure 2 illustrates the final result of the _IfcSectionedSpine_. The body (shown transparently) is not fully defined by the exchange definition.

![render](../../../../figures/ifcsectionedspine.jpg)

Figure 2 — Sectioned spine result

> NOTE Definition according to ISO/CD 10303-42:1992
> A sectioned spine is a representation of the shape of a three dimensional object composed of a spine curve and a number of planar cross sections. The shape is defined between the first element of cross sections and the last element of this set.
>
> NOTE A sectioned spine may be used to represent a surface or a solid but the interpolation of the shape between the cross-sections is not defined. For the representation of a solid all cross-sections are closed curves.

> NOTE Entity adapted from **sectioned_spine** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. none of the cross sections, after being placed by the cross section positions, shall intersect
2. none of the cross sections, after being placed by the cross section positions, shall lie in the same plane
3. the local origin of each cross section position shall lie at the beginning or end of a composite curve segment.

## Attributes

### SpineCurve
A single composite curve, that defines the spine curve. Each of the composite curve segments correspond to the part between two cross-sections.

### CrossSections
A list of at least two cross sections, each defined within the xy plane of the position coordinate system of the cross section. The position coordinate system is given by the corresponding list CrossSectionPositions.

### CrossSectionPositions
Position coordinate systems for the cross sections that form the sectioned spine. The profiles defining the cross sections are positioned within the xy plane of the corresponding position coordinate system.

### Dim
The dimensionality of the spine curve is always 3.

## Formal Propositions

### CorrespondingSectionPositions
The set of cross sections and the set of cross section positions shall be of the same size.

### ConsistentProfileTypes
The profile type (either AREA or CURVE) shall be consistent within the list of the profiles defining the cross sections.

### SpineCurveDim
The curve entity which is the underlying spine curve shall have the dimensionality of 3.
