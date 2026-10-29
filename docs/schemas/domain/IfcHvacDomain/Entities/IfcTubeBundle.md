# IfcTubeBundle

A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTubeBundleType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no tube bundle type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcTubeBundleType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Inlet_NOTDEFINED

Inlet.

#### SOURCE_Outlet_NOTDEFINED

Uutlet.

### Property Sets for Objects



### Quantity Sets



