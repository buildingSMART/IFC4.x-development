# IfcMaterialLayerSetUsage

The _IfcMaterialLayerSetUsage_ determines the usage of _IfcMaterialLayerSet_ in terms of its location and orientation relative to the associated element geometry. The location of material layer set shall be compatible with the building element geometry (that is, material layers shall fit inside the element geometry). The rules to ensure the compatibility depend on the type of the building element.
<!-- end of short definition -->

> EXAMPLE  For a cavity brick wall with shape representation SweptSolid, the _IfcMaterialLayerSet.TotalThickness_ shall be equal to the wall thickness. Also the _OffsetFromReferenceLine_ shall match the exact positions between the two shape representations of _IfcWall_, that is the _IfcShapeRepresentation_'s with _RepresentationIdentifier_="Axis" and _RepresentationIdentifier_="Body".

> NOTE  Model view definitions or implementer agreements may provide more instructions on matching between building element geometry and material layer set usage.

The _IfcMaterialLayerSetUsage_ is always assigned to an individual occurrence object (and only to relevant subtypes of _IfcElement_). The _IfcMaterialLayerSet_, referenced by _ForLayerSet_, can however be shared among several occurrence objects. If the element type is available (in other words, an instance of the relevant subtype of _IfcElementType_ exists), then the _IfcMaterialLayerSet_ can be assigned to the element type. The assignment between a subtype of _IfcElement_ and the _IfcMaterialLayerSetUsage_ is handled by _IfcRelAssociatesMaterial_.

Attribute use definition

The _IfcMaterialLayerSetUsage_ is primarily intended to be associated with planar building elements having a constant thickness. With further agreements on the interpretation of _LayerSetDirection_, the usage can be extended also to other cases, for example to curved building elements, provided that the material layer thicknesses are constant.

Generally, an element may be layered in any of its primary directions, denoted by its x, y or z axis. The geometry use definitions at each specific type of building element will determine the applicable _LayerSetDirection_.

The following examples illustrate how the _IfcMaterialLayerSetUsage_ attributes (_LayerSetDirection_, _DirectionSense_, _OffsetFromReferenceLine_) can be used in different cases. Normative material use definitions are documented at each element (how these shall be used).

Figure 1 shows an example of the use of _IfcMaterialLayerSetUsage_ aligned to the axis of a wall.

> EXAMPLE For a layered wall with extruded geometric representation (vertical extrusion), the layer set direction will be perpendicular to extrusion direction, and can be derived from the direction of the wall axis. With the_DirectionSense_ (positive in this example) the individual _IfcMaterialLayers_ are assigned consecutively right-to-left or left-to-right. For a curved wall, "direction denoting the wall thickness" can be derived from the direction of the wall axis, and it will remain perpendicular to the wall path. The _DirectionSense_ applies as well.

> NOTE According to the _IfcWall_ material use definition the _LayerSetDirection_ for _IfcWall_ is always AXIS2 (that is, along the y-axis), as shown in this example.

![Mls usage](../../../../figures/ifcmateriallayersetusage_wall-01.png)

Figure 1 — Material layer set usage for wall

Figure 2 shows an example of the use of _IfcMaterialLayerSetUsage_ aligned to a slab.

> EXAMPLE  For a slab with perpendicular extruded geometric representation, the _LayerSetDirection_ will coincide with the extrusion direction (in positive or negative sense). In this example, the material layer set base is the extruded profile and consistent with the _IfcExtrudedAreaSolid.Position_, with the _DirectionSense_ being positive, the individual _IfcMaterialLayers_ are built up from the base towards the positive z direction in this case.

> NOTE  According to the _IfcSlab_ material use definition the _LayerSetDirection_ for _IfcSlab_ is always AXIS3 (that is, along the z-axis).

![Mls usage](../../../../figures/ifcmateriallayersetusage_slab-01.png)

Figure 2 — Material layer set usage for slab

Figure 3 shows an example of the use of _IfcMaterialLayerSetUsage_ aligned to a roof slab with non-perpendicular extrusion.

> EXAMPLE  For a slab with non-perpendicular extruded geometric representation, the guidelines above apply as well<small>. The material layer thickness and the <em>OffsetFromReferenceLine</em> are always measured
perpendicularly, even if the extrusion direction is not perpendicular. Therefore the total material layer thickness is
not equal to the extrusion depth of the geometry.</small>

![Mls usage](../../../../figures/ifcmateriallayersetusage_roofslab-01.png)

Figure 3 — Material layer set usage for roof slab

## Attributes

### ForLayerSet
The _IfcMaterialLayerSet_ set to which the usage is applied.

### LayerSetDirection
Orientation of the material layer set relative to element reference geometry. The meaning of the value of this attribute shall be specified in the geometry use section for each element. For extruded shape representation, direction can be given along the extrusion path (e.g. for slabs) or perpendicular to it (e.g. for walls).

> NOTE The _LayerSetDirection_ for _IfcWall_ shall be AXIS2 (i.e. the y-axis) and for _IfcSlab_ and _IfcPlate_ it shall be AXIS3 (i.e. the z-axis).

> NOTE Whether the material layers of the set being used shall 'grow' into the positive or negative direction of the given axis, shall be defined by _DirectionSense_ attribute.

### DirectionSense
Denotes whether the material layer set is oriented in positive or negative sense along the specified axis (defined by LayerSetDirection). "Positive" means that the consecutive layers (the _IfcMaterialLayer_ instances in the list of _IfcMaterialLayerSet.MaterialLayers_) are placed face-by-face in the direction of the positive axis as established by LayerSetDirection: for AXIS2 it would be in +y, for AXIS3 it would be +z. "Negative" means that the layers are placed face-by-face in the direction of the negative LayerSetDirection. In both cases, starting at the material layer set base line.
> NOTE the material layer set base line (MlsBase) is located by OffsetFromReferenceLine, and may be on the positive or negative side of the element reference line (or plane); positive or negative for MlsBase placement does not depend on the DirectionSense attribute, but on the relevant element axis.

### OffsetFromReferenceLine
Offset of the material layer set base line (MlsBase) from reference geometry (line or plane) of element. The offset can be positive or negative, unless restricted for a particular building element type in its use definition or by implementer agreement. A positive value means, that the MlsBase is placed on the positive side of the reference line or plane, on the axis established by LayerSetDirection (in case of AXIS2 into the direction of +y, or in case of AXIS3 into the direction of +z). A negative value means that the MlsBase is placed on the negative side, as established by LayerSetDirection (in case of AXIS2 into the direction of -y).
> NOTE the positive or negative sign in the offset only affects the MlsBase placement, it does not have any effect on the application of DirectionSense for orientation of the material layers; also DirectionSense does not change the MlsBase placement.

### ReferenceExtent
Extent of the extrusion of the elements body shape representation to which the _IfcMaterialLayerSetUsage_ applies. It is used as the reference value for the upper _OffsetValues[2]_ provided by the _IfcMaterialLayerWithOffsets_ subtype for included material layers.

> IFC4 CHANGE New attribute added to the end of attribute list.

> NOTE The attribute _ReferenceExtent_ shall be asserted, if an _IfcMaterialLayerWithOffsets_ is included in the _ForLayerSet.MaterialLayers_ list of material layers.

> NOTE The _ReferenceExtent_ for _IfcWall_ is the reference height starting at z=0 being the XY plane of the object coordinate system.
