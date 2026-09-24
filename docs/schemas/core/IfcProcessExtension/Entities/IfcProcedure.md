# IfcProcedure

An _IfcProcedure_ is a logical set of actions to be taken in response to an event or to cause an event to occur.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2

> IFC4 CHANGE _ProcedureType_ renamed to _PredefinedType_ and made optional (upward compatible). Where rules WR1 and WR2 have been removed.

### Use definitions

_IfcProcedure_ is used to capture information about stepped processes such as calibration, start/stop procedures for equipment items, designated actions to take in the event of an emergency etc. A procedure is not a task, but may describe a set of tasks and their order of occurrence in response to or to cause an event.

As shown in Figure 1, _IfcProcedure_ does not restrict anything but describes specific steps of how something should happen. While a procedure does control/restrict in the sense of indicating "this is how the task should be performed" by nature of describing inner detail, this is not different than parts of a product indicating "this is how the parts should be assembled". Consequently, it doesn't restrict the outer item as a whole but provides inner detail of the item.

![procedure example](../../../../figures/ifcprocedure_example.png)

Figure 1 — Procedure relationships

## Attributes

### PredefinedType
Identifies the predefined types of a procedure from which
  the type required may be set.

## Formal Propositions

### HasName
The Name attribute should be inserted to describe the task name.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.

## Concepts

### Control Assignment

An _IfcProcedure_ may be assigned to an _IfcWorkCalendar_ to indicate times when such procedure may be performed using _IfcRelAssignsToControl_; otherwise the effective calendar is determined by the nearest _IfcProcess_ ancestor with a calendar assigned. Advisory notes should be assigned to the specific _IfcProcess_ for which it gives advice using _IfcRelAssignsToProcess_.

### Object Nesting

The _IfcProcedure_ may be contained within an _IfcTask_ or _IfcProcedure_ using the _IfcRelNests_ relationship. An _IfcProcedure_ may in turn nest other _IfcProcedure_ or _IfcEvent_ entities. Such nesting indicates decomposed level of detail.

### Object Typing

_IfcProcedure_ defines the anticipated or actual occurrence of any procedure; common information about procedure types is handled by _IfcProcedureType_.

### Process Assignment

> NOTE A particular type of _IfcProcedure_ is a caution, warning or other form of advisory note. Typically, it is anticipated that such a procedure would be assigned to the specific _IfcProcess_ for which it gives advice using _IfcRelAssignsToProcess_.

### Product Assignment

For building operation scenarios, _IfcProcedure_ may be assigned to a product (_IfcElement_ subtype) using _IfcRelAssignsToProduct_ to indicate a specific product occurrence that performs the procedure.

> EXAMPLE An _IfcActuator_ may have a "Close" procedure. If the _IfcProcedure_ is defined by an _IfcProcedureType_ and the _IfcProcedureType_ is assigned to a product type (using _IfcRelAssignsToProduct_), then the _IfcProcedure_ must be assigned to one or more occurrences of the specified product type using _IfcRelAssignsToProduct_.

### Property Sets for Objects



### Sequential Connectivity

The relationship _IfcRelSequence_ is used to indicate control flow. An _IfcProcedure_ as a successor to an _IfcEvent_ indicates that the procedure should be performed in response to the event. An _IfcProcedure_ as a predecessor to an _IfcEvent_ indicates that the event should be triggered following the procedure. As procedures have arbitrary duration, the _IfcRelSequence.SequenceType_ attribute has no effect on an _IfcProcedure_ but still applies to the opposite end of the relationship if _IfcTask_ is used.

