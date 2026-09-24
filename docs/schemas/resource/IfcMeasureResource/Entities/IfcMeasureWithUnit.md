# IfcMeasureWithUnit

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-41:1992
> A measure with unit is the specification of a physical quantity as defined in ISO 31 (clause 2).

_IfcMeasureWithUnit_ has two usages:
1. For representing measure value together with its unit on the entity type attribute level; thus overriding the IFC model global unit assignments.
2. For conversion based unit to give the conversion rate and its base.

> NOTE Corresponding ISO 10303 name: measure_with_unit, please refer to ISO/IS 10303-41 for the final definition of the formal standard.

> HISTORY New entity in IFC1.5.1.

## Attributes

### ValueComponent
The value of the physical quantity when expressed in the specified units.

### UnitComponent
The unit in which the physical quantity is expressed.
