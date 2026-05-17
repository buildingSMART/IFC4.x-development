# IfcArchElementType

The element type _IfcArchElementType_ defines a list of commonly shared property set definitions of an arch element and an optional list of product representations. It is used to define an arch element specification (the specific product information that is common to all occurrences of that element type).
<!-- end of short definition -->

{ .extDef}

An _IfcArchElementType_ is used to define the common properties of a certain type of arch element that may be applied to many occurrences of that type. The occurrences of an _IfcArchElementType_ are represented by instances of _IfcArchElement_.

> NOTE The _IfcArchElementType_ may pre-define common surface and material layer information using either _IfcMaterialProfileSet_ (for steel ribs) or _IfcMaterialLayerSet_ (for laminated segments).

> HISTORY New entity in IFC4.4.

## Attributes

### PredefinedType
Predefined types of arch elements from which the type of an _IfcArchElementType_ is selected. The _PredefinedType_ shall not be _USERDEFINED_ unless the _ElementType_ attribute is also set on the type-level supertype _IfcElementType_.
