# IfcConstructionProductResource

_IfcConstructionProductResource_ defines the role of a product that is consumed (wholly or partially), or occupied in the performance of construction.
<!-- end of short definition -->

> HISTORY New entity in IFC2.0. Renamed from IfcProductResource in IFC2x.

Occurrences of _IfcConstructionProductResource_ are usage of products to assist the process of construction. More specifically, they are usage of products that result from some construction processes and that are then used as resources to facilitate further construction. For instance, formworks can be instantiated as products resulting from the process ‘constructing formwork’. However, they are used as resources in the process ‘pouring concrete’ in a later stage of the project.

## Attributes

### PredefinedType
Defines types of construction product resources.
> IFC4 New attribute.

## Formal Propositions

### CorrectPredefinedType

## Concepts

### Object Typing



### Resource Assignment



#### IfcElement

Indicates a physical element manifesting the resource such as nails (in bulk).

### Resource Cost



#### Product_IfcCostValue_IfcMonetaryMeasure

The unit cost for purchasing the product.

#### Shipping_IfcCostValue_IfcMonetaryMeasure

The unit cost for transporting the product.

### Resource Quantity



#### Product_IfcQuantityCount

The unit count of the product used such as 1 for each or 12 for a dozen.

