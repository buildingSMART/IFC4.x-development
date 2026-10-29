# IfcLamp

A lamp is an artificial light source such as a light bulb or tube.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcLampType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no lamp type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcLampType_.

## Concepts

### Material Set



#### Bulb

Material from which the bulb is constructed such as glass.

#### Conductor

Material from which the conductor is constructed.

#### Filament

Material from which the filament is constructed.

### Object Typing



### Port Nesting



#### SINK_Socket_LIGHTING

The socket providing electricity to the lamp.

### Property Sets for Objects



### Quantity Sets



