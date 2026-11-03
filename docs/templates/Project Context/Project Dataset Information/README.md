Project Dataset Information
==========================

Projects may define external datasets, which may be used to attach arbitrary machine readable information to objects contained within the same project or referencing projects.

```
concept {
    IfcContext:HasAssociations -> IfcRelAssociatesDataset:RelatedObjects
    IfcContext:LongName -> IfcLabel_1
    IfcContext:ObjectType -> IfcLabel_2
    IfcContext:Phase -> IfcLabel_3
    IfcRelAssociatesDataset:RelatingDataset -> IfcDatasetInformation
    IfcDatasetInformation:Identification -> IfcIdentifier_0
    IfcDatasetInformation:Name -> IfcLabel_0
    IfcDatasetInformation:Description -> IfcText
    IfcDatasetInformation:Location -> IfcURIReference_0
    IfcDatasetInformation:ElectronicFormat -> IfcIdentifier_1
    IfcDatasetInformation:SchemaReference -> IfcURIReference_1
    IfcDatasetInformation:Identification[binding="DatasetIdentification"]
    IfcDatasetInformation:Location[binding="DatasetLocation"]
    IfcDatasetInformation:SchemaReference[binding="DatasetSchemaReference"]
}
```