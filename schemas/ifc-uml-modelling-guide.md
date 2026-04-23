# IFC - UML Modelling Guide

This document explains how every concept in the IFC 4.3 standard is represented
in the modular `.uml` files found in `IFC4.x-development/schemas/`. It is intended
for developers parsing or reading the UML files directly.

The UML files use XMI 2.0 serialization (`xmi:version="20131001"`) with the
Eclipse UML2 5.0 profile. The aim is not a strict UML-to-EXPRESS mapping — the
goal is to use UML tooling for schema maintenance in a way that is familiar to
EXPRESS-minded people. As such, the style sometimes resembles EXPRESS-G in a
UML container.

---

## File structure

One `.uml` file per IFC subschema, named after the subschema:

```
schemas/
  ifc4x3_add2.uml           — top-level aggregate (imports all subschemas)
  propertytypes.uml         — PEnum definitions shared across subschemas
  IfcKernel.uml             — core layer
  IfcGeometryResource.uml   — resource layer
  IfcSharedBldgElements.uml — interoperability layer
  IfcArchitectureDomain.uml — domain layer
  ...
```

Each file contains a `uml:Model` root with a single `uml:Package` named after
the subschema. All schema content is nested inside that package as
`packagedElement` children.

---

## Entities

Entities are `packagedElement` elements with `xmi:type="uml:Class"`.

```xml
<packagedElement xmi:type="uml:Class" xmi:id="cl_IfcWall" name="IfcWall">
  ...
</packagedElement>
```

**Abstract entities** have `isAbstract="true"`:

```xml
<packagedElement xmi:type="uml:Class" xmi:id="cl_IfcProduct" name="IfcProduct"
                 isAbstract="true">
```

**Supertype (inheritance)** is encoded as a `generalization` child element:

```xml
<generalization xmi:type="uml:Generalization" xmi:id="gen_123"
                general="cl_IfcBuiltElement"/>
```

The `general` attribute references the parent entity by its local `xmi:id`.
For cross-file references, an `href` is used:

```xml
<generalization xmi:type="uml:Generalization" xmi:id="gen_456">
  <general xmi:type="uml:Class"
           href="IfcProductExtension.uml#cl_IfcSpatialElement"/>
</generalization>
```

---

## Attributes

Attributes are `ownedAttribute` children of an entity class.

```xml
<ownedAttribute xmi:type="uml:Property" xmi:id="at_IfcWall_PredefinedType"
                name="PredefinedType" isOrdered="false">
  <type xmi:type="uml:Enumeration"
        href="IfcSharedBldgElements.uml#en_IfcWallTypeEnum"/>
  <lowerValue xmi:type="uml:LiteralInteger" xmi:id="lower_1" value="0"/>
  <upperValue xmi:type="uml:LiteralUnlimitedNatural" xmi:id="upper_1" value="1"/>
</ownedAttribute>
```

### Optionality

- `lowerValue value="0"` — OPTIONAL attribute
- `lowerValue value="1"` — mandatory attribute

### Aggregates

EXPRESS aggregates (LIST, SET, BAG, ARRAY) are encoded in the attribute **name**
rather than UML multiplicities, to preserve EXPRESS semantics precisely.
The name suffix encodes the aggregate type and bounds:

| Suffix pattern | EXPRESS meaning        |
|----------------|------------------------|
| `_LU[1:?]`     | `LIST [1:?] OF UNIQUE` |
| `_S[0:?]`      | `SET [0:?] OF`         |
| `_L[1:3]`      | `LIST [1:3] OF`        |
| `_A[3:3]`      | `ARRAY [3:3] OF`       |

Example: `UAxes_LU[1:?]` means `LIST [1:?] OF UNIQUE IfcGridAxis`.

Nested aggregates (e.g. `LIST [1:?] OF LIST [3:?] OF UNIQUE IfcPositiveInteger`)
are encoded verbatim in the name for the same reason.

The `lowerValue` and `upperValue` on such attributes encode only optionality
(0 = optional, 1 = mandatory), not the aggregate bounds.

### Derived attributes

Derived attributes have `isDerived="true"` and carry a `defaultValue` with
the EXPRESS derivation expression:

```xml
<ownedAttribute xmi:type="uml:Property" name="WorldCoordinateSystem"
                isDerived="true">
  <defaultValue xmi:type="uml:OpaqueExpression">
    <language>EXPRESS</language>
    <body>IfcAxis2Placement := ParentContext.WorldCoordinateSystem</body>
  </defaultValue>
</ownedAttribute>
```

