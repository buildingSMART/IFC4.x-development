# IfcClassificationSelect

The _IfcClassificationSelect_ enables selection of whether a classification reference is to be referenced from an external source, or whether a classification is referenced as such.
<!-- end of short definition -->

> NOTE Generally, it is expected that selection will be by _IfcClassificationReference_ to identify an individual classification notation that classifies an element in the building information model. For example an element, such as _IfcTank_, might be further classified by assigning an _IfcClassificationReference_ with _Identification_ = "L6814" and a _ClassificationSource_ identifying the appropriate version of Uniclass. _IfcClassification_ should only be selected in circumstances where there could be a need to indicate the classification system that will be used without associating a notation or reference to an individual object. This may occur for higher level objects such as _IfcProject_, _IfcSystem_, or similar. For example an _IfcStructuralAnalysisModel_ might be classified to be applicable to a particular version of EuroCode.

> HISTORY New select type in IFC2x

> IFC4 CHANGE Select renamed from IfcClassificationNotationSelect.
