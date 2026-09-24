# IfcMetric

An _IfcMetric_ is used to capture quantitative resultant metrics that can be applied to objectives.
<!-- end of short definition -->

_IfcMetric_ is a subtype of _IfcConstraint_ and may be associated with any subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by _IfcResourceConstraintRelationship_.

The aim of _IfcMetric_ is to capture the quantitative aspects of a constraint.

```
digraph dot_neato {
IfcResourceConstraintRelationship [label=<IfcResource<br />ConstraintRelationship>, pos="200,-70!"];
IfcElementQuantity [label=IfcElementQuantity, pos="0,0!"];
IfcQuantityWeight [label=<{IfcQuantityWeight | Name: NetWeight<br />WeightValue: 20}>, pos="0,-70!"];

IfcObjective [label=<{IfcObjective| Name: Safe lifting weight<br />LogicalAggregator: LOGICALAND<br />ObjectiveQualifier: HEALTHANDSAFETY}>, pos="450,-70!"];

IfcMetric2 [label=<{IfcMetric | Benchmark: GREATERTHANOREQUALTO<br />DataValue: 19}>, pos="300,-170!"];
IfcMetric [label=<{IfcMetric | Benchmark: LESSTHANOREQUALTO<br />DataValue: 21}>,pos="600,-170!"];
IfcReference2 [label=<{IfcReference | AttributeIdentifier: WeightValue }>, pos="300,-270!"];
IfcReference [label=<{IfcReference | AttributeIdentifier: WeightValue }>, pos="600,-270!"];

IfcElementQuantity -> IfcQuantityWeight [label="Quantities[1]"];
IfcResourceConstraintRelationship -> IfcQuantityWeight [headlabel=<Related<br />Resource<br/>Objects[1]>, labelfontsize=7, labelangle=45, labeldistance=3]
IfcResourceConstraintRelationship -> IfcObjective [headlabel=<Relating<br />Constraint>, labelfontsize=7, labelangle=-25, labeldistance=3.2]

IfcObjective -> IfcMetric [label="BenchmarkValues[2]"];
IfcObjective -> IfcMetric2 [label="BenchmarkValues[1]"];
IfcMetric2 -> IfcReference2 [label="ReferencePath"];
IfcMetric -> IfcReference [label="ReferencePath"];
}
```

Figure USERDEFCONSTRAINT — An example user defined constraint.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE ReferencePath attribute added for indicating the value to be constrained along a path of attribute references.

## Attributes

### Benchmark
Enumeration that identifies the type of benchmark data.

### ValueSource
Reference source for data values.

If _DataValue_ refers to an _IfcTable_, this attribute identifies the relevant column identified by _IfcTableColumn_._Identifier_.

### DataValue
The value to be compared on associated objects. A null value indicates comparison to null.
> IFC4 ADD1 CHANGE This attribute is now optional.

### ReferencePath
Optional path to an attribute to be constrained on associated objects.
If provided, the metric may be validated by resolving the path to the current value on associated object(s), and comparing such value with _DataValue_ according to the _Benchmark_.
