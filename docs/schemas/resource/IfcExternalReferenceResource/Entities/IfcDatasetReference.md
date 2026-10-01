# IfcDatasetReference

An _IfcDatasetReference_ is a reference to the location of a dataset. The reference is given by a system interpretable _Location_ attribute (a URL string) where the document can be found, and an optional inherited internal reference _Identification_, which refers to a system interpretable position within the dataset. The optional inherited _Name_ attribute is meant to have meaning for human readers. Optional dataset metadata can also be captured through reference to _IfcDatasetInformation_.
Furthermore, the optional _Filter_ attribute can be used to provide a text as e.g. SQL, XQuery etc to filter out data when only a subset is relevant for the dataset reference.
<!-- end of short definition -->

## Attributes

### Description
Description of the dataset reference for informational purposes.

### ReferencedDataset
Information about the referenced dataset.

### Filter
An optional text as e.g. SQL, XQuery etc to filter out data when only a subset is relevant for the dataset reference.

### DatasetRefForObjects
The dataset reference with which objects are associated.

## Formal Propositions

### WR1
A name should only be given, if no dataset information (including the dataset name) is attached.

