# IfcFaceBound

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A face bound is a loop which is intended to be used for bounding a face.

> NOTE Entity adapted from **face_bound** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0

## Attributes

### Bound
The loop which will be used as a face boundary.

### Orientation
This indicated whether (TRUE) or not (FALSE) the loop has the same sense when used to bound the face as when first defined. If sense is FALSE the senses of all its component oriented edges are implicitly reversed when used in the face.
