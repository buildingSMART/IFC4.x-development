Annotation 2D Geometry
======================

The 'Annotation 2D Geometry' is used, when the representation of an annotation includes specific drafting representation elements, in particular areas for hatching and text.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ : 'Annotation'
*  _IfcShapeRepresentation_._RepresentationType_ : 'Annotation2D'
* _IfcShapeRepresentation_._Items_ :
    * subtypes of _IfcPoint_ and _IfcCurve_ being two-dimensional and within an _IfcGeometricCurveSet_
    * subtypes of _IfcAnnotationFillArea_ for hatches
    * _IfcTextLiteralWithExtentWithExtent_ for text

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcAnnotationFillArea
    IfcShapeRepresentation:Items -> IfcIndexedPolyCurve_2
    IfcShapeRepresentation:Items -> IfcCartesianPoint
    IfcShapeRepresentation:Items -> IfcTextLiteralWithExtent
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Annotation"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Annotation2D"]
    IfcAnnotationFillArea:OuterBoundary -> IfcIndexedPolyCurve_0
    IfcAnnotationFillArea:InnerBoundaries -> IfcIndexedPolyCurve_1
    IfcAnnotationFillArea:StyledByItem -> IfcStyledItem_0:Item
    IfcIndexedPolyCurve_0:Points -> IfcCartesianPointList2D_0
    IfcIndexedPolyCurve_0:Segments -> IfcArcIndex_0
    IfcIndexedPolyCurve_0:Segments -> IfcLineIndex_0
    IfcIndexedPolyCurve_1:Points -> IfcCartesianPointList2D_1
    IfcIndexedPolyCurve_1:Segments -> IfcArcIndex_1
    IfcIndexedPolyCurve_1:Segments -> IfcLineIndex_1
    IfcStyledItem_0:Styles -> IfcFillAreaStyle
    IfcFillAreaStyle -> Geometry_Fill_Area_Style
    IfcIndexedPolyCurve_2:Points -> IfcCartesianPointList2D_2
    IfcIndexedPolyCurve_2:StyledByItem -> IfcStyledItem_1:Item
    IfcCartesianPointList2D_2:CoordList -> IfcLengthMeasure
    IfcStyledItem_1:Styles -> IfcCurveStyle
    IfcCurveStyle -> Geometry_Curve_Style
    IfcTextLiteralWithExtent:Literal -> IfcPresentableText
    IfcTextLiteralWithExtent:Placement -> IfcAxis2Placement2D
    IfcTextLiteralWithExtent:Path -> IfcTextPath
    IfcTextLiteralWithExtent:StyledByItem -> IfcStyledItem_2:Item
    IfcStyledItem_2:Styles -> IfcTextStyle
    IfcTextStyle -> Geometry_Text_Style
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
