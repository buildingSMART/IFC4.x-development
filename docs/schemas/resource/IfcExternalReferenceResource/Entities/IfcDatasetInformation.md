# IfcDatasetInformation

_IfcDatasetInformation_ captures "metadata" of an external dataset. The actual content of the dataset is not defined in this specification; instead, it can be found following the _Location_ attribute.

The same _IfcDatasetInformation_ can be referenced from the exchange structure in total or in parts (e.g. by refering to particular chapters or paragraphs) using the _IfcDatasetReference_. All _IfcDatasetReference_'s that utilize the _IfcDatasetInformation_ are accessible by the inverse relationship _HasDatasetReferences_.
<!-- end of short definition -->

## Attributes

### SchemaReference
An optional attribute for referencing a schema that defines the possible content and structure of the dataset (e.g. xsd).

### DatasetInfoForObjects
The objects to which the dataset information applies.

### HasDatasetReferences
The dataset references to which the document applies.

