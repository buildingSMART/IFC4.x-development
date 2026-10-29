# IfcPermit

A permit is a permission to perform work in places and on artifacts where regulatory, security or other access restrictions apply.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _PermitID_ renamed to _Identification_ and promoted to supertype _IfcControl_, attributes _PredefinedType_, _Status_, and _LongDescription_ added.

## Attributes

### PredefinedType
Identifies the predefined types of permit that can be granted.

> IFC4 CHANGE The attribute has been added.

### Status
The status currently assigned to the permit.

> IFC4 CHANGE The attribute has been added.

### LongDescription
Detailed description of the request.

> IFC4 CHANGE The attribute has been added.

## Concepts

### Aggregation



#### ACCESS_IfcWorkCalendar

A work calendar may indicate the time period of the permit and allowed times when work may be performed. Such work calendar may have assigned resources indicating equipment or labor permitted at various times.

#### WORK_IfcWorkSchedule

A work schedule may indicate tasks and scheduled times where the work schedule type may designate whether tasks and/or times are planned or actual. Such work schedule may have assigned tasks indicating detail, where tasks may be assigned to products and may have assigned resources.

### Approval Association

Approvals may be associated to indicate the status of acceptance or rejection using the IfcRelAssociatesApproval relationship where RelatingApproval refers to an IfcApproval and RelatedObjects contains the IfcPermit. Approvals may be split into sub-approvals using IfcApprovalRelationship to track approval status separately for each party where RelatingApproval refers to the higher-level approval and RelatedApprovals contains one or more lower-level approvals. The hierarchy of approvals implies sequencing such that a higher-level approval is not executed until all of its lower-level approvals have been accepted.

### Control Assignment

Figure 312 illustrates assignment relationships as indicated:


* IfcActor (IfcRelAssignsToActor): Organization issuing the permit such as a local government agency or security organization.


 The IfcPermit may have assignments of its own using the IfcRelAssignsToControl relationship where RelatingControl refers to the IfcPermit and RelatedObjects contains one or more objects of the following types:

* IfcActor: Organization(s) bound to the permit, typically a single contractor.


![Assignment Use Definition](../../../../figures/ifcpermit-assignment.png)
Figure 312 — Permit assignment

### Object Nesting



#### IfcPermit

A permit may be nested to indicate permit amendments, in order of issue.

### Property Sets for Objects



