Complementary Data Decomposition
================================

Provision of an aggregation structure where the data, representing the composite, is decomposed into parts represented by other data fragments.

The composite then provides exclusively the following:

* _Product Placement_ &mdash; the common object coordinate system to which the parts are placed relative

By default the following constraints apply to an element being decomposed by _Complementary Data Decomposition_:

* _Body Geometry_ &mdash; composite is constructed from the sum of the _Body Geometry_ of the parts;
* the composite shall not have an own _Body Geometry_, body geometry is provided at the parts;
* the composite shall not have an own _Material_ assignment, material is assigned to the parts.


```
concept {
    IfcComplementaryData_0:IsDecomposedBy -> IfcRelAggregates:RelatingObject
    IfcRelAggregates:RelatedObjects -> IfcComplementaryData_1
    IfcComplementaryData_1:Name -> IfcLabel
    IfcComplementaryData_0:IsDecomposedBy[binding="IsDecomposedBy"]
    IfcRelAggregates:RelatedObjects[binding="RelatedObjects"]
    IfcComplementaryData_1:Name[binding="PartName"]
}
```
