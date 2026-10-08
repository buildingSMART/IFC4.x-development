# IfcFeatureElementSubtraction

The _IfcFeatureElementSubtraction_ is specialization of the general feature element, that represents an existence dependent element which modifies the shape and appearance of the associated master element. The _IfcFeatureElementSubtraction_ offers the ability to handle shape modifiers as semantic objects within the IFC object model that subtract from the shape of the master element.
<!-- end of short definition -->

> NOTE A single subtraction feature such as the subtype _IfcOpeningElement_ is assigned by a single subtraction relationship _IfcRelVoidsElement_ to one occurrence of _IfcElement_. It establishes a 1:1 relationship between the opening and the element. An element may have several _IfcRelVoidsElement_ relationships, enabling several voids.

The voiding relationship between a master element and a subtraction feature is geometrically resolved by a Boolean difference operation.

The local placement for _IfcFeatureElementSubtraction_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations. The local placement is always defined in relation to the local placement of the building element from which the feature element substraction is substracted:

* The _PlacementRelTo_ attribute of _IfcObjectPlacement_ shall point (if given) to the object placement of the _IfcElement_, which is used in the _VoidsElements.RelatingElement_ inverse attribute (the parent element of the feature).

> HISTORY New entity in IFC2x2.

> IFC2x2 CHANGE The entity is introduced as an upward compatible extension of the IFC2x scheme. It is an intermediate abstract supertype without defining its own explicit attributes.

## Attributes

### VoidsElements
Reference to the _Voids_ Relationship that uses this Opening Element to create a void within an Element. The Opening Element can only be used to create a single void within a single Element.

## Formal Propositions

### HasNoSubtraction
A feature subtraction (e.g. an opening element) can not have other openings to void itself. The inverse relationship _HasOpenings_ shall therefore be NIL.

### IsNotFilling
A feature subtraction (e.g. an opening element) can not be a filling of another void. The inverse relationship _FillsVoids_ shall therefore be NIL.
