# IfcMaterialLayer

_IfcMaterialLayer_ is a single and identifiable part of an element which is constructed of a number of layers (one or more). Each _IfcMaterialLayer_ has a constant thickness and is located relative to the referencing _IfcMaterialLayerSet_ along the material layer set base (MlsBase).
<!-- end of short definition -->

Air gaps within a material layer set are represented as an _IfcMaterialLayer_ with the attribute _IsVentilated_ having the value TRUE or UNKNOWN. Such air gaps shall be interpreted as voids (not having a material).

> EXAMPLE A cavity wall with brick masonry used with an air gap in between would be modeled using three _IfcMaterialLayer_'s: [1] Brick, [2] Air gap, [3] Brick. The inner layer "Brick" would have a _Name_ = "Brick", an individual _LayerThickness_, and potentially a _Category_ indicating it as "load bearing", and a _Priority_ that controls how this material layer interacts with other material layers in wall connections.

The _IfcMaterialLayer_ may have a material layer name which may differ from the _IfcMaterial_ name referenced.

> EXAMPLE The _IfcMaterialLayer_ name of an insulation layer can be "Insulation", whereas the _IfcMaterial_ name is "polystyrene insulating boards".

> HISTORY New entity in IFC1.5

> IFC4 CHANGE The attributes _Name_, _Description_, _Category_, _Priority_ have been added at the end of attribute list. Data type of _LayerThickness_ relaxed to _IfcNonNegativeLengthMeasure_.

## Attributes

### Material
Optional reference to the material from which the layer is constructed. Note that if this value is not given, it does not denote a layer with no material (an air gap), it only means that the material is not specified at that point.

### LayerThickness
The thickness of the material layer. The meaning of "thickness" depends on its usage. In case of building elements elements utilizing _IfcMaterialLayerSetUsage_, the dimension is measured along the positive _LayerSetDirection_ as specified in _IfcMaterialLayerSetUsage_.

> NOTE The attribute value can be 0. for material thicknesses very close to zero, such as for a membrane. Material layers with thickess 0. may not be rendered in the geometric representation.

> IFC4 CHANGE The attribute datatype has been changed to _IfcNonNegativeLengthMeasure_ allowing for 0. as thickness.

### IsVentilated
Indication of whether the material layer represents an air layer (or cavity).
* set to TRUE if the material layer is an air gap and provides air exchange from the layer to the outside air.
* set to UNKNOWN if the material layer is an air gap and does not provide air exchange (or when this information about air exchange of the air gap is not available).
* set to FALSE if the material layer is a solid material layer (the default).

### Name
The name by which the material layer is known.

### Description
Definition of the material layer in more descriptive terms than given by attributes Name or Category.

### Category
Category of the material layer, e.g. the role it has in the layer set it belongs to (such as 'load bearing', 'thermal insulation' etc.). The list of keywords might be extended by model view definitions, however the following keywords shall apply in general:
* 'LoadBearing' — for all material layers having a load bearing function.
* 'Insulation' — for all material layers having an insolating function.
* 'Inner finish' — for the material layer being the inner finish.
* 'Outer finish' — for the material layer being the outer finish.

### Priority
The relative priority of the layer, expressed as normalised integer range [0..100]. Controls how layers intersect in connections and corners of building elements: a layer from one element protrudes into (i.e. displaces) a layer from another element in a joint of these elements if the former element's layer has higher priority than the latter. The priority value for a material layer in an element has to be set and maintained by software applications in relation to the material layers in connected elements.

> NOTE The layer priority at a connection may be overridden by the priority attributes of _IfcRelConnectsPathElements_ if that relationship is used to establish a logical connection between two building elements having a layer structure.

### ToMaterialLayerSet
Reference to the _IfcMaterialLayerSet_ in which the material layer is included.

## Formal Propositions

### NormalizedPriority
The _Property_ shall all be given as a normalized integer range [0..100], where 0 is the lowest and 100 the highest priority of the material layer.
