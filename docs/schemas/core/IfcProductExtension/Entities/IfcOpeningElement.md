# IfcOpeningElement

The opening element stands for opening, recess or chase, all reflecting voids. It represents a void within any element that has physical manifestation. Openings can be inserted into walls, slabs, beams, columns, or other elements.
<!-- end of short definition -->

There are two different types of opening elements. The attribute _PredefinedType_ should be used to capture the differences:

* an opening, where the thickness of the opening is greater or equal to the thickness of the element —
 the attribute _PredefinedType_ is set to _OPENING_
* a recess or niche, where the thickness of the recess is smaller than the thickness of the element —
 the attribute _PredefinedType_ is set to _RECESS_ for a recess or niche.

If the value for _PredefinedType_ is omitted, or the value is set to _NOTDEFINED_, no specific information of whether it is an opening or recess shall be assumed.

An _IfcOpeningElement_ has to be inserted into an _IfcElement_ by using the _IfcRelVoidsElement_ relationship. It may be filled by an _IfcDoor_, _IfcWindow_, or another filling element by using the relationship _IfcRelFillsElement_. Depending on the type of the _IfcShapeRepresentation_ of the _IfcOpeningElement_ the voiding relationship implies:

* if the _IfcShapeRepresentation.RepresentationIdentifier_ = 'Body', then the Body shape representation of the opening has to be subtracted from the body shape representation of the voided element - implicit Boolean difference operation.
* if the _IfcShapeRepresentation.RepresentationIdentifier_ = 'Reference', then the Reference shape representation of the opening is not subtracted. It is provided in addition to the hole in the Body shape representation of the voided element.

The _IfcOpeningElement_ shall not participate in the containment relationship, i.e. it is not linked directly to the spatial structure of the project. It has a mandatory _VoidsElements_ inverse relationship pointing to the _IfcElement_ that is contained in the spatial structure. The inverse relationship _ContainedInStructure_ shall be NIL.

> REFERENCE Definition according to ISO 6707-1: void in a building element

> NOTE The entity _IfcOpeningStandardCase_ has been deleted. Use an _IfcOpeningElement_ with a single extrusion body perpendicular to the wall or slab instead.

> NOTE See _IfcRelVoidsElement_ for a diagram on how to apply spatial containment and the voiding relationship.

> IFC2x CHANGE The intermediate ABSTRACT supertypes _IfcFeatureElement_ and _IfcFeatureElementSubtraction_ have been added.

> IFC4 CHANGE The attribute _PredefinedType_ has been added at the end of the attribute list.

> HISTORY New entity in IFC1.0

## Attributes

### PredefinedType

Predefined generic type for an opening that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

### HasFillings

Reference to the _Filling_ Relationship that is used to assign Elements as Fillings for this Opening Element. The Opening Element can be filled with zero-to-many Elements.

## Formal Propositions

### CorrectPredefinedType

Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to _USERDEFINED_.

## Concepts

### Body SweptSolid Geometry

The 'Body' representation of _IfcOpeningElement_ can be represented using the representation types 'SweptSolid'. The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation.RepresentationIdentifier_: 'Body'
* _IfcShapeRepresentation.RepresentationType_: 'SweptSolid'

The following constraints are recommended:

* _IfcShapeRepresentation.Items_ may include a single, or multiple, instances of _IfcExtrudedAreaSolid_.
* _IfcExtrudedAreaSolid.SweptArea_ shall support _IfcRectangleProfileDef_, _IfcCircleProfileDef_ and _IfcArbitraryClosedProfileDef_.
* If multiple instances of _IfcExtrudedAreaSolid_ are used, the extrusion direction of each extrusion should be equal.

If parametric profiles are used, the parameters may be interpreted to be the dimensions of the opening:

* _IfcRectangleProfileDef.YDim_ interpreted as opening height
* _IfcRectangleProfileDef.XDim_ interpreted as opening width

There are two main extrusion directions: perpendicular and parallel.

**Perpendicular Swept Solid Representation Type**

For a perpendicular swept solid, _IfcExtrudedAreaSolid.ExtrudedDirection_ shall extrude the profile perpendicular to the element it is voiding. This may be horizontal for wall openings, or vertical for floor openings.

![standard opening](../../../../figures/ifcopeningelement_horizontal-layout1.png "Figure FULLEXTRUSION — Opening with full extrusion")

![recess](../../../../figures/ifcopeningelement_recess-layout1.png "Figure RECESS — Opening with recess extrusion")

> NOTE The local placement directions for the _IfcOpeningElement_ in Figure FULLEXTRUSION and Figure RECESS are only given as an example; other directions are valid as well.

> NOTE Rectangles are now defined centrally, so the placement location has to be set to _IfcCartesianPoint_(XDim/2,YDim/2)

**Parallel Swept Solid Representation Type**

For a parallel swept solid,_IfcExtrudedAreaSolid.ExtrudedDirection_ shall extrude the profile parallel to the element it is voiding. This may be vertical in the case of walls.

Parallel extrusions shall be used when an opening or recess has a non rectangular foot print geometry that does not change along the height of the opening or recess.

Figure VERTEXTRUDE shows a vertical extrusion with multiple extrusion bodies for the opening. Each extrusion body has a different extrusion length.

![vertical extrusion](../../../../figures/ifcopeningelement_vertical-layout1.png "Figure VERTEXTRUDE — Opening with multiple extrusions")

> NOTE The local placement directions for the _IfcOpeningElement_ in Figure VERTEXTRUDE are only given as an example, other directions are valid as well.

### Product Local Placement

The local placement for _IfcOpeningElement_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations.

* The _PlacementRelTo_ relationship of _IfcLocalPlacement_ should point to the local placement of the element which is voided by the opening, i.e. referred to by _VoidsElement.RelatingBuildingElement_.

### Property Sets for Objects



### Quantity Sets



### Reference Geometry

Since there are no Boolean operations, either as _IfcBooleanResult_ or implicitly by _IfcRelVoidsElement_, the geometry of the _IfcOpeningElement_ shall not be used to subtract the opening from the 'Body' shape representation of the voided element.

### Reference SweptSolid PolyCurve Geometry

Since there are no Boolean operations, either as _IfcBooleanResult_ or implicitly by _IfcRelVoidsElement_, the geometry of the _IfcOpeningElement_ shall not be used to subtract the opening from the 'Body' shape representation of the voided element.

### Reference Tessellation Geometry

Since there are no Boolean operations, either as _IfcBooleanResult_ or implicitly by _IfcRelVoidsElement_, the geometry of the _IfcOpeningElement_ shall not be used to subtract the opening from the 'Body' shape representation of the voided element.
