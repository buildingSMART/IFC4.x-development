# IfcRelServicesBuildings

The _IfcRelServicesBuildings_ is an objectified relationship that defines the relationship between a system and the sites, buildings, storeys, spaces, or spatial zones, it serves. Examples of systems are:

* building service systems (heating, cooling, waste water system) represented by instances of _IfcDistributionSystem_;
* building systems (fenestration, shading) represented by instances of _IfcBuildingSystem_;
* zones as collection of logically grouped spaces represented by instances of _IfcZone_
* idealized structural analysis systems represented by instances of _IfcStructuralAnalysisModel_.
<!-- end of short definition -->

> NOTE The name _IfcRelServicesBuildings_ is a known anomaly, as the relationship is not restricted to buildings anymore.

> HISTORY New entity in IFC1.0.

> IFC2x CHANGE The data type of the attribute _RelatedBuildings_ has been changed from _IfcBuilding_ to its supertype _IfcSpatialStructureElement_ with upward compatibility for file based exchange.

> IFC4.3.0.0 DEPRECATION Use IfcRelReferencedInSpatialStructure instead.

## Attributes

### RelatingSystem
System that services the Buildings.

### RelatedBuildings
Spatial structure elements (including site, building, storeys) that are serviced by the system.
> IFC2x CHANGE The data type has been changed from _IfcBuilding_ to _IfcSpatialStructureElement_ with upward compatibility for file based exchange.

> IFC4 CHANGE The data type has been changed from _IfcSpatialStructureElement_ to _IfcSpatialElement_ with upward compatibility for file based exchange.
