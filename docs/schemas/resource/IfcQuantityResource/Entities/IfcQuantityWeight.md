# IfcQuantityWeight

_IfcQuantityWeight_ is a physical element quantity that defines a derived weight measure to provide an element's physical property. It is normally derived from the physical properties of the element under the specific measure rules given by a method of measurement.
<!-- end of short definition -->

> EXAMPLE The amount of reinforcement used within a building element may be measured according to its weight. The actual size of the weight depends on the method of measurement used.

> HISTORY New entity in IFC2x. It replaces the calcXxx attributes used in previous IFC Releases.

## Attributes

### WeightValue
Mass measure value of this quantity.

### Formula
A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.
> IFC4 CHANGE Attribute added to the end of the attribute list.

## Formal Propositions

### WR21
If a unit is given, the unit type shall be mass unit.\
			>NOTE There is no distinction between the concept of "Mass" and "Weight" in the current IFC Release.

### WR22
A valid weight quantity shall be greater than or equal to zero.
