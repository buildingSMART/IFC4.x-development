# IfcPerson

This entity represents an individual human being.
<!-- end of short definition -->

> NOTE Many countries have legislation concerning the identification of individual persons within databases. Although the intent of the IFC Model is to act as a specification for data exchange and sharing, an IFC file might in some situations be considered to be a database that enables identification of a particular person under the terms of such legislation. Users should be aware of the constraints of legislation that might apply in the places where IFC files are used.

> NOTE Entity adapted from **person** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.1.

> IFC4 CHANGE Attribute _Id_ renamed to _Identification_. WHERE rule relaxed to allow omission of names if _Identification_ is provided.

## Attributes

### Identification
Identification of the person.

### FamilyName
The name by which the family identity of the person may be recognized.
> NOTE Depending on geographical location and culture, family name may appear either as the first or last component of a name.

### GivenName
The name by which a person is known within a family and by which he or she may be familiarly recognized.
> NOTE Depending on geographical location and culture, given name may appear either as the first or last component of a name.

### MiddleNames
Additional names given to a person that enable their identification apart from others who may have the same or similar family and given names.
> NOTE Middle names are not normally used in familiar communication but may be asserted to provide additional identification of a particular person if necessary. They may be particularly useful in situations where the person concerned has a family name that occurs commonly in the geographical region.

### PrefixTitles
The word, or group of words, which specify the person's social and/or professional standing and appear before his/her names.

### SuffixTitles
The word, or group of words, which specify the person's social and/or professional standing and appear after his/her names.

### Roles
Roles played by the person.

### Addresses
Postal and telecommunication addresses of a person.

> NOTE A person may have several addresses.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used. Use Pset_Address instead related to an IfcActor with _TheActor_ pointing to this entity.

### EngagedIn
The inverse relationship to IfcPersonAndOrganization relationships in which IfcPerson is engaged.

## Formal Propositions

### IdentifiablePerson
Requires that the identification or/ and the family name or/ and the given name is provided as minimum information.

### ValidSetOfNames
If middle names are provided, the family name or/ and the given name shall be provided too.
