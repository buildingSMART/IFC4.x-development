Helmert Transition Segment
==========================

The Helmert transition segment is a special case of a fourth order spiral where the curvature rate of change is a quadratic function and the terms are dependent on the length L measured from the inflection point. The parameter value is defined as the deflection i.e. bearing angle &Theta.

The terms for the first half of the segment:
QuadraticTerm = L/√2
rest are 0.

Terms for the second half of the segment:
QuadraticTerm =  -L/√2
LinearTerm = L/4
Constant = -1

```
concept {
    IfcCurveSegment:ParentCurve -> IfcSecondOrderPolynomialSpiral
    IfcCurveSegment:SegmentStart -> IfcLengthMeasure_0
    IfcCurveSegment:SegmentLength -> IfcLengthMeasure_1
    IfcSecondOrderPolynomialSpiral:QuadraticTerm -> IfcLengthMeasure_0
    IfcSecondOrderPolynomialSpiral:LinearTerm -> IfcLengthMeasure_1
    IfcSecondOrderPolynomialSpiral:ConstantTerm -> IfcReal
    IfcSecondOrderPolynomialSpiral:QuadraticTerm[binding="QuadraticTerm"]
    IfcSecondOrderPolynomialSpiral:LinearTerm[binding="LinearTerm"]
    IfcSecondOrderPolynomialSpiral:ConstantTerm[binding="Constant"]
}
```
