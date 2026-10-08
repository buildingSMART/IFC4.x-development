# IfcFlowMeter

A flow meter is a device that is used to measure the flow rate in a system.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFlowMeterType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no flow meter type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcFlowMeterType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Inlet_ENERGYMETER_ELECTRICAL

Inlet from utility.

#### SOURCE_Outlet_ENERGYMETER_ELECTRICAL

Measured use.

#### SINK_Inlet_GASMETER_GAS

Inlet from utility.

#### SOURCE_Outlet_GASMETER_GAS

Measured use.

#### SINK_Inlet_OILMETER_OIL

Inlet from utility.

#### SOURCE_Outlet_OILMETER_OIL

Measured use.

#### SINK_Inlet_WATERMETER_DOMESTICCOLDWATER

Inlet from utility.

#### SOURCE_Outlet_WATERMETER_DOMESTICCOLDWATER

Measured use.

### Property Sets for Objects



### Quantity Sets



