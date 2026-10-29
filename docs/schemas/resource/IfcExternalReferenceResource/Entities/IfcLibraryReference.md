# IfcLibraryReference

An _IfcLibraryReference_ is a reference into a library of information by _Location_ (provided as a URI). It also provides an optional inherited _Identification_ key to allow more specific references to library sections or tables. The inherited _Name_ attribute allows for a human interpretable identification of the library item. Also, general information on the library from which the reference is taken, is given by the _ReferencedLibrary_ relation which identifies the relevant occurrence of _IfcLibraryInformation_.
<!-- end of short definition -->

The _IfcLibraryReference_ additionally provides the capability to handle multilingual library entries. The _Language_ attribute then holds the language tag for the language used by the strings kept in the _Name_ and the _Description_ attribute.

Depending on the type of technology used by the library, different IfcLibraryReference.Identification identifiers will be appropriate:

Publisher | Technology | Identifier
--- | --- | ---
ASHRAE | BACnet | 32-bit decimal BACnetObjectIdentifier indicating type ID and instance ID (e.g.'12.15' for Digital Input #15).
Brick Development Team | Brick | Full URI with no abbreviation (e.g. 'http://example.org/digitaltwin#AHU01', not 'digitaltwin:AHU01')
IETF | IPv4 | 32-bit decimal address for an IPv4 network (e.g.'192.168.1.1').
IETF | IPv6 | 128-bit hexadecimal address for an IPv6 network.
IETF | MAC | 48-bit hexadecimal form of MAC address.
ISOIEC | LonTalk | 48-bit hexadecimal neuron ID.
OPCFoundation | OPC | Hierarchical ItemID in alphanumeric form (i.e. 'B204.Tank2.Temperature)
SmartLabs | Insteon | 24-bit hexadecimal instance address.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE _Description_ and _Language_ attribute added; _ReferencedLibrary_ attribute added (reversing previous ReferenceIntoLibrary inverse relationship).

## Attributes

### Description
Additional description provided for the library reference.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### Language
The language in which a library reference is expressed.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### ReferencedLibrary
The library information that is being referenced.

### LibraryRefForObjects
The library reference with which objects are associated.
> IFC4 CHANGE New inverse attribute.
