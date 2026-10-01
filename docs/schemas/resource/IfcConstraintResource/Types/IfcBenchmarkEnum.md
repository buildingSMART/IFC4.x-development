# IfcBenchmarkEnum

_IfcBenchmarkEnum_ is an enumeration used to identify the logical comparators that can be applied in conjunction with constraint values.
<!-- end of short definition -->

> HISTORY New enumeration in IFC2.0

> IFC4 CHANGE Extended to include comparators for item-set and set-item comparisons: INCLUDES, NOTINCLUDES, INCLUDEDIN and NOTINCLUDEDIN, to test if an individual item is a member of a given aggregation, or if an aggregation has a given individual item as a member.

## Items

### GREATERTHAN
Identifies that a value must be greater than that set by the constraint.

### GREATERTHANOREQUALTO
Identifies that a value must be either greater than or equal to that set by the constraint.

### LESSTHAN
Identifies that a value must be less than that set by the constraint.

### LESSTHANOREQUALTO
Identifies that a value must be either less than or equal to that set by the constraint.

### EQUALTO
Identifies that a value must be equal to that set by the constraint.

### NOTEQUALTO
Identifies that a value must be not equal to that set by the constraint.

### INCLUDES
Identifies that an aggregation (set, list or table) must include the value (individual item) set by the constraint.

### NOTINCLUDES
Identifies that an aggregation (set, list or table) must not include the value (individual item) set by the constraint.

### INCLUDEDIN
Identifies that a value (individual item) must be included in the aggregation (set, list or table) set by the constraint.

### NOTINCLUDEDIN
Identifies that a value (individual item) must not be included in the aggregation (set, list or table) set by the constraint.
