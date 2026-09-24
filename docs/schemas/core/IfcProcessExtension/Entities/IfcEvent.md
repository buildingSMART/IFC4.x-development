# IfcEvent

An _IfcEvent_ is something that happens that triggers an action or response.
<!-- end of short definition -->

> HISTORY New entity in IFC4

### Use definitions

_IfcEvent_ is used to capture information about particular things that happen or that may happen. Particularly used in work plans (or process maps) they identify e.g. a point at which a message containing information may be issued or at which a rule or constraint is invoked.

## Attributes

### PredefinedType
Identifies the predefined types of an event from which the type required may be set.

### EventTriggerType
Identifies the predefined types of event trigger from which the type required may be set.

### UserDefinedEventTriggerType
A user defined event trigger type, the value of which is asserted when the value of an event trigger type is declared as USERDEFINED.

### EventOccurenceTime
The date and/or time at which an event occurs.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.

### CorrectTypeAssigned
Either the _EventTriggerType_ attribute is unset, or the attribute _UserDefinedEventTriggerType_ must be asserted when the value of _EventTriggerType_ is set to _USERDEFINED_.

## Concepts

### Control Assignment

An _IfcEvent_ may be assigned to an _IfcWorkCalendar_ to indicate times when such event is active using _IfcRelAssignsToControl_; otherwise the effective calendar is determined by the nearest _IfcProcess_ ancestor with a calendar assigned.

### Object Nesting

_IfcEvent_ may be contained within an _IfcTask_ using the _IfcRelNests_ relationship. The event is considered active during the time period of the enclosing task (including any assigned _IfcWorkCalendar_); that is such event may be triggered within the task time period but not outside of it. As an _IfcEvent_ is considered to be atomic, no use is anticipated for nesting processes inside the event.

### Object Typing

The _IfcEvent_ defines the anticipated or actual occurrence of any event; common information about event types is handled by _IfcEventType_.

### Product Assignment

For building operation scenarios, _IfcEvent_ may be assigned to a product (_IfcElement_ subtype) using _IfcRelAssignsToProduct_ to indicate a specific product occurrence that sources the event.

> EXAMPLE An _IfcSensor_ for a motion sensor may have a "Motion Sensed" event. If the _IfcEvent_ is defined by an _IfcEventType_ and the _IfcEventType_ is assigned to a product type (using _IfcRelAssignsToProduct_), then the _IfcEvent_ must be assigned to one or more occurrences of the specified product type using _IfcRelAssignsToProduct_.

### Property Sets for Objects



### Sequential Connectivity

The relationship _IfcRelSequence_ is used to indicate control flow. An _IfcEvent_ as a predecessor (_IfcRelSequence.RelatingProcess_) indicates that the succeeding process (typically _IfcProcedure_ or _IfcTask_) is triggered in response to the event. An _IfcEvent_ as a successor (_IfcRelSequence.RelatedProcess_) indicates that the completion of the preceeding process causes the event to be triggered. As events have zero duration, the _IfcRelSequence.SequenceType_ attribute has no effect on an _IfcEvent_ but still applies to the opposite end of the relationship if _IfcTask_ is used.

