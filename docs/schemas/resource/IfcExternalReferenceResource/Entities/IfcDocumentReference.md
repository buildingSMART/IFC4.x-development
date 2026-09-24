# IfcDocumentReference

An _IfcDocumentReference_ is a reference to the location of a document. The reference is given by a system interpretable _Location_ attribute (a URL string) where the document can be found, and an optional inherited internal reference _Identification_, which refers to a system interpretable position within the document. The optional inherited _Name_ attribute is meant to have meaning for human readers. Optional document metadata can also be captured through reference to _IfcDocumentInformation_.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0

## Attributes

### Description
Description of the document reference for informational purposes.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### ReferencedDocument
The document that is referenced.

### DocumentRefForObjects
The document reference with which objects are associated.
> IFC4 CHANGE New inverse attribute.

## Formal Propositions

### WR1
A name should only be given, if no document information (including the document name) is attached
