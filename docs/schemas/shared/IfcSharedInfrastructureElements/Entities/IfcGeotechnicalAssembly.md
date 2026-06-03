# IfcGeotechnicalAssembly

Representation of the abstract concept of a geological and geotechnical model, usually an interpretation but sometimes created direct from ground penetrating measurement.
<!-- end of short definition -->

Use of an assembly is optional but can carry the methodology and uncertainty information.
Such assemblies will include _IfcGeotechnicalStratum_ entity types and may include other entity types such as _IfcPile_, _IfcSlab_ or _IfcSensor_ to represent the capping, lining or logging equipment present.
_IfcBorehole_ or _IfcGeoslice_ can have a physical reality as a construction hazard alongside being the carrier for the interpreted results. Geological hazards may be associated to any _IfcGeotechnicalAssembly_ or _IfcGeotechnicalStratum_.

> DEPRECATION The entity _IfcGeotechnicalAssembly_ shall not be used anymore, use _IfcGeoScienceModel_ instead.
