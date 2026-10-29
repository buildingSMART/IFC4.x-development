Reference Value Time Series
===========================



```
concept {
    IfcPropertyReferenceValue:Name -> IfcIdentifier
    IfcPropertyReferenceValue:Specification -> IfcText
    IfcPropertyReferenceValue:PropertyReference -> IfcIrregularTimeSeries
    IfcIrregularTimeSeries:Values -> IfcIrregularTimeSeriesValue
    IfcIrregularTimeSeriesValue:ListValues -> IfcValue
    IfcPropertyReferenceValue:Name[binding="PropertyName"]
    IfcPropertyReferenceValue:PropertyReference[binding="Value"]
    IfcIrregularTimeSeriesValue:ListValues[binding="Reference"]
}
```