### Inverse attributes

Inverse attributes are encoded as `uml:Association` elements at the package
level, not as `ownedAttribute` children of the entity. See the **Associations
and inverse attributes** section below.

### Type references

Attribute types are referenced via `href` to elements in the same or other files:

| Target type | href pattern                                   |
|-------------|------------------------------------------------|
| Entity      | `IfcGeometryResource.uml#cl_IfcPoint`          |
| Enumeration | `IfcSharedBldgElements.uml#en_IfcWallTypeEnum` |
| Data type   | `IfcMeasureResource.uml#dt_IfcLengthMeasure`   |
| Select type | `IfcGeometryResource.uml#un_IfcAxis2Placement` |

---

## WHERE rules

WHERE rules are `ownedRule` children of the entity class:

```xml
<ownedRule xmi:type="uml:Constraint" xmi:id="ct_IfcGridAxis_WR1" name="WR1">
  <specification xmi:type="uml:OpaqueExpression" xmi:id="expr_1" name="WR1">
    <language>EXPRESS_WHERE</language>
    <body>AxisCurve.Dim = 2</body>
  </specification>
</ownedRule>
```

The `body` contains the full EXPRESS WHERE rule expression, which may span
multiple lines. The rule name is in the `name` attribute of the `ownedRule`.

---

## EXPRESS functions

Functions are `packagedElement` elements with `xmi:type="uml:Constraint"`,
containing the full EXPRESS function body:

```xml
<packagedElement xmi:type="uml:Constraint" xmi:id="ct_IfcCorrectLocalPlacement"
                 name="IfcCorrectLocalPlacement">
  <specification xmi:type="uml:OpaqueExpression">
    <language>EXPRESS_FUNCTION</language>
    <body>FUNCTION IfcCorrectLocalPlacement
  (AxisPlacement : IfcAxis2Placement;
   RelPlacement  : IfcObjectPlacement) : LOGICAL;
  ...
END_FUNCTION;</body>
  </specification>
</packagedElement>
```

Functions are grouped inside their subschema's `Functions/` subfolder in the
markdown documentation, but in the UML they appear directly in the package
alongside entities.

---

## Enumerations (IfcXxxTypeEnum)

EXPRESS enumerations are `packagedElement` elements with
`xmi:type="uml:Enumeration"`. Enumeration values are `ownedLiteral` children:

```xml
<packagedElement xmi:type="uml:Enumeration" xmi:id="en_IfcWallTypeEnum"
                 name="IfcWallTypeEnum">
  <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal_1"
                name="MOVABLE"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal_2"
                name="PARTITIONING"/>
  ...
  <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal_n"
                name="USERDEFINED"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal_n1"
                name="NOTDEFINED"/>
</ownedLiteral>
</packagedElement>
```

These are the standard IFC entity type enumerations (e.g. `IfcWallTypeEnum`,
`IfcDoorTypeEnum`). They are distinct from property enumerations (`PEnum_`).
See the **Property enumerations** section below.

---

## Data types

Defined types (e.g. `IfcLengthMeasure`, `IfcLabel`) are `packagedElement`
elements with `xmi:type="uml:DataType"`. Their underlying type is encoded
as a `generalization`:

```xml
<packagedElement xmi:type="uml:DataType" xmi:id="dt_IfcLengthMeasure"
                 name="IfcLengthMeasure">
  <generalization xmi:type="uml:Generalization" xmi:id="gen_1">
    <general xmi:type="uml:DataType" href="ifc4x3_add2.uml#dt_REAL"/>
  </generalization>
</packagedElement>
```

### String length constraints

String types with length constraints (e.g. `IfcGloballyUniqueId = STRING(22) FIXED`)
encode the constraint as an OCL `ownedRule`:

```xml
<ownedRule xmi:type="uml:Constraint" xmi:id="ct_strlen" name="strlen">
  <specification xmi:type="uml:OpaqueExpression">
    <language>OCL</language>
    <body>self.size() = 22</body>
  </specification>
</ownedRule>
```

---

## Select types

SELECT types are `packagedElement` elements with `xmi:type="uml:Dependency"` at the package level, where the `client` is the select type and the `supplier` is each member type:

```xml
<packagedElement xmi:type="uml:Dependency" xmi:id="dependency_1377"
                 client="un_IfcAxis2Placement"
                 supplier="cl_IfcAxis2Placement2D"/>
<packagedElement xmi:type="uml:Dependency" xmi:id="dependency_1378"
                 client="un_IfcAxis2Placement"
                 supplier="cl_IfcAxis2Placement3D"/>
```

