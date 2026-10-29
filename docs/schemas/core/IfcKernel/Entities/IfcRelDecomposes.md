# IfcRelDecomposes

The decomposition relationship, _IfcRelDecomposes_, defines the general concept of elements being composed or decomposed. The decomposition relationship denotes a whole/part hierarchy with the ability to navigate from the whole (the composition) to the parts and vice versa.
<!-- end of short definition -->

Decompositions may be constrained by requiring both the whole and its parts, to be of the same type - thus establishing a nesting relationship. Or they may require some form of physical containment, thus establishing special types of aggregation relationships.

> NOTE There are two special names for decomposition, which are linguistically distinguished, nesting and aggregation. The subtypes of _IfcRelDecomposes_ will introduce either the nesting or aggregation convention (see _IfcRelNests_ and _IfcRelAggregates_).

> EXAMPLE A cost element is a nest of other cost elements, or a structural frame is an aggregation of beams and columns. Both are applications of the decomposition relationship.

Decompositions imply a dependency, i.e. the definition of the whole depends on the definition of the parts and the parts depend on the existence of the whole. The decomposition relationship can be applied in a recursive manner, i.e. a decomposed element can be part in another decomposition. Cyclic references must be prevented at application level.

> HISTORY New entity in IFC1.5, it is a generalisation of the IFC2.0 entity _IfcRelNests_.

> IFC4 CHANGE The differentiation between the aggregation and nesting is determined to be a non-ordered or an ordered collection of parts. The attributes _RelatingObject_ and _RelatedObjects_ have been demoted to the subtypes.
