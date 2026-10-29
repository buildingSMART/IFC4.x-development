# IfcDiscreteAccessoryType

The element component type **IfcDiscreteAccessoryType** defines commonly shared information for occurrences of discrete accessories. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a discrete accessory type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcDiscreteAccessoryType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcDiscreteAccessoryType** are represented by instances of _IfcDiscreteAccessory_.

> HISTORY New entity in IFC4.

Type Use Definition

The exact type information of the _IfcDiscreteAccessoryType_ is given in the _PredefinedType_ attribute, possibly in combination with the _ElementType_ attribute inherited from _IfcElementType_. Standard _ElementType_ designations are provided for guideline below. The list is not exhaustive and the list of definitions may be extended based on local agreements.

Corbels as separate components:

* **'Hidden steel corbel'**: Corbel system made from steel components embedded into the master element.
* **'Visible steel corbel'**: Corbel system made from steel components protruding from the master element.
* **'Visible concrete corbel'**: Corbel system made as a separate precast concrete component added to the master element.

Connecting accessories, for example for sandwich wall panels:

* **'Diagonal truss connector'**: A fixing device in truss form with diagonal cross bars holding two precast concrete panels together in a sandwich wall panel.
* **'Ladder truss connector'**: A fixing device in truss form with straight cross bars in ladder form holding two precast concrete panels together in a sandwich wall panel.
* **'Panel suspender'**: A straight fixing device holding two precast concrete panels together in a sandwich wall panel.

Electrical accessories for precast concrete elements:

* **'Protective plug'**: Protective plug used in element for protecting electrical accessories during manufacturing, transportation and assembly.

Fixing parts:

* **'Standard fixing plate'**: Standard fixing plate.
* **'Edge fixing plate'**: Fixing plate attached to the edge of an element.
* **'Corner fixing plate'**: Fixing plate attached to the corner of an element.
* **'Slab fixing plate'**: Fixing plate for slabs.
* **'Channel fixing'**: Fixing channels, often realized as cast-in channels.
* **'Balcony hinge'**: Accessory supporting and fixing balconies.
* **'Frame shoe'**: Fixing shoe for frames.
* **'Thermo frame'**: Thermo frame.
* **'Column shoe'**: Fixing shoe for columns.
* **'Wall shoe'**: Fixing shoe for walls.
* **'Fixing socket'**: Fixing socket.

Joint accessories:

* **'Neoprene bearing plate'**: Rubber plate used as a bearing in, for example, joints between column corbels and beams.
* **'Working joint reinforcement'**: Reinforcement accessory used in working joints.
* **'Expansion joint reinforcement'**: Reinforcement accessory used in expansion joints.
* **'Ribbed steel bar extension'**: Extension accessory made of a ribbed (reinforcement) bar used in joints.
* **'Steel pin bolt'**: Pin bolt used to join together, for example, columns and beams.
* **'Concrete dowel'**: Dowel pin used in joints.
* **'Concrete groove'**: A groove made in a joint.
* **'Steel plate'**: A steel plate used as an accessory in a joint.
* **'Wire loop'**: A joint connector accessory made from a wire loop.
* **'Steel loop'**: A joint connector accessory made from a steel bar loop.
* **'Sealing strip'**: A strip sealing the joint.
* **'Sealing compound'**: Sealing compound protecting and sealing the joint.

Lifting accessories:

* **'Wire lifting hook'**: A lifting aid in the form of a wire loop.
* **'Steel lifting hook'**: A lifting aid in the form of a steel bar loop.
* **'Lifting socket'**: A lifting aid in the form of a socket.
* **'Steel lifting anchor'**: A lifting aid in the form of a steel lifting anchor.
* **'Lifting hole'**: A lifting aid in the form of a hole.

Accessories mainly used in the building services domain:

* **'Antivibration'** : An isolating device to prevent other elements to be effected by vibrations.
* **'Drop rod'** : A length of material providing a hanging support to a bracket. Note that a drop rod is considered to include nuts and washers required for securing.
* **'Duct foot'** : A base support used to receive a vertical pipe .
* **'Framing'** : A frame placed around a penetration to prevent scraping against the building surface or structure.
* **'Grommet'** : An element placed within a penetration that seals the penetration for a particular reason.
* **'Rack'** : A set of shelving for the purposes of storage that may be freestanding or bolted to a structure.
* **'Safety part'** : A part, typically installed in vertical shafts at each level, to ensure safety from falling when entering the shaft.
* **'Sleeve'** : A thin barrier placed between a penetration and a penetrating element.
* **'Support section'** : A section of material that is used as an intermediate support upon which multiple brackets can be mounted.

## Attributes

### PredefinedType
Subtype of discrete accessory

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.
