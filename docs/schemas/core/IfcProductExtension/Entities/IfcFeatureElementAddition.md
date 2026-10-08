# IfcFeatureElementAddition

A feature element addition is a specialization of the general feature element, that represents an existence dependent element which modifies the shape and appearance of the associated master element. The _IfcFeatureElementAddition_ offers the ability to handle shape modifiers as semantic objects within the IFC object model that add to the shape of the master element.
<!-- end of short definition -->

The _IfcFeatureElementAddition_ is associated to its master element by virtue of the objectified relationship _IfcRelProjectsElement_. This relationship implies a Boolean 'union' operation between the shape of the master element and the shape of the addition feature.

The local placement for _IfcFeatureElementAddition_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations. The local placement is always defined in relation to the local placement of the element to which the feature element is added:

* The _PlacementRelTo_ attribute of _IfcObjectPlacement_ shall point (if given) to the object placement of the _IfcElement_, which is used in the _ProjectsElements.RelatingElement_ inverse attribute (the parent element of the feature).

> HISTORY New entity in IFC2x2.

> IFC2x2 CHANGE The entity is introduced as an upward compatible extension of the IFC2x platform. It is an intermediate abstract supertype without defining its own explicit attributes.

## Attributes

### ProjectsElements
Reference to the _IfcRelProjectsElement_ relationship that uses this _IfcFeatureElementAddition_ to create a volume addition at an element. The _IfcFeatureElementAddition_ can only be used to create a single addition at a single element using Boolean addition operation.
