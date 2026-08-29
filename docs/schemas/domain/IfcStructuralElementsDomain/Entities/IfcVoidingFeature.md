# IfcVoidingFeature

A voiding feature is a modification of an element which reduces its volume. Such a feature may be manufactured in different ways, for example by cutting, drilling, or milling of members made of various materials, or by inlays into the formwork of cast members made of materials such as concrete.
<!-- end of short definition -->

The standard use of instances of _IfcVoidingFeature_ is as a part of element type objects (instances of subtypes of _IfcElementType_). The part–whole relationship is established by an aggregation relationship object, expressing the decomposition of an element type into one or more additive elements (element parts) and zero or more feature elements.

> HISTORY New entity in IFC4.

{ .use-head}
Containment Use Definition

Voiding features shall have no spatial containment relationship to the spatial structure since they are dependent on element types without spatial containment relationships or on an element occurrence with own spatial containment relationship.

* The _SELF\IfcElement.ContainedInStructure_ relationship shall be NIL.

## Attributes

### PredefinedType
Qualifies the feature regarding its shape and configuration relative to the voided element.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Body Geometry



#### IfcCsgSolid_CSG

Volumetric representations may be used to semi-parametrically model the actual volume of the void created by the feature. Attributes in the shape model directly correspond with feature parameters, for example diameter of circular holes or length and width of cutouts. The objects within the shape model of the feature's shape representation can be included into a CSG model within a representation map of the parent element type.

#### IfcShellBasedSurfaceModel_ShellBasedSurfaceModel

Surface representations of cutting planes by means of IfcShellBasedSurfaceModel. The faces within the surface model may be included into a B-Rep model within a representation map of the parent element type.

### Product Local Placement

The local placement for IfcVoidingFeature is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* In case of features which are part of an element type, absolute placement into the type object's implied coordinate system shall be used.
* In case of features which are voiding an element occurrence, the PlacementRelTo relationship of IfcLocalPlacement shall point to the local placement of the respective element.

### Property Sets for Objects

### Quantity Sets



### Reference Geometry

Since there are no Boolean operations, either as _IfcBooleanResult_ or implicitly by _IfcRelVoidsElement_, the geometry of the _IfcOpeningElement_ shall not be used to subtract the opening from the 'Body' shape representation of the voided element.


### Reference SweptSolid PolyCurve Geometry



### Reference Tessellation Geometry



