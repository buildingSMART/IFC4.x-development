# IfcRelAssociatesDataset

The objectified relationship (_IfcRelAssociatesDataset_) handles the assignment of a dataset (items of the select _IfcDatasetSelect_) to objects occurrences (subtypes of _IfcObject_) or object types (subtypes of _IfcTypeObject_).

The relationship is used to assign a dataset reference or a more detailed dataset information to objects. A single dataset reference can be applied to multiple objects.

The inherited attribute _RelatedObjects_ define the objects to which the document association is applied. The attribute _RelatingDataset_ is the reference to a dataset reference, applied to the object(s).
<!-- end of short definition -->

## Attributes

### RelatingDataset
Dataset information or reference which is applied to the objects.

