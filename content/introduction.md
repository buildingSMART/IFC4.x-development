!template

The Industry Foundation Classes (IFC) are an open international standard for sharing data of the built asset industry. The standard comprises:

 1. A schema (provided in various forms, see [scope](scope.htm))
{%- if is_iso %}
 2. Documentation (provided in HTML)
{%- else %}
 2. Documentation (provided in HTML, authored in Markdown)
{%- endif %}
 3. Property and Quantity Set definitions (standardized definitions for an extensibility mechanism realised in the schema - provided in XML and available in the HTML documentation)
 4. Exchange or serialization mechanisms of data files, see [scope](scope.htm)

The prevalent exchange format for IFC is the Step Physical File Format (ISO
10303-21:2002) based on the schema publication using the EXPRESS language (ISO 10303-11:2004). It is a clear-text encoding of the entity instances that
make up the exchange, in which attribute values are provided as an ordered
sequence of unnamed values. 

## Conventions

The IFC specification includes terms, concepts and data specification items that originate from use within disciplines, trades, and professions of the construction and facility management industry sector. Terms and concepts use the plain English words, the data items within the data specification follow a naming convention.

* the data item names for types, entities, rules and functions start with the prefix "Ifc" and continue with the English words in CamelCase naming convention (no underscore, first letter in word in upper case);
* the attribute names within an entity follow the CamelCase naming convention with no prefix;
* the property set definitions that are part of this standard start with the prefix "Pset_" and continue with the English words in CamelCase naming convention;
* the quantity set definitions that are part of this standard start with the prefix "Qto_" and continue with the English words in CamelCase naming convention.

Entity inheritance diaphrams use the following color coding:

* Light gray box - abstract entities ![](abstract_entity.png)
* Dark gray box - instantiatable entities ![](instantiable_entity.png)
* Blue box - entity document on the selected page ![](current_entity.png)
* Red box - depreciated entities ![](depreciated_entity.png)

Hierarchical entity class relationships are indicated with an upwards blue arrow (![](entity_hierarchy.png)).

