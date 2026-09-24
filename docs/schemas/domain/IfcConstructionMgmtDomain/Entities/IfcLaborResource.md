# IfcLaborResource

An _IfcLaborResource_ is used in construction with particular skills or crafts required to perform certain types of construction or management related work.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE The attribute _Skillset_ has been deleted; use LongDescription to describe the skillset.

The purpose of an _IfcLaborResource_ is to identify a skillset that may be required or used. The skillset identified may be (for instance) charge-hand, foreman, labourer, plumbers mate etc. and provides a designation of a particular level of skill. It can be used to identify the generic type of labour resource that is required for a purpose without having to be specific about the actor (person or organization) providing the resource occurrence. It may be particularly useful when creating an overall plan for a process or processes. For instance, within maintenance or work planning there may be a known task that needs to be done which is planned to require a 'chargehand pipe fitter'. There may be several such labour resources available and so the need to identify which will be used is not necessary at the planning stage.

At a later stage, individual actors can be determined for the labour resources. This is achieved through specifying the actor through _IfcActor_. The actor is then identified as the labour resource occurrence through the _IfcRelAssignsToResource.RelatedResource_ attribute. The _IfcLaborResource_ provides the _IfcRelAssignsToResource_._RelatingResource_ attribute.

## Attributes

### PredefinedType
Defines types of labour resources.
> IFC4 New attribute.

## Formal Propositions

### CorrectPredefinedType

## Concepts

### Object Typing



### Quantity Sets



### Resource Assignment



#### IfcActor

Indicates specific people manifesting the resource such as laborers.

### Resource Cost



#### Standard_IfcCostValue_IfcMonetaryMeasure

Wages incurred for work during standard hours.

#### Overtime_IfcCostValue_IfcMonetaryMeasure

Wages incurred for work during overtime hours.

### Resource Quantity



#### Labor_IfcQuantityTime

Quantity of labor, typically per hour.

