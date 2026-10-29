# IfcTransportElement

A transport element is a generalization of all transport related objects that move people, animals or goods within a Facility. The _IfcTransportElement_ defines the occurrence of a transport element, that (if given), is expressed by the _IfcTransportElementType_.
<!-- end of short definition -->

> EXAMPLE Transportation elements include elevator (lift), escalator, moving walkway, etc.

> NOTE More detailed equipment that may be a part of a transportation device, like a lifting hook, is defined as _IfcDiscreteAccessory_. It maybe included as a part of the _IfcTransportElement_ by virtue of the objectified relationship _IfcRelAggregates_.

Transport element can describe fixed or non fixed elements, which can either be identified as specified operational assets within a facility or vehicles that interact with the facility as a user or customer.
In the case of operational assets, instances of _IfcTransportElement_ can represent individual identifiable vehicles or structures with properties such as serial numbers, registration numbers etc. and be typed accordingly by instances of _IfcTransportElementType_.

In the case of transport elements that interact as users or customers, such as cars on a road or vessels at a port, _IfcTransportElementType_ is used to define element specifications which are used to design, analyse and provide operational constraints to the facility.

Depending on local classification systems transport elements and transportation systems in buildings are either considered as part of a built system, or as part of a built service system. Within IFC they are considered as part of a built system and may have to be mapped appropriately.

> HISTORY New entity in IFC2x.

> IFC2x CHANGE The attribute _PredefinedType_ (previously OperationType) is made optional.

> IFC4 CHANGE The last attributes CapacityByWeight and CapacityByNumber are removed, use Pset_TransportElementCommon instead.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _IfcTransportElement_ attribute is unset (e.g. because an _IfcTransportElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no transport element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcTransportElementType_.

## Concepts

### Object Typing

IfcTransportElement defines the occurrence of any transportation device, common information about transportation device types (or styles) is handled by IfcTransportElementType. The IfcTransportElementType (if present) may establish the common type name, usage (or predefined) type, common material layer set, common set of properties and common shape representations (using IfcRepresentationMap). The IfcTransportElementType is attached using the _IfcRelDefinesByType.RelatingType_ objectified relationship and is accessible by the inverse _<font color="#0000FF">IsTypedBy</font>_ attribute.

If no IfcTransportElementType is attached (i.e. if only occurrence information is given) the PredefinedType should be provided. If set to .USERDEFINED. a user defined value can be provided by the ObjectType attribute.

### Property Sets for Objects



### Spatial Containment

* The IfcTransportElement is placed within the project spatial hierarchy using the objectified relationship IfcRelContainedInSpatialStructure, referring to it by its inverse attribute _SELF\IfcElement.ContainedInStructure_. Subtypes of IfcSpatialStructureElement are valid spatial containers, with IfcBuilding being the default container.

