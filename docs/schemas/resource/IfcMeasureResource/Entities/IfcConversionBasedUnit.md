# IfcConversionBasedUnit

An IfcConversionBasedUnit is used to define a unit that has a conversion rate to a base unit. To identify some commonly used conversion based units, the standard designations (case insensitive) for the _Name_ attribute are indicated in Table 1.
<!-- end of short definition -->

|Name|Description|
|--- |--- |
|'inch'|Length measure equal to 25.4 mm|
|'foot'|Length measure equal to 304.8 mm|
|'US survey foot'|Length measure equal to 304.80060960122 mm (i.e. the approximate value of 1200/3937 meters)|
|'yard'|Length measure equal to 914.4 mm|
|'mile'|Length measure equal to 1609.344 m|
|'square inch'|Area measure equal to 0.00064516 square meters|
|'square foot'|Area measure equal to 0.09290304 square meters|
|'square yard'|Area measure equal to 0.83612736 square meters|
|'acre'|Area measure equal to 4046.873 square meters|
|'square mile'|Area measure equal to 2589988 square meters|
|'cubic inch'|Volume measure equal to 0.00001638706 cubic meters|
|'cubic foot'|Volume measure equal to 0.028316846592 cubic meters|
|'cubic yard'|Volume measure equal to 0.7645549 cubic meters|
|'litre'|Volume measure equal to 0.001 cubic meters|
|'fluid ounce UK'|Volume measure equal to 0.0000284130625 cubic meters|
|'fluid ounce US'|Volume measure equal to 0.00002957353 cubic meters|
|'pint UK'|Volume measure equal to 0.000568 cubic meters|
|'pint US'|Volume measure equal to 0.0004731765 cubic meters|
|'gallon UK'|Volume measure equal to 0.004546 cubic meters|
|'gallon US'|Volume measure equal to 0.003785412 cubic meters|
|'degree'|Plane angle measure equal to π/180 rad|
|'ounce'|Mass measure equal to 28.349523125 g|
|'pound'|Mass measure equal to 0.45359237 kg|
|'ton UK'|Mass measure equal to 1016.0469088 kg, also known as long ton, gross ton, shipper's ton|
|'ton US'|Mass measure equal to 907.18474 kg, also known as short ton, net ton|
|'lbf'|Force measure equal to 4.4482216153 N, also known as pound-force|
|'kip'|Force measure equal to 4448.2216153 N, also known as kilopound-force|
|'psi'|Pressure measure equal to 6894.7572932 Pa, also known as pound-force per square inch|
|'ksi'|Pressure measure equal to 6894757.2932 Pa, also known as kilopound-force per square inch|
|'minute'|Time measure equal to 60 s|
|'hour'|Time measure equal to 3600 s|
|'day'|Time measure equal to 86400 s|
|'btu'|Energy measure equal to 1055.056 J, also known as British Thermal Unit|

Table 1 — Standard unit names

> EXAMPLE An inch is a converted unit. It is from the Imperial system, its name is "inch" and it can be related to the SI unit, millimetre, through a measure with unit whose value is 25.4 millimetre. A foot is also a converted unit. It is from the Imperial system, its name is "foot" and it can be related to an _IfcSIUnit_, millimetre, either directly or through the unit called "inch". Note that several US customary units differ from Imperial units (nonmetric English units) of the same name.

> NOTE Definition according to ISO/CD 10303-41:1992
> A conversion based unit is a unit that is defined based on a measure with unit.

> NOTE Entity adapted from **conversion_based_unit** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.1.

> IFC2x3 CHANGE Standard names of typical units added.

> IFC4 CHANGE Further names added: square inch, square foot, square mile, square yard, cubic inch, cubic foot, cubic yard, fluid ounce UK/US, ton UK/US, degree.

## Attributes

### Name
The word, or group of words, by which the conversion based unit is referred to.

### ConversionFactor
The physical quantity from which the converted unit is derived.

### HasExternalReference
Reference to external information, e.g. library, classification, or document information, which is associated with the conversion-based unit.
> IFC4 CHANGE New inverse attribute.
