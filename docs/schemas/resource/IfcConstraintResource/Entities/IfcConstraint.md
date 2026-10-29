# IfcConstraint

An _IfcConstraint_ is used to define a constraint or limiting value or boundary condition that may be applied to an object or to the value of a property.
<!-- end of short definition -->

Constraints may be subdivided into user-defined constraints and system-defined constraints. User-defined constraints are applied by a user and are restricted to high-level definitions such as object properties. System-defined constraints may apply to any object attribute, are typically defined by an application to enforce data validation or parametric behaviour, and are intended to be enforced by applications but not to be directly editable by an end-user.

_IfcConstraint_ may be associated with any subtype of _IfcObjectDefinition_ or _IfcPropertyDefinition_ through the _IfcRelAssociatesConstraint_ relationship to indicate a system-defined constraint, or may be associated with _IfcResourceObjectSelect_ (such as _IfcPropertySingleValue_) by _IfcResourceConstraintRelationship_ to indicate a user-defined constraint.

A constraint must have a name applied through the _IfcConstraint.Name_ attribute and optionally, a description through _IfcConstraint.Description_. The grade of the constraint (hard, soft, advisory) must be specified through _IfcConstraint.ConstraintGrade_ or _IfcConstraint.UserDefinedGrade_ whilst the source, creating actor and time at which the constraint is created may be optionally asserted through _IfcConstraint.ConstraintSource_, _IfcConstraint.CreatingActor_ and _IfcConstraint.CreationTime_.

A constraint may also have additional external information (such as classification or document information) associated to it by _IfcExternalReferenceRelationship_, accessible through inverse attribute _IfcConstraint.HasExternalReferences_

> HISTORY New entity in IFC2.0

> IFC4 CHANGE CreationTime changed to IfcDateTime for ISO 8601 representation, HasExternalReferences new inverse attribute.

## Attributes

### Name
A human-readable name to be used for the constraint.

### Description
A human-readable description that may apply additional information about a constraint.

### ConstraintGrade
Enumeration that qualifies the type of constraint.

### ConstraintSource
Any source material, such as a code or standard, from which the constraint originated.

### CreatingActor
Person and/or organization that has created the constraint.

### CreationTime
Time when information specifying the constraint instance was created.

### UserDefinedGrade
Allows for specification of user defined grade of the constraint beyond the enumeration values (hard, soft, advisory) provided by ConstraintGrade attribute of type _IfcConstraintEnum_.
When a value is provided for attribute UserDefinedGrade in parallel the attribute ConstraintGrade shall have enumeration value USERDEFINED.

### HasExternalReferences
Reference to an external references, e.g. library, classification, or document information, that are associated to the constraint.
> IFC4 CHANGE New inverse attribute.

### PropertiesForConstraint
Reference to the properties to which the constraint is applied.

## Formal Propositions

### WR11
The attribute UserDefinedGrade must be asserted when the value of the ConstraintGrade is set to USERDEFINED.
