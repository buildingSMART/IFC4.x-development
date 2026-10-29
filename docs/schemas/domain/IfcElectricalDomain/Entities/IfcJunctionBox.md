# IfcJunctionBox

A junction box is an enclosure within which cables are connected.
<!-- end of short definition -->

Cables may be members of an electrical circuit (for electrical power systems) or be information carriers (in a telecommunications system). A junction box is typically intended to conceal a cable junction from sight, eliminate tampering or provide a safe place for electrical connection.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcJunctionBoxType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no junction box type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcJunctionBoxType_.

## Concepts

### Element Connectivity



#### IfcDiscreteAccessory

Indicates a cover plate for the junction box, having ObjectType 'JunctionBoxCoverPlate'.

### Element Filling



#### IfcCovering

Covering such as drywall applied to a wall or ceiling, for which the junction box fills.

### Element Nesting

> EXAMPLE A switch, outlet, light fixture, or other component that may fit within one of the gangs of the junction box may be nested.

> IFC4 ADD1 CHANGE Junction boxes no longer have ports defined, but rely on element nesting for indicating containment of electrical devices.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Property Sets for Objects



### Quantity Sets



