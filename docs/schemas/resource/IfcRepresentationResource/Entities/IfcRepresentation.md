# IfcRepresentation

The _IfcRepresentation_ defines the general concept of representing product properties and in particular the product shape.
<!-- end of short definition -->

{ .extDef}
> NOTE Definition from ISO 10303-43:
> A representation is a collection of one or more representation items that are related in a specified representation context. The relationship of representation item to representation context is the basis for distinguishing which representation item entities are related. A representation item can be related to a representation context directly, when it occurs as an element is a representation, or indirectly, when it is referenced through any number of intervening entities, each of type representation item.

> NOTE Entity adapted from **representation** defined in ISO 10303-42.

> HISTORY New entity in IFC2.0

{ .change-ifc2x3}
> IFC2x3 CHANGE The inverse attributes _LayerAssignments_ and _RepresentationMap_ have been added with upward compatibility.

{ .change-ifc2x4}
> IFC4 CHANGE Entity _IfcRepresentation_ has been changed into an ABSTRACT supertype.

{ .use-head}
Representation Use Definition

Each representation, either _IfcShapeRepresentation_, or _IfcTopologyRepresentation_ shall have a well defined:

* _ContextOfItems_: Reference to an _IfcGeometricRepresentationContext_ as agreed for this representation.
* _RepresentationIdentifier_: Name of the representation, for example, 'Body' for 3D shape, 'FootPrint' for 2D ground view, 'Axis' for reference axis.
* _RepresentationType_: Name for the geometric, or topological representation type, for example, 'SweptSolid' for 3D swept solids, 'Brep' for boundary representation.

> NOTE Guidelines for applying correct values to those attributes are provided in the geometry use definition section at each subtype of _IfcElement_. These guidelines can be further refined in view definitions or implementer agreements.

## Attributes

### ContextOfItems
Definition of the representation context for which the different subtypes of representation are valid.

### RepresentationIdentifier
The optional identifier of the representation as used within a project.

### RepresentationType
The description of the type of a representation context. The representation type defines the type of geometry or topology used for representing the product representation. More information is given at the subtypes _IfcShapeRepresentation_ and _IfcTopologyRepresentation_.
The supported values for context type are to be specified by implementers agreements.

### Items
Set of geometric representation items that are defined for this representation.

### RepresentationMap
Use of the representation within an _IfcRepresentationMap_. If used, this _IfcRepresentation_ may be assigned to many representations as one of its _Items_ using an _IfcMappedItem_. Using _IfcRepresentationMap_ is the way to share one representation (often of type _IfcShapeRepresentation_) by many products.
{ .change-ifc2x3}
> IFC2x3 CHANGE The inverse attribute _LayerAssignments_ has been added

### LayerAssignments
Assignment of the whole representation to a single or multiple layer(s). The _LayerAssigments_ can be overridden by _LayerAssigments_ of the _IfcRepresentationItem_'s within the list of _Items_.
> NOTE Implementation agreements can restrict the maximum number of layer assignments to 1.

{ .change-ifc2x3}
> IFC2x3 CHANGE The inverse attribute _LayerAssignments_ has been added

### OfProductRepresentation
Reference to the product representations to which this individual representation applies. In most cases it is the reference to one or many product shapes, to which this shape representation is applicable.
{ .change-ifc2x4}
> IFC4 CHANGE Inverse relationship cardinality relaxed to be 0:N.
