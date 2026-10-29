# IfcCostSchedule

An _IfcCostSchedule_ brings together instances of _IfcCostItem_ either for the purpose of identifying purely cost information as in an estimate for constructions costs or for including cost information within another presentation form such as a work order.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE Attribute _ID_ renamed to _Identification_ and promoted to supertype _IfcControl_, _PredefinedType_ made optional, attributes _PreparedBy_, _SubmittedBy_, _TargetUsers_ removed.

## Attributes

### PredefinedType
Predefined generic type for a cost schedule that is specified in an enumeration. There may be a property set given specifically for the predefined types.

> IFC4 CHANGE The attribute has been made optional.

### Status
The current status of a cost schedule. Examples of status values that might be used for a cost schedule status include:
* PLANNED
* APPROVED
* AGREED
* ISSUED
* STARTED

### SubmittedOn
The date and time on which the cost schedule was submitted.
> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### UpdateDate
The date and time that this cost schedule is updated; this allows tracking the schedule history.
> IFC4 CHANGE Type changed from IfcDateTimeSelect.

## Concepts

### Approval Association

Approvals may be associated to indicate the status of acceptance or rejection using the IfcRelAssociatesApproval relationship where RelatingApproval refers to an IfcApproval and RelatedObjects contains the IfcCostSchedule. Approvals may be split into sub-approvals using IfcApprovalRelationship to track approval status separately for each party where RelatingApproval refers to the higher-level approval and RelatedApprovals contains one or more lower-level approvals. The hierarchy of approvals implies sequencing such that a higher-level approval is not executed until all of its lower-level approvals have been accepted.

### Control Assignment

 The IfcCostSchedule may be assigned to the following entities using relationships as indicated:


* IfcActor (IfcRelAssignsToActor): Persons and organizations involved in the preparation, submittal, and as target users.


 The IfcCostSchedule may have assignments of its own using the IfcRelAssignsToControl relationship where RelatingControl refers to the IfcCostSchedule and RelatedObjects contains one or more objects of the following types:

* IfcCostItem: Indicates costs published within this cost schedule, typically a single root cost item forming a hierarchy of nested cost items.

