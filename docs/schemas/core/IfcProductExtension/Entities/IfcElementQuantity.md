# IfcElementQuantity

An _IfcElementQuantity_ defines a set of derived measures of an element's physical property. Elements could be spatial structure elements (like buildings, storeys, or spaces) or building elements (like walls, slabs, finishes). The _IfcElementQuantity_ gets assigned to the element by using the _IfcRelDefinesByProperties_ relationship.
<!-- end of short definition -->

The optional _MethodOfMeasurement_ attribute defines the code, e.g. from a standard method of measurement, which had been used to calculate the element quantity.

> NOTE The recognizable values for the name and the method of measurement attributes have to be agreed upon in further agreement documents, such as implementers agreements. Some of these agreements might be limited to a certain region, to which the method of measurement applies.

The name attribute, given at the individual _Quantities_ provides a recognizable semantic meaning of the element quantity. Both information is needed to establish a precise meaning for the measure value. An optional description may be assigned to each of the _Quantities_. All quantities assigned by a single instance of _IfcElementQuantity_ are deemed to have been generated according to the same method of measurement. However several instances of _IfcElementQuantity_ are assignable to an element, thus allowing for an element having quantities generated according to several methods of measurement.

> EXAMPLE To exchange the net floor area of spaces in the German region (as _IfcSpace_), the name might be 'Netto-Grundfläche' (net floor area), and the method of measurement might be accordingly 'DIN277-2' (German industry norm no. 277 edition 2).

> EXAMPLE The same instance of _IfcSpace_ may have a different area measure assigned in the German region according to a housing regulation, the name would be 'Wohnfläche' and the method of measurement would be '2.BV'. It would be attached to the _IfcSpace_ by a separate _IfcRelDefinesByProperties_ relationship.

The _IfcElementQuantity_ can have the following subtypes of _IfcPhysicalQuantity_ within its SET of _Quantities_, which count for the basis measure types used:

* count measure
* weight measure
* length measure
* area measure
* volume measure
* time measure

Base quantities are quantity definitions that are independent of a particular method of measurement and therefore internationally applicable. Base quantities are defined as gross and net values and provided by measurement of the correct geometric shape representation of the element. This specification includes a set of base quantity definition. See each subtype of _IfcElement_ for applicable base quantities.

The following general agreements apply for each base quantity set

* _IfcElementQuantity.Name_ = &lt;name of the qto definition template>
* _IfcElementQuantity.MethodOfMeasurement_ = 'BaseQuantities'
* _IfcElementQuantity.Quantities_ = SET of subtypes of _IfcPhysicalSimpleQuantity_ with values for the _Name_ attribute as published as part of this specification.

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Subtyped from new intermediate _IfcQuantitySet_ supertype.

## Attributes

### MethodOfMeasurement
Name of the method of measurement used to calculate the element quantity. The method of measurement attribute has to be made recognizable by further agreements.

> IFC2x2-Addendum-1 change: The attribute has been changed to be optional

### Quantities
The individual quantities for the element, can be a set of length, area, volume, weight or count based quantities.

## Formal Propositions

### UniqueQuantityNames
Every individual _IfcPhysicalQuantity_ within the set _Quantities_ shall have a unique _Name_ attribute value.
> HISTORY New rule in IFC4
