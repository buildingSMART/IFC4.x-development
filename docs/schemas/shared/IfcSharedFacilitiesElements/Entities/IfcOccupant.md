# IfcOccupant

An occupant is a type of actor that defines the form of occupancy of a property.
<!-- end of short definition -->

The principal purpose of **IfcOccupant** is to determine the nature of occupancy of a property for a particular actor. All characteristics relating to the actor (name and organization details) are inherited from the _IfcActor_ entity.

> HISTORY New entity in IFC2x

## Attributes

### PredefinedType
Predefined occupant types from which that required may be set.

> IFC4 CHANGE Attribute made optional.

## Formal Propositions

### WR31
The attribute ObjectType must be asserted when the value of the IfcOccupantTypeEnum is set to USERDEFINED.

## Concepts

### Actor Assignment



#### IfcSpatialStructureElement

Indicates the property to be occupied. Particular details of the agreement relating to the occupancy of a property are dealt within the Pset_PropertyAgreement that is defined for the instance of IfcSpatialStructureElement. This means that an occupant may be related to a site, building, building storey or space through the _IfcSpatialStructureElement.ElementComposition_ attribute. For instance, if the property concerned is several office spaces on a building storey, it might be appropriate to reference _IfcBuildingStorey.ElementComposition=PARTIAL_. Occupants of a property may be considered to be the parties to an agreement. The roles that the occupant may play in respect to an agreement are defined in the IfcOccupantTypeEnum enumeration. If the role is not specified by the predefined contents of this enumeration, the value USERDEFINED may be set and the ObjectType attribute asserted.

