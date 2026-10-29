# IfcLibraryInformation

> NOTE This functionality has been superseded by the URI convention in IFC. More info on the use of URI references in different IFC versions can be found on [this documentation page](https://github.com/buildingSMART/bSDD/blob/master/Documentation/bSDD-IFC%20documentation.md). The use of IfcLibraryInformation is discouraged. 

An _IfcLibraryInformation_ describes an external structured store of information, normally organized in a manner which allows information lookup through an index or reference value. _IfcLibraryInformation_ provides the library _Name_ and optional _Description_, _Version_, _VersionDate_ and _Publisher_ attributes. A _Location_ may be added for electronic access to the library.
<!-- end of short definition -->

> HISTORY New entity in IFC2x.

> IFC4 CHANGE _Location_ and _Description_ attributes added; _Publisher_ and _VersionDate_ data type changed; _HasLibraryReferences_ inverse attribute added (previous LibraryReference changed to inverse).

> IFC4.3.0.0 CHANGE IfcLibraryInformation now is explicitly defined for use to reference external systems.

## Attributes

### Name
The name which is used to identify the library.

### Version
Identifier for the library version used for reference.

### Publisher
Information of the organization that acts as the library publisher.
> IFC4 CHANGE The data type has been changed to _IfcActorSelect_.

### VersionDate
Date of the referenced version of the library.
> IFC4 CHANGE The data type has been changed to _IfcDateTime_, the date and time string according to ISO8601.

### Location
Resource identifier or locator, provided as URI, URN or URL, of the library information for online references.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### Description
Additional description provided for the library revision information.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### LibraryInfoForObjects
The library information with which objects are associated.
> IFC4 CHANGE New inverse attribute.

### HasLibraryReferences
The library references to which the library information applies.
