# IfcPerformanceHistory

_IfcPerformanceHistory_ is used to document the actual performance of an occurrence instance over time. It includes machine-measured data from building automation systems and human-specified data such as task and resource usage. The data may represent actual conditions, predictions, or simulations.
<!-- end of short definition -->

The realtime data tracked by performance history takes the form of property sets where all properties are based on time series. Unlike design-based data at occurrences and types, performance-driven data is time-sensitive and may change in realtime by some measurement device. Data may be captured at irregular intervals such as when values change beyond established thresholds, or at regular intervals of specified duration.

### Declaration use definition
_IfcPerformanceHistory_ may be declared within a project using _IfcRelDeclares_ where _RelatingContext_ refers to the _IfcProject_ and _RelatedDefinitions_ includes the _IfcPerformanceHistory_. Default units (used for property sets) are indicated by the declaring project. Only top-level objects are declared; nested performance history objects (through _IfcRelNests_) do not participate in such relationship.

> HISTORY New entity in IFC2x2.

## Attributes

### LifeCyclePhase
Describes the applicable building life-cycle phase. Typical values should be DESIGNDEVELOPMENT, SCHEMATICDEVELOPMENT, CONSTRUCTIONDOCUMENT, CONSTRUCTION, ASBUILT, COMMISSIONING, OPERATION, etc.

### PredefinedType
Predefined generic type for a performance history that is specified in an enumeration.
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Concepts

### Aggregation

IfcPerformanceHistory may be decomposed into components using IfcRelNests where RelatingObject refers to the enclosing IfcPerformanceHistory and RelatedObjects contains one or more IfcPerformanceHistory components. Composition indicates breakdown of further detail and may correspond to the hierarchy of objects it represents.

### Library Association

IfcPerformanceHistory may refer to external systems, such as a time series data source within a building automation system or a cost code in an accounting system for resource allocation.

### Control Assignment



#### IfcGroup

A system or zone for which time-based system information is provided, such as overall status parameters of a building control system.

#### IfcProduct

A building space, physical device, or port for which time-based information is provided, such as a chiller or an analog input within a device.

#### IfcProcess

A process for which time-based information is provided, such as an alarm event being raised and acknowledged, or regular and overtime costs incurred for a task.

#### IfcResource

A resource for which usage is recorded or planned over time, such as wage rates and number of workers at particular times.

### Property Sets for Performance

The property sets relating to this entity are defined by IfcPropertySet and attached by the IfcRelDefinesByProperties relationship. They are accessible by the IsDefinedBy inverse attribute. Applicable property sets are defined at assigned entities (primarily IfcDistributionElement subtypes) where _IfcPropertySetTemplate.PropertySetType_ is PSET_PERFORMANCEDRIVEN.

In addition to standard property sets defined within this specification, if the underlying information source provides metadata (specific type information), then custom property sets may capture such data, where corresponding IfcPropertySetTemplate and IfcPropertyTemplate objects may be defined for such information to be accessed by other applications.

