# IfcCoordinateReferenceSystem

The _IfcCoordinateReferenceSystem_ is a definition of a coordinate reference system by means of qualified identifiers only. The interpretation of the identifier is expected to be well-known to the receiving software.
<!-- end of short definition -->

> NOTE Definition from OpenGIS Abstract Specification, Topic 2:
> A coordinate reference system is a coordinate system which is related to the real world by a datum. The coordinate system is composed of a set of coordinate axes with specified units of measure. The datum specifies the relationship of a coordinate system to the earth. The resulting combination of coordinate system and datum is a coordinate reference system.

The unambiguous identifier by which the coordinate reference system is know, is stored in the _Name_ attribute. Well defined identifiers include the geodetic and the vertical CRS, each with its own datum. In these cases the _GeodeticDatum_ can be omitted.

> EXAMPLE The code 'EPSG:5555' identifies the combination of *ETRS89 / UTM zone 32N + DHHN92 height* (i.e., a projected CRS + a vertical CRS). The code **'EPSG:6258'** identifies the **geodetic datum** of the projected CRS *ETRS89 / UTM zone 32N* (itself identified as EPSG:25832). The code **'EPSG:5181'** identifies the **vertical datum** of the vertical CRS *DHHN92 height* (itself identified as EPSG:5783).

> NOTE One widely-used, publicly-available authority is the European Petroleum Survey Group (EPSG), and use of this authority is currently specified in several OGC Implementation Specifications. Software used to transport IFC engineering models into GIS applications (and vice versa) is expected to have knowledge about the OGC Implementation Specifications.

> HISTORY New entity in IFC4.

## Attributes

### Name
Name by which the coordinate reference system is identified.
> NOTE The name shall be taken from the list recognized by the European Petroleum Survey Group EPSG. It should then be qualified by the EPSG namespace, for example as 'EPSG:5555'.

> NOTE The *Name* shall contain only one EPSG code. When there is not one EPSG that unambiguously identifies the CRS, _IfcWellKnownText_ shall be used. Combining multiple EPSG codes in one string for *Name* (e.g., 'EPSG:2056,EPSG:5728') is not allowed.

> NOTE The name shall be 'WKT' if an EPSG code does not exist for the coordinate reference system (CRS). In this case, the CRS shall be further specified using the _IfcWellKnownText_ entity.

### Description
Informal description of this coordinate reference system.

### GeodeticDatum
Name by which this datum is identified. The geodetic datum is associated with the coordinate reference system and indicates the shape and size of the rotation ellipsoid and this ellipsoid's connection and orientation to the actual globe/earth. It needs to be provided, if the _Name_ identifier does not unambiguously define the geodetic datum as well.

> EXAMPLE geodetic datums include:
>
> **EPSG:6326** (WGS84 World Geodetic System 1984, used in GPS); 
> **ED50** (European Datum 1950, also identified as EPSG:6230); 
> **EUREF89** (European Terrestrial Reference Frame 1989, also identified as EPSG:1178).

### WellKnownText

Well Known Text (WKT) definition for this coordinate reference system inversely associated as a _IfcWellKnownText_ entity.

### HasCoordinateOperation
Indicates conversion between coordinate reference systems. In particular it refers to an _IfcCoordinateOperation_ between this coordinate reference system, and another coordinate reference system.

## Formal Propositions

### NameOrWKT
Ensures that the coordinate reference system is properly specified by either a reference to an EPSG code in *Name* or a well known text in *WellKnownText*.
