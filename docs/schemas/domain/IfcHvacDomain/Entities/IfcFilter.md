# IfcFilter

A filter is an apparatus used to remove particulate or gaseous matter from fluids and gases.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcFilterType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no filter type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcFilterType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Media

Material used for filtering particulates.

### Object Typing



### Port Nesting



#### SINK_Inlet_AIRPARTICLEFILTER_AIRCONDITIONING

Incoming fluid.

#### SOURCE_Outlet_AIRPARTICLEFILTER_AIRCONDITIONING

Outgoing fluid.

#### SINK_Inlet_COMPRESSEDAIRFILTER_COMPRESSEDAIR

Incoming fluid.

#### SOURCE_Outlet_COMPRESSEDAIRFILTER_COMPRESSEDAIR

Outgoing fluid.

#### SINK_Inlet_ODORFILTER_EXHAUST

Incoming fluid.

#### SOURCE_Outlet_ODORFILTER_EXHAUST

Outgoing fluid.

#### SINK_Inlet_OILFILTER_OIL

Incoming fluid.

#### SOURCE_Outlet_OILFILTER_OIL

Outgoing fluid.

#### SINK_Inlet_STRAINER_DRAINAGE

Incoming fluid.

#### SOURCE_Outlet_STRAINER_DRAINAGE

Outgoing fluid.

#### SINK_Inlet_WATERFILTER_DOMESTICCOLDWATER

Incoming fluid.

#### SOURCE_Outlet_WATERFILTER_DOMESTICCOLDWATER

Outgoing fluid.

### Property Sets for Objects



### Quantity Sets



