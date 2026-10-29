# IfcWorkControl

An _IfcWorkControl_ is an abstract supertype which captures information that is common to both _IfcWorkPlan_ and _IfcWorkSchedule_.
<!-- end of short definition -->

> HISTORY New entity in IFC2x

> CHANGE IFC4 Corrected assignment of resources to work control in documentation. Assignment of tasks to work control updated based on changes of task time definitions and the introduction of a summary task. Identifier has been renamed (now Identification) and promoted to supertype _IfcControl_

A work control may have resources assigned to it. This is handled by the _IfcRelAssignsToControl_ relationship. A work control should also define a context that gives further information about its usage. If no special context information is required then the _IfcProject_ instance as a global context should be used instead. An explicit link between the work control and the _IfcProject_ via _IfcRelDeclares_ should then be provided.

The attribute _IfcWorkControl.Purpose_ is used to define the purpose of either a work schedule or a work plan. In the case of _IfcWorkPlan_, the purpose attribute can be used to determine if the work plan is for cost estimating, task scheduling or some other defined purpose.

## Attributes

### CreationDate
The date that the plan is created.

### Creators
The authors of the work plan.

### Purpose
A description of the purpose of the work schedule.

### Duration
The total duration of the entire work schedule.

### TotalFloat
The total time float of the entire work schedule.

### StartTime
The start time of the schedule.

### FinishTime
The finish time of the schedule.

## Concepts

### Control Assignment

From IFC4 onwards the assignment of tasks to the work control is handled by the IfcRelAssignsToControl relationship. IfcRelAssignsTasks as used in previous IFC releases has been deleted and can not be used any longer. Another change in IFC4 is that it is not necessary to assign each task to a work control as it is regarded to be sufficient if the summary task (root task in the task hierarchy defined through IfcRelNests relationships) is assigned to a work control.

### Property Sets for Objects



