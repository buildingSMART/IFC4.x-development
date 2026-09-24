# IfcExternalReference

An _IfcExternalReference_ is the identification of information that is not explicitly represented in the current model or in the project database (as an implementation of the current model). Such information may be contained in classifications, documents or libraries. The _IfcExternalReference_ identifies a particular item, such as a dictionary entry, a classification notation, or a document reference within the external source.
<!-- end of short definition -->

Only the _Location_ (as a URL) is given to describe the place where the information can be found. Also an optional _Identification_ as a key to allow more specific references (as to sections or tables) is provided. The _Identification_ defines a system interpretable method to identify the relevant part of information at the source. In addition a human interpretable _Name_ can be assigned to identify the information subject, such as a classification code.

_IfcExternalReference_ is an abstract supertype of all external reference entities.

> HISTORY New entity in IFC2x.

> IFC 2x4 CHANGE Attribute _Identification_ renamed from ItemReference, attribute _Location_ datatype changed, and inverse attribute _ExternalReferenceForResources_ added.

## Attributes

### Location
Location, where the external source (classification, document or library) can be accessed by electronic means. The electronic location is provided as an URI, and would normally be given as an URL location string.
> IFC4 CHANGE The data type has been changed from _IfcLabel_ to _IfcURIReference_
> .

### Identification
The _Identification_ provides a unique identifier of the referenced item within the external source (classification, document or library). It may be provided as
* a key, e.g. a classification notation, like NF2.3
* a handle
* a uuid or guid


It may be human readable (such as a key) or not (such as a handle or uuid) depending on the context of its usage (which has to be determined by local agreement).
> IFC4 CHANGE Attribute renamed from _ItemReference_ for consistency.
>

### Name
Optional name to further specify the reference. It can provide a human readable identifier (which does not necessarily need to have a counterpart in the internal structure of the document).

### ExternalReferenceForResources
Reference to all associations between this external reference and objects within the _IfcResourceObjectSelect_ that are tagged by the external reference.

> IFC4 CHANGE New inverse attribute added with upward compatibility.
>

## Formal Propositions

### WR1
One of the attributes of IfcExternalReference should have a value assigned.
