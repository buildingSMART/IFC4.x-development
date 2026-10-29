# IfcOwnerHistory

_IfcOwnerHistory_ defines all history and identification related information. In order to provide fast access it is directly attached to all independent objects, relationships and properties.
<!-- end of short definition -->

_IfcOwnerHistory_ is used to identify the creating and owning application and user for the associated object, as well as capture the last modifying application and user.

> HISTORY New entity in IFC1.0.

> IFC4 CHANGE ChangeAction is now optional and a related WHERE rule enforces conditions when it is asserted.

**Informal Propositions**

1. If LastModifiedDate is defined but ChangeAction is not asserted, then the state of ChangeAction is assumed to be UNDEFINED.
2. If both LastModifiedDate and ChangeAction are asserted, then the state of ChangeAction applies to the value asserted in LastModifiedDate.

## Attributes

### OwningUser
Direct reference to the end user who currently "owns" this object. Note that IFC includes the concept of ownership transfer from one user to another and therefore distinguishes between the Owning User and Creating User.

### OwningApplication
Direct reference to the application which currently "owns" this object on behalf of the owning user of the application. Note that IFC includes the concept of ownership transfer from one application to another and therefore distinguishes between the Owning Application and Creating Application.

### State
Enumeration that defines the current access state of the object.

### ChangeAction
Enumeration that defines the actions associated with changes made to the object.

### LastModifiedDate
Date and Time expressed in UTC (Universal Time Coordinated, formerly Greenwich Mean Time or GMT) at which the last modification was made by LastModifyingUser and LastModifyingApplication.

### LastModifyingUser
User who carried out the last modification using LastModifyingApplication.

### LastModifyingApplication
Application used to make the last modification.

### CreationDate
The date and time expressed in UTC (Universal Time Coordinated, formerly Greenwich Mean Time or GMT) when first created by the original OwningApplication. Once defined this value remains unchanged through the lifetime of the entity.

## Formal Propositions

### CorrectChangeAction
If ChangeAction is asserted and LastModifiedDate is not defined, ChangeAction must be set to NOTDEFINED