---

## Associations and inverse attributes

Associations between entities (including inverse attributes) are encoded as
`packagedElement` elements with `xmi:type="uml:Association"` at the package
level:

```xml
<packagedElement xmi:type="uml:Association"
                 xmi:id="as_IfcGrid_UAxes"
                 name="IfcGrid_UAxes"
                 memberEnd="end_1 end_2">
  <ownedEnd xmi:type="uml:Property" xmi:id="end_1"
            name="INV_HasGrids_S[0:?]"
            association="as_IfcGrid_UAxes"
            type="cl_IfcGrid">
    ...
  </ownedEnd>
</packagedElement>
```

### Asymmetric inverses

When an inverse is defined on a more specific type than the forward relationship
points to (common with SELECT types), the suppressed forward relationship name
is encoded in parentheses:

```xml
<ownedEnd xmi:type="uml:Property" xmi:id="end_983"
          name="(RelatingClassification)"
          association="as_IfcClassification_ClassificationForObjects">
```

The parentheses indicate this end is not serialized as a direct attribute —
it names the forward attribute associated with the inverse.

---

## Property sets

Property sets are `packagedElement` elements with `xmi:type="uml:Class"` and
a name starting with `Pset_` or `Qto_`. They are identified solely by this
naming convention — there is no stereotype or special type.

```xml
<packagedElement xmi:type="uml:Class" xmi:id="cl_Pset_WallCommon"
                 name="Pset_WallCommon">
  <ownedComment xmi:type="uml:Comment" xmi:id="comment_1">
    <body>PSET_TYPEDRIVENOVERRIDE</body>
  </ownedComment>
  ...
</packagedElement>
```

### Template type

The `ownedComment` body encodes the pset template type, which governs
applicability behaviour:

| Template type             | Meaning                                                               |
|---------------------------|-----------------------------------------------------------------------|
| `PSET_TYPEDRIVENOVERRIDE` | Applies to both type entity and occurrence; occurrence overrides type |
| `PSET_OCCURRENCEDRIVEN`   | Applies to occurrence entities only                                   |
| `PSET_PERFORMANCEDRIVEN`  | Performance-based measurement sets                                    |
| `PSET_MATERIALDRIVEN`     | Applies to materials                                                  |
| `PSET_PROFILEDRIVEN`      | Applies to profiles                                                   |

### Properties within a pset

Properties are `ownedAttribute` children of the pset class. The property
type is determined by the combination of the `type` element and multiplicity:

| Condition                                  | Property type                |
|--------------------------------------------|------------------------------|
| `uml:Enumeration` type reference           | `IfcPropertyEnumeratedValue` |
| `uml:DataType` href, lower=0, upper=1      | `IfcPropertySingleValue`     |
| `uml:DataType` href, lower=0, upper=*      | `IfcPropertyListValue`       |
| `uml:DataType` href with `BOUNDED` comment | `IfcPropertyBoundedValue`    |
| `uml:Class` type reference                 | `IfcPropertyReferenceValue`  |

The data type name is extracted from the `href` fragment after the `#` and
prefix (e.g. `IfcMeasureResource.uml#dt_IfcLengthMeasure` → `IfcLengthMeasure`).

### Pset-to-entity applicability

Applicability is encoded as `uml:Dependency` elements at the package level:

```xml
<packagedElement xmi:type="uml:Dependency" xmi:id="dependency_1"
                 client="cl_Pset_WallCommon"
                 supplier="cl_IfcWall"/>
```

- `client` references the pset by its local `xmi:id`
- `supplier` references the entity — either by local `xmi:id` or by `href`
  for cross-file references

### Predefined type applicability

When a pset applies only to a specific predefined type value, predefined type
values are represented in two ways in the UML:

1. As `ownedLiteral` elements within the `uml:Enumeration` (standard enumeration encoding)
2. As `uml:Class` elements that are subtypes of the occurrence or type object class
   that defines the `PredefinedType` attribute

These predefined type classes are named using the TypeEnum name followed by a dot
and the enumeration value (e.g. `IfcRoadPartTypeEnum.BICYCLECROSSING`). The dot
in the name excludes them from EXPRESS serialization. Their xmi:id uses an
underscore instead of the dot (e.g. `cl_IfcRoadPartTypeEnum_BICYCLECROSSING`).

