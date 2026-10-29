# IfcLightFixture

A light fixture is a container that is designed for the purpose of housing one or more lamps and optionally devices that control, restrict or vary their emission.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcLightFixtureType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no light fixture type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcLightFixtureType_.

## Concepts

### Lighting Geometry

This represents the light emission of the item having _IfcShapeRepresentation.RepresentationType_ of 'LightSource' and containing one or more IfcLightSource subtypes.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Connectivity



#### IfcRelConnectsElements_IfcCovering

Indicates a suspended ceiling anchoring the light fixture.

#### IfcRelFillsElements_IfcOpeningElement

Indicates embedding the light fixture in a building element such as a suspended ceiling.

### Object Typing



### Port Nesting



#### SINK_Line_POINTSOURCE_ELECTRICAL

The power supply line, typically a cable connected to a switch.

#### SOURCE_Socket_POINTSOURCE_LIGHTING

A socket providing electricity to a lamp with one terminal.

#### SINK_Line_DIRECTIONSOURCE_ELECTRICAL

The power supply line, typically a cable connected to a switch.

#### SOURCE_Socket1_DIRECTIONSOURCE_LIGHTING

A socket providing electricity to a lamp with two terminals.

#### SOURCE_Socket2_DIRECTIONSOURCE_LIGHTING

A socket providing electricity to a lamp with two terminals.

#### SOURCE_Socket3_DIRECTIONSOURCE_LIGHTING

A socket providing electricity to a lamp with two terminals.

#### SOURCE_Socket4_DIRECTIONSOURCE_LIGHTING

A socket providing electricity to a lamp with two terminals.

### Property Sets for Objects



### Quantity Sets



