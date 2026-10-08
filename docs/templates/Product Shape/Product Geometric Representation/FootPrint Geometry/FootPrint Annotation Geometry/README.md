FootPrint Annotation Geometry
=============================

The 'FootPrint Annotation Geometry' is the representation for the floor plan projection of the geometric representation of elements, comprising of mainly 2D curves, hatches and additional annotations such as a tag number or similar.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

*  _IfcShapeRepresentation_._RepresentationIdentifier_ : 'FootPrint'
*  _IfcShapeRepresentation_._RepresentationType_ : 'Annotation2D'
* _IfcShapeRepresentation_._Items_ :
    * subtypes of _IfcPoint_ and _IfcCurve_ being two-dimensional and within an _IfcGeometricCurveSet_
    * subtypes of _IfcAnnotationFillArea_ for hatches
    * _IfcTextLiteralWithExtent_ for text

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcShapeRepresentation:Items -> IfcAnnotationFillArea
    IfcShapeRepresentation:Items -> IfcTextLiteralWithExtent
    IfcLabel_0 -> constraint_0
    constraint_0[label="=FootPrint"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Annotation2D"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
