Material Layer Set
==================

Material layer sets are associated with products or product types to indicate a parametric specification of layers having specified thickness filling a boundary defined on the product, or the occurrences of the product type. Examples of such products or product types are slabs, walls, and plates.


```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSet

    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayer:Name -> IfcLabel_0
    IfcMaterialLayer:Material -> IfcMaterial_0
    IfcMaterialLayer:Name[binding="Name"]
    
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure

    IfcMaterial_0:Name -> IfcLabel_1
    IfcMaterial_0:Name[binding="Name"]

}
```
