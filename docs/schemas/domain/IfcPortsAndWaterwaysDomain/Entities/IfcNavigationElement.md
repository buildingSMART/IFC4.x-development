# IfcNavigationElement

A navigation element is an active or passive built element who's primary function is to provide navigational instructions and warnings to vessels, this could be in the form of a floating buoy, a fixed beacon.
<!-- end of short definition -->

Navigation elements can aggregate other components and elements to form the entire structure. this might include a frame structure to form the body, instances of _IfcSign_ for signage or instances of _IfcSignal_ for supplementary lights an/or sound signals.

## Attributes

### PredefinedType
Identifies the predefined type of a navigational element. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcNavigationElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcNavigationElementType_.
