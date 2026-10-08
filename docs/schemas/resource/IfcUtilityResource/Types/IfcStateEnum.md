# IfcStateEnum

The _IfcStateEnum_ enumeration identifies the state or accessibility of the object (for example, read/write, locked).
<!-- end of short definition -->

Valid enumerations are:

> HISTORY New enumeration in IFC2.0.

> IFC2x3 CHANGE This concept was initially introduced in IFC2.0 as _IfcModifiedFlag_ of type BINARY(3) FIXED and has been modified in R2x3 to an enumeration. It was initially introduced as a first step towards providing facilities for partial model exchange and is intended for use primarily by a model server so that an application can identify the state of the object.

## Items

### READWRITE
Object is in a Read-Write state. It may be modified by an application.

### READONLY
Object is in a Read-Only state. It may be viewed but not modified by an application.

### LOCKED
Object is in a Locked state. It may not be accessed by an application.

### READWRITELOCKED
Object is in a Read-Write-Locked state. It may not be accessed by an application.

### READONLYLOCKED
Object is in a Read-Only-Locked state. It may not be accessed by an application.
