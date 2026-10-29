# IfcPropertyBoundedValue

A property with a bounded value, _IfcPropertyBoundedValue_, defines a property object which has a maximum of two (numeric or descriptive) values assigned, the first value specifying the upper bound and the second value specifying the lower bound. It defines a property - value bound (min-max) combination for which the property _Name_, an optional _Description_, the optional _UpperBoundValue_ with measure type, the optional _LowerBoundValue_ with measure type, and the optional _Unit_ is given. A set point value can be provided in addition to the upper and lower bound values for operational value setting.
<!-- end of short definition -->

The unit is handled by the _Unit_ attribute, see Table 1 for an example of a bounded property:

* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.

The _IfcPropertyBoundedValue_ allows for the specification of an interval for the value component of the property description. If either the _LowerBoundValue_ or the _UpperBoundValue_ is not given, then it indicates an open bound (either a minimum value or a maximum value). The interval is by definition inclusive, that is, the value given for the _LowerBoundValue_ or the _UpperBoundValue_ is included in the interval.

> NOTE An _IfcPropertyBoundedValue_ may be exchanged with no values assigned yet. In this case the _LowerBoundValue_ and the _UpperBoundValue_ are set to NIL.


|Name|UpperBoundValue|LowerBoundValue|SetPointValue|Type (through IfcValue)|Unit|
|--- |--- |--- |--- |--- |--- |
|OverallHeight|2300|1930||IfcPositiveLengthMeasure|-|
|OverallWidth|1.25|0.9||IfcPositiveLengthMeasure|m|
|MaxHeight|20.0|||IfcPositiveLengthMeasure|-|
|MinWeight||20||IfcMassMeasure|kg|

Table 1 — Bounded property with values, measure types and units. Where rules ensures same measure type for all values

> HISTORY  New entity in IFC2x.

> IFC2x2 CHANGE The attribute type of the attribute _UpperBoundValue_ and _LowerBoundValue_ has been made optional with upward compatibility for file based exchange.

> IFC4 CHANGE The attribute _SetPointValue_ has been added.

**Informal Propositions**

1. If the measure type for the upper and lover bound value is a numeric measure, then the following shall be true: _UpperBoundValue_ > _LowerBoundValue_.

## Attributes

### UpperBoundValue
Upper bound value for the interval defining the property value. If the value is not given, it indicates an open bound (all values to be greater than or equal to _LowerBoundValue_).

### LowerBoundValue
Lower bound value for the interval defining the property value. If the value is not given, it indicates an open bound (all values to be lower than or equal to _UpperBoundValue_).

### Unit
Unit for the upper and lower bound values, if not given, the default value for the measure type is used as defined by the global unit assignment at _IfcProject.UnitInContext_. The applicable unit is then selected by the underlying TYPE of the _UpperBoundValue_, _LowerBoundValue_, and _SetPointValue_)

### SetPointValue
Set point value as typically used for operational value setting.
> IFC4 CHANGE The attribute has been added at the end of the attribute list.

## Formal Propositions

### SameUnitUpperLower
The measure type of the _UpperBoundValue_ shall be the same as the measure type of the _LowerBoundValue_, if both (upper and lower bound) are given.

### SameUnitUpperSet
The measure type of the _UpperBoundValue_ shall be the same as the measure type of the _SetPointValue_, if both (upper bound and set point) are given.

### SameUnitLowerSet
The measure type of the _LowerBoundValue_ shall be the same as the measure type of the _SetPointValue_, if both (lower bound and set point) are given.