{% if not is_iso %}
buildingSMART International publishes translations of those terms and concepts into other human languages on [translations.buildingsmart.org](https://translations.buildingsmart.org).
{% endif %}

## Model View Definitions

Official model view definitions (MVDs) exist as related specifications. The official MVD policy for IFC 4.3 currently holds 3 levels of implementation for IFC:

- Reference View
- Alignment Based View
- Design Transfer View

These three MVDs can be seen as three levels of implementation for IFC 4.3. They are gradual levels adding more advanced features to the implementations. Vendors can get certified for IFC import against these MVDs. Export certification can be done against the MVDs, but also against more granular functional parts. These can be found on  [validate.buildingsmart.org](https://validate.buildingsmart.org).
{%- if not is_iso %}
The IFC documentation is deposited at [standards.buildingsmart.org](https://standards.buildingsmart.org).

| **MVD abbreviation** | RV                                                                                                  | AbV                                                                                                                                                          |
|----------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**             | Reference View                                                                                      | Alignment-based View                                                                                                                                         |
| **Purpose**          | Suitable for data exchanges based on reference models, where the exchange is mainly one-directional | Suitable for data exchanges based on alignment, linear placement relative to it, and other concepts associated to civil, infrastructure and geospatial works |
| **Use**              | Intended as a reference and not a full exchange of the design intent.                               | Can be used as a reference, but its added value is the exchange of some parametric constructs (e.g., alignment, advanced solid geometry)                     |
| **Scope**            | Strict superset of IFC4 Reference View. Usually small in scope and easier to implement.             | Strict superset of the IFC4.3 Reference View, hence larger in scope.                                                                                         |


{% endif %}

## Architecture
  
The data schema architecture of IFC defines four conceptual layers, each individual schema is assigned to exactly one conceptual layer. The figure below shows the schema architecture of the IFC layered architecture.

![Figure 1 — Data schema architecture with conceptual layers](https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/content/IFC4_layered_architecture.png)

1. **Resource layer** — the lowest layer includes all individual schemas containing resource definitions, those definitions do not include a globally unique identifier and shall not be used independently of a definition declared at a higher layer;
2. **Core layer** — the next layer includes the kernel schema and the core extension schemas, containing the most general entity definitions, all entities defined at the core layer, or above carry a globally unique id and optionally owner and history information;
3. **Interoperability layer** — the next layer includes schemas containing entity definitions that are specific to a general product, process or resource specialization used across several disciplines, those definitions are typically utilized for inter-domain exchange and sharing of construction information;
4. **Domain layer** — the highest layer includes schemas containing entity definitions that are specializations of products, processes or resources specific to a certain discipline, those definitions are typically utilized for intra-domain exchange and sharing of information.
In this picture the 'tunnel' domain is transparent since this is not part of the current IFC 4.3 yet, but is aimed to be included in a future update.

## Compatibility

Built assets have a long lifetime. Compatibility between IFC releases is a key concern in the development of the standard. 

*Backward compatibility* is the ability for a data file, written against a previous release of the standard, to be readable by an application supporting a later version.

The classes in the ISO 10303-11 EXPRESS schema distribution of this international standard are typically reflected in program code and directly influence the structure (attribute counts, attribute types) of exchanges using the ISO 10303-21 exchange format.

Conversely, Property and Quantity Sets are generally more supplementary data that don't
affect functioning of the software interfaces to the same extent. Property and Quantity
Sets are also explicitly provided to rapidly address specific use cases and
evolving software capabilities. Changes in Property and Quantity Sets do
not affect the structure (attribute counts, attribute types) of the ISO 10303-21 exchange formats.

As such, compatibility of Property and Quantity Sets is not held to the same
standard as is the case for compatibility of the EXPRESS schema.

Except in rare cases, backward compatibility is a hard requirement in the
evolution of the IFC standard. Nevertheless, there is a varying degree of
severity in the types of changes that could occur. For example, renaming an
entity name, or inserting an attribute at the beginning of the attribute
sequence causes a near irrecoverable error in parsing a file written against
a previous release of the
standard. Whereas adding an enumeration item to an existing enumeration is
deemed fully backwards compatible.

> NOTE Forward compatibility is not explicitly considered in the development of this release, but seen as a desirable feature where possible.

### Deprecation

As the IFC standard evolves certain constructs become unfavourable, since they
have been superseded by other constructs, because implementation in software proved inadequate or because
flaws were found in the definition that were impossible to correct in a
backwards compatible fashion.

In such cases the choice is often made to *deprecate* the construct, giving
implementers ample time to adapt their software.

> NOTE 1 Complying interpreters shall still be able to import deprecated definitions.

> NOTE 2 Complying interpreters shall consider modifying the export using the proposed alternative definitions instead of the deprecated ones.

### List of known backward incompatibilities of this document with ISO 16739-1:2018

> NOTE For a full list of changes see the Change logs in Appendix F.

The following entities, types and functions have been deleted in this release:

* IfcBeamStandardCase
* IfcBuildingElement
* IfcBuildingElementType
* IfcColumnStandardCase
* IfcCorrectObjectAssignment
* IfcDoorStandardCase
* IfcDoorStyle
* IfcDoorStyleConstructionEnum
* IfcDoorStyleOperationEnum
* IfcMemberStandardCase
* IfcNullStyle
* IfcObjectTypeEnum
* IfcOpeningStandardCase
* IfcPlateStandardCase
* IfcPresentationStyleAssignment
* IfcPresentationStyleSelect
* IfcProxy
* IfcSlabElementedCase
* IfcSlabStandardCase
* IfcStyleAssignmentSelect
* IfcWallElementedCase
* IfcWindowStandardCase
* IfcWindowStyle
* IfcWindowStyleConstructionEnum
* IfcWindowStyleOperationEnum

The following entities, attributes and enumerators have been deprecated in this release:

* IfcBuildingSystem
* IfcCivilElement
* IfcCivilElementType
* IfcElectricDistributionBoard
* IfcElectricDistributionBoardType
* IfcFaceBasedSurfaceModel
* IfcPostalAddress
* IfcRelConnectsPortToElement
* IfcRelServicesBuildings
* IfcTelecomAddress
* IfcTrapeziumProfileDef
* IfcBuilding.BuildingAddress
* IfcBuilding.ElevationOfRefHeight
* IfcBuilding.ElevationOfTerrain
* IfcBuildingStorey.Elevation
* IfcOrganization.Addresses
* IfcPerson.Addresses
* IfcSite.LandTitleNumber
* IfcSite.SiteAddress
* IfcSurfaceStyleRendering.DiffuseTransmissionColour
* IfcSurfaceStyleRendering.ReflectionColour
* IfcSurfaceStyleRendering.TransmissionColour
* IfcSurfaceTexture.Parameter
* IfcTextureCoordinateGenerator.Parameter
* IfcCableCarrierFittingTypeEnum.CROSS
* IfcCableCarrierFittingTypeEnum.REDUCER
* IfcCableCarrierFittingTypeEnum.TEE
* IfcFireSuppressionTerminalTypeEnum.SPRINKLERDEFLECTOR
* IfcGeographicElementTypeEnum.SOIL_BORING_POINT

The following backward incompatibilities have been introduced in this release:

|  | Severity | Element | Incompatibility |
|---|---|---|---|
| 1 | Major | IfcGridPlacement | Result of PlacementRelTo attribute moving up to IfcObjectPlacement. |
| 2 | Minor | IfcCountMeasure | Definition changed from NUMBER to INTEGER. |
