# IfcAsset

An asset is a uniquely identifiable grouping of elements acting as a single entity that has a financial value or that can be operated on as a single unit.
<!-- end of short definition -->

An asset is generally the level of granularity at which maintenance operations are undertaken. An asset is a group that can contain one or more elements. Whilst the financial value of a component or element can be defined, financial value is also defined for accounting purposes at the level of the asset.

There are a number of actors that can be associated with an asset, each actor having a role. Actors within the scope of the project are indicated using the IfcRelAssignsToActor relationship in which case roles should be defined through the IfcActorRole class; otherwise principal actors are identified as attributes of the class. In the existence of both, direct attributes take precedence.

There are a number of costs that can be associated with an asset, each cost having a role. These are specified through the _OriginalValue_, _CurrentValue_, _TotalReplacementCost_ and _DepreciatedValue_ attributes.

> HISTORY New entity in IFC2x.

> IFC4 CHANGE All attributes made optional and date values changed to use _IfcDate_.

## Attributes

### Identification
A unique identification assigned to an asset that enables its differentiation from other assets.
> NOTE The asset identifier is unique within the asset register. It differs from the globally unique id assigned to the instance of an entity populating a database.

### OriginalValue
The cost value of the asset at the time of purchase.

### CurrentValue
The current cost value of the asset.

### TotalReplacementCost
The total cost of replacement of the asset.

### Owner
The name of the person or organization that 'owns' the asset.

### User
The name of the person or organization that 'uses' the asset.

### ResponsiblePerson
The person designated to be responsible for the asset.
> NOTE In some regulations (for example, UK Health and Safety at Work Act, Electricity at Work Regulations), management of assets must have a person identified as being responsible and to whom regulatory, insurance and other organizations communicate. In places where there is not a legal requirement, the responsible person would be the asset manager but would not have a legal status.

### IncorporationDate
The date on which an asset was incorporated into the works, installed, constructed, erected or completed.
> NOTE This is the date on which an asset is considered to start depreciating.

> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### DepreciatedValue
The current value of an asset within the accounting rules and procedures of an organization.

## Concepts

### Classification Association

The operating function of an asset within an organization may be particularly valuable in situations where one organization provides and maintains core services and another organization adds and maintains terminal services. Operating function can be designated through the use of one or more classification references.

### Group Assignment



#### IfcElement

Physical elements that comprise the asset.

### Property Sets for Objects



