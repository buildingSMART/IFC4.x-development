# IfcMaterialDefinition

_IfcMaterialDefinition_ is a general supertype for all material related information items in IFC that have common material related properties that may include association of material with some shape parameters or assignments to identified parts of a component.
<!-- end of short definition -->

There are three ways of assigning materials to a single component or multiple components; they are characterized as:

* by layer - assigning a material to a layer with constant thickness
* by profile - assigning a material to a profile with a constant of varying shape along an extrusion
* by constituents - assigning a material to an identified part of a component shape; the identification is by a keyword rather than by a shape parameter

Each instantiable subtype of _IfcMaterialDefinition_ may have material properties assigned, or have an external classification of its definition. It can be assigned to either a subtype of _IfcElement_, or a subtype of _IfcElementType_ by using the objectified relationship _IfcRelAssociatesMaterial_.

> HISTORY  New entity in IFC4

## Attributes

### AssociatedTo
Use of the _IfcMaterialDefinition_ subtypes within the material association of an element occurrence or element type. The association is established by the _IfcRelAssociatesMaterial_ relationship.
> IFC4 CHANGE The inverse attribute has been added.

### HasExternalReferences
Reference to external references, e.g. library, classification, or document information, that are associated to the material.
> IFC4 CHANGE The inverse attribute has been added.

### HasProperties
Material properties assigned to instances of subtypes of _IfcMaterialDefinition_.
> IFC4 CHANGE The inverse attribute has been added.
