from enum import Enum, auto

class concept_type(Enum):
    # Packaged class, with normal undirected associations
    SIMPLE_UNARY = auto()
    # Packaged undirected association class
    PROPERTY_OR_QUANTITY_SET = auto()
    # Packaged undirected association class
    OBJECT_TYPING = auto()
    # Packaged directed association class
    DIRECTIONAL_BINARY = auto()
    # Packaged intermediate class with normal undirected associations
    DIRECTIONAL_GROUPED = auto()
    # N-ary packaged association class
    # currently, only approach with concept-introduced string labels
    NARY = auto()
    # Because incomplete or contradictory
    NO_PARAMETRIZATION = auto()

concepts = {
('Property Sets for Objects', ('LowerValue', ('IfcPropertyBoundedValue', 'LowerBoundValue')), ('PredefinedType', ('IfcObject', 'PredefinedType')), ('Properties', ('IfcPropertySet', 'HasProperties')), ('PropertyName', ('IfcPropertyListValue', 'Name')), ('PsetName', ('IfcPropertySet', 'Name')), ('Reference', ('IfcPropertyEnumeration', 'Name')), ('SetValue', ('IfcPropertyBoundedValue', 'SetPointValue')), ('UpperValue', ('IfcPropertyBoundedValue', 'UpperBoundValue')), ('Value', ('IfcPropertyListValue', 'ListValues'))):
concept_type.PROPERTY_OR_QUANTITY_SET,
('Property Sets for Contexts', ):
concept_type.DIRECTIONAL_BINARY,
('Property Sets for Performance', ('PredefinedType', ('IfcObject', 'PredefinedType'))):
concept_type.PROPERTY_OR_QUANTITY_SET,
('Property Sets for Materials',):
concept_type.PROPERTY_OR_QUANTITY_SET,
('Property Sets for Profiles',):
concept_type.PROPERTY_OR_QUANTITY_SET,
('Object Nesting', ('Type', ('IfcRelNests', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Actor Assignment', ('Type', ('IfcRelAssignsToActor', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Object Typing', ('HasType', ('IfcObject', 'IsTypedBy')), ('RelatingType', ('IfcRelDefinesByType', 'RelatingType')), ('TypeName', ('IfcTypeObject', 'Name'))):
concept_type.OBJECT_TYPING,
('Quantity Sets', ('AreaValue', ('IfcQuantityArea', 'AreaValue')), ('CountValue', ('IfcQuantityCount', 'CountValue')), ('LengthValue', ('IfcQuantityLength', 'LengthValue')), ('QsetName', ('IfcElementQuantity', 'Name')), ('Quantities', ('IfcElementQuantity', 'Quantities')), ('QuantityName', ('IfcQuantityTime', 'Name')), ('TimeValue', ('IfcQuantityTime', 'TimeValue')), ('VolumeValue', ('IfcQuantityVolume', 'VolumeValue')), ('WeightValue', ('IfcQuantityWeight', 'WeightValue'))):
concept_type.PROPERTY_OR_QUANTITY_SET,
('Material Constituent Set', ('ConstituentName', ('IfcMaterialConstituent', 'Name'))):
concept_type.SIMPLE_UNARY,
('Material Set',):
concept_type.NARY,
('Port Nesting', ('Flow', ('IfcDistributionPort', 'FlowDirection')), ('PortName', ('IfcDistributionPort', 'Name')), ('PredefinedType', ('IfcDistributionElement', 'PredefinedType')), ('SystemType', ('IfcDistributionPort', 'SystemType'))):
concept_type.NARY,
('Control Flow', ('Type', ('IfcRelFlowControlElements', 'RelatingFlowElement'))):
concept_type.DIRECTIONAL_BINARY,
('Alignment Layout',):
concept_type.SIMPLE_UNARY,
('Alignment Geometry Gradient', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Alignment Geometry Cant', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Alignment Cant Attributes',):
concept_type.SIMPLE_UNARY,
('Alignment Horizontal Attributes',):
concept_type.SIMPLE_UNARY,
('Alignment Vertical Attributes',):
concept_type.SIMPLE_UNARY,
('Annotation 2D Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Annotation 3D Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Group Assignment', ('IsGrouped', ('IfcGroup', 'IsGroupedBy')), ('RelatedObjects', ('IfcRelAssignsToGroup', 'RelatedObjects'))):
concept_type.SIMPLE_UNARY,
('Spatial Containment', ('RelatingStructure', ('IfcRelContainedInSpatialStructure', 'RelatingStructure')), ('SpatialElementName', ('IfcSpatialElement', 'Name'))):
concept_type.DIRECTIONAL_BINARY,
('Element Composition', ('Decomposes', ('IfcElement', 'Decomposes')), ('ElementName', ('IfcElement', 'Name')), ('RelatingObject', ('IfcRelAggregates', 'RelatingObject'))):
concept_type.SIMPLE_UNARY,
('Axis 3D Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Product Assignment', ('Type', ('IfcRelAssignsToProduct', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Spatial Composition', ('ProjectName', ('IfcProject', 'Name')), ('RelatingObject', ('IfcRelAggregates', 'RelatingObject')), ('SpatialElementName', ('IfcSpatialElement', 'Name'))):
concept_type.DIRECTIONAL_BINARY,
('Spatial Decomposition', ('RelatedObjects', ('IfcRelAggregates', 'RelatedObjects')), ('SpatialElementName', ('IfcSpatialElement', 'Name'))):
concept_type.DIRECTIONAL_BINARY,
('Spatial Container', ('Type', ('IfcRelContainedInSpatialStructure', 'RelatedElements'))):
concept_type.DIRECTIONAL_BINARY,
('Material Profile Set Usage', ('Name', ('IfcMaterialProfile', 'Name'))):
concept_type.SIMPLE_UNARY,
('Material Layer Set Usage', ('Name', ('IfcMaterialLayer', 'Name'))):
concept_type.SIMPLE_UNARY,
('Object Connectivity',):
concept_type.SIMPLE_UNARY,
('Resource Assignment', ('Type', ('IfcRelAssignsToResource', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Resource Cost', ('CostName', ('IfcAppliedValue', 'Name')), ('CostType', ('IfcConstructionResource', 'BaseCosts')), ('ValueType', ('IfcAppliedValue', 'AppliedValue'))):
concept_type.NARY,
('Resource Quantity', ('QuantityName', ('IfcPhysicalSimpleQuantity', 'Name')), ('QuantityType', ('IfcConstructionResource', 'BaseQuantity'))):
concept_type.NARY,
('Resource Type Assignment', ('Type', ('IfcRelAssignsToResource', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Control Assignment', ('Type', ('IfcRelAssignsToControl', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Product Type Assignment', ('Type', ('IfcRelAssignsToProduct', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Axis Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Clearance Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Type Axis Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Type Clearance Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Type Lighting Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Door Type Attributes',):
concept_type.SIMPLE_UNARY,
('FootPrint Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Element Openings', ('FillsVoids', ('IfcOpeningElement', 'FillsVoids')), ('HasOpenings', ('IfcElement', 'HasOpenings')), ('OpeningElementType', ('IfcOpeningElement', 'PredefinedType')), ('RelatedBuiltElement', ('IfcRelFillsElement', 'RelatedBuildingElement')), ('RelatedOpeningElement', ('IfcRelVoidsElement', 'RelatedOpeningElement'))):
concept_type.DIRECTIONAL_BINARY,
('Product Linear Placement', ('HasPlacement', ('IfcProduct', 'ObjectPlacement')), ('LinearPositioningElementName', ('IfcLinearPositioningElement', 'Name')), ('RelativePlacement', ('IfcLinearPlacement', 'RelativePlacement')), ('RelativeToElement', ('IfcLocalPlacement', 'PlacesObject'))):
concept_type.SIMPLE_UNARY,
('Element Voiding Features', ('HasOpenings', ('IfcElement', 'HasOpenings')), ('RelatedVoidingFeature', ('IfcRelVoidsElement', 'RelatedOpeningElement')), ('VoidingFeatureType', ('IfcVoidingFeature', 'PredefinedType'))):
concept_type.SIMPLE_UNARY,
('Surface Feature Adherence', ('HasSurfaceFeatures', ('IfcElement', 'HasSurfaceFeatures')), ('RelatedSurfaceFeatures', ('IfcRelAdheresToElement', 'RelatedSurfaceFeatures')), ('SurfaceFeatureName', ('IfcSurfaceFeature', 'Name'))):
concept_type.SIMPLE_UNARY,
('Body AdvancedSwept Directrix Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body AdvancedSwept DiskSolid PolyCurve Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body AdvancedSwept Tapered Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body SectionedSolidHorizontal', ('CrossSections', ('IfcSectionedSolidHorizontal', 'CrossSections')), ('Directrix', ('IfcSectionedSolidHorizontal', 'Directrix')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body SweptSolid Composite Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body SweptSolid ParameterizedProfile Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body SweptSolid CompositeCurve Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Body SweptSolid PolyCurve Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('FootPrint Annotation Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('FootPrint GeomSet PolyCurve Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Surface Sectioned Geometry', ('CrossSections', ('IfcSectionedSurface', 'CrossSections')), ('Directrix', ('IfcSectionedSurface', 'Directrix')), ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Surface Tessellation Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Product Grid Placement',):
concept_type.SIMPLE_UNARY,
('Type Body Tessellated Geometry', ('Geometry', ('IfcShapeRepresentation', 'Items'))):
concept_type.SIMPLE_UNARY,
('Body Tessellation Geometry',):
concept_type.SIMPLE_UNARY,
('Element Type Predefined Type',):
concept_type.SIMPLE_UNARY,
('Earthworks Cuttings', ('EarthworksCutType', ('IfcEarthworksCut', 'PredefinedType')), ('FillsVoids', ('IfcEarthworksCut', 'FillsVoids')), ('HasOpenings', ('IfcElement', 'HasOpenings')), ('RelatedBuiltElement', ('IfcRelFillsElement', 'RelatedBuildingElement')), ('RelatedEarthworksCut', ('IfcRelVoidsElement', 'RelatedOpeningElement'))):
concept_type.SIMPLE_UNARY,
('Grid Attributes', ('UAxes', ('IfcGrid', 'UAxes')), ('VAxes', ('IfcGrid', 'VAxes')), ('WAxes', ('IfcGrid', 'WAxes'))):
concept_type.SIMPLE_UNARY,
('Element Connectivity',):
concept_type.SIMPLE_UNARY,
('Element Filling', ('Type', ('IfcRelVoidsElement', 'RelatingElement'))):
concept_type.DIRECTIONAL_BINARY,
('Mechanical Fastener Attributes',):
concept_type.SIMPLE_UNARY,
('Mechanical Fastener Type Attributes',):
concept_type.SIMPLE_UNARY,
('Product Relative Positioning', ('PositioningElement', ('IfcRelPositions', 'RelatingPositioningElement'))):
concept_type.SIMPLE_UNARY,
('Product Span Positioning', ('EndPositionName', ('IfcRelPositions', 'Name')), ('EndPositionType', ('IfcReferent', 'PredefinedType')), ('EndPositionedRelativeTo', ('IfcProduct', 'PositionedRelativeTo')), ('StartPositionName', ('IfcRelPositions', 'Name')), ('StartPositionType', ('IfcReferent', 'PredefinedType')), ('StartPositionedRelativeTo', ('IfcProduct', 'PositionedRelativeTo'))):
concept_type.SIMPLE_UNARY,
('Product Geometry Colour',):
concept_type.SIMPLE_UNARY,
('Product Geometry Layer',):
concept_type.SIMPLE_UNARY,
('Project Units', ('ConversionUnitName', ('IfcConversionBasedUnit', 'Name')), ('ConversionUnitType', ('IfcConversionBasedUnit', 'UnitType')), ('DerivedUnitType', ('IfcDerivedUnit', 'UnitType')), ('HasUnits', ('IfcContext', 'UnitsInContext')), ('SIUnitName', ('IfcSIUnit', 'Name')), ('SIUnitType', ('IfcSIUnit', 'UnitType'))):
concept_type.SIMPLE_UNARY,
('Project Representation Context', ('ContextIdentifier', ('IfcGeometricRepresentationContext', 'ContextIdentifier')), ('ContextType', ('IfcGeometricRepresentationContext', 'ContextType')), ('SubContextIdentifier', ('IfcGeometricRepresentationSubContext', 'ContextIdentifier')), ('SubContextType', ('IfcGeometricRepresentationSubContext', 'ContextType'))):
concept_type.NARY,
('Project Declaration', ('Type', ('IfcRelDeclares', 'RelatedDefinitions'))):
concept_type.DIRECTIONAL_BINARY,
('Project Representation Context 2D', ('ContextIdentifier', ('IfcGeometricRepresentationContext', 'ContextIdentifier')), ('ContextType', ('IfcGeometricRepresentationContext', 'ContextType')), ('SubContextIdentifier', ('IfcGeometricRepresentationSubContext', 'ContextIdentifier')), ('SubContextType', ('IfcGeometricRepresentationSubContext', 'ContextType'))):
concept_type.SIMPLE_UNARY,
('Element Decomposition', ('IsDecomposedBy', ('IfcElement', 'IsDecomposedBy')), ('PartName', ('IfcElement', 'Name')), ('RelatedObjects', ('IfcRelAggregates', 'RelatedObjects'))):
concept_type.DIRECTIONAL_BINARY,
('Reinforcing Bar Type Attributes',):
concept_type.SIMPLE_UNARY,
('Reinforcing Mesh Attributes',):
concept_type.SIMPLE_UNARY,
('Reinforcing Mesh Type Attributes',):
concept_type.SIMPLE_UNARY,
('Survey Points Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Topography Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('FootPrint GeomSet Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Group Spatial Connectivity', ('GroupName', ('IfcGroup', 'Name')), ('ReferenceContext', ('IfcRelReferencedInSpatialStructure', 'Name')), ('ReferencedInStructures', ('IfcSpatialElement', 'ReferencedInStructures')), ('RelatedGroups', ('IfcRelReferencedInSpatialStructure', 'RelatedElements'))):
concept_type.SIMPLE_UNARY,
('Spatial Interference', ('InterferenceType', ('IfcRelInterferesElements', 'InterferenceType')), ('InterferesSpatialElements', ('IfcSpatialElement', 'InterferesElements')), ('RelatedSpatialElement', ('IfcRelInterferesElements', 'RelatedElement')), ('RelatedSpatialElementName', ('IfcSpatialElement', 'Name')), ('SpatialElementName', ('IfcSpatialElement', 'Name'))):
concept_type.SIMPLE_UNARY,
('Spatial Interference With Zones', ('InteferenceZone', ('IfcRelInterferesElements', 'InterferenceSpace')), ('InterferenceType', ('IfcRelInterferesElements', 'InterferenceType')), ('InterferesSpatialElements', ('IfcSpatialElement', 'InterferesElements')), ('RelatedSpatialElement', ('IfcRelInterferesElements', 'RelatedElement')), ('RelatedSpatialElementName', ('IfcSpatialElement', 'Name')), ('SpatialElementName', ('IfcSpatialElement', 'Name')), ('SpatialZoneType', ('IfcSpatialZone', 'PredefinedType'))):
concept_type.SIMPLE_UNARY,
('Spatial Element Type Predefined Type',):
concept_type.SIMPLE_UNARY,
('Spatial Zone Attributes', ('LongName', ('IfcSpatialZone', 'LongName')), ('Name', ('IfcSpatialZone', 'Name'))):
concept_type.SIMPLE_UNARY,
('Structural Activity', ('AppliedLoad', ('IfcStructuralActivity', 'AppliedLoad')), ('RelatingElement', ('IfcRelConnectsStructuralActivity', 'RelatingElement'))):
concept_type.NARY,
('Reference Topology', ('Topology', ('IfcTopologyRepresentation', 'Items'))):
concept_type.DIRECTIONAL_BINARY,
('Structural Connectivity', ('StructuralConnection', ('IfcRelConnectsStructuralMember', 'RelatedStructuralConnection'))):
concept_type.DIRECTIONAL_BINARY,
('System Element Attributes', ('LongName', ('IfcSystem', 'LongName')), ('Name', ('IfcSystem', 'Name'))):
concept_type.SIMPLE_UNARY,
('Tendon Attributes',):
concept_type.SIMPLE_UNARY,
('Tendon Type Attributes',):
concept_type.SIMPLE_UNARY,
('Path Connectivity', ('RelatedElement', ('IfcRelConnectsPathElements', 'RelatedElement'))):
concept_type.DIRECTIONAL_BINARY,
('Axis 2D Geometry', ('Identifier', ('IfcShapeRepresentation', 'RepresentationIdentifier')), ('Items', ('IfcShapeRepresentation', 'Items')), ('Type', ('IfcShapeRepresentation', 'RepresentationType'))):
concept_type.SIMPLE_UNARY,
('Window Attributes', ('OverallHeight', ('IfcWindow', 'OverallHeight')), ('OverallWidth', ('IfcWindow', 'OverallWidth')), ('PartitioningType', ('IfcWindow', 'PartitioningType')), ('TypePartitioningType', ('IfcWindowType', 'PartitioningType'))):
concept_type.SIMPLE_UNARY,
('Window Type Attributes',):
concept_type.SIMPLE_UNARY
}

def get(name):
    return {k[0].replace(" ", ""): v for k, v in concepts.items()}.get(name)