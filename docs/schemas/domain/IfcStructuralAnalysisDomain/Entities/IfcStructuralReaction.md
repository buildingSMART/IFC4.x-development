# IfcStructuralReaction

A structural reaction is a structural activity that results from a structural action imposed to a structural item or building element. Examples are support reactions, internal forces, and deflections.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Inverse attribute _Causes_ deleted; use _IfcRelAssignsToProduct_ via _HasAssignments_ instead.

Structural reactions are grouped into _IfcStructuralResultGroup_s via the inverse relationship _HasAssignments_ and an _IfcRelAssignsToGroup_ relationship object. _IfcStructuralResultGroup.ResultGroupFor_ finally refers to the structural analysis model in which the results occur.

It is furthermore possible to establish relationships between reactions in one analysis model and actions which they cause in another analysis model. For example, a support reaction from one structural system may be taken over as a load onto another supporting structural system. This is expressed by means of the inverse relationship _HasAssignments_ of the reaction and an _IfcRelAssignsToProduct_ relationship object. _IfcRelAssignsToProduct.Name_ is set to 'Causes' and _IfcRelAssignsToProduct.RelatingProduct_ refers to an instance of a subtype of _IfcStructuralAction_.
