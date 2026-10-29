# IfcOrganization

A named and structured grouping with a corporate identity.
<!-- end of short definition -->

> NOTE The relationships between _IfcOrganization_'s, like between department within a company, can be expressed using the objectified relationship _IfcOrganizationRelationship_.

> NOTE Entity adapted from **organization** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.1.

> IFC4 CHANGE Attribute 'Id' renamed to _Identification_.

## Attributes

### Identification
Identification of the organization.

### Name
The word, or group of words, by which the organization is referred to.

### Description
Text that relates the nature of the organization.

### Roles
Roles played by the organization.

### Addresses
Postal and telecom addresses of an organization.

> NOTE There may be several addresses related to an organization.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used. Use Pset_Address instead related to an IfcActor with _TheActor_ pointing to this entity.

### IsRelatedBy
The inverse relationship for relationship RelatedOrganizations of IfcOrganizationRelationship.

### Relates
The inverse relationship for relationship RelatingOrganization of IfcOrganizationRelationship.

### Engages
Inverse relationship to IfcPersonAndOrganization relationships in which IfcOrganization is engaged.
