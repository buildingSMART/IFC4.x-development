Dataset Association
====================

The concept _Dataset Association_ describes how objects or object types can have associated datasets indicating external machine readable files. Datasets may be referenced in their entirety or as subsets using a _Filter_ which depends on the dataset type. Contents within datasets may be referenced from any object.

Typical document meta data, such as format, issue date, editor, and similar, can be captured with the association, the dataset content however remains with the external files.


```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesDataset:RelatedObjects
    IfcRelAssociatesDataset:Name -> IfcLabel_0
    IfcRelAssociatesDataset:RelatingDataset -> IfcDatasetReference
    IfcDatasetReference:Location -> IfcURIReference
    IfcDatasetReference:Identification -> IfcIdentifier
    IfcDatasetReference:Name -> IfcLabel_1
    IfcDatasetReference:Description -> IfcText
    IfcDatasetReference:Filter -> IfcText
    IfcRelAssociatesDataset:Name[binding="Name"]
}
```