Material Profile Set
====================

Material profile sets are associated with products or product types where materials are placed in cross-sections of specified dimensions following a path defined at occurrences of the type. Examples of such products are beams, columns, members, reinforcing, footings, piles, pipe segments, duct segments, and cable segments.

> EXAMPLE  Material profile sets can be provided at the _IfcColumnType_, defining the common material information for all occurrences of the same column type. It is then accessible by the inverse _IsTypedBy_ relationship at IfcColumn pointing to _IfcColumnType_ having the _HasAssociations_ inverse relationship to _IfcRelAssociatesMaterial_ with _RelatingMaterial_ referring to the _IfcMaterialProfileSet_. If an individual material association is provide at the _IfcColumn_ and the _IfcColumnType_, then the material directly assigned to _IfcColumn_ overrides the material assigned to _IfcColumnType_.


```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSet

    IfcMaterialProfileSet:MaterialLayers -> IfcMaterialProfile
    IfcMaterialProfile:Name -> IfcLabel_0
    IfcMaterialProfile:Material -> IfcMaterial_0
    IfcMaterialProfile:Name[binding="Name"]

    IfcMaterialProfile:Profile -> IfcProfileDef_0

    IfcProfileDef_0:ProfileType -> IfcProfileTypeEnum
    IfcProfileDef_0:ProfileName -> IfcLabel_2

    IfcMaterial_0:Name -> IfcLabel_1
    IfcMaterial_0:Name[binding="Name"]

}
```