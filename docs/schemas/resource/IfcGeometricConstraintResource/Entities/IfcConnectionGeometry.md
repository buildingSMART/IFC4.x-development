# IfcConnectionGeometry

_IfcConnectionGeometry_ is used to describe the geometric and topological constraints that facilitate the physical connection of two objects. It is envisioned as a control that applies to the element connection relationships.
<!-- end of short definition -->

> NOTE The element connection relationship normally provides for a logical connection information, by referencing the relating and related elements. If in addition an _IfcConnectionGeometry_ is provided, physical connection information is given by specifying exactly where at the relating and related element the element connection occurs. Using the eccentricity subtypes, the connection can also be described when there is a physical distance (or eccentricity) between the connection elements.

The _IfcConnectionGeometry_ allows for the provision of connection constraints between geometric and topological elements, the following connection geometry/topology types are in scope:

* point | vertex point
* curve | edge curve
* surface | face surface
* solid model | closed shell

> HISTORY New entity in IFC1.5.

> IFC2x3 CHANGE The definition of the subtypes has been enhanced by allowing either geometric representation items (point | curve | surface) or topological representation items with associated geometry (vertex point | edge curve | face surface).
