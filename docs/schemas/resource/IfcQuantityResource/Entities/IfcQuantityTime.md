# IfcQuantityTime

_IfcQuantityTime_ is an element quantity that defines a time measure to provide a property of time related to an element. It is normally given by the recipe information of the element under the specific measure rules given by a method of measurement.
<!-- end of short definition -->

> EXAMPLE The amount of time needed to pour concrete for a wall is given as a time quantity for the labor part of the recipe information.

> HISTORY New entity in IFC2x2.

## Attributes

### TimeValue
Time measure value of this quantity.

### Formula
A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.
> IFC4 CHANGE Attribute added to the end of the attribute list.

## Formal Propositions

### WR21
If a unit is given, the unit type shall be time unit.

### WR22
A valid weight quantity shall be greater than or equal to zero.
