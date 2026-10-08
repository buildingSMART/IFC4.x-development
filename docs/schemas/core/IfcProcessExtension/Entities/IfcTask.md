# IfcTask

An _IfcTask_ is an identifiable unit of work to be carried out in a construction project.
<!-- end of short definition -->

A task is typically used to describe an activity for the construction or installation of products, but is not limited to these types. For example it might be used to describe design processes, move operations and other design, construction and operation related activities as well.

Quantities of resources consumed by the task are dealt with by defining the _IfcElementQuantity_ for the resource and not at the instance of _IfcTask_.

> HISTORY New entity in IFC1.0. Renamed from _IfcWorkTask_ in IFC2x.

> IFC4 CHANGE Attributes _TaskTime_ and _PredefinedType_ added. _IfcMove_ and _IfcOrderRequest_ have been removed in IFC4 and are now represented by _IfcTask_. _IfcRelAssignsTasks_ relationship has been removed as well.

### Attribute use definition

Each occurrence of _IfcTask_ is given a name that is indicative of its content (_IfcRoot.Name_). A textual description of the task may be provided and this may be further elaborated by a narrative long description (_IfcProcess.LongDescription_). A work method may be declared for the method of work used in carrying out a task. A task is identified as being either a milestone task or not. A milestone task is defined by the marker _IsMilestone_. and has no duration. A status and priority for each task may also be set.

### Time and duration use definition

Compared to previous IFC releases, basic task time information (scheduled start time, scheduled finish time, duration) is now directly attached to _IfcTask_ through the _TaskTime_ attribute. Regular tasks are defined through _IfcTaskTime_. Recurring tasks are defined through _IfcTaskTimeRecurring_. In case a regular task is derived from a recurring task both tasks should be linked together through a _IfcRelNests_ relationship, where _IfcRelNests.IsNestedBy_ points to the recurring task and _IfcRelNests.Nests_ points to all regular tasks that have been derived from the recurring task.

### Representation of other activities

The use definitions for _IfcTask_ have been generalised to represent other activities as well, including activities that had been defined by own entities in previous IFC releases. This includes

* Order actions
* Move operations

_IfcTask_ represents an order that might be carried out by a Helpdesk acting the role of interface for the organization between the facility user and the functional requirement of fulfilling their needs. The actual task represented by the _IfcTask_ entity is turning a request into an order and initiating the action that will enable the order to be completed. The _IfcProjectOrder_ or one of its subtypes including maintenance work order, is related to the _IfcTask_ using _IfcRelAssignsToControl_.

_IfcTask_ can also be used to describe an activity that moves people, groups within an organization or complete organizations together with their associated furniture and equipment from one place to another. It thus replaces the previous IFC entity _IfcMove_. The functionality is represented in _IfcTask_ as follows:

* Move from: The place from which actors and their associated equipment are moving. Use _IfcRelAssignsToProcess_ where _RelatingProcess_ points to the task and _RelatedObjects_ holds the location(s) from which to move.
* Move to: The place to which actors and their associated equipment are moving. Use _IfcRelAssignsToProduct_ where _RelatedObjects_ points to the task(s) and _RelatingProduct_ points to the location to which to move.
* Punch list: A list of points concerning a move that require attention. Use _LongDescription_ or else identify sub-tasks to track punch list items individually via _IfcRelNests_.

## Attributes

### Status
Current status of the task.

> NOTE Particular values for status are not specified, these should be determined and agreed by local usage. Examples of possible status values include 'NOTSTARTED', 'STARTED', 'COMPLETED'.

### WorkMethod
The method of work used in carrying out a task.

> NOTE This attribute should not be used if the work method is specified for the _IfcTaskType_

### IsMilestone
Identifies whether a task is a milestone task (= TRUE) or not (= FALSE).

> NOTE In small project planning applications, a milestone task may be understood to be a task having no duration. As such, it represents a singular point in time.

### Priority
A value that indicates the relative priority of the task (in comparison to the priorities of other tasks).

### TaskTime
Time related information for the task.

> IFC4 CHANGE Attribute added

### PredefinedType
Identifies the predefined types of a task from which the type required may be set.

> IFC4 CHANGE Attribute added

## Formal Propositions

### HasName
The _Name_ attribute should be inserted to describe the task name.

### CorrectPredefinedType
The attribute _ObjectType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.

## Concepts

### Classification Association

An _IfcTask_ may be assigned a Work Breakdown Structure (WBS) code from of a published external structure or company standard. As well as being used to designate the code, the classification structure also enables the source of the work breakdown structure classification to be identified.

### Constraint Association

