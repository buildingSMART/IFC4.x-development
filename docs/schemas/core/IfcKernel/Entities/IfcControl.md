# IfcControl

_IfcControl_ is the abstract generalization of all concepts that control or constrain the utilization of products, processes, or resources in general. It can be seen as a regulation, cost schedule, request or order, or other requirements applied to a product, process or resource whose requirements and provisions must be fulfilled.
<!-- end of short definition -->

> EXAMPLE Controls include action requests, cost schedules, project orders, work plans, and work calendars.

> HISTORY New entity in IFC1.0.

> IFC4 CHANGE Attribute _Identification_ added.

## Attributes

### Identification
An identifying designation given to a control
  It is the identifier at the occurrence level.

> IFC4 CHANGE Attribute unified by promoting from various subtypes of _IfcControl_.

### Controls
Reference to the relationship that associates the control to the object(s) being controlled.

## Concepts

### Control Assignment

Controls have assignments from products, processes, or other objects by using the relationship object _IfcRelAssignsToControl_.

