# IfcStructuralAnalysisModel

The _IfcStructuralAnalysisModel_ is used to assemble all information needed to represent a structural analysis model. It encompasses certain general properties (such as analysis type), references to all contained structural members, structural supports or connections, as well as loads and the respective load results.
<!-- end of short definition -->

Important functionalities for the description of an analysis model are derived from existing IFC entities:

* From _IfcSystem_ it inherits the ability to couple the built system via _IfcRelReferencedInSpatialStructure_ to one or more _IfcSpatialElement_ subtypes as necessary.

* From _IfcGroup_ it inherits the inverse attribute IsGroupedBy, pointing to the relationship class _IfcRelAssignsToGroup_ . This allows the grouping of structural members (instances of _IfcStructuralMember_), and supports (instances of _IfcStructuralConnection_ which belong to a specific analysis model.

>> NOTE Loads (as instances of _IfcStructuralAction_ are not included through IsGroupedBy. Loads are assigned through the LoadedBy attribute relationship, using load groups as a grouping mechanism. Only top-level load groups should be referenced via LoadedBy, i.e. load combinations if any load combinations exist, or load cases if no load combinations exist in this analysis model.

>> NOTE Results (as instances of _IfcStructuralReaction_ are not included through IsGroupedBy. Results are assigned through the HasResults attribute relationship, using result groups as a grouping mechanism.

* From _IfcObjectDefinition_ it inherits the inverse attribute IsDecomposedBy pointing to the relationship class _IfcRelAggregates_. It provides the hierarchy between the separate (partial) analysis models.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Attribute _SharedPlacement_ and informal propositions added, allowing for easy retrieval of the common object placement and for specification of the analysis model's coordinate system before any structural item is instantiated. WHERE rule added.

**Informal Propositions**

1. If one or more structural item (instance of a subtype of _IfcStructuralItem_ is grouped into an _IfcStructuralAnalysisModel_, the attribute SharedPlacement shall be provided with a value.
2. The _ObjectPlacement_ of all structural items which are grouped into the same instance of _IfcStructuralAnalysisModel_ shall refer to the same instance of _IfcObjectPlacement_ as _IfcStructuralAnalysisModel_.SharedPlacement.


> NOTE This rule is necessary to achieve consistent topology representations. The topology representations of structural items in an analysis model are meant to share vertices and edges und must therefore have the same object placement.

> NOTE A structural item may be grouped into more than one analysis model. In this case, all these models must use the same instance of _IfcObjectPlacement_.

## Attributes

### PredefinedType


### OrientationOf2DPlane


### LoadedBy


### HasResults


### SharedPlacement


## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Aggregation



#### IfcStructuralAnalysisModel

This relationship provides the hierarchy between separate (partial) analysis models.

### Group Assignment



#### IfcStructuralItem

Structural members and connections assigned to the analysis model.

