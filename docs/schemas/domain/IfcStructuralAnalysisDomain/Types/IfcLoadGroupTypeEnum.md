# IfcLoadGroupTypeEnum

This enumeration is used to distinguish between different levels of load grouping. It allows to differentiate between load groups, load cases, and load combinations.
<!-- end of short definition -->

> HISTORY New enumeration in IFC2x2.

> IFC4 CHANGE LOAD_COMBINATION_GROUP deprecated. Load cases are directly assigned to load combinations with different factors for each load case—load combination pair by means of _IfcRelAssignsToGroupByFactor_.

## Items

### LOAD_GROUP
Groups instances of subtypes of _IfcStructuralAction_. It shall be used as a container for loads grouped together for specific purposes, such as loads which are part of a special load pattern.

### LOAD_CASE
Groups LOAD_GROUPs and instances of subtypes of _IfcStructuralAction_.
   It should be used as a container for loads with the same origin.

### LOAD_COMBINATION
An intermediate level between LOAD_CASE and LOAD_COMBINATION. This level is obsolete and deprecated. Before the introduction of _IfcRelAssignsToGroupByFactor_, the purpose of this level was to provide a factor with which one or more LOAD_CASEs occur in a LOAD_COMBINATION.

### USERDEFINED
A grouping level which does not follow the standard hierarchy of load group types.

### NOTDEFINED
The grouping level is not yet known.
