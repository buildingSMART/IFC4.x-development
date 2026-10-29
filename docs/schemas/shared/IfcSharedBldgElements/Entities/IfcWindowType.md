# IfcWindowType

The element type _IfcWindowType_ defines commonly shared information for occurrences of windows. The set of shared information may include:

* common properties within shared property sets
* common material information
* common partitioning of panels
* common operation types of panels
* common shape representations
<!-- end of short definition -->

A window type defines the particular parameter of the lining and one (or several) panels through the _IfcWindowLiningProperties_ and the _IfcWindowPanelProperties_ as predefined property sets applicable to windows only.

It is used to define a window specification, or window style (the specific product information that is common to all occurrences of that window type). Window types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcWindowType_ within building models are represented by instances of _IfcWindow_.

> HISTORY New entity in IFC4. The entity _IfcWindowType_ replaces the previous definition _IfcWindowStyle_ (which is deprecated in IFC4).

Partitioning type use definition

The _IfcWindowTypePartitioningEnum_ defines the general layout of the window type and its symbolic presentation. Depending on the enumerator, the appropriate instances of _IfcWindowLiningProperties_ and _IfcWindowPanelProperties_ are attached in the list of _HasPropertySets_. The _IfcWindowTypePartitioningEnum_ mainly determines the way of partitioning the window into individual window panels and thereby number and position of window panels.

See geometry use definitions at _IfcWindowTypePartitioningEnum_ for the correct usage of panel partitioning and _IfcWindowPanelProperties_ for the opening symbols for different panel operation types.

Material Use Definition

The material of the _IfcWindowType_ is defined by the _IfcMaterialConstituentSet_ or as fall back by _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial_._RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

The following keywords for _IfcMaterialConstituentSet.MaterialConstituents[n].Name_ shall be used:

* 'Lining' - to indicate that the material constituent applies to to the window lining
* 'Framing' - to indicate that the material constituent applies to to the window panels, if not provided, the 'Lining' material information applied to panels as well
* 'Glazing' - to indicate that the material constituent applies to to the glazing part

If the fall back single _IfcMaterial_ is referenced, it applies to the lining and framing of the window.

Geometry Use Definitions:

The _IfcWindowType_ may define the common shape of window occurrences. The common shape can be defined by applying the _RepresentationMaps_ attribute to refer to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations (e.g. with _IfcShapeRepresentation_'s having an _RepresentationIdentifier_ 'Box', 'Profile', 'FootPrint', or 'Body')

>> NOTE The product shape representations are defined as _RepresentationMaps_ (attribute of the supertype _IfcTypeProduct_), which get assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[n]_ being an _IfcMappedItem_. See _IfcTypeProduct_ for further information.

>> NOTE The values of attributes _RepresentationIdentifier_ and _RepresentationType_ of _IfcShapeRepresentation_ are restricted in the same way as those for _IfcWindow_.

## Attributes

### PredefinedType
Identifies the predefined types of a window element from which the type required may be set.

### PartitioningType
Type defining the general layout of the window type in terms of the partitioning of panels.

### ParameterTakesPrecedence
The Boolean value reflects, whether the parameter given in the attached lining and panel properties exactly define the geometry (TRUE), or whether the attached style shape take precedence (FALSE). In the last case the parameter have only informative value. If not provided, no such information can be inferred.

### UserDefinedPartitioningType
Designator for the user defined partitioning type, shall only be provided, if the value of _PartitioningType_ is set to USERDEFINED.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Property Sets for Types

Two subtypes of _IfcPreDefinedPropertySet_ are applicable to _IfcWindowType_:

* _IfcWindowLiningProperties_ - a single instance to define the shape parameters of the window lining
* _IfcWindowPanelProperties_ - one or several instances to define the shape parameters of the window panel(s)

### Type Body Geometry



### Window Type Attributes



