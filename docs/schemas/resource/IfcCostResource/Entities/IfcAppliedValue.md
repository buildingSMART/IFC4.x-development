# IfcAppliedValue

This entity captures a value driven by a formula, with additional qualifications including unit basis, valid date range, and categorization.
<!-- end of short definition -->

The extent of the _IfcAppliedValue_ is determined by the _AppliedValue_ attribute which may be defined either as an _IfcMeasureWithUnit_ or as an _IfcMonetaryMeasure_ or as an _IfcRatioMeasure_ via the _IfcAppliedValueSelect_ type.

Optionally, an _IfcAppliedValue_ may have an applicable date. This is intended to fix the date on which the value became relevant for use. It may be the date on which the value was set in the model or it may be a prior or future date when the value becomes operable. Similarly, an _IfcAppliedValue_ may have a 'fixed until' date. This is intended to fix the date on which the value ceases to be relevant for use.

An instance of _IfcAppliedValue_ may have a unit basis asserted. This is defined as an _IfcMeasureWithUnit_ that determines the extent of the unit value for application purposes. It is assumed that when this attribute is asserted, then the value given to _IfcAppliedValue_ is that for unit quantity. This is not enforced within the schema and thus needs to be controlled within an application.

Applied values may be referenced from a document (such as a price list). The relationship between one or more occurrences of _IfcAppliedValue_ (or its subtypes) is achieved through the use of the _IfcExternalReferenceRelationship_ in which the document provides the _IfcExternalReferenceRelationship.RelatingExtReference_ and the value occurrences are the _IfcExternalReferenceRelationship.RelatedResourceObjects_.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Entity made non-abstract to support general formula expressions of constraints, data type of date-based attributes changed into _IfcDate_, _ValueType_ and _Condition_ promoted from _IfcCostValue_, _Components_ and _ArithmeticOperator_ attributes added to replace _IfcAppliedValueRelationship_ for more efficient encoding and reference tracking.

**Informal Propositions**

1. When the *ArithmeticOperator* equals `MODULO`, the list of *Components* shall contain exactly two values, which shall be positive integers.

## Attributes

### Name
A name or additional clarification given to a cost value.

### Description
The description that may apply additional information about a cost value.

### AppliedValue
The extent or quantity or amount of an applied value.

### UnitBasis
The number and unit of measure on which the unit cost is based.

Note: As well as the normally expected units of measure such as length, area, volume etc., costs may be based on units of measure which need to be defined e.g. sack, drum, pallet, item etc. Unit costs may be based on quantities greater (or lesser) than a unitary value of the basis measure. For instance, timber may have a unit cost rate per X meters where X > 1; similarly for cable, piping and many other items. The basis number may be either an integer or a real value.

Note: This attribute should be asserted for all circumstances where the cost to be applied is per unit quantity. It may be asserted even for circumstances where an item price is used, in which case the unit cost basis should be by item (or equivalent definition).

### ApplicableDate
The date on or from which an applied value is applicable.
> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### FixedUntilDate
The date until which applied value is applicable.
> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### Category
Specification of the type of cost used.

> NOTE There are many possible types of cost value that may be identified. Whilst there is a broad understanding of the meaning of names that may be assigned to different types of costs, there is no general standard for naming cost types nor are there any broadly defined classifications. To allow for any type of cost value, the _IfcLabel_ datatype is assigned.



In the absence of any well defined standard, it is recommended that local agreements should be made to define allowable and understandable cost value types within a project or region.

### Condition
The condition under which a cost value applies.

For example, within the context of a bid submission, this may refer to an option that may or may not be elected.

### ArithmeticOperator
The arithmetic operator applied to component values.

### Components
Optional component values from which _AppliedValue_ is calculated.

### HasExternalReference
Reference to an external reference, e.g. library, classification, or document information, that is associated to the IfcAppliedValue.
> IFC4 CHANGE New inverse attribute.