Constraints may be applied to a task's scheduled duration, start, or finish, by setting the _IfcMetric.ReferencePath_ to the corresponding attribute on the _IfcTaskTime_ entity.

Figure FIXEDDURATION indicates fixed duration of task with _ConstraintGrade=HARD_ and _Benchmark=EQUALTO_ such that changes to an assigned _IfcConstructionResource.Usage.ScheduleWork_ should impact _IfcConstructionResource.Usage.ScheduleUsage_, and vice-versa.

```
digraph dot_neato {
IfcTask [pos="0,0!"];
IfcTaskTime [pos="0,-70!"];

IfcRelAssociatesConstraint [label=<IfcRelAssociates<br/>Constraint>, pos="200,0!"];

IfcObjective [label=<{IfcObjective | ObjectiveQualifier: PARAMETER}>, pos="400,0!"];
IfcMetric [label=<{IfcMetric | ConstraintGrade: HARD<br />Benchmark: EQUALTO}>, pos="400,-70!"];
IfcReference [label=<{IfcReference | AttributeIdentifier: TaskTime}>, pos="400,-140!"];
IfcReference2 [label=<{IfcReference | AttributeIdentifier: ScheduleDuration }>, pos="400,-210!"];

IfcTask -> IfcTaskTime [label="TaskTime"]
IfcRelAssociatesConstraint -> IfcTask [headlabel="RelatedObjects[1]", labelangle=90, labeldistance="3"]
IfcRelAssociatesConstraint -> IfcObjective [taillabel="RelatingConstraint", labelangle=90, labeldistance="3"]
IfcObjective -> IfcMetric [headlabel="BenchmarkValues[1]"];
IfcMetric -> IfcReference [headlabel="ReferencePath"];
IfcReference -> IfcReference2 [headlabel="InnerReference"];
}
```

Figure FIXEDDURATION — Constraining the task duration

Figure STARTCONSTRAINT indicates how to constrain the scheduled start date of the task. Depending on the _ConstraintGrade_ and _Benchmark_ the constraint may indicate different meanings as shown in Table STARTCONSTRAINTTYPES.

ConstraintGrade | Benchmark | Indicates
--- | --- | ---
HARD | EQUALTO | Must start on
HARD | GREATERTHANOREQUALTO | Start no earlier than
HARD | LESSTHANOREQUALTO | Start no later than
SOFT | LESSTHAN | Start as soon as possible

Table STARTCONSTRAINTTYPES — Different constraints that can be applied to a start date

```
digraph dot_neato {
IfcTask [pos="0,0!"];
IfcTaskTime [pos="0,-70!"];

IfcRelAssociatesConstraint [label=<IfcRelAssociates<br/>Constraint>, pos="200,0!"];

IfcObjective [label=<{IfcObjective | ObjectiveQualifier: PARAMETER}>, pos="400,0!"];
IfcMetric [label=<{IfcMetric | ConstraintGrade: SOFT<br />Benchmark: LESSTHAN}>, pos="400,-70!"];
IfcReference [label=<{IfcReference | AttributeIdentifier: TaskTime}>, pos="400,-140!"];
IfcReference2 [label=<{IfcReference | AttributeIdentifier: ScheduleStart }>, pos="400,-210!"];

IfcTask -> IfcTaskTime [label="TaskTime"]
IfcRelAssociatesConstraint -> IfcTask [headlabel="RelatedObjects[1]", labelangle=90, labeldistance="3"]
IfcRelAssociatesConstraint -> IfcObjective [taillabel="RelatingConstraint", labelangle=90, labeldistance="3"]
IfcObjective -> IfcMetric [headlabel="BenchmarkValues[1]"];
IfcMetric -> IfcReference [headlabel="ReferencePath"];
IfcReference -> IfcReference2 [headlabel="InnerReference"];
}
```

Figure STARTCONSTRAINT — Constraining the task start date to start as soon as possible

Figure FINISHCONSTRAINT indicates how to constrain the scheduled finish date of the task. Depending on the _ConstraintGrade_ and _Benchmark_ the constraint may indicate different meanings as shown in Table FINISHCONSTRAINTTYPES.

ConstraintGrade | Benchmark | Indicates
--- | --- | ---
HARD | EQUALTO | Must finish on
HARD | GREATERTHANOREQUALTO | Finish no earlier than
HARD | LESSTHANOREQUALTO | Finish no later than
SOFT | GREATERTHAN | Finish as late as possible

Table FINISHCONSTRAINTTYPES — Different constraints that can be applied to a start date

