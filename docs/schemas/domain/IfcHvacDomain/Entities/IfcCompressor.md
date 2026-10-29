# IfcCompressor

A compressor is a device that compresses a fluid typically used in a refrigeration circuit.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCompressorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no compressor type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCompressorType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Refrigerant

Refrigerant material.

### Object Typing



### Port Nesting



#### SINK_RefrigerantIn_REFRIGERATION

Uncompressed vapor refrigerant entering the compressor.

#### SOURCE_RefrigerantOut_REFRIGERATION

Compressed vapor refrigerant leaving the compressor.

### Property Sets for Objects



### Quantity Sets



