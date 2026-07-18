# IfcCorrectDimensions

The function returns whether the dimensional exponents of the given unit type matches the given exponents.
<!-- end of short definition -->

Argument definitions:

- `m`: (input) the name of the unit type for which the dimensional exponents are tested.
- `Dim`: (input) the dimensional exponents to be tested against corresponding unit type name.

> HISTORY A correction has been made in IFC4 to correct the right hand side for the comparison in case of ELECTRICCAPACITANCEUNIT to IfcDimensionalExponents(-2, -1, 4, 2, 0, 0, 0)