```
digraph dot_neato {
IfcTask [pos="0,0!"];
IfcTaskTime [pos="0,-70!"];

IfcRelAssociatesConstraint [label=<IfcRelAssociates<br/>Constraint>, pos="200,0!"];

IfcObjective [label=<{IfcObjective | ObjectiveQualifier: PARAMETER}>, pos="400,0!"];
IfcMetric [label=<{IfcMetric | ConstraintGrade: SOFT<br />Benchmark: GREATERTHAN}>, pos="400,-70!"];
IfcReference [label=<{IfcReference | AttributeIdentifier: TaskTime}>, pos="400,-140!"];
IfcReference2 [label=<{IfcReference | AttributeIdentifier: ScheduleFinish }>, pos="400,-210!"];

IfcTask -> IfcTaskTime [label="TaskTime"]
IfcRelAssociatesConstraint -> IfcTask [headlabel="RelatedObjects[1]", labelangle=90, labeldistance="3"]
IfcRelAssociatesConstraint -> IfcObjective [taillabel="RelatingConstraint", labelangle=90, labeldistance="3"]
IfcObjective -> IfcMetric [headlabel="BenchmarkValues[1]"];
IfcMetric -> IfcReference [headlabel="ReferencePath"];
IfcReference -> IfcReference2 [headlabel="InnerReference"];
}
```

Figure FINISHCONSTRAINT — Constraining the task finish date to finish as late as possible

### Control Assignment

Occurrences of _IfcTask_ may be assigned to an _IfcWorkControl_ (either a work plan or a work schedule) through _IfcRelAssignsToControl_. Please note that the _IfcRelAssignsTasks_ relationship class has been removed in IFC4 and is no longer available.

### Object Nesting

_IfcTask_ may be contained within an _IfcTask_ using the _IfcRelNests_ relationship. An _IfcTask_ may in turn nest other _IfcTask_, _IfcProcedure_ or _IfcEvent_ entities. Such nesting indicates decomposed level of detail. From IFC4 onwards it is required to have a summary task (root of all tasks), which is used to define a link to the work plan or work schedule. All subtasks of the summary tasks are then implicitly linked to this work plan or work schedule. Please note that the summary task is used for data organization and not meant to store typical task information as defined by the user. It is therefore recommended that the summary task is hidden from the user to avoid confusion. Please also note that _IfcRelNests_ is used to show the dependency between regular tasks and recurring task definitions (please see the section about time and duration use definitions).

As shown in Figure 1, the installation of a number of items of equipment within a particular space may be the subject of a single task which is identified as 'fix equipment in space 123'. _IfcTask_ represents the occurrence of a work performance of a type of process in a construction plan.

![task example](../../../../figures/ifctask_example.png)

Figure 1 — Task visualization

A task may nest other tasks as sub-items; the nesting relationship is modeled by _IfcRelNests_ as shown in Figure 2. For example, the construction of a stud wall may be designated as a nesting task named 'install wall #1' including other tasks such as 'install dry wall', 'install studs', 'wall taping', and 'erect wall' as sub-processes. A value that indicates the relative tree view position of the task (in comparison to the tree view position of other tasks and the task hierarchy defined by _IfcRelNests_).

The task order information that is used for viewing purposes is derived from the order defined by the _IfcRelNests_ relationship and thus is independent of the logical task order defined through _IfcRelSequence_. The hierarchy and order defined through _IfcRelNests_ enables to order the tasks in a tree view or list view structure.

![task instantiation diagram](../../../../figures/ifctask_instantiation_diagram.png)

Figure 2 — Task nesting relationships

A top-level task is declared within the _IfcProject_ using the _IfcRelDeclares_ relationship.

### Object Typing

The _IfcTask_ defines the anticipated or actual occurrence of any task; common information about task types is handled by _IfcTaskType_.

> EXAMPLE It includes fixed duration, fixed unit or fixed work. An _IfcTask_ can be aggregated to a task type in order to specify a task sequence or any time related information, e.g. the duration of a task. Please see the documentation of _IfcTaskType_ for further information.

### Process Assignment

It is suggested to use the 'summary task' (root element of the task hierarchy that is required for task management purposes) to assign all subtask to a work plan or work schedule. Resources used by tasks are assigned by _IfcRelAssignsToProcess_.

### Product Assignment



### Property Sets for Objects



### Sequential Connectivity

The relationship _IfcRelSequence_ is used to indicate control flow. An _IfcTask_ as a successor to an _IfcTask_ indicates logical sequence how these tasks should be performed. _IfcTask_ entities can be triggered or can trigger _IfcEvent_ entities, which is also defined through the relationship _IfcRelSequence_.

