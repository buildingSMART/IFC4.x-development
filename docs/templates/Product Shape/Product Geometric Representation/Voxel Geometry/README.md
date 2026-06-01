Voxel Geometry
===================



```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcVoxelGrid
    IfcVoxelGrid:HasColours -> IfcIndexedColourMap:MappedTo
    IfcIndexedColourMap:Colours -> IfcColourRgbList:ColourList
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure
    IfcIndexedColourMap:MappedTo -> IfcTessellatedItem:HasColours

    IfcProduct:ReferencedBy -> IfcRelAssignsToProduct:RelatingProduct
    IfcRelAssignsToProduct:RelatedObjects -> IfcVoxelData:HasAssignments
    IfcRelAssignsToProduct:RelatedObjects[binding="Type"]
    IfcVoxelData:Representation -> IfcProductDefinitionShape
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Voxel"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```