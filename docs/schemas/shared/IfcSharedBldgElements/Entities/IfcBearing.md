# IfcBearing

Type of building element that is usually used to transmit loads from superstructure to substructure, and usually allowing movement (displacement or rotation) in one or more degrees of freedom. It is typically a mechanical component procured as a whole and installed on site, but in simple cases it may be built on site (composed of other building elements, element components, etc.).
<!-- end of short definition -->

> NOTE The sliding and roller materials are to be assigned to the bearing with the _Material Constituent Set_ concept.

> NOTE The displacements and rotations accommodated can be defined in the _Pset_BearingCommon_ property set.

## Attributes

### PredefinedType
Predefined generic type for a bearing that is specified in an enumeration. There may be a property set given specifically for the predefined types.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBearingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no bearing type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBearingType_.

## Concepts

### Property Sets for Objects



