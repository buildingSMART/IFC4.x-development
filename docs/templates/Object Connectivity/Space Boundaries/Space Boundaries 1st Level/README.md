Space Boundaries 1st Level
==========================

Spaces may have boundaries defined by building elements such as walls, slabs, doors, and windows. Such information may be used to determine heat transmission through surrounding materials.

```
concept {
    IfcSpace:BoundedBy -> IfcRelSpaceBoundary1stLevel_0:RelatingSpace
    IfcRelSpaceBoundary1stLevel_0:RelatedBuildingElement -> IfcElement
    IfcRelSpaceBoundary1stLevel_0:ConnectionGeometry -> IfcConnectionSurfaceGeometry
    IfcRelSpaceBoundary1stLevel_0:ParentBoundary -> IfcRelSpaceBoundary1stLevel_1
    IfcRelSpaceBoundary1stLevel_0:PhysicalOrVirtualBoundary -> IfcPhysicalOrVirtualEnum
    IfcRelSpaceBoundary1stLevel_0:InternalOrExternalBoundary -> IfcInternalOrExternalEnum
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcSurfaceOfLinearExtrusion
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcCurveBoundedPlane
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcCurveBoundedSurface
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcFaceBasedSurfaceModel
    IfcSurfaceOfLinearExtrusion:SweptCurve -> IfcArbitraryOpenProfileDef
    IfcArbitraryOpenProfileDef:Curve -> IfcIndexedPolyCurve
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean_0
    IfcCartesianPointList2D:CoordList -> IfcLengthMeasure
    IfcCurveBoundedPlane:BasisSurface -> IfcPlane
    IfcPlane:Position -> IfcAxis2Placement3D_0
    IfcCurveBoundedSurface:BasisSurface -> IfcCylindricalSurface
    IfcCurveBoundedSurface:Boundaries -> IfcOuterBoundaryCurve
    IfcCurveBoundedSurface:ImplicitOuter -> IfcBoolean_1
    IfcCylindricalSurface:Position -> IfcAxis2Placement3D_1
    IfcOuterBoundaryCurve:Segments -> IfcCompositeCurveSegment
    IfcFaceBasedSurfaceModel:FbsmFaces -> IfcOpenShell
    IfcOpenShell:CfsFaces -> IfcFace
    IfcFace:Bounds -> IfcFaceOuterBound
}
```
