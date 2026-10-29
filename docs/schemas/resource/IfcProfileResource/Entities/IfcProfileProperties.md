# IfcProfileProperties

This is a collection of properties applicable to section profile definitions.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Entity made non-abstract. Subtypes _IfcGeneralProfileProperties_, _IfcStructuralProfileProperties_, and _IfcStructuralSteelProfileProperties_ deleted. Attribute _ProfileName_ deleted, use _ProfileDefinition.ProfileName_ instead. Attribute _ProfileDefinition_ made mandatory. Attributes _Name_, _Description_, and _HasProperties_ added (inherited from _IfcExtendedProperties_).

## Attributes

### ProfileDefinition
Profile definition which is qualified by these properties.
