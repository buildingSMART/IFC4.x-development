IfcConstraintResource
=====================

The _IfcConstraintResource_ schema provides for the specification of constraints (_IfcConstraint_) that may be applied to any object that is a subtype of _IfcObjectDefinition_ or _IfcPropertyDefinition_ (through the provision of the relationship class _IfcRelAssociatesConstraint_). Also, constraints may be applied to specific resource objects, such as an _IfcProperty_ (through the provision of the relationship class _IfcResourceConstraintRelationship_).

A grade may be set for the constraint that establishes whether it is a hard constraint (must be satisfied), a soft constraint (should be satisfied) or simply advisory.

A constraint must be named and may optionally have one or more sources within which it is defined or from which it is taken. Additionally, a constraint may optionally be assigned a creating actor, creation date and a description.

Constraints may be either qualitative (an objective constraint) or quantitative (a measured constraint or metric). A qualifier can be applied to an objective constraint that determines the purpose for which it is applied. It may be applied to define the constraining values beyond which building codes may be violated or to limit the selectable range of values as in a specification (for example, value of A must be greater than A but less than B). Several possible purposes are provided through an enumeration.

A measured constraint or metric defines the actual value or values of a constraint. Values can be defined in terms of a benchmark requirement which sets the intent of the constraint, for example, whether the benchmark is greater than (>), or less than (<). The value of a constraint may be defined according to a number of data types that are available through a select mechanism.

> EXAMPLE  A constraint advised by a manufacturer beyond which maintenance must be undertaken on a pump might be qualified as a 'TriggerCondition', named 'PumpMaintenanceCondition', have as its source 'ManufacturerData' and be graded as 'Advisory'. It could have as a single value 10\^-2 / sec as the frequency of vibration and have a benchmark of 'GreaterThanOrEqualTo'.

> HISTORY  New schema in IFC2x.

> IFC4 CHANGE  The classification of constraints shall not be done using _IfcConstraintClassificationRelationship_ anymore (entity deleted); the capability of associating external references to constraints has been introduced by _IfcExternalReferenceRelationship_ in _IfcExternalReferenceResource_ schema and should be used instead. The aggregation of constraints shall not be done using _IfcConstraintAggregationRelationship_ anymore (entity deleted); the capability of associating aggregated constraints is now handled by an attribute at _IfcObjective_.
