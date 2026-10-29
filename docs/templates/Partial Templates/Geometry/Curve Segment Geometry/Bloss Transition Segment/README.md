Bloss Transition Segment
========================

The Bloss transition segment is a special case of a fifth order spiral where the curvature rate of change is a cubic function and the terms are dependent on the length L measured from the inflection point. The parameter value is defined as the deflection i.e. bearing angle &Theta.

Only the cubic and quadratic terms are populated with the following values:

- CubicTerm = L/³√2
- QuadraticTerm = L/√3

```
concept {
    IfcCurveSegment:ParentCurve -> IfcThirdOrderPolynomialSpiral
    IfcThirdOrderPolynomialSpiral:CubicTerm -> IfcLengthMeasure_0
    IfcThirdOrderPolynomialSpiral:QuadraticTerm -> IfcLengthMeasure_1
}
```
