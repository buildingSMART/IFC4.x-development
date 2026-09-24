# IfcPump

A pump is a device which imparts mechanical work on fluids or slurries to move them through a channel or pipeline. A typical use of a pump is to circulate chilled water or heating hot water in a building services distribution system.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPumpType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no pump type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPumpType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Impeller

Material from which the impeller of the pump is constructed. In the case of a positive displacement pump, the piston acts as the impeller.

#### Seal

Material from which the impeller shaft seal of the pump is constructed.

### Object Typing



### Port Nesting



#### SINK_Power_ELECTRICAL

Receives electrical power.

#### SINK_Inlet_NOTDEFINED

Fluid entering pump.

#### SOURCE_Outlet_NOTDEFINED

Fluid leaving pump.

### Property Sets for Objects



### Quantity Sets