```xml
<!-- Predefined type class — subtype of IfcRoadPart -->
<packagedElement xmi:type="uml:Class"
                 xmi:id="cl_IfcRoadPartTypeEnum_BICYCLECROSSING"
                 name="IfcRoadPartTypeEnum.BICYCLECROSSING">
  <generalization xmi:type="uml:Generalization"
                  xmi:id="gen_21458"
                  general="cl_IfcRoadPart"/>
</packagedElement>

<!-- Pset associated to the predefined type class -->
<packagedElement xmi:type="uml:Dependency"
                 xmi:id="dependency_21657"
                 client="cl_Pset_RoadDesignCriteriaCommon"
                 supplier="cl_IfcRoadPartTypeEnum_BICYCLECROSSING"/>
```

The naming convention for the xmi:id is `cl_IfcXxxTypeEnum_VALUE`. The entity
name is derived by stripping the `TypeEnum_VALUE` suffix (`IfcRoadPart`), and
the predefined type value is the part after the last `_` (`BICYCLECROSSING`).

For `PSET_TYPEDRIVENOVERRIDE` psets with a predefined type, the applicability
implies both the occurrence entity (`IfcRoadPart/BICYCLECROSSING`) and the type
entity (`IfcRoadPartType/BICYCLECROSSING`).

---

## Property enumerations (PEnum_)

Property enumerations are defined in `propertytypes.uml` as `uml:Enumeration`
elements with names starting with `PEnum_` or `Penum_`:

```xml
<packagedElement xmi:type="uml:Enumeration" xmi:id="en_PEnum_ElementStatus"
                 name="PEnum_ElementStatus">
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="NEW"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="EXISTING"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="DEMOLISH"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="TEMPORARY"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="OTHER"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="NOTKNOWN"/>
  <ownedLiteral xmi:type="uml:EnumerationLiteral" name="UNSET"/>
</packagedElement>
```

They are referenced from pset properties via `href`:

```xml
<type xmi:type="uml:Enumeration"
      href="propertytypes.uml#en_PEnum_ElementStatus"/>
```

Or as a local inline reference when defined in the same file:

```xml
<ownedAttribute name="AirTerminalShape" type="en_PEnum_AirTerminalShape">
```

PEnum values prefixed with `Penum_` (lowercase e) exclude themselves from
EXPRESS serialization — they are property-level enumerations only, not schema
types.

---

## Quantity sets (Qto_)

Quantity sets follow the same structure as property sets — `uml:Class` elements
with names starting with `Qto_`. They use `uml:Dependency` for applicability
in the same way. Quantities within a Qto are `ownedAttribute` children with
type references to `IfcAreaMeasure`, `IfcLengthMeasure`, etc.

---

## Predefined type subclasses (dot notation)

Predefined type values appear as `uml:Class` elements with a
dot in the name (e.g. `IfcDoor.GATE`). The dot pattern identifies these as
predefined type pseudo-classes — they are excluded from EXPRESS serialization
and exist only to enable pset applicability links in the UML model.

---

## What is NOT in the UML files

The UML files contain the machine-readable schema. The following IFC content
is defined elsewhere:

| Content                                                  | Location                                                                               |
|----------------------------------------------------------|----------------------------------------------------------------------------------------|
| Entity descriptions and extended descriptions            | `docs/schemas/{layer}/{package}/Entities/{EntityName}.md`                              |
| Attribute descriptions                                   | `## Attributes` section of entity markdown files                                       |
| Entity notes, history, examples, deprecations            | Annotation blocks in entity markdown files                                             |
| Informal propositions                                    | Entity markdown files (prose, not machine-readable)                                    |
| Property set descriptions                                | `docs/schemas/{layer}/{package}/PropertySets/Pset_*.md`                                |
| Property base definitions                                | `docs/properties/{PropertyName}.md`                                                    |
| Property enumeration descriptions and value descriptions | `docs/schemas/{layer}/{package}/PropertyEnumerations/PEnum_*.md`                       |
| Concept templates                                        | `docs/templates/{category}/{template}/README.md`                                       |
| General usages                                           | `schemas/mvd/GeneralUsage.csv`                                                         |
| MVD applicability                                        | `schemas/mvd.csv`                                                                      |
| EXPRESS functions documentation                          | `docs/schemas/{layer}/{package}/Functions/{FunctionName}.md`                           |
| WHERE rules documentation                                | `## Formal Propositions` section of entity markdown files                              |
| Figures                                                  | `docs/figures`                                                                         |
| Examples IFC files in documentation                      | In the `https://github.com/buildingSMART/IFC4.3.x-sample-models` repo, under `models/` |
