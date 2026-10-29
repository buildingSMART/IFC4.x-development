# IfcGeometricSet

The _IfcGeometricSet_ is used for the exchange of shape representation consisting of (2D or 3D) points, curves, and surfaces, which do not have a topological structure (such as connected face sets or shells), are not tessellated and are not solid models (such as swept solids, CSG or Brep).
<!-- end of short definition -->

> NOTE Definition from ISO/CD 10303-42:
> This entity is intended for the transfer of models when a topological structure is not available.

> NOTE Entity adapted from **geometric_set** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

## Attributes

### Elements
The geometric elements which make up the geometric set, these may be points, curves or surfaces; but are required to be of the same coordinate space dimensionality.

### Dim
The space dimensionality of this class, it is identical to the first element in the set. A where rule ensures that all elements have the same dimensionality.

## Formal Propositions

### ConsistentDim
All elements within a geometric set shall have the same dimensionality.
