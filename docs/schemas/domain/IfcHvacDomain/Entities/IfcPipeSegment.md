# IfcPipeSegment

A pipe segment is used to typically join two sections of a piping network.
<!-- end of short definition -->

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPipeSegmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no pipe segment type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPipeSegmentType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

#### Coating

The outer coating, if applicable.

#### Insulation

The insulating wrapping, if applicable.

#### Lining

The inner lining, if applicable.

### Object Typing



### Port Nesting



#### SINK_Inlet_NOTDEFINED

The flow inlet.

#### SOURCE_Outlet_NOTDEFINED

The flow outlet.

### Property Sets for Objects



### Quantity Sets



