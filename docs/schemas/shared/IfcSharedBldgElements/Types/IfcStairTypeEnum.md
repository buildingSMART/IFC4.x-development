# IfcStairTypeEnum

This enumeration defines the basic configuration of the stair type in terms of the number of stair flights and the number of landings. The type also distinguished turns by windings or by landings. In addition the subdivision of the straight and changing direction stairs is included. The stair configurations are given for stairs without and with one, two or three landings.
<!-- end of short definition -->

Stairs which are subdivided into more than three landings, or stairs with non-regular shapes are to be defined with type being USERDEFINED or NOTDEFINED.

> HISTORY New enumeration in IFC2.0.

## Items

### STRAIGHT_RUN_STAIR
A stair extending from one level to another without turns or winders. The stair consists of one straight flight.

![](../../../../figures/ifcstairtypeenum-fig01.gif)

### TWO_STRAIGHT_RUN_STAIR
A straight stair consisting of two straight flights without turns but with one landing.

![](../../../../figures/ifcstairtypeenum-fig06.gif)

### QUARTER_WINDING_STAIR
A stair consisting of one flight with a quarter winder, which is making a 90° turn. The direction of the turn is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig02.gif)

### QUARTER_TURN_STAIR
A stair making a 90° turn, consisting of two straight flights connected by a quarterspace landing. The direction of the turn is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig07.gif)

### HALF_WINDING_STAIR
A stair consisting of one flight with one half winder, which makes a 180° turn. The orientation of the turn is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig04.gif)

### HALF_TURN_STAIR
A stair making a 180° turn, consisting of two straight flights connected.

![](../../../../figures/ifcstairtypeenum-fig08.gif)

by a halfspace landing. The orientation of the turn is determined by the walking line.

### TWO_QUARTER_WINDING_STAIR
A stair consisting of one flight with two quarter winders, which make a
90° turn. The stair makes a 180° turn. The direction of the turns is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig03.gif)

### TWO_QUARTER_TURN_STAIR
A stair making a 180° turn, consisting of three straight flights connected by two quarterspace landings. The direction of the turns is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig10.gif)

### THREE_QUARTER_WINDING_STAIR
A stair consisting of one flight with three quarter winders, which make a
90° turn. The stair makes a 270° turn. The direction of the turns is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig03a.gif)

### THREE_QUARTER_TURN_STAIR
A stair making a 270° turn, consisting of four straight flights connected
by three quarterspace landings. The direction of the turns is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig10a.gif)

### SPIRAL_STAIR
A stair constructed with winders around a circular newel often without landings. Depending on outer boundary it can be either a circular, elliptical or rectangular spiral stair. The orientation of the winding stairs is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig05.gif)

### DOUBLE_RETURN_STAIR
A stair having one straight flight to a wide quarterspace landing, and two side flights from that landing into opposite directions. The stair is making a 90° turn. The direction of traffic is determined by the walking line.

![](../../../../figures/ifcstairtypeenum-fig09.gif)

### CURVED_RUN_STAIR
A stair extending from one level to another without turns or winders. The stair is consisting of one curved flight.

![](../../../../figures/ifcstairtypeenum-fig11.gif)

### TWO_CURVED_RUN_STAIR
A curved stair consisting of two curved flights without turns but with one landing.

![](../../../../figures/ifcstairtypeenum-fig12.gif)

### LADDER
a piece of equipment consisting of a series of bars or steps between two upright elements used for climbing up or down something.

### USERDEFINED
Free form stair (user defined operation type).

### NOTDEFINED

