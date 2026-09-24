# IfcClassification

An _IfcClassification_ is used for the arrangement of objects into a class or category according to a common purpose or their possession of common characteristics. A classification in the sense of _IfcClassification_ is taxonomy, or taxonomic scheme, arranged in a hierarchical structure. A category of objects relates to other categories in a generalization-specialization relationship. Therefore the classification items in an classification are organized in a tree structure.
<!-- end of short definition -->

The _IfcClassification_ identifies the classification system or source to which a classification reference refers to. Each classification reference may reference an instance of _IfcClassification_. A classification system declared may be either formally published, or it may be a locally defined method of classifying information.

> NOTE Examples for such formally published classifications are Omniclass, Uniclass, Masterformat, or DIN277.

There are two methods to define and reference a classification system:

1. Including the classification system structure within the dataset: Here a hierarchical tree of _IfcClassificationReference_'s is included that defines the classification system including the relationship between the classification items. The _ReferencedSource_ attribute of _IfcClassificationReference_ links the classification item to the parent item, and the parent item finally to the _IfcClassification_.
2. Referencing the classification system by a classification key or id: Here the _IfcClassificationReference_ is used to assign a classification id or key as _Identification_ attribute and it may link by _ReferencedSource_ attribute directly to the _IfcClassification_.

> HISTORY New entity in IFC1.5

> IFC 2x4 CHANGE Attribute _Edition_ made optional. Attributes: _Description_, _Location_, and _ReferenceTokens_ and inverse attribute _HasReferences_ added.

## Attributes

### Source
Source (or publisher) for this classification.
> NOTE that the source of the classification means the person or organization that was the original author or the person or organization currently acting as the publisher.

### Edition
The edition or version of the classification system from which the classification notation is derived.
> NOTE the version labeling system is specific to the classification system.

> IFC4 CHANGE The attribute has been changed to be optional.

### EditionDate
The date on which the edition of the classification used became valid.
> NOTE The indication of edition may be sufficient to identify the classification source uniquely but the edition date is provided as an optional attribute to enable more precise identification where required.

> IFC4 CHANGE The data type has been changed to _IfcDate_, the date string according to ISO8601.

### Name
The name or label by which the classification used is normally known.
> NOTE Examples of names include CI/SfB, Masterformat, BSAB, Uniclass, STABU, DIN276, DIN277 etc.

### Description
Additional description provided for the classification.
> IFC4 CHANGE New attribute added at the end of the attribute list.

### Specification
Resource identifier or locator, provided as URI, URN or URL, of the classification.

> IFC4 CHANGE New attribute added at the end of the attribute list.

### ReferenceTokens
The delimiter tokens that are used to mark the boundaries of individual facets (substrings) in a classification reference.


This typically applies then the _IfcClassification_ is used in
conjunction with _IfcClassificationReference_'s. If only one _ReferenceToken_ is provided, it applies to all boundaries of individual facets, if more than one _ReferenceToken_ are provided, the first token applies to the first boundary, the second token to the second boundary, and the n^th^ token to the n^th^ and any additional boundary.

> NOTE Tokens are typically recommended within the classification itself and each token will have a particular role.

> EXAMPLE 1 To indicate that the facet delimiter used for DIN277-2 reference key "2.1" ("Office rooms") is ".", a single _ReferenceToken_ ['.'] is provided. To indicate that the facet delimiter used for Omniclass Table 13 (space by function) reference key "13-15 11 34 11" ("Office") are "-" and " ", two _ReferenceToken_'s ['-', ' '] are provided.

> EXAMPLE 2 The use of _ReferenceTokens_ can also be extended to include masks. The use need to be agreed in view definitions or implementer agreements that stipulates a "mask syntax" that should be used.

> IFC4 CHANGE New attribute added at the end of the attribute list.

### ClassificationForObjects
The classification with which objects are associated.
> IFC4 CHANGE New inverse attribute.

### HasReferences
The classification references to which the classification applies. It can either be the final classification notation, or an intermediate classification item.
