# IfcElectricFlowStorageDevice

An electric flow storage device is a device in which electrical energy is stored and from which energy may be progressively released.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricFlowStorageDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric flow storage device type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricFlowStorageDeviceType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_ELECTRICAL

Incoming power used to charge the flow storage device.

#### SOURCE_Load_ELECTRICAL

Outgoing power backed by the flow storage device.

### Property Sets for Objects



### Quantity Sets



