# IfcElectricGenerator

An electric generator is an engine that is a machine for converting mechanical energy into electrical energy.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricGeneratorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric generator type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricGeneratorType_.

## Concepts

### Aggregation



#### ENGINEGENERATOR_IfcEngine

Engine-Generator sets may optionally include an engine to indicate specific detail.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SOURCE_Load_ELECTRICAL

Outgoing power from generator.

### Property Sets for Objects



### Quantity Sets



