# IfcSubContractResource

_IfcSubContractResource_ is a construction resource needed in a construction process that represents a sub-contractor.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE The attribute _SubContractor_ has been deleted; use _IfcRelAssignsToResource_ to assign an _IfcActor_ to fulfill the role as the subcontractor. The attribute _JobDescription_ has been deleted; use _LongDescription_ to describe the job.

An _IfcSubContractResource_ can be used in cost estimating and work planning with or without specifying the subcontractor and contract agreement.

The purpose of an _IfcSubContractResource_ is to indicate work of a particular type that is that is to be engaged through the use of a sub-contract. Its aim is to identify the description of the sub-contract work required. It can be used to identify the generic type of sub-contract resource that is required for a purpose without having to be specific about the actor (person or organization) providing the resource occurrence. It may be particularly useful when creating an overall plan for a process or processes. For instance, within maintenance or work planning there may be a known task that needs to be done which is planned to require an 'insulation specialist'.

A subcontract resource may be described at various stages and levels of detail through its assignments:

* Subcontract resource designated for particular tasks
* Actors identified to request bids
* Cost schedules (bids) received from actors
* Project order (work order, change order, etc.) executed

## Attributes

### PredefinedType
Defines types of subcontract resources.
> IFC4 New attribute.

## Formal Propositions

### CorrectPredefinedType

## Concepts

### Object Typing



### Resource Assignment



#### IfcActor

Indicates a specific organization to be considered to fulfill the resource or invited to bid on the resource.

