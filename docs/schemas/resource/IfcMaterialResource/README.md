IfcMaterialResource
===================

The schema _IfcMaterialResource_ contains the types and entities that are used to define materials (substances, of which products are made of). Materials are defined generically.

> NOTE  The references to the usage of materials is made from the relevant elements through the objectified relationship _IfcRelAssociatesMaterial_.

Material definitions are distinguished by how they apply to elements or element types and by their components (layers, profiles, parts).

Material designation can be made for element occurrences to support a limited range of their parametric representation using

1. a structured set of material layers _IfcMaterialLayerSetUsage_ and how the layers relate to the reference axis or plane,
2. a structured set of material profiles _IfcMaterialProfileSetUsage_ and how the profiles relate to the reference axis.

Material designation can be made for element occurrences or element types without applying a parametric meaning using

1. a set of material layers (with a specified configuration by sequence and thickness of material layers) _IfcMaterialLayerSet_, or
2. a set of material profiles (with a specified configuration by positioning and outline profile of material profiles) _IfcMaterialProfileSet_, or
3. a set of materials (without a specified configuration or structure) _IfcMaterialConstituentSet_, or
4. as fallback by a single material _IfcMaterial_ (including composite materials),

These options are exposed for association with _IfcElement_ or _IfcElementType_ and their subtypes through a select type _IfcMaterialSelect_. The association is realized by the objectified relationship _IfcRelAssociatesMaterial_, accessible by the inverse relationship _AssociatedTo_. Some associations to specific material entities may be restricted as not being appropriate within the specialized element or element type definitions.

The following material properties and information sets can be assigned to an _IfcMaterialDefinition_, or only to a single _IfcMaterial_.

* Material properties;
* Material classification and material library reference;
* Material presentation in shape models (e.g. by color, hatching, rendering);
* Relation to the ingredients of a material composite.

> HISTORY  New schema in IFC1.0

> IFC4 CHANGE  Definition of material properties and their assignment to _IfcMaterial_ or other appropriate options in _IfcMaterialSelect_ is now fully captured by _IfcMaterialProperties_ using the general _IfcProperty_ approach. Specific predefined subtypes of _IfcMaterialProperties_ are no longer available.

> DEPRECATION  Material designation by using _IfcMaterialList_ is deprecated and should not be used. The classification of materials should not be done using _IfcMaterialClassificationRelationship_ anymore (entity type deprecated); the _IfcExternalReferenceRelationship_ in _IfcExternalReferenceResource_ schema should be used instead.
