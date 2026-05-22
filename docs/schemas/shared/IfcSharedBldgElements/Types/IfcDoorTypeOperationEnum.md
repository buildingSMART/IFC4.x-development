# IfcDoorTypeOperationEnum

This enumeration defines the basic ways to describe how an _IfcDoor_ or _IfcDoorType_ operate, as shown in the figures below. It combines the partitioning of the access barrier into single or multiple panels and the operation types of those panels.
<!-- end of short definition -->

In the most common case of swinging doors the _IfcDoorTypeOperationEnum_ defined the hinge side (left hung or right hung) and the opening direction (opening to the left, opening to the right). Whether the door opens inwards or outwards is determined by the local coordinate system of the _IfcDoor_

> NOTE There are different definitions in various countries on what a left opening or left hung or left swing door is (same for right). Therefore the IFC definition terms may derive from the local standard and may need to be mapped appropriately.

> HISTORY New Enumeration in IFC4.

{ .change-ifc2x4}
> IFC4 CHANGE The new _IfcDoorTypeOperationEnum_ replaces the use of _IfcDoorStyleOperationEnum_ that is deprecated from IFC4 onwards.

Note that:

1. Figures are shown in the ground view.
2. Figures (symbolic representation) depend on the national building code.
3. These figures/ are only shown as illustrations, the actual representation in the ground view might differ.
4. Open to the outside is declared as open into the direction of the positive y-axis, determined by the _ObjectPlacement_ at _IfcDoor_
5. The location of the panel relative to the wall thickness is defined by the _ObjectPlacement_ at _IfcDoor_, and the _IfcDoorLiningProperties.LiningOffset_ parameter.

## Items

### SINGLE_SWING_LEFT
Door with one panel that opens (swings) to the left. The hinges are on the left side as viewed in the direction of the positive y-axis.

![single swing left](../../../../figures/ifcdoortypeenum-fig01.gif)

![single swing left](../../../../figures/ifcdoortypeenum-fig01b.gif)

### SINGLE_SWING_RIGHT
Door with one panel that opens (swings) to the right. The hinges are on the right side as viewed in the direction of the positive y-axis.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![single swing right](../../../../figures/ifcdoortypeenum-fig02.gif)

![single swing right](../../../../figures/ifcdoortypeenum-fig02b.gif)

### DOUBLE_DOOR_SINGLE_SWING
Door with two panels, one opens (swings) to the left, the other opens (swings) to the right.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing](../../../../figures/ifcdoortypeenum-fig03.gif)

![double swing](../../../../figures/ifcdoortypeenum-fig03b.gif)

### DOUBLE_DOOR_SINGLE_SWING_OPPOSITE_LEFT
Door with two panels that both open to the left, one panel swings in one direction and the other panel swings in the opposite direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![opposite left](../../../../figures/ifcdoortypeenum-fig07.gif)

### DOUBLE_DOOR_SINGLE_SWING_OPPOSITE_RIGHT
Door with two panels that both open to the right, one panel swings in one direction and the other panel swings in the opposite direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![opposite right](../../../../figures/ifcdoortypeenum-fig08.gif)

### DOUBLE_SWING_LEFT
Door with one panel that swings in both directions and to the left in the main traffic direction. Also called double acting door.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing left](../../../../figures/ifcdoortypeenum-fig04.gif)

![double swing left](../../../../figures/ifcdoortypeenum-fig04b.gif)

### DOUBLE_SWING_RIGHT
Door with one panel that swings in both directions and to the right in the main traffic direction. Also called double acting door.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing right](../../../../figures/ifcdoortypeenum-fig05.gif)

![double swing right](../../../../figures/ifcdoortypeenum-fig05b.gif)

### DOUBLE_DOOR_DOUBLE_SWING
Door with two panels, one swings in both directions and to the right in the main traffic direction, the other swings also in both directions and to the left in the main traffic direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double double swing](../../../../figures/ifcdoortypeenum-fig06.gif)

![double double swing](../../../../figures/ifcdoortypeenum-fig06b.gif)

### SLIDING_TO_LEFT
Door with one panel that is sliding to the left.

![sliding to left](../../../../figures/ifcdoortypeenum-fig09.gif)

![sliding to left](../../../../figures/ifcdoortypeenum-fig09b.gif)

### SLIDING_TO_RIGHT
Door with one panel that is sliding to the right.

![sliding to right](../../../../figures/ifcdoortypeenum-fig10.gif)

![sliding to right](../../../../figures/ifcdoortypeenum-fig10b.gif)

### DOUBLE_DOOR_SLIDING
Door with two panels, one is sliding to the left the other is sliding to the right.

![double sliding](../../../../figures/ifcdoortypeenum-fig11.gif)

![double sliding](../../../../figures/ifcdoortypeenum-fig11b.gif)

### FOLDING_TO_LEFT
Door with one panel that is folding to the left.

![folding to left](../../../../figures/ifcdoortypeenum-fig12.gif)

![folding to left](../../../../figures/ifcdoortypeenum-fig12b.gif)

### FOLDING_TO_RIGHT
Door with one panel that is folding to the right.

![folding to right](../../../../figures/ifcdoortypeenum-fig13.gif)

![folding to right](../../../../figures/ifcdoortypeenum-fig13b.gif)

### DOUBLE_DOOR_FOLDING
Door with two panels, one is folding to the left, the other is folding to the right.

![double folding](../../../../figures/ifcdoortypeenum-fig14.gif)

![double folding](../../../../figures/ifcdoortypeenum-fig14b.gif)

### REVOLVING
An entrance door consisting of four leaves set in a form of a cross and revolving around a central vertical axis (the four panels are described by a single _IfcDoor_ panel property).

![revolving](../../../../figures/ifcdoortypeenum-fig15.gif)

### ROLLINGUP
Door that opens by rolling up.

> NOTE Whether it rolls up to the inside or outside is determined at the <em>IfcDoor</em>.

![rolling](../../../../figures/ifcdoortypeenum-fig16.gif)

![rolling](../../../../figures/ifcdoortypeenum-fig16b.gif)

### SWING_FIXED_LEFT
Door with one panel that opens (swings) to the left and one fixed panel. The hinges of the swinging panel are on the left side as viewed in the direction of the positive y-axis.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![swinging left and fixed](../../../../figures/ifcdoortypeenum-fig18.gif)

![swinging left and fixed](../../../../figures/ifcdoortypeenum-fig18b.gif)

### SWING_FIXED_RIGHT
Door with one panel that opens (swings) to the right and one fixed panel. The hinges of the swinging panel are on the right side as viewed in the direction
of the positive y-axis.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![swinging right and fixed](../../../../figures/ifcdoortypeenum-fig19.gif)

![swinging right and fixed](../../../../figures/ifcdoortypeenum-fig19b.gif)

### DOUBLE_DOOR_LIFTING_VERTICAL
Double panel lifting vertical.

### LIFTING_HORIZONTAL
Lifting horizontal.

### LIFTING_VERTICAL_LEFT
Lifting vertical left.

### LIFTING_VERTICAL_RIGHT
Lifting vertical right.

### REVOLVING_VERTICAL
Revolving vertical.

### USERDEFINED
User defined operation type.

### NOTDEFINED
A door with a not defined operation type is considered as a door with a lining, but no panels. It is thereby always open.

![not defined](../../../../figures/ifcdoortypeenum-fig17.gif)
