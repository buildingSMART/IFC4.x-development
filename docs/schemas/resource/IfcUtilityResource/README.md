IfcUtilityResource
==================

The resource schema _IfcUtilityResource_ deals with the general concepts of Ownership and Change. It also includes a basic information construct: Tables. The classes of this schema are referenced throughout the whole IFC Object Model by all of its model layers. The _IfcUtilityResource_ schema consequently contains model specifications for specifying the information content of a number of utility types.

This schema contains the following concepts:

* Ownership
* History
* Table

Each object, relationship and type definition will provide information about their current ownership. Ownership information is the currently "owning" application and the owning (responsible) actor. This ownership information can be used for access and change permissions. Ownership can be transferred from one person to another through the life cycle of a project.

The history of an IFC object is captured simply in the form of last modifying user, application and date.

The table datatype is general purpose and may be used for any two dimensional matrix type document. It allows information to be recorded in rows and columns where each column is labeled with the type of information it contains. The model does not allow for any mathematical operations on the information content of a table (that is, it does not function as a spreadsheet).

> HISTORY  The various types of registries were removed from this schema in IFC2.0 since the method used within applications to store those types of information could differ between different applications.

> IFC2x CHANGE  This schema was significantly simplified in IFC2x to reduce overhead.
