# IfcReinforcingMeshType

The reinforcing element type **IfcReinforcingMeshType** defines commonly shared information for occurrences of reinforcing meshs. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a reinforcing mesh type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcReinforcingMeshType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcReinforcingMeshType** are represented by instances of _IfcReinforcingMesh_.

> HISTORY New entity in IFC4.

Geometry Use Definition

The _IfcReinforcingMeshType_ may define the shared geometric representation for many mesh occurrences. The _RepresentationMaps_ attribute refers to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations.

## Attributes

### PredefinedType
Subtype of reinforcing mesh.

### MeshLength
The overall length of the mesh measured in its longitudinal direction.

### MeshWidth
The overall width of the mesh measured in its transversal direction.

### LongitudinalBarNominalDiameter
The nominal diameter denoting the cross-section size of the longitudinal bars.

### TransverseBarNominalDiameter
The nominal diameter denoting the cross-section size of the transverse bars.

### LongitudinalBarCrossSectionArea
The effective cross-section area of the longitudinal bars of the mesh.

### TransverseBarCrossSectionArea
The effective cross-section area of the transverse bars of the mesh.

### LongitudinalBarSpacing
The spacing between the longitudinal bars. Note: an even distribution of bars is presumed; other cases are handled by classification or property sets.

### TransverseBarSpacing
The spacing between the transverse bars. Note: an even distribution of bars is presumed; other cases are handled by classification or property sets.

### BendingShapeCode
If this mesh type is bent rather than planar, this attribute provides a shape code per a standard like ACI 315, ISO 3766, or a similar standard. It is presumed that a single standard for defining the mesh bending is used throughout the project and that this standard is referenced from the _IfcProject_ object through the _IfcDocumentReference_ mechanism.

### BendingParameters
If this mesh type is bent rather than planar, this attribute provides bending shape parameters. Their meaning is defined by the bending shape code and the respective standard.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.

### BendingShapeCodeProvided
Bending parameters must be accompanied by a shape code.

## Concepts

### Reinforcing Mesh Type Attributes



