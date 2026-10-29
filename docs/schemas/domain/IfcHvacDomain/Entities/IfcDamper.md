# IfcDamper

A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcDamperType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no damper type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDamperType_.

## Concepts

### Material Set



#### Blade

The material from which the damper blades are constructed.

#### Frame

The material from which the damper frame is constructed.

#### Seal

The material from which the damper seals are constructed.

### Object Typing



### Port Nesting



#### SINK_AirIn_AIRCONDITIONING

Air entering damper.

#### SOURCE_AirOut_AIRCONDITIONING

Air leaving damper, with flow regulated according to position of damper.

### Property Sets for Objects



### Quantity Sets



