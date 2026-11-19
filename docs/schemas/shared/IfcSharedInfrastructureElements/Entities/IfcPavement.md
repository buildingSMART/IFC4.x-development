# IfcPavement

Type of built element in a road or other paved area to provide an even surface sustaining loads from vehicles or pedestrians, usually comprising several courses.
<!-- end of short definition -->

NOTE Definition from ISO 6707-1: road, runway, or similar construction above the subgrade.

## Attributes

### PredefinedType
Identifies the predefined type of a pavement element. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcPavementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPavementType_.
