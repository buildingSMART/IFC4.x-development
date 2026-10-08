IfcElectricalDomain
===================

The _IfcElectricalDomain_ schema forms part of the Domain Layer of the IFC Model. It extends the ideas concerning building services outlined in the _IfcSharedBldgServiceElements_ schema. It defines concepts of cabled systems where the cabling carries electrical supply, data, telephone signals or other forms of cable transmission.

Additionally the schema defines various devices that are connected by cabling, protection of electrical devices, provision and concepts of light fixtures within buildings, the cabling itself and methods for supporting and carrying cables.

The scope of the _IfcElectricalDomain_ is defined as:

1. cabled systems for power distribution and lighting, data, telecommunications, security, signalling, control and audio visual purposes,
2. equipment that is used within such systems,
3. connection of equipment to circuits, distribution points etc,
4. steady state operation of electrical installations,
5. light fixtures (fittings), their types and the provision of such information as is necessary to enable lighting calculations that provide physically accurate illuminance.

Note that for electrical systems, the schema has the particular scope of low voltage electrical installations according to Volts (V) and Alternating Current (AC) or Direct Current (DC), from 12V (AC/DC) to 1000V (AC) or 1500V (DC) in accordance with ISO/IEC definitions where installations in scope are considered to commence at a meter where the public utility supply terminates or at a transformer where voltage is stepped down to the low voltage range in scope.

Other electrical systems including extra low, medium and high voltage may be specified using this schema but the provisions of such systems have not yet been specifically provided for.

Similarly, whilst the electrical domain schema may be used for data, telecommunications, security, signalling, control and audio visual purposes, the specific provisions required of these types of systems are not yet fully captured and elaborated within the model.

The _IfcElectricalDomain_ schema supports ideas including types of:

* audio-visual appliance,
* cable carrier fittings (for conduit, cable tray, cable duct and ladder),
* electrical appliance,
* electric motor,
* distribution panels,
* generator,
* junction box,
* light fixture,
* lamp,
* outlet,
* protective device,
* protective device tripping unit,
* switching device,
* transformer,

The following items are in scope but not elaborated:

* medium and high voltage installations over 1000V AC and 1500V DC
* systems with voltage of less than 12 volts (AC/DC)
* audio-visual systems
* telecommunications systems
* data systems
* cabling for signal and control systems
* cable routers (cable ladders)
* computer network cabling and devices used on networks

The following are deemed to be out of scope of the _IfcElectricalDomain_ schema at this time:

* public utility supply of electrical services
* non steady state/transient states of operation of electrical installations
* security arrangements associated with safety of electrical installations
* communication signals between automation devices or bus systems
* sensors (which are dealt with in the _IfcBuildingControlsDomain_ schema)
* spotlight mirror systems whereby a spotlight is directed towards a distant mirror that the distributes the light energy (other than as a group of separately defined objects)
* lighting for specialist purposes (for example, stage, painting)

An electrical circuit is formed from electrical devices connected together with power carrying cables. Up to IFC4, an instance of an electrical circuit has been defined as an _IfcElectricalCircuit_ (subtype of _IfcSystem_). This is now deleted as of IFC4. Instead, electrical systems together with other cable systems and other forms of distribution system are now identified through the _IfcDistributionSystem.PredefinedType::IfcDistributionSystemEnum_, along with specific property sets.

> HISTORY  New schema in IFC2x.

> IFC4 CHANGE  Electrical circuit specification modified, scope expanded to support communications systems.
