# IfcRelAssociates

The association relationship _IfcRelAssociates_ refers to sources of information (most notably a classification, library, document, approval, constraint, or material). The information associated may reside internally or externally to the project data. There is no dependency implied by the association.
<!-- end of short definition -->

> EXAMPLE Further external information may be provided to the tank equipment (as subtype of _IfcProduct_) in terms of its classification and instruction documents, the source of the additional information is held external to the project data model.

Association relationships can be established to objects (occurrences as subtypes of _IfcObject_) or to types (as subtypes of _IfcTypeObject_). Some associations (such as approval, or document) may also be applied to property templates (as subtypes of _IfcPropertyDefinition_).

> EXAMPLE The classification information for the storage tank equipment may be associated to the _IfcTankType_ (subtype of _IfcTypeObject_), defining the specific information for all occurences of that tank in the project. Therefore the association of the Uniclass notation 'Pr_60_50_10' may be associated by a subtype of _IfcRelAssociates_ to the type information.

> EXAMPLE The classification information for a particular space within a building may be associated to the _IfcSpace_ object (subtype of _IfcObject_), defining a particular occurrence of space. Therefore the association of the DIN notation 'NF 1.5' may be associated by a subtype of _IfcRelAssociates_ to the object.

The association relationship establishes an association between one to many objects or property templates and the associated information. The subtypes of _IfcRelAssociates_ establish the particular semantic meaning of the association relationship.

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Entity has been changed into an ABSTRACT supertype

## Attributes

### RelatedObjects
Set of object or property definitions to which the external references or information is associated. It includes object and type objects, property set templates, property templates and property sets and contexts.
> IFC4 CHANGE The attribute datatype has been changed from _IfcRoot_ to _IfcDefinitionSelect_.
