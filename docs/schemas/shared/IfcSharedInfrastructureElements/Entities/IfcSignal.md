# IfcSignal

A signal is an active device that conveys information or instructions to users, by means of an audio, visual signal or a combination of both.
<!-- end of short definition -->

The primary distinction from an _IfcSign_ is that a signal is active and therefore a subtype of _IfcFlowTerminal_ usually requiring power and data connections for its operation.
An instance of _IfcSignal_ represents a singular signalling device in a larger assembled unit or connected system, such as an individual frame within a railway signal, a single light unit in a traffic light system or an audio signal or light mounted on a navigational buoy.
Signals can be physically aggregated together into an assembly which can include multiple signal instances (and also sign instances) and the associated supporting structural elements such as a simple pole or a rigid frame gantry (see Signal Assembly for examples).
Signals can be logically (functionally) grouped together into a signalling system (a type of distribution system) to represent a connected group of signals for example a group of traffic lights controlling an road intersection.

## Attributes

### PredefinedType
Identifies the predefined type of a signal. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcSignalType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSignalType_.
