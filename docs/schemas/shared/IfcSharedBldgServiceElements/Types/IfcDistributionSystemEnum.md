# IfcDistributionSystemEnum

This enumeration identifies different types of distribution systems. It is used to designate systems by their function as well as ports of devices within such systems to restrict connectivity to compatible connections.
<!-- end of short definition -->

> HISTORY New enumeration in IFC4.

Ports for cable carriers may be connected using _IfcCableCarrierSegment_ and _IfcCableCarrierFitting_. Type objects for cable carrier segments and fittings (_IfcCableCarrierSegmentType_ and _IfcCableCarrierFittingType_ that are not specific to a particular system type may have ports with _PredefinedType_ of NOTDEFINED which indicates that occurrences of such objects may connect to ports of any other cable-carrier based port. Valid enumerations for cable carriers are the same as that for cables, and may be asserted if ports of the contained cables are all of the same type.

## Items

### AIRCONDITIONING
Conditioned air distribution system for purposes of maintaining a temperature range within one or more spaces.

### AUDIOVISUAL
A transport of a single media source, having audio and/or video streams.

### CHEMICAL
Arbitrary chemical further qualified by property set, such as for medical or industrial use.

### CHILLEDWATER
Nonpotable chilled water, such as circulated through an evaporator.

### COMMUNICATION
Communication.

### COMPRESSEDAIR
Compressed air system.

### CONDENSERWATER
Nonpotable water, such as circulated through a condenser.

### CONTROL
A transport or network dedicated to control system usage.

### CONVEYING
Arbitrary supply of substances.

### DATA
A network having general-purpose usage.

### DISPOSAL
Arbitrary disposal of substances.

### DOMESTICCOLDWATER
Unheated potable water distribution system.

### DOMESTICHOTWATER
Heated potable water distribution system.

### DRAINAGE
Drainage collection system.

### EARTHING
A path for equipotential bonding, conducting current to the ground.

### ELECTRICAL
A circuit for delivering electrical power.

### ELECTROACOUSTIC
An amplified audio signal such as for loudspeakers.

### EXHAUST
Exhaust air collection system for removing stale or noxious air from one or more spaces.

### FIREPROTECTION
Fire protection sprinkler system.

### FUEL
Arbitrary supply of fuel.

### GAS
Gas-phase materials such as methane or natural gas.

### HAZARDOUS
Hazardous material or fluid collection system.

### HEATING
Water or steam heated from a boiler and circulated through radiators.

### LIGHTING
A circuit dedicated for lighting, such as a fixture having sockets for lamps.

### LIGHTNINGPROTECTION
A path for conducting lightning current to the ground.

### MUNICIPALSOLIDWASTE
Items consumed and discarded, commonly known as trash or garbage.

### OIL
Oil distribution system.

### OPERATIONAL
Operating supplies system.

### POWERGENERATION
A path for power generation.

### RAINWATER
Rainwater resulting from precipitation which directly falls on a parcel.

### REFRIGERATION
Refrigerant distribution system for purposes of fulfilling all or parts of a refrigeration cycle.

### SECURITY
A transport or network dedicated to security system usage.

### SEWAGE
Sewage collection system.

### SIGNAL
A raw analog signal, such as modulated data or measurements from sensors.

### STORMWATER
Stormwater resulting from precipitation which runs off or travels over the ground surface.

### TELEPHONE
A transport or network dedicated to telephone system usage.

### TV
A transport of multiple media sources such as analog cable TV, satellite TV, or over-the-air TV.

### VACUUM
Vacuum distribution system.

### VENT
Vent system for wastewater piping systems.

### VENTILATION
Ventilation air distribution system involved in either the exchange of air to the outside as well as circulation of air within a building.

### WASTEWATER
Water adversely affected in quality by anthropogenic influence, possibly originating from sewage, drainage, or other source.

### WATERSUPPLY
Arbitrary water supply.

### CATENARY_SYSTEM
A longitudinal distribution system that supports contact wires, including catenary wire droppers and stich wires.

### OVERHEAD_CONTACTLINE_SYSTEM
An overhead contact line system above the upper limit of the train using an overhead contact line and a catenary system to supply current to traction units.

### RETURN_CIRCUIT
A distribution system which forms the intended path for the traction return current and the current under fault conditions.

### FIXEDTRANSMISSIONNETWORK
Represents all wired networks that provide a data transmission channel using optical fiber cables, copper cables or both. It aggregates many technologies that are based on the multiplexing method.

### OPERATIONALTELEPHONYSYSTEM
A system that allows communications between operators (e.g. switchtender, traffic regulator, operational agents, etc.) in operational centers and on the infrastructure site (e.g. railway, tunnel or road).

### MOBILENETWORK
Mobile network insures wireless communication by providing a secure platform for voice and data communication between infrastructure operators, including drivers, dispatchers, shunting team members and station controllers.

### MONITORINGSYSTEM
Sensor-based system for building and infrastructure environmental monitoring and control.

### USERDEFINED


### NOTDEFINED

