# IfcStructuralAction

A structural action is a structural activity that acts upon a structural item or building element.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _DestabilizingLoad_ made optional. Attribute _CausedBy_ deleted; use _IfcRelAssignsToProduct_ via _ReferencedBy_ instead.

Relationship use definition

Structural actions are grouped into either an _IfcStructuralLoadGroup_ of predefined type LOAD_GROUP or, more often, an _IfcStructuralLoadCase_. This is accomplished via the inverse relationship _HasAssignments_ and an _IfcRelAssignsToGroup_ relationship object. _IfcStructuralLoadGroup.LoadGroupFor_ or _IfcStructuralLoadCase.LoadGroupFor_ respectively refers to the structural analysis model(s) in which the loads are used.

It is furthermore possible to establish relationships between actions in one analysis model and reactions in another analysis model which cause the actions. For example, a support reaction from one structural system may be taken over as a load onto another supporting structural system. This is expressed by means of the inverse relationship _ReferencedBy_ of the action and an _IfcRelAssignsToProduct_ relationship object. _IfcRelAssignsToProduct.Name_ is set to 'Causes' and _IfcRelAssignsToProduct.RelatedObjects_ refers to an instance of a subtype of _IfcStructuralReaction_.

## Attributes

### DestabilizingLoad
Indicates if this action may cause a stability problem. If it is 'FALSE', no further investigations regarding stability problems are necessary.
