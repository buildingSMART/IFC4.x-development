# IfcCourse

A built element whose length greatly exceeds its thickness and often also its width, usually of a single material laid on site on top of another horizontal or nearly horizontal built element. A course is distinctive from a earthworks element in that a course is a graded granular (which can be bound or unbound) material that is generally processed in some fashion, where as earthworks elements are soil earthen based structure that can be formed by removal and transport of general ground material.
<!-- end of short definition -->

Structurally a course does not have capacity to carry loads over open span, or to be removed or replaced as a single unit. examples of courses include:
* Graded aggregate layers
* Graded sand layers
* Cement bounded material (CBM)
* Asphalt layers

## Attributes

### PredefinedType
Identifies the predefined type of a course element. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcCourseType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCourseType_.
