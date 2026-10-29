# IfcChangeActionEnum

_IfcChangeActionEnum_ identifies the type of change that might have occurred to the object during the last session (for example, added, modified, deleted). This information is required in a partial model exchange scenario so that an application or model server will know how an object might have been affected by the previous application. Valid enumerations are:
<!-- end of short definition -->

Consider Application A will create an IFC dataset that it wants to publish to others for modification and have the ability to subsequently merge these changes back into the original model. Before publication, it may want to set the _IfcChangeActionEnum_ to NOCHANGE to establish a baseline so that other application changes can be easily identified. Application B then receives this IFC dataset and adds a new object and sets _IfcChangeActionEnum_ to ADDED with Application B defined as the OwningApplication. Application B then modifies an existing object and (re)defines the LastModifiedDate to the time of the modification, LastModifyingUser to the _IfcPersonAndOrganization_ making the change, and sets the LastModifyingApplication to Application B. When Application A receives this modified dataset, it can determine which objects have been added and modified by Application B and either merge or reject these changes as necessary. Consequently, the intent is that an application only modifies the value of _IfcChangeActionEnum_ when it does something to the object, with the further intent that a model server is responsible for clearing the _IfcChangeActionEnum_ back to NOCHANGE when it is ready to be republished.

> HISTORY New enumeration in IFC2.0.

> IFC4 CHANGE Enumerators MODIFIEDADDED and MODIFIEDDELETED have been removed

## Items

### NOCHANGE
Object has not been modified.

### MODIFIED
A modification to the object has been made by the user and application defined by the LastModifyingUser and LastModifyingApplication respectively.

### ADDED
The object has been created by the user and application defined by the OwningUser and OwningApplication respectively.

### DELETED
The object has been deleted by the user and application defined by the LastModifyingUser and LastModifyingApplication respectively.

### NOTDEFINED
The change action is not known or has not been defined.
