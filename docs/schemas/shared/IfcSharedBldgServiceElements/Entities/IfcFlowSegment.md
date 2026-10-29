# IfcFlowSegment

The distribution flow element _IfcFlowSegment_ defines the occurrence of a segment of a flow distribution system.
<!-- end of short definition -->

The _IfcFlowSegment_ defines a particular occurrence of a segment inserted in the spatial context of a project. The parameters defining the type of the segment and/or its shape are defined by the _IfcFlowSegmentType_, which is related by the inverse relationship IsDefinedBy pointing to _IfcRelDefinesByType_.

> HISTORY New entity in IFC2.0.

> IFC4 CHANGE This entity has been deprecated for instantiation and will become ABSTRACT in a future release; new subtypes should now be used instead.

## Concepts

### Axis Geometry

Standard representations are defined at the supertype IfcDistributionFlowElement. For parametric flow segments where IfcMaterialProfileSetUsage is defined and an 'Axis' representation is defined, then the 'Body' representation may be generated using the 'SweptSolid' or 'AdvancedSweptSolid' representation types by sweeping the profile(s) along the axis.

### Material Profile Set Usage

The material of the IfcFlowSegment is defined using one of the following entities:


* IfcMaterialProfileSetUsage : for parametric segments, this defines the cross section and alignment to the 'Axis' representation, from which the 'Body' representation may be generated.
* IfcMaterialProfileSet : for non-parametric segments (having fixed length or path), this may define the cross section for analysis purposes, however the 'Body' representation is independently generated.
* IfcMaterialConstituentSet : for elements containing multiple materials where profiles are not applicable, this indicates materials at named parts.
* IfcMaterial : for elements comprised of a single material where profiles are not applicable, this indicates the material.


The material is attached by the RelatingMaterial attribute on the IfcRelAssociatesMaterial relationship. It is accessible by the HasAssociations inverse attribute. Material information can also be given at the IfcFlowSegmentType, defining the common attribute data for all occurrences of the same type. Standard names and material types are defined at subtypes.
