# IfcGeoScienceFeatureTypeEnum

Defines the different predefined types of geoscience features that can specify an _IfcGeoScienceFeature_.
<!-- end of short definition -->


## Items
### DISCRETEDISCONTINUITY
Any interuption of the continuity in the rock material with its attendant mechanical, hydraulic and thermal properties.

### FOLD
A fold is formed by one or more systematically curved layers, surfaces, or lines in a rock body. A fold denotes a structure formed by the deformation of a geologic structure, such as a contact of which the original undeformed geometry is presumed, to form a structure that may be described by the translation of an abstract line (the fold axis) parallel to itself along some curvilinear path (the fold profile). Folds have a hinge zone (zone of maximum curvature along the surface) and limbs (parts of the deformed surface not in the hinge zone). Folds are described by an axial surface, hinge line, profile geometry, the solid angle between the limbs, and the relationships between adjacent folded surfaces if the folded structure is a layering fabric.

### FLUIDBODY
A distinct body of some fluid (liquid, gas) that fills the voids of a container such as an aquifer, system of aquifers, water well, etc. In hydrogeology this body is usually constituted by groundwater, but the model allows for other types of fillers e.g. petroleum.

### PIEZOMETRICWATERLEVEL
A surface on a fluid body within a local or regional area, e.g. piezometric, potentiometric, water table, salt wedge, etc.

### VOIDBODY
A discrete air filled geological feature, including caves and other voids.

### GEOLOGICUNIT
May represent a body of material in the Earth whose complete and precise extent is inferred to exist (e.g., North American Data Model GeologicUnit, Stratigraphic unit in the sense of NACSN, or International Stratigraphic Code ), or a classifier used to characterize parts of the Earth (e.g. lithologic map unit like 'granitic rock' or 'alluvial deposit', surficial units like 'till' or 'old alluvium'). It includes both formal units (i.e. formally adopted and named in an official lexicon) and informal units (i.e. named but not promoted to a lexicon) and unnamed units (i.e., recognizable, described and delineable in the field but not otherwise formalised). In simpler terms, a geologic unit is a package of earth material (generally rock or soil).

### GEOTECHNICALUNIT
A surface or a volume in which the mechanical behaviour and other design-relevant characteristics are characterized using the same geotechnical parameters values. Several alternative classifications (=GeotechModels) can be required in a project for different design tasks.

### HAZARDAREA
Discrete spatial object representing a natural hazard.

### HYDROGEOUNIT
Any soil or rock unit or zone that by virtue of its hydraulic properties has a distinct influence on the storage or movement of groundwater (after ANS, 1980).

### FAULT
A shear displacement structure includes all brittle to ductile style structures along which displacement has occurred, from a simple, single 'planar' surface to a fault system comprised of tens of strands of both brittle and ductile nature. This structure may have some significant thickness (a deformation zone) and have an associated body of deformed rock that may be considered a deformation unit (which geologicUnitType is ?DeformationUnit?) which can be associated to the ShearDisplacementStructure using GeologicFeatureRelation from the GeoSciML Extension package

### CONTACT
A contact is a general concept representing any kind of surface separating two geologic units, including primary boundaries such as depositional contacts, all kinds of unconformities, intrusive contacts, and gradational contacts, as well as faults that separate geologic units.

### PHYSICALPROPERTYDISTRIBUTION
Additional option (alternative to discrete models) to describe a +/- continuous spatial distribution of any physical parameter (geotechnical key-parameters, permeabilty, likelyhood of. e.g. a fault or any other uncertainty-related information)

### USERDEFINED
User-defined type.

### NOTDEFINED
Undefined type.
