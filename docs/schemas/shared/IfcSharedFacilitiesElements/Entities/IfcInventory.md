# IfcInventory

An inventory is a list of items within an enterprise.
<!-- end of short definition -->

Various types of inventory can be included. These are identified by the range of values within the inventory type enumeration which includes space, asset, and furniture. User defined inventories can also be defined for lists of particular types of element such as may be required in operating and maintenance instructions. Such inventories should be constrained to contain a list of elements of a restricted type.

There are a number of actors that can be associated with an inventory, each actor having a role. Actors within the scope of the project are indicated using the IfcRelAssignsToActor relationship in which case roles should be defined through the IfcActorRole class; otherwise principal actors are identified as attributes of the class. In the existence of both, direct attributes take precedence.

There are a number of costs that can be associated with an inventory, each cost having a role. These are specified through the _CurrentValue_ and _OriginalValue_ attributes.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE All attributes optional, Where Rule removed.

## Attributes

### PredefinedType
A list of the types of inventories from which that required may be selected.
> IFC4 CHANGE Attribute made optional.

### Jurisdiction
The organizational unit to which the inventory is applicable.

### ResponsiblePersons
Persons who are responsible for the inventory.

### LastUpdateDate
The date on which the last update of the inventory was carried out.

> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### CurrentValue
An estimate of the current cost value of the inventory.

### OriginalValue
An estimate of the original cost value of the inventory.

## Concepts

### Group Assignment



#### IfcAsset

Assets included in the inventory.

#### IfcElement

Elements such as furniture included in the inventory.

#### IfcSpace

Spaces included in the inventory.

