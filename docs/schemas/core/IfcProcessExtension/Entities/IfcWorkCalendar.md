# IfcWorkCalendar

An _IfcWorkCalendar_ defines working and non-working time periods for tasks and resources. It enables to define both specific time periods, such as from 7:00 till 12:00 on 25th August 2009, as well as repetitive time periods based on frequently used recurrence patterns, such as each Monday from 7:00 till 12:00 between 1st March 2009 and 31st December 2009.
<!-- end of short definition -->

> HISTORY New entity in IFC4.

A work calendar is a subtype of _IfcControl_ and thus inherits the feature for controlling other objects through _IfcRelAssignsToControl_, which is used to define a work calendar for tasks (_IfcTask_) and resources (_IfcResource_). It also inherits a name and description attribute, whereas a name shall be given and a description may be given as an indication of its content and usage.

The definition of time periods can be derived from a base calendar and/or modified/defined by a set of working times and non-working exception times. All time periods defined by _IfcWorkCalendar.ExceptionTimes_ override the time periods inherited from the base calendar (base calendar is defined as the next applicable calendar for the task or resource). Thus, exception times replace the working times from the base calendar.

Figure 1 shows the definition of a work calendar, which is defined by a set of work times and exception times. The work times are defined as recurring patterns with optional boundaries (applying from and/or to a specific date). The shown example defines a simple work calendar with working times Monday to Thursday 8:00 to 12:00 and 13:00 to 17:00, Friday 8:00 to 14:00 and as exception every 1st Monday in a month the work starts one hour later - i.e. the working time on every 1st Monday in a month is overridden to be 9:00 to 12:00 and 13:00 to 17:00. Both the working time and the exception time is valid for the period of 01.09.2010 till 30.08.2011.

![task type instantiation diagram](../../../../figures/ifcworkcalendar_instantiation_diagram.png "Figure 1 — Work calendar instantiation")

## Attributes

### WorkingTimes
Set of times periods that are regarded as an initial set-up of working times. Exception times can then further restrict these working times.

### ExceptionTimes
Set of times periods that define exceptions (non-working times) for the given working times including the base calendar, if provided.

### PredefinedType
Identifies the predefined types of a work calendar from which the type required may be set.

> IFC4 CHANGE Attribute added

## Formal Propositions

### CorrectPredefinedType
The attribute _ObjectType_ must be asserted when the value of the _IfcWorkCalendarTypeEnum_ is set to _USERDEFINED_.

## Concepts

### Control Assignment

The base calendar of a work calendar is defined by _IfcRelAssignsToControl_, where _IfcRelAssignsToControl.RelatingControl_ is linked with the base calendar and _IfcRelAssignsToControl.RelatedObjects_ is linked with work calendars that are derived from the base calendar. Although not restricted by the _IfcRelAssignsToControl_ relationship it is only allowed to have one base calendar.

