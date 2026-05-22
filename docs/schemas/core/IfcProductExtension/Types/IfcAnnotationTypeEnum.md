# IfcAnnotationTypeEnum

This enumeration defines the different types of Annotation elements an _IfcAnnotation_ object can represent.
<!-- end of short definition -->

## Items

### SURVEY
Annotation used for survey information, such as survey points, survey lines or survey areas.

> EXAMPLE Typically used in surveying or mapping to indicate the location, elevation, or other relevant data about a specific point or area.

> NOTE The shape representation of the _IfcAnnotation_ indicates if it is a survey point, survey line, survey area or any other type of representation connected to survey. 

### CONTOURLINE
Annotation used to illustrate lines connecting points of equal elevation or depth, on a map or chart.

> EXAMPLE Typically used in cartography, geography, or geology maps, where the spacing of lines at constant intervals of elevation may be used as an indication of slope.

### TEXT
A textual annotation.

### DIMENSION
Annotation used to illustrate the measurement or size of an object, often accompanied by numerical values.

### LEADER
Annotation that includes a line or arrow.

> EXAMPLE Typically used to connect an object to a specific point of reference or to an explanation.

### SYMBOL
Annotation that employs graphical symbols or icons to represent specific meanings.

### ISOBAR
Annotation used to illustrate lines connecting points of equal pressure on a map or chart. 

> EXAMPLE Typically used on weather maps or to show pressure gradient in spaces, chambers or externally.

### ISOLUX
Annotation used to illustrate lines connecting points of equal illuminance or light intensity.

> EXAMPLE Typically used in lighting design or photometry to show the distribution of illumination levels and/or day lighting in a space or externally.

### ISOTHERM
Annotation used to illustrate lines connecting points of equal temperature on a map or chart.

> EXAMPLE Typically used in to show the heating or cooling distribution within a space or to show temperature distribution on a geographic map.

### USERDEFINED
User-defined type.

### NOTDEFINED
Undefined type.
