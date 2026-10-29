# IfcCooledBeam

A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCooledBeamType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cooled beam type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCooledBeamType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_ChilledWaterIn_CHILLEDWATER

Chilled water entering.

#### SOURCE_ChilledWaterOut_CHILLEDWATER

Chilled water leaving.

### Property Sets for Objects



### Quantity Sets



