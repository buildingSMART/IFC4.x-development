# IfcPropertySingleValue

The property with a single value _IfcPropertySingleValue_ defines a property object which has a single (numeric or descriptive) value assigned. It defines a property - single value combination for which the property _Name_, an optional _Description_, and an optional _NominalValue_ with measure type is provided. In addition, the default unit as specified within the project unit context can be overridden by assigning an _Unit_.
<!-- end of short definition -->

The unit is handled by the _Unit_ attribute, see Table 1 for an example of various single value properties:

* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.


|Name|NominalValue|Type (through IfcValue)|Unit|
|--- |--- |--- |--- |
|Description|Manufacturer "A" door|IfcLabel|-|
|PanelThickness|0.12|IfcPositiveLengthMeasure|-|
|ThermalTransmittance|2.6|IfcThermalTransmittanceMeasure|W/(m2K)|

Table 1 — Single value properties with values, measure types and units

> HISTORY  New entity in IFC1.0.

> IFC2x CHANGE Entity has been renamed from IfcSimpleProperty.

> IFC2x3 CHANGE  Attribute _NominalValue_ has been made OPTIONAL with upward compatibility for file based exchange.

## Attributes

### NominalValue
Value and measure type of this property.
> NOTE By virtue of the defined data type, that is selected from the SELECT _IfcValue_, the appropriate unit can be found within the _IfcUnitAssignment_, defined for the project if no value for the unit attribute is given.

> IFC2x3 CHANGE The attribute has been made optional with upward compatibility for file based exchange.

### Unit
Unit for the nominal value, if not given, the default value for the measure type (given by the TYPE of nominal value) is used as defined by the global unit assignment at IfcProject.
