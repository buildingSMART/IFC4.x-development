Alignment Layout - Reusing Horizontal Layout
============================================

Nesting and aggregation relationships between _IfcAlignment_'s and their layouts, in the case where multiple alignments re-use the same horizontal layout definition.

In the diagram below is an example of a *parent* alignment, with the horizontal layout, and two *child* alignments, one with a vertical layout, and the other with a vertical and a cant layout; both re-using the definition of the horizontal layout from the *parent* alignment.

When defining the list of segments for the business logic (i.e., _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_, _IfcAlignmentCantSegment_):

1. A **zero-length segment** shall be added, at the end of the list of segments for _IfcAlignmentSegment.DesignParameters_.
2. If the geometry definition is also present, and it is not IfcOffsetCurveByDistances, IfcPolyline or IfcIndexedPolyCurve, then each of the zero-length segments shall have a _IfcCurveSegment_ counterpart - of length zero.

```
concept {
    IfcAlignment_0:IsNestedBy -> IfcRelNests_0:RelatingObject
    IfcAlignment_0:IsDecomposedBy -> IfcRelAggregates_0:RelatingObject
    IfcRelAggregates_0:RelatedObjects -> IfcAlignment_1
    IfcRelAggregates_0:RelatedObjects -> IfcAlignment_2
    IfcRelNests_0:RelatedObjects -> IfcAlignmentHorizontal
    IfcAlignmentHorizontal:IsNestedBy -> IfcRelNests_1:RelatingObject
    IfcRelNests_1:RelatedObjects -> IfcAlignmentSegment_0
    IfcAlignmentSegment_0:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignment_1:IsNestedBy -> IfcRelNests_2:RelatingObject
    IfcRelNests_2:RelatedObjects -> IfcAlignmentVertical_1
    IfcAlignmentVertical_1:IsNestedBy -> IfcRelNests_3:RelatingObject
    IfcRelNests_3:RelatedObjects -> IfcAlignmentSegment_1
    IfcAlignmentSegment_1:DesignParameters -> IfcAlignmentVerticalSegment_1
    IfcAlignment_2:IsNestedBy -> IfcRelNests_4:RelatingObject
    IfcRelNests_4:RelatedObjects -> IfcAlignmentVertical_2
    IfcAlignmentVertical_2:IsNestedBy -> IfcRelNests_6:RelatingObject
    IfcRelNests_6:RelatedObjects -> IfcAlignmentSegment_3
    IfcAlignmentSegment_3:DesignParameters -> IfcAlignmentVerticalSegment_2
    IfcRelNests_4:RelatedObjects -> IfcAlignmentCant
    IfcAlignmentCant:IsNestedBy -> IfcRelNests_5:RelatingObject
    IfcRelNests_5:RelatedObjects -> IfcAlignmentSegment_2
    IfcAlignmentSegment_2:DesignParameters -> IfcAlignmentCantSegment
}
```
