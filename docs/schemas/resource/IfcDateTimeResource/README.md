IfcDateTimeResource
===================

The _IfcDateTimeResource_ schema defines several generic date and time specific concepts that can be used to identify context within calendars, schedules, and time series. These concepts include:

*  _IfcDate_, _IfcTime_, _IfcDateTime_ and _IfcDuration_. All given values should be provided in context and converted into a Gregorian date context and be shall be processable by a receiving application.
* Time series, which are a set of discrete data each with an associated date and time stamp, allowing a natural association of data collected over intervals of time. Time series data can be represented using the following entities:
    *  _IfcRegularTimeSeries_: Time series data arrive predictably at predefined intervals and are represented by the entity, and
    *  _IfcIrregularTimeSeries_: some or all time stamps do not follow a repetitive pattern and unpredictable bursts of data may arrive at unspecified points in time.  Time series data must be normalized using the following rules:
    * All time (universal, local, daylight savings, and solar) is normalized against the ISO 8601 standard GMT/UTC (Universal Coordinated Time).
    * The normalized data refer to the preceding time unit.
    * Any rollover is handled by the application providing the data. Rollover occurs, for example, when the measurement device resets itself while measuring and the recording data do not include the data measured before the reset.
    * Only the time when data are taken is recorded.
* Time associated with processes such as resource allocation (_IfcResourceTime_), time for task completion (_IfcTaskTime_), work patterns (_IfcWorkTime_), and scheduled events (_IfcEventTime_).

> NOTE  The schema _IfcDateTimeResource_ includes definitions that are based on [ISO 8601](../content/bibliography.htm#iso-8601)

> HISTORY  This schema has been significantly modified in IFC4. The original concepts of _IfcDateTimeResource_ and _IfcTimeSeriesResource_ were introduced in IFC2.0 and IFC2x2 and merged into the _IfcDateTimeResource_ in IFC4.

> IFC4 CHANGE  The new types _IfcDate_, _IfcTime_, _IfcDateTime_ and _IfcDuration_ cancel and replace the previous entities _IfcCalendarDate_, _IfcDateAndTime_, _IfcLocalTime_, and _IfcCoordinatedUniversalTimeOffset_.
