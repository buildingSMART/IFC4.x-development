# IfcStructuralPlanarAction

This entity defines an action with constant value which is distributed over a surface.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Intermediate supertype _IfcStructuralSurfaceAction_ inserted.

> NOTE Like its supertype _IfcStructuralSurfaceAction_, this action type may also act on curved faces.

## Formal Propositions

### SuitableLoadType
A planar action shall place either a planar force or a temperature load.

### ConstPredefinedType
This surface action subtype is restricted to constant load distribution over its domain.
