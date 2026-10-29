# IfcDerivedUnit

A derived unit is a unit that is formed from an expression of other units.
<!-- end of short definition -->

```
digraph dot_neato {
IfcUnitAssignment [pos="0,0!"];
IfcDerivedUnit [label=<{IfcDerivedUnit | UnitType: LINEARVELOCITYUNIT<br />Name: mph}>, pos="0,-70!"];
IfcDerivedUnitElement_0 [label=<{IfcDerivedUnitElement | Exponent: 1}>, pos="-100,-140!"];
IfcDerivedUnitElement_1 [label=<{IfcDerivedUnitElement | Exponent: -1}>, pos="100,-140!"];

IfcConversionBasedUnit_0 [label=<{IfcConversionBasedUnit | UnitType: LENGTHUNIT<br />Name: mile}>, pos="-200,-210!"];
IfcDimensionalExponents_0 [label=<{IfcDimensionalExponents | LengthExponent: 1}>, pos="-300,-280!"];
IfcMeasureWithUnit_0 [label=<{IfcMeasureWithUnit | ValueComponent: 1609}>, pos="-100,-280!"];
IfcSIUnit_0 [label=<{IfcSIUnit | UnitType: LENGTHUNIT<br />Name: METRE}>, pos="-100,-350!"];

IfcConversionBasedUnit_1 [label=<{IfcConversionBasedUnit | UnitType: TIMEUNIT<br />Name: hour}>, pos="200,-210!"];
IfcDimensionalExponents_1 [label=<{IfcDimensionalExponents | TimeExponent: 1}>, pos="300,-280!"];
IfcMeasureWithUnit_1 [label=<{IfcMeasureWithUnit | ValueComponent: 3600}>, pos="100,-280!"];
IfcSIUnit_1 [label=<{IfcSIUnit | UnitType: TIMEUNIT<br />Name: SECOND}>, pos="100,-350!"];

IfcUnitAssignment -> IfcDerivedUnit [label="Units"];
IfcDerivedUnit -> IfcDerivedUnitElement_0 [headlabel="Elements[1]", labelangle=130, labeldistance=3];
IfcDerivedUnit -> IfcDerivedUnitElement_1 [headlabel="Elements[2]", labelangle=-130, labeldistance=3];

IfcDerivedUnitElement_0 -> IfcConversionBasedUnit_0 [headlabel="Unit", labelangle=130, labeldistance=3];
IfcConversionBasedUnit_0 -> IfcDimensionalExponents_0 [headlabel="Dimensions", labelangle=130, labeldistance=3];
IfcConversionBasedUnit_0 -> IfcMeasureWithUnit_0 [headlabel="ConversionFactor", labelangle=-130, labeldistance=3];
IfcMeasureWithUnit_0 -> IfcSIUnit_0 [headlabel="UnitComponent", labelangle=80, labeldistance=4];

IfcDerivedUnitElement_1 -> IfcConversionBasedUnit_1 [headlabel="Unit", labelangle=-130, labeldistance=3];
IfcConversionBasedUnit_1 -> IfcDimensionalExponents_1 [headlabel="Dimensions", labelangle=-130, labeldistance=3];
IfcConversionBasedUnit_1 -> IfcMeasureWithUnit_1 [headlabel="ConversionFactor", labelangle=130, labeldistance=3];
IfcMeasureWithUnit_1 -> IfcSIUnit_1 [headlabel="UnitComponent", labelangle=80, labeldistance=4];
}
```

Figure MPH — An example of how to assign miles per hour as a derived unit

> REFERENCE Definition according to ISO/CD 10303-41:1992 of `derived_unit`.

> HISTORY New entity in IFC1.5.1.

## Attributes

### Elements
The group of units and their exponents that define the derived unit.

### UnitType
Type of the derived unit chosen from an enumeration of derived unit types for use in IFC models.

> EXAMPLE The imperial unit name for a velosity measure is miles per hour, or mph, with a UnitType of .LINEARVELOCITYUNIT.

### UserDefinedType
Type of the derived unit if the UnitType attribute is set to USERDEFINED.

> NOTE The UserDefinedType shall only be used if the unit type is not available in UnitType.

### Name
Name of the unit in addition to the unit type, particularly when the derived unit elements refer to conversion or context based units.

> EXAMPLE The imperial unit name for a velocity measure is miles per hour, or MPH, with a _Name_ of 'MPH'.

### Dimensions
Dimensional exponents derived using the function IfcDeriveDimensionalExponents using (SELF) as the input value.

## Formal Propositions

### WR1
Units as such shall not be re-defined as derived units.

### WR2
When attribute UnitType has enumeration value USERDEFINED
then attribute UserDefinedType shall also have a value.
