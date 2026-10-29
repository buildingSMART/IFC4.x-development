# IfcMedicalDevice

A medical device is attached to a medical piping system and operates upon medical gases to perform a specific function. Medical gases include medical air, medical vacuum, oxygen, carbon dioxide, nitrogen, and nitrous oxide.
<!-- end of short definition -->

Outlets for medical gasses should use _IfcValve_ with PredefinedType equal to GASTAP, containing an _IfcDistributionPort_ with FlowDirection=SINK and PredefinedType equal to COMPRESSEDAIR, VACUUM, or CHEMICAL, and having property sets on the port further indicating the gas type and pressure. Tanks for medical gasses should use _IfcTank_ with PredefinedType equal to PRESSUREVESSEL, containing an _IfcDistributionPort_ with FlowDirection=SOURCE and PredefinedType=CHEMICAL, and having property sets on the port further indicating the gas type and pressure range.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType


### CorrectTypeAssigned

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Power_VACUUMSTATION_ELECTRICAL

Receives electrical power.

#### SOURCE_Vacuum_VACUUMSTATION_VACUUM

Provides suction.

### Property Sets for Objects



### Quantity Sets



