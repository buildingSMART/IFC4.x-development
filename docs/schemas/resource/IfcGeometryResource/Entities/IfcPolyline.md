# IfcPolyline

The _IfcPolyline_ is a bounded curve with only linear segments defined by a list of Cartesian points. If the first and the last Cartesian point in the list are identical, then the polyline is a closed curve, otherwise it is an open curve.
<!-- end of short definition -->

> EXAMPLE Figure 1 illustrates a bounded _IfcPolyline_ and shows the parametric length of each segment and of the total polyline.

![polyline examples](../../../../figures/ifcpolyline-fig1.png "Figure 1 — Bounded _IfcPolyline_ with parametric length")

> NOTE Definition according to ISO/CD 10303-42:1992
> A polyline is a bounded curve of _n_ - 1 linear segments, defined by a list of _n_ points, P~1~, P~2~ ... P~n~. The _i_th segment of the curve is parameterized as follows:
>> ![Image](../../../../figures/ifcpolyline-math1.gif)  _for_ 1 ≤ _i_ ≤ _n_ - 1
> where _i_ - 1 ≤ _u_ ≤ _i_ and with parametric range of 0 <≤ _u_ ≤ _n_ - 1.

> NOTE Entity adapted from **polyline** in ISO 10303-42.

> HISTORY New entity in IFC1.0

## Attributes

### Points
The points defining the polyline.

## Formal Propositions

### SameDim
The space dimensionality of all Points shall be the same.
