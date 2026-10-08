# IfcDocumentInformationRelationship

An _IfcDocumentInformationRelationship_ is a relationship entity that enables a document to have the ability to reference other documents. It is used to describe relationships in which one document may reference one or more other sub documents or where a document is used as a replacement for another document (but where both the original and the replacing document need to be retained).
<!-- end of short definition -->

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Subtyped from _IfcResourceLevelRelationship_, order of attributes changed.

## Attributes

### RelatingDocument
The document that acts as the parent, referencing or original document in a relationship.

### RelatedDocuments
The document that acts as the child, referenced or replacing document in a relationship.

### RelationshipType
Describes the type of relationship between documents. This could be sub-document, replacement etc. The interpretation has to be established in an application context.
