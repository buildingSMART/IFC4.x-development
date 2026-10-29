# IfcObjectDefinition

An _IfcObjectDefinition_ is the generalization of any semantically treated thing or process, either being a type or an occurrence. Object definitions can be named, using the inherited _Name_ attribute, which should be a user-recognizable label for the object occurrence. Further explanations to the object can be given using the inherited _Description_ attribute. A context is a specific kind of object definition as it provides the project or library context in which object types and object occurrences are defined.
<!-- end of short definition -->

Objects are independent pieces of information that might contain or reference other pieces of information. There are five essential kinds of relationships in which object definitions (by their instantiable subtypes) can be involved:

* **Assignment of other objects** - an assignment relationship (_IfcRelAssigns_) that refers to other types of objects and creates a bi-directional association. The semantic of the assignment is established at the level of the subtypes of the general _IfcRelAssigns_ relationship. There is no dependency implied a priori by the assignment.
* **Association to external resources** - an association relationship (_IfcRelAssociates_) that refers to external sources of information (most notably a classification or document) and creates a uni-directional association. There is no dependency implied by the association.
* **Aggregation of other objects** - an aggregation relationship (_IfcRelAggregates_) that establishes an unordered, spatial whole/part relation and creates a bi-directional relation. There is an implied dependency established.
* **Nesting of other objects** - a nesting relationship (_IfcRelNests_) that establishes an ordered, non-spatial whole/part relation and creates a bi-directional relation. There is an implied dependency established.
* **Declaration within a context** - a relationship (_IfcRelDeclares_) of the uppermost object definition within the object definition tree (e.g. the summary object within an object nesting tree) to the context (a project or project library). It applies the units, representation context and other context information to this object definition and all dependent ones.

> NOTE The link between the uppermost object in the spatial structure tree, that is _IfcSite_ or _IfcBuilding_, and the context provided by _IfcProject_ is created using the _IfcRelAggregates_ relationship. See _IfcProject_ for more information.

> HISTORY New abstract entity in IFC2x3.

> IFC4 CHANGE The new subtype _IfcContext_ and the relationship to context _HasContext_ has been added. The decomposition relationship is split into ordered nesting (_Nests_, _IsNestedBy_) and un-ordered aggregating (_Decomposes_, _IsDecomposedBy_).

## Attributes

### HasAssignments
Reference to the relationship objects, that assign (by an association relationship) other subtypes of _IfcObject_ to this object instance. Examples are the association to products, processes, controls, resources or groups.

### Nests
References to the decomposition relationship being a nesting. It determines that this object definition is a part within an ordered whole/part decomposition relationship. An object occurrence or type can only be part of a single decomposition (to allow hierarchical structures only).

> IFC4 CHANGE The inverse attribute datatype has been added and separated from _Decomposes_ defined at _IfcObjectDefinition_.

### IsNestedBy
References to the decomposition relationship being a nesting. It determines that this object definition is the whole within an ordered whole/part decomposition relationship. An object or object type can be nested by several other objects (occurrences or types).

> IFC4 CHANGE The inverse attribute datatype has been added and separated from _IsDecomposedBy_ defined at _IfcObjectDefinition_.

### HasContext
References to the context providing context information such as project unit or representation context. It should only be asserted for the uppermost non-spatial object.

> IFC4 CHANGE The inverse attribute datatype has been added.

### IsDecomposedBy
References to the decomposition relationship being an aggregation. It determines that this object definition is the whole within an unordered whole/part decomposition relationship. An object definition can be aggregated by several other objects (occurrences or parts).

> IFC4 CHANGE The inverse attribute datatype has been changed from the supertype _IfcRelDecomposes_ to subtype _IfcRelAggregates_.

### Decomposes
References to the decomposition relationship being an aggregation. It determines that this object definition is a part within an unordered whole/part decomposition relationship. An object definition can only be part of a single decomposition (to allow hierarchical structures only).

> IFC4 CHANGE The inverse attribute datatype has been changed from the supertype _IfcRelDecomposes_ to subtype _IfcRelAggregates_.

### HasAssociations
Reference to the relationship objects, that associates external references or other resource definitions to the object. Examples are the association to library, documentation or classification.

## Concepts

### Classification Association

Any object occurrence or object type can have a reference to a specific classification reference, i.e. to a particular facet within a classification system.

