# IfcTimeSeries

A time series is a set of a time-stamped data entries. It allows a natural association of data collected over intervals of time. Time series can be regular or irregular. In regular time series data arrive predictably at predefined intervals. In irregular time series some or all time stamps do not follow a repetitive pattern and unpredictable bursts of data may arrive at unspecified points in time.
<!-- end of short definition -->

The modeling of buildings and their performance involves data that are generated and recorded over a period of time. Such data cover a large spectrum, from weather data to schedules of all kinds to status measurements to reporting to everything else that has a time related aspect. Their correct placement in time is essential for their proper understanding and use, and the _IfcTimeSeries_ subtypes provide the appropriate data structures to accommodate these types of data.

> HISTORY New entity in IFC2x2.

## Attributes

### Name
An unique name for the time series.

### Description
A text description of the data that the series represents.

### StartTime
The start time of a time series.

### EndTime
The end time of a time series.

### TimeSeriesDataType
The time series data type.

### DataOrigin
The origin of a time series data.

### UserDefinedDataOrigin
Value of the data origin if DataOrigin attribute is USERDEFINED.

### Unit
The unit to be assigned to all values within the time series. Note that mixing units is not allowed. If the value is not given, the global unit for the type of _IfcValue_, as defined at _IfcProject.UnitsInContext_ is used.

### HasExternalReference
Reference to an external reference, e.g. library, classification, or document information, that is associated to the IfcTimeSeries.
> IFC4 CHANGE New inverse attribute.
