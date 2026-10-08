# IfcSIUnit

The _IfcSIUnit_ covers both standard base SI units such as meter and second, and derived SI units such as Pascal, square meter and cubic meter.
<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-41:1992
> An SI unit is the fixed quantity used as a standard in terms of which items are measured as defined by ISO 1000 (clause 2).

> NOTE Corresponding ISO 10303 name: si_unit, please refer to ISO/IS 10303-41 for the final definition of the formal standard.

> HISTORY New entity in IFC1.5.1.

## Attributes

### Prefix
The SI Prefix for defining decimal multiples and submultiples of the unit.

### Name
The word, or group of words, by which the SI unit is referred to.

> NOTE Even though the SI system's base unit for mass is kilogram, the _IfcSIUnit_ for mass is gram if no _Prefix_ is asserted.

### Dimensions
The dimensional exponents of SI units are derived by function _IfcDimensionsForSIUnit_.
