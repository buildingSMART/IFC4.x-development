# IfcContext

_IfcContext_ is the generalization of a project context in which objects, type objects, property sets, and properties are defined. The _IfcProject_ as subtype of _IfcContext_ provides the context for all information on a construction project, it may include one or several _IfcProjectLibrary_'s as subtype of _IfcContext_ to register the included libraries for the project. A library of products that is referenced is declared within the _IfcProjectLibrary_ as the context of that library.
<!-- end of short definition -->

Context definitions can be named, using the inherited _Name_ attribute, which should be a user-recognizable key or number for the context. The _LongName_ can add a full name. Further explanations to the context can be given using the inherited _Description_ attribute.

A Context is declared by the relationship object _IfcRelDeclares_ that refers to the corresponding objects within the context. More specific relationships are introduced at the level of subtypes.

> HISTORY New abstract entity in IFC4.

## Attributes

### ObjectType
The object type denotes a particular type that indicates the object further. The use has to be established at the level of instantiable subtypes.
> NOTE Subtypes of _IfcContext_ do not introduce a _PredefinedType_ attribute, therefore the usage of _ObjectType_ is not bound to the selection of USERDEFINED within the _PredefinedType_ enumeration.

### LongName
Long name for the context as used for reference purposes.

### Phase
Current project phase, or life-cycle phase of this project. Applicable values have to be agreed upon by view definitions or implementer agreements.

### RepresentationContexts
Context of the representations used within the context. When the context is a project and it includes shape representations for its components, one or several geometric representation contexts need to be included that define e.g. the world coordinate system, the coordinate space dimensions, and/or the precision factor.
> IFC4 CHANGE The attribute has been changed to be optional. Change made with upward compatibility for file based exchange.

### UnitsInContext
Units globally assigned to measure types used within the context.
> IFC4 CHANGE The attribute has been changed to be optional. Change made with upward compatibility for file based exchange.

### IsDefinedBy
Set of relationships to property set definitions attached to this context. Those statically or dynamically defined properties contain alphanumeric information content that further defines the context.
> IFC4 CHANGE The data type has been changed from _IfcRelDefines_ to _IfcRelDefinesByProperties_ with upward compatibility for file based exchange.

### Declares
Reference to the _IfcRelDeclares_ relationship that assigns the uppermost entities of included hierarchies to this context instance.
> NOTE The spatial hierarchy is assigned to _IfcProject_ using the _IfcRelAggregates_ relationship. This is a single exception due to compatibility reasons with earlier releases.
