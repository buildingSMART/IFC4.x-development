# IfcDocumentInformation

_IfcDocumentInformation_ captures "metadata" of an external document. The actual content of the document is not defined in this specification; instead, it can be found following the _Location_ attribute.
<!-- end of short definition -->

The same _IfcDocumentInformation_ can be referenced from the exchange structure in total or in parts (e.g. by referring to particular chapters or paragraphs) using the _IfcDocumentReference_. All _IfcDocumentReference_'s that utilize the _IfcDocumentInformation_ are accessible by the inverse relationship _HasDocumentReferences_.

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Attribute _HasDocumentReferences_ changed to be inverse, attribute _Location_ added, and attribute _ElectronicFormat_ modified.

## Attributes

### Identification
Identifier that uniquely identifies a document.
> IFC4 CHANGE Attribute renamed from _DocumentId_.

### Name
File name or document name assigned by owner.

### Description
Description of document and its content.

### Location
Resource identifier or locator, provided as URI, URN or URL, of the document information for online references.
> IFC4 CHANGE New attribute added at the place of the removed attribute _DocumentReferences_.

### Purpose
Purpose for this document.

### IntendedUse
Intended use for this document.

### Scope
Scope for this document.

### Revision
Document revision designation.

### DocumentOwner
Information about the person and/or organization acknowledged as the 'owner' of this document. In some contexts, the document owner determines who has access to or editing right to the document.

### Editors
The persons and/or organizations who have created this document or contributed to it.

### CreationTime
Date and time stamp when the document was originally created.
> IFC4 CHANGE The data type has been changed to _IfcDateTime_, the date time string according to ISO8601.

### LastRevisionTime
Date and time stamp when this document version was created.
> IFC4 CHANGE The data type has been changed to _IfcDateTime_, the date time string according to ISO8601.

### ElectronicFormat
Describes the media type used in various internet protocols, also referred to as "Content-type", or "MIME-type (Multipurpose Internet Mail Extension), of the document being referenced. It is composed of (at least) two parts, a type and a subtype.
> NOTE The iana (Internet Assigned Numbers Authority) published the media types.

> EXAMPLE 'image/png' denotes an image type of png (Portable Network Graphics) subtype, 'application/pdf' denotes an application specific type of pdf (Portable Document Format) subtype

> IFC4 CHANGE The data type has been changed from entity data type to _IfcIdentifier_.

### ValidFrom
Date when the document becomes valid.
> IFC4 CHANGE The data type has been changed to _IfcDate_, the date string according to ISO8601.

### ValidUntil
Date until which the document remains valid.
> IFC4 CHANGE The data type has been changed to _IfcDate_, the date string according to ISO8601.

### Confidentiality
The level of confidentiality of the document.

### Status
The current status of the document. Examples of status values that might be used for a document information status include:
- DRAFT
- FINAL DRAFT
- FINAL
- REVISION

### DocumentInfoForObjects
The document information with which objects are associated.
> IFC4 CHANGE New inverse attribute.

### HasDocumentReferences
The document references to which the document applies

### IsPointedTo
An inverse relationship from the IfcDocumentInformationRelationship to the related documents.

### IsPointer
An inverse relationship from the IfcDocumentInformationRelationship to the relating document.
