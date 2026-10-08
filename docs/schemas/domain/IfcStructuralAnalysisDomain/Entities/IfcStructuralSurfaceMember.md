# IfcStructuralSurfaceMember

Instances of _IfcStructuralSurfaceMember_ describe face members, that is, structural analysis idealizations of slabs, walls, and shells. Surface members may be planar or curved.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Use definitions changed, WHERE rule added.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_. The local coordinate system is established by the reference surface given by topology representation.

****Material Use Definition****

The material of direct instances _IfcStructuralSurfaceMember_ (in contrast to instances of the subtype _IfcStructuralSurfaceMemberVarying_) is defined by _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

The material is specified minimally by a name which corresponds with an agreed upon standardized structural material designation. An external reference to the source which specifies the material designation should be provided. Alternatively, structural material properties may be provided by means of _IfcMaterialProperties_.

Direct instances of _IfcStructuralSurfaceMember_ are assumed to be located centrically relative to their reference surface. Their depth is provided in the attribute _Thickness_.

## Attributes

### PredefinedType
Type of member with respect to its load carrying behaviour in this analysis idealization.

### Thickness
Defines the typically understood thickness of the structural surface member, measured normal to its reference surface.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Material Layer Set Usage

The material of direct instances IfcStructuralSurfaceMember (in contrast to instances of the subtype IfcStructuralSurfaceMemberVarying) is defined by IfcMaterialLayerSetUsage and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse HasAssociations relationship.

The material is specified minimally by a name which corresponds with an agreed upon standardized structural material designation. An external reference to the source which specifies the material designation should be provided. Alternatively, structural material properties may be provided by means of IfcMaterialProperties.

In the absence of material layer set usage, direct instances of IfcStructuralSurfaceMember are assumed to be located centrically relative to their reference surface. Their depth is provided in the attribute Thickness.

### Reference Topology

Direct instances of IfcStructuralSurfaceMember shall have a topology representation which consists of one IfcFaceSurface, representing the reference surface of the surface member. See definitions at IfcStructuralItem for further specifications.

The local coordinate system is established by the reference surface given by topology representation.

### Structural Connectivity



#### IfcStructuralCurveConnection

Connections to curve members along edge(s) of surface.

#### IfcStructuralSurfaceConnection

Connections to surface members within face(s) of surface.

