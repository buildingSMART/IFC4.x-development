# IfcConstructionEquipmentResource

_IfcConstructionEquipmentResource_ is usage of construction equipment to assist in the performance of construction. Construction Equipment resources are wholly or partially consumed or occupied in the performance of construction.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0.

Occurrences of _IfcConstructionEquipmentResource_ are products that are used as resources to assist the process of construction. More specifically, they are products that are standalone items brought to a project to fulfil a particular purpose. Examples might be a tower crane or other mobile crane, a screwing machine, or a lifting hoist.

Instances of any subtype of _IfcProduct_ may be assigned to the equipment resource using _IfcRelAssignsToResource_ in order to characterize the equipment further, as described at the supertype _IfcResource_. Examples of relevant subtypes of _IfcProduct_ are _IfcDiscreteAccessory_ or _IfcBuiltElement_ (for particular cases where more precise usage details are not available).

## Attributes

### PredefinedType
Defines types of construction equipment resources.
> IFC4 New attribute.

## Formal Propositions

### CorrectPredefinedType

## Concepts

### Object Typing



### Quantity Sets



### Resource Assignment



#### IfcTransportElement

Indicates a physical element manifesting the resource such as a crane.

### Resource Cost



#### Usage_IfcCostValue_IfcMonetaryMeasure

The amount incurred for acquiring the equipment, such as rental fees or depreciation.

#### Operation_IfcCostValue_IfcMonetaryMeasure

The amount incurred for operating the equipment, such as fuel and maintenance.

#### Deployment_IfcCostValue_IfcMonetaryMeasure

The amount incurred for mobilizing and decommissioning the equipment.

### Resource Quantity



#### Operation_IfcQuantityTime

The unit basis for operating the equipment, such as an hour.

