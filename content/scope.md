!template

The IFC 'Industry Foundation Classes for data sharing in the construction and facility management industries' is an open international standard for Building Information Model (BIM) data that are exchanged and shared among software applications used by the various participants in the construction or facility management industry sector. The standard includes definitions that cover data required for buildings and infrastructure works over their life cycle.
The coverage of infrastructure facilities now incorporated into IFC includes bridges, roads, railways, waterways and port facilities.

The IFC comprises the publication of a data schema, its documentation, the property and quantity set definitions and the mechanism of an exchange file format structure.
The schema, property and quantity sets and usage constraints are internally authored as a UML Class diagram
{%- if not is_iso %}
[available as XMI file](https://github.com/{{ target_repo }}/tree/{{ branch }}/schemas)
{%- endif %}
{% if is_iso -%}
and published as the following computer interpretable schemas:
{%- else -%}
and published as [computer interpretable schemas](https://github.com/buildingSMART/IFC4.3.x-output), including:
{%- endif %}

* In [EXPRESS data specification language](../annex-a-express.html), according to ISO 10303-11,
* In [XML Schema definition language (XSD)](../annex-a-xsd.html), according to ISO 10303-28
{% if not is_iso -%}
* As RDF/OWL Schema (under development),
* As JavaScript Object Notation Schema (under development),
* As a JSON structured [taxonomy](https://github.com/buildingSMART/IFC4.3.x-output/blob/master/IFC.json) of entities, predefined types and properties.
{% endif %}

> NOTE See Annex A ‘Computer interpretable listings’ for the publication of schemas.

The exchange file formats for exchanging and sharing data according to the computer interpretable schemas are:

* Clear text encoding of the exchange structure, defined in ISO 10303-21,
* Extensible Markup Language (XML), defined in XML Schema W3C Recommendation with IFC specific translations,
{% if not is_iso -%}
* RDF/OWL, defined by W3C and the buildingSMART projects,
* JSON JavaScript Object Notation, defined by the buildingSMART projects.
{% endif %}

{% if not is_iso %}
An overview of the file formats can be seen on [the technical website](https://technical.buildingsmart.org/standards/ifc/ifc-formats/). Alternative exchange file formats may be used if they conform to the data schemas.
{% endif %}

The full IFC standard is used to define one or many recognized workflows in the construction and facility management industry sector. Such an exchange scenario definition of the IFC data schema and referenced data is referred to as a Model View Definition (MVD). Each MVD identifies data exchange requirements for developing software applications. Conforming software applications need to identify the model view definition they conform to when applying for Software Certification.

## General use

The following are within the scope of this release of IFC:

 1. BIM exchange format definitions that are required during the life cycle phases of buildings and infrastructure:

    * demonstrating the need;
    * conception of need;
    * outline feasibility;
    * substantive feasibility study and outline financial authority;
    * outline conceptual design;
    * full conceptual design;
    * coordinated design;
    * procurement and full financial authority;
    * production information;
    * construction;
    * operation and maintenance.

 2. BIM exchange format definitions that are required by the various disciplines involved within the life cycle phases:

    * architecture and civil engineering design;
    * service and utilities engineering;
    * structural engineering;
    * procurement;
    * construction planning;
    * facility and utility management;
    * project management;
    * client requirement management;
    * industry authorities for permits and approval.

 3. BIM exchange format definitions including:

    * project structure;
    * physical components;
    * spatial components;
    * analysis items;
    * processes;
    * resources;
    * controls;
    * actors;
    * context definition.
