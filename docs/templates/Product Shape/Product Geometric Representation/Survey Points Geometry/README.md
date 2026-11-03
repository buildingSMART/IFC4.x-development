Survey Points Geometry
==========================

Elements may provide a 'SurveyPoints' representation for defining a contour for _IfcSite_. It contains the survey points as a set of Cartesian points and optionally breaklines.

The representation identifier and type and the only allowed single representation item of the 'SurveyPoints' representation are:

_IfcShapeRepresentation_.RepresentationIdentifier = 'SurveyPoints'
_IfcShapeRepresentation_.RepresentationType : 'GeometricCurveSet'
_IfcShapeRepresentation_.Items = _IfcGeometricCurveSet_

```
concept {
    IfcSite:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcGeometricCurveSet:Elements -> IfcCartesianPoint
    IfcGeometricCurveSet:Elements -> IfcPolyline
    IfcGeometricCurveSet:Elements -> IfcCartesianPointList2D
    IfcGeometricCurveSet:Elements -> IfcIndexedPolyCurve
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
    IfcLabel_0 -> constraint_0
    constraint_0[label="='SurveyPoints'"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="='GeometricCurveSelect'"]
}
```