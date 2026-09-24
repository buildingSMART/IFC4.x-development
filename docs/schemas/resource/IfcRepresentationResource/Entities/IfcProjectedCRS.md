# IfcProjectedCRS

_IfcProjectedCRS_ is a coordinate reference system (CRS) of the map to which the map translation of the local engineering coordinate system of the construction or facility engineering project relates. The projected coordinate reference system is assumed to be a 2D or 3D right-handed Cartesian coordinate system, the optional _MapUnit_ attribute can be used to determine the length unit used by the map.
<!-- end of short definition -->

Despite what its name suggests:

* If the referenced _IfcGeometricRepresentationContext_ is 3D, then _IfcProjectedCRS_ shall be a **compound coordinate reference system**, meaning a combination of multiple CRS from which a _GeodeticDatum_ and a _VerticalDatum_ can always be unambiguously identified.

* If the referenced _IfcGeometricRepresentationContext_ is 2D, then _IfcProjectedCRS_ can be either a **projected coordinate reference system** or a **compound coordinate reference system**.

> EXAMPLE The code EPSG:9286 (ETRS89 + NAP height) is the combination of a geographic CRS (ETRS89) and a vertical CRS (NAP height), with their respective datums.

> EXAMPLE The code EPSG:9306 (HS2 Survey Grid + HS2-VRF height) is the combination of a projected CRS (HS2 Survey Grid), and a vertical CRS (HS2-VRF height), with their respective datums.

The unambiguous identifier by which the coordinate reference system is known, is stored in the inherited _Name_ attribute. Well defined identifiers include the map projection, the map zone information, and all required datums. In these cases the attributes _VerticalDatum_, _MapProjection_, _MapZone_ as well as the inherited attribute _GeodeticDatum_ can be omitted.

> EXAMPLE The code 'EPSG:5555' identifies the combination of *ETRS89 / UTM zone 32N + DHHN92 height* (i.e., a projected CRS + a vertical CRS). The code **'EPSG:6258'** identifies the **geodetic datum** of the projected CRS *ETRS89 / UTM zone 32N* (itself identified as EPSG:25832). The code **'EPSG:5181'** identifies the **vertical datum** of the vertical CRS *DHHN92 height* (itself identified as EPSG:5783).

> NOTE Definition from OpenGIS Abstract Specification, Topic 2:
> A 2D (or with vertical coordinate axis 3D) coordinate reference system used to approximate the shape of the earth on a planar surface, but in such a way that the distortion that is inherent to the approximation is carefully controlled and known. Distortion correction is commonly applied to calculated bearings and distances to produce values that are a close match to actual field values.

> HISTORY New entity in IFC4.

## Attributes

### VerticalDatum
Name by which the vertical datum is identified. The vertical datum is associated with the height axis of the coordinate reference system and indicates the reference plane and fundamental point defining the origin of a height system. It needs to be provided, if the _Name_ identifier does not unambiguously define the vertical datum as well and if the coordinate reference system is a 3D reference system.

> EXAMPLE vertical datums include: 'EPSG:5181' (Deutsches Haupthöhennetz 1992); 'EPSG:5215' (European Vertical Reference Frame 2007)

### MapProjection
Name by which the map projection is identified.

> EXAMPLE map projections include: UTM; Gauss-Krueger

### MapZone
Name by which the map zone, relating to the _MapProjection_, is identified.

> EXAMPLE map zones includes: for UTM, the zone number, like 32 for UTM32; for Gauss-Krueger, the zone number, like 3 for GK3

### MapUnit

Unit of the coordinate axes composing the map coordinate system.

> NOTE Only length measures are in scope and all two or three axes of the map coordinate system shall have the same length unit.

> NOTE If MapUnit is omitted, the unit for the coordinate axes is taken from the default units, as stated in IfcProject.UnitInContext.

## Formal Propositions

### IsLengthUnit
The map unit shall be given, if present, as a length unit.
