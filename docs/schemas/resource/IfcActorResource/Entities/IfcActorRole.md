# IfcActorRole

This entity indicates a role which is performed by an actor, either a person, an organization or a person related to an organization.
<!-- end of short definition -->

> NOTE The list of roles of the enumeration values of the _Role_ attribute can never be complete. Therefore using enumeration value USERDEFINED, the user can provide any role as a value of the attribute _UserDefinedRole_.

> NOTE Entity adapted from **organization_role** and **person_role** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.1.

## Attributes

### Role
The name of the role played by an actor. If the Role has value USERDEFINED, then
the user defined role shall be provided as a value of the attribute UserDefinedRole.

### UserDefinedRole
Allows for specification of user defined roles beyond the
enumeration values provided by Role attribute of type IfcRoleEnum.
When a value is provided for attribute UserDefinedRole in parallel
the attribute Role shall have enumeration value USERDEFINED.

### Description
A textual description relating the nature of the role played by an actor.

### HasExternalReference
Reference to external information, e.g. library, classification, or document information, which is associated with the actor role.
> IFC4 CHANGE New inverse attribute.

## Formal Propositions

### WR1
If the attribute _Role_ has the enumeration value USERDEFINED then a value for the attribute _UserDefinedRole_ shall be asserted.
