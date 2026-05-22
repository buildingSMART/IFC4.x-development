# PEnum_WindowPanelPositionEnum

This enumeration defines the basic configuration of the window type in terms of the location of window panels. The window configurations are given for windows with one, two or three panels (including fixed panels) as shown in Figure 1. It corresponds to the _OperationType_ of the _IfcWindowType_ definition, which references the _IfcWindowPanelProperties_.
<!-- end of short definition -->

Windows which are subdivided into more than three panels have to be defined by the geometry only. The type of such windows is given by an _IfcWindowType.PartitioningType_ = USERDEFINED or NOTDEFINED (see _IfcWindowTypePartitioningEnum_ for details).

| Enumerator from IfcWindowTypePartitioningEnum | Use of enumerators from IfcWindowPanelPositionEnum | Figure |
| --- | --- | --- |
| DoublePanelVertical | first IfcWindowPanelProperties with PanelPosition = LEFT<br>second IfcWindowPanelProperties with PanelPosition = RIGHT | ![](../../../../figures/ifcwindowpanelpositionenum-fig01.gif) |
| DoublePanelHorizontal | first IfcWindowPanelProperties with PanelPosition = TOP<br>second IfcWindowPanelProperties with PanelPosition = BOTTOM | ![](../../../../figures/ifcwindowpanelpositionenum-fig02.gif) |
| TriplePanelVertical | first IfcWindowPanelProperties with PanelPosition = LEFT<be>second IfcWindowPanelProperties with PanelPosition = MIDDLE<br>third IfcWindowPanelProperties with PanelPosition = RIGHT | ![](../../../../figures/ifcwindowpanelpositionenum-fig03.gif) |
| TriplePanelHorizontal | first IfcWindowPanelProperties with PanelPosition = TOP<br>second IfcWindowPanelProperties with PanelPosition = MIDDLE<br>third IfcWindowPanelProperties with PanelPosition = BOTTOM | ![](../../../../figures/ifcwindowpanelpositionenum-fig04.gif) |
| TriplePanelBottom | first IfcWindowPanelProperties with PanelPosition = LEFT<br>second IfcWindowPanelProperties with PanelPosition = RIGHT<br>third IfcWindowPanelProperties with PanelPosition = BOTTOM | ![](../../../../figures/ifcwindowpanelpositionenum-fig05.gif) |
| TriplePanelTop | first IfcWindowPanelProperties with PanelPosition = TOP<br>second IfcWindowPanelProperties with PanelPosition = LEFT<br>third IfcWindowPanelProperties with PanelPosition = RIGHT | ![](../../../../figures/ifcwindowpanelpositionenum-fig06.gif) |
| TriplePanelLeft | first IfcWindowPanelProperties with PanelPosition = LEFT<br>second IfcWindowPanelProperties with PanelPosition = TOP<br>third IfcWindowPanelProperties with PanelPosition = BOTTOM | ![](../../../../figures/ifcwindowpanelpositionenum-fig07.gif) |
| TriplePanelRight | first IfcWindowPanelProperties with PanelPosition = TOP<br>second IfcWindowPanelProperties with PanelPosition = BOTTOM<br>third IfcWindowPanelProperties with PanelPosition = RIGHT | ![](../../../../figures/ifcwindowpanelpositionenum-fig08.gif) |

> HISTORY New enumeration in IFC2.0.

Note:

1. The figures/ are shown as elevations in the XZ plane of the local placement of the window, looking into the direction of the positive Y axis.
2. These figures/ are only shown as illustrations.

## Items

### LEFT
Left.

### MIDDLE
Middle.

### RIGHT
Right.

### BOTTOM
Bottom.

### TOP
Top.

### NOTDEFINED
Undefined.

### OTHER

Other.

### NOTKNOWN

Not known.

### UNSET

Unset.