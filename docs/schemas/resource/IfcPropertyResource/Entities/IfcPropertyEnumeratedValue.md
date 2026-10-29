# IfcPropertyEnumeratedValue

A property with an enumerated value, _IfcPropertyEnumeratedValue_, defines a property object which has a value assigned that is chosen from an enumeration. It defines a property - value combination for which the property _Name_, an optional _Description_, the optional _EnumerationValues_ with measure type and optionally an _Unit_ is given.
<!-- end of short definition -->

> NOTE Multiple choices from the property enumeration are supported.

The unit is handled by the _Unit_ attribute, see Table 1 for an example of a enumerated property:

* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
* If the _Unit_ attribute is given, then the unit assigned by the unit attribute overrides the globally assigned unit.

More precisely: The _IfcPropertyEnumeratedValue_ defines a property, which value is selected from a defined list of enumerators. The enumerators are stored in a dynamic enumeration of values including the type information from _IfcValue_ (see _IfcPropertyEnumeration_). This enables applications to use an enumeration value as a property within a property set (_IfcPropertySet_) including the allowed list of values.

> NOTE An _IfcPropertyEnumeratedValue_ may be exchanged with no values assigned yet. In this case the _EnumerationValues_ are set to NIL.


|Name|Value (EnumerationValue)|Type (through IfcValue)|IfcPropertyEnumeration (Name)|
|--- |--- |--- |--- |
|BladeAction|Opposed|IfcLabel|DamperBladeActionEnum|
|BladeAction|Parallel|IfcLabel|DamperBladeActionEnum|

Table 1 — Enumerated property with values, measure types and units

The _IfcPropertyEnumeratedValue_ refers to an _IfcPropertyEnumeration_, see Table 2 for an example:

|Name|EnumerationValues|Type (through IfcValue)|Unit|
|--- |--- |--- |--- |
|DamperBladeActionEnum|(Parallel, Opposed, Other, Unset)|IfcLabel|-|

Table 2 — Property enumeration with enumerators

It is not mandatory to use an instance of _IfcPropertyEnumeration_ to hold the applicable values for _IfcPropertyEnumeratedValue_, however this is the preferred way. A single instance of _IfcPropertyEnumeration_ can be referenced by multiple instances of _IfcPropertyEnumeratedValue_.

> HISTORY  New entity in IFC2.0.

> IFC2x CHANGE Entity has been renamed from IfcEnumeratedProperty

> IFC4 CHANGE Attribute _EnumerationValues_ has been made OPTIONAL with upward compatibility for file based exchange.

## Attributes

### EnumerationValues
Enumeration values, which shall be listed in the referenced _IfcPropertyEnumeration_, if such a reference is provided.
> IFC4 CHANGE The attribute has been made optional with upward compatibility for file based exchange.

### EnumerationReference
Enumeration from which a enumeration value has been selected. The referenced enumeration also establishes the unit of the enumeration value.

## Formal Propositions

### WR21
Each value within the list of _EnumerationValues_ shall be a member of the list of _EnumerationValues_ at the referenced _IfcPropertyEnumeration_ (provided that both, the _EnumerationValues_ and _EnumerationReference_, are asserted).
