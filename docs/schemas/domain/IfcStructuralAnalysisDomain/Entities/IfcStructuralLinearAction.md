# IfcStructuralLinearAction

This entity defines an action with constant value which is distributed over a curve.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Intermediate supertype _IfcStructuralCurveAction_ inserted.

> NOTE Like its supertype _IfcStructuralCurveAction_, this action type may also act on curved edges.

## Formal Propositions

### SuitableLoadType
A linear action shall place either a linear force or a temperature load.

### ConstPredefinedType
This curve action subtype is restricted to constant load distribution over its domain.
