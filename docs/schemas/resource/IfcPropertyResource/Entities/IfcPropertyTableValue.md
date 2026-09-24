# IfcPropertyTableValue

_IfcPropertyTableValue_ is a property with a value range defined by a property object which has two lists of (numeric or descriptive) values assigned. The values specify a table with two columns. The defining values provide the first column and establish the scope for the defined values (the second column). An optional _Expression_ attribute may give the equation used for deriving the range value, which is for information purposes only.
<!-- end of short definition -->

The _IfcPropertyTableValue_ defines a defining/defined property value combination for which the property name, the table with defining and defined values with measure type (and optional the units for defining and defined values) are given.

> NOTE The _IfcPropertyTableValue_ only captures properties that can be expressed by a table with two columns. Use IfcPropertyReferenceValue with the PropertyReference being an IfcTable to express all those properties that require a table with tree or more columns.

The units are handled by the _DefiningUnit_ and _DefinedUnit_ attributes, see Table 1 for an example of a table value property:

* If the _DefiningUnit_ or _DefinedUnit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
* If the _DefiningUnit_ or _DefinedUnit_ attribute is given, then the unit assigned by the unit attribute overrides the globally assigned unit.

The _IfcPropertyTableValue_ allows for the specification of a table of defining/defined value pairs of the property description. The optional attribute _CurveInterpolation_ allows to determine the interval between two given values.


|Name|DefiningValues|DefiningValue Type (through IfcValue)|DefinedValues|DefinedValue Type (through IfcValue)|DefiningUnit|DefinedUnit|
|--- |--- |--- |--- |--- |--- |--- |
|SoundTransmissionLoss|100|IfcFrequencyMeasure|20|IfcNumericMeasure|-|dB|
||200|IfcFrequencyMeasure|42|IfcNumericMeasure|||
||400|IfcFrequencyMeasure|46|IfcNumericMeasure|||
||800|IfcFrequencyMeasure|56|IfcNumericMeasure|||
||1600|IfcFrequencyMeasure|60|IfcNumericMeasure|||
||3200|IfcFrequencyMeasure|65|IfcNumericMeasure|||

Table 1 — Table value property with values, measure types and units

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Attributes _DefiningValues_ and _DefinedValues_ have been made OPTIONAL with upward compatibility for file based exchange. The attribute _CurveInterpolation_ has been added.



**Informal Propositions**

1. The list of _DefinedValues_ and the list of _DefiningValues_ are corresponding lists.

## Attributes

### DefiningValues
List of defining values, which determine the defined values. This list shall have unique values only.
> IFC4 CHANGE The attribute has been made optional with upward compatibility for file based exchange.

### DefinedValues
Defined values which are applicable for the scope as defined by the defining values.
> IFC4 CHANGE The attribute has been made optional with upward compatibility for file based exchange.

### Expression
Expression for the derivation of defined values from the defining values, the expression is given for information only, i.e. no automatic processing can be expected from the expression.

### DefiningUnit
Unit for the defining values, if not given, the default value for the measure type (given by the TYPE of the defining values) is used as defined by the global unit assignment at IfcProject.

### DefinedUnit
Unit for the defined values, if not given, the default value for the measure type (given by the TYPE of the defined values) is used as defined by the global unit assignment at IfcProject.

### CurveInterpolation
Interpolation of the curve between two defining and defined values that are provided. if not provided a linear interpolation is assumed.
> IFC4 CHANGE The attribute has been added at the end of the attribute list.

## Formal Propositions

### WR21
Either both _DefiningValues_ and _DefinedValues_ are not provided, or the number of members in the list of _DefiningValues_ shall be the same as the number of members in the list of _DefinedValues_.

### WR22
If _DefiningValues_ are provided, then all values within the list of _DefiningValues_ shall have the same measure type.

### WR23
If _DefinedValues_ are provided, then all values within the list of _DefinedValues_ shall have the same measure type.
