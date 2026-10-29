IfcMeasureResource
==================

The _IfcMeasureResource_ schema specifies units and defined measure types that may be assigned to quantities.

> NOTE  The fundamental unit types used in this schema are based on the SI system defined in ISO 1000+A1, 1992, 1998. Units in measurement systems other than SI may be derived using this schema. Many definitions declared in the _IfcMeasureResource_ schema is adapted from [ISO 10303-41](../content/bibliography.htm#iso-10303-41)

> NOTE  In the definitions of the unit exponents the use of superscript font has been omitted. Therefore, m2 means square metre, m3 means cubic meter.

In different types of units there are five basic cases:

* Basic SI-units, which cover a number of fundamental units of mainly physical quantities defined by [ISO-1000](../content/bibliography.htm#iso-1000) such as meter or millimeter as unit for length measure or square meter as a unit for area measure. The unit may have a scaling prefix (for example: milli, kilo).
* Derived SI-units, which are defined as a derivation of the basic SI-units, for example, Newton (kg m / s2) as a unit of force. Both basic and derived SI-units are in the IFCs represented by IfcSIUnit.
* Conversion based units, which can be derived from SI-units by a scaling factor; e.g. inch which can be defined using SI-unit for length measure, i.e. an inch is 25.4 millimeters.
* Derived units, which can be defined as a derivation or combination of a number of basic units. In a derived unit each of the basic unit "component" has a dimensional exponent in defining the derived unit; e.g. kg / m2, where kilogram (kg) has dimensional exponent 1 and meter (m) has exponent -2.
* Context dependent units, which cannot be defined as conversion based unit using SI-units.

With regard to the usage of the measure defined types (for example, _IfcLengthMeasure_, _IfcTimeMeasure_) as attribute datatypes in this specification, there are three basic cases:

First, the datatype of an attribute of an entity type is a measure defined type as such without possibility on an instance level to define the unit of the measure value:

```
ENTITY IfcBoundingBox
SUBTYPE OF(IfcGeometricRepresentationItem);
Corner : IfcCartesianPoint;
XDim : IfcPositiveLengthMeasure;
YDim : IfcPositiveLengthMeasure;
ZDim : IfcPositiveLengthMeasure;
END_ENTITY;
```

In this case, it is the global unit assignment for the corresponding unit for the measure type that defines the unit for all the usages of this defined measure type (except for cases 2 and 3 below).

Second, the datatype of an attribute is IfcMeasureWithUnit, which allows for definition of unit per instance of that entity type, independent and possibly overriding the global unit assignment:

```
ENTITY IfcConversionBasedUnit
 SUPERTYPE OF (ONEOF
  (IfcConversionBasedUnitWithOffset))
 SUBTYPE OF (IfcNamedUnit);
  Name : IfcLabel;
  ConversionFactor : IfcMeasureWithUnit;
END_ENTITY;
```

In this case the relevant measure defined type (from the IfcMeasureWithUnit.ValueComponent : IfcValue select list) is not exactly defined by the schema, but implied by the context.

Third, the entity type has a separate "unit" attribute which allows for defining the unit for another attribute of the entity type for representing the actual value:

```
ENTITY IfcPropertySingleValue
SUBTYPE OF (IfcSimpleProperty);
NominalValue : IfcValue;
Unit : OPTIONAL IfcUnit;
END_ENTITY;
```

Although in the cases 2 and 3 different units could be used for different instances of the same entity type or for the same measure type in attributes of different entity types, it is recommended not to mix different units for same measure defined types, if it can be avoided. Below some examples of each of the above basic cases are given.

> NOTE  In the example instantiations in the form of IFC data exchange files, mainly the measure and unit -relevant attributes are given the values; the other attributes are given no values (in the form of $-sign) independent of whether they should actually have values because of being nonoptional attributes.

Table 1 indicates measures, units, and corresponding data types.

|Measure|Type|Unit|Symbol|Derivation|IfcSIUnitEnum|IfcUnitEnum|IfcDerivedUnitEnum|Defined value types|
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|Absorbed dose, specific energyimpact, kerma, absorbed dose index|SI / Derived|gray|Gy|J / kg|GRAY|ABSORBEDDOSEUNIT||IfcAbsorbedDoseMeasure|
|Acceleration|Derived|||m / s2|||ACCELERATIONUNIT|IfcAccelerationMeasure|
|Acidity (pH)|Derived|pH|pH|mol / l|||PHUNIT|IfcPHMeasure|
|Activity (of radionuclide)|SI / Derived|becquerel|Bq|1 / s|BECQUEREL|RADIOACTIVITYUNIT||IfcRadioActivityMeasure|
|Amount of substance|SI/Basic|mole|mol||MOLE|AMOUNTOFSUBSTANCEUNIT||IfcAmountOfSubstanceMeasure|
|Angular velocity|Derived|||rad / s|||ANGULARVELOCITYUNIT|IfcAngularVelocityMeasure|
|Area|SI/Derived|square metre|m2|m2|SQUARE_METRE|AREAUNIT||IfcAreaMeasure|
|Area density|Derived|||kg / m2|||AREADENSITYUNIT|IfcAreaDensityMeasure|
|-||||||||IfcBoolean|
|-||||||||IfcComplexNumber|
|Compound plane angle|Compound|||degree, min, s|||COMPOUNDPLANEANGLEUNIT|IfcCompoundPlaneAngleMeasure|
|-||||||||IfcContextDependentMeasure|
|-||||||||IfcCountMeasure|
|-||||||||IfcDescriptiveMeasure|
|Capacitance|SI / Derived|farad|F|C / V|FARAD|ELECTRICCAPACITANCEUNIT||IfcElectricCapacitanceMeasure|
|Celsius temperature|SI / Basic|degree Celsius|ºC|1 ºC = 1 K|DEGREE_CELSIUS|THERMODYNAMICTEMPERATUREUNIT||IfcThermodynamicTemperatureMeasure|
|Curvatue|Derived|||rad / m|||CURVATUREUNIT|IfcCurvatureMeasure|
|-||||||||IfcDate (lexical representation according to ISO 8601)|
|-||||||||IfcDateTime (lexical representation according to ISO 8601)|
|Dose equivalent, dose equivalent index|SI / Derived|sievert|Sv|J / kg|SIEVERT|DOSEEQUIVALENTUNIT||IfcDoseEquivalentMeasure|
|-||||||||IfcDuration  (lexical representation according to ISO 8601)|
|Dynamic viscosity|Derived|||Pa · s|||DYNAMICVISCOSITYUNIT|IfcDynamicViscosityMeasure|
|Electric charge, quantity of electricity|SI / Derived|coulomb|C|A · s|COULOMB|ELECTRICCHARGEUNIT||IfcElectricChargeMeasure|
|Electric conductance|SI / Derived|siemens|S|1 / W|SIEMENS|ELECTRICCONDUCTANCEUNIT||IfcElectricConductanceMeasure|
|Electric current|SI / Basic|ampere|A||AMPERE|ELECTRICCURRENTUNIT||IfcElectricCurrentMeasure|
|Electric potential, potential difference, tension, electromotive force|SI / Derived|volt|V|W / A|VOLT|ELECTRICVOLTAGEUNIT||IfcElectricVoltageMeasure|
|Electric resistance|SI / Derived|ohm|W|V / A|OHM|ELECTRICRESISTANCEUNIT||IfcElectricResistanceMeasure|
|Energy, work, quantity of heat|SI / Derived|joule|J|N · m|JOULE|ENERGYUNIT||IfcEnergyMeasure|
|Force|SI / Derived|newton|N|kg · m / s2|NEWTON|FORCEUNIT||IfcForceMeasure|
|Frequency|SI / Derived|hertz|Hz|1 / s|HERTZ|FREQUENCYUNIT||IfcFrequencyMeasure|
|Heat flux density|Derived|||W / m2|||HEATFLUXDENSITYUNIT|IfcHeatFluxDensityMeasure|
|Heating value|Derived|||J / kg|||HEATINGVALUEUNIT|IfcHeatingValueMeasure|
|-||||||||IfcIdentifier|
|Illuminance|SI / Derived|lux|lx|lm / m2|LUX|ILLUMINANCEUNIT||IfcIlluminanceMeasure|
|Inductance|SI / Derived|henry|H|Wb / A|HENRY|INDUCTANCEUNIT||IfcInductanceMeasure|
|-||||||||IfcInteger|
|(Integer) Count rate|Derived|||1 / s|||INTEGERCOUNTRATEUNIT|IfcIntegerCountRateMeasure|
|Ion concentration|Derived|||g / l|||IONCONCENTRATIONUNIT|IfcIonConcentrationMeasure|
|Isothermal moisture capacity|Derived|||m3 / kg|||ISOTHERMALMOISTURECAPACITYUNIT|IfcIsothermalMoistureCapacityMeasure|
|Kinematic viscosity|Derived|||m2 / s|||KINEMATICVISCOSITYUNIT|IfcKinematicViscosityMeasure|
|Length|SI / Basic|metre|m||METRE|LENGTHUNIT||IfcLengthMeasure|
|-||||||||IfcLabel|
|Linear force|Derived|||N / m|||LINEARFORCEUNIT|IfcLinearForceMeasure|
|Linear moment|Derived|||N · m / m|||LINEARMOMENTUNIT|IfcLinearMomentMeasure|
|Linear stiffness|Derived|||N / m|||LINEARSTIFFNESSUNIT|IfcLinearStiffnessMeasure|
|Linear velocity|Derived|||m / s|||LINEARVELOCITYUNIT|IfcLinearVelocityMeasure|
|-||||||||IfcLogical|
|Luminous flux|SI / Derived|lumen|lm|cd · sr|LUMEN|LUMINOUSFLUXUNIT||IfcLuminousFluxMeasure|
|Luminous intensity|SI / Basic|candela|cd||CANDELA|LUMINOUSINTENSITYUNIT||IfcLuminousIntensityMeasure|
|Luminous intensity distribution|Derived|||cd / lm|||LUMINOUSINTENSITYDISTRIBUTIONUNIT|IfcLuminousIntensityDistributionMeasure|
|Magnetic flux|SI / Derived|weber|Wb|V · s|WEBER|MAGNETICFLUXUNIT||IfcMagneticFluxMeasure|
|Magnetic flux density|SI / Derived|tesla|T|Wb / m2|TESLA|MAGNETICFLUXDENSITYUNIT||IfcMagneticFluxDensityMeasure|
|Mass|SI / Basic|gram|g (kg)||GRAM|MASSUNIT||IfcMassMeasure|
|Mass density|Derived|||kg / m3|||MASSDENSITYUNIT|IfcMassDensityMeasure|
|Mass flow rate|Derived|||kg / s|||MASSFLOWRATEUNIT|IfcMassFlowRateMeasure|
|Mass per length|Derived|||kg / m|||MASSPERLENGTHUNIT|IfcMassPerLengthMeasure|
|Modulus of elasticity|Derived|||N / m2|||MODULUSOFELASTICITYUNIT|IfcModulusOfElasticityMeasure|
|Modulus of linear subgrade reaction|Derived|||N / m2|||MODULUSOFLINEARSUBGRADEREACTIONUNIT|IfcModulusOfLinearSubgradeReactionMeasure|
|Modulus of rotational subgrade reaction|Derived|||N · m / m · rad|||MODULUSOFROTATIONALSUBGRADEREACTIONUNIT|IfcModulusOfRotationalSubgradeReactionMeasure|
|Modulus of subgrade reaction|Derived|||N / m3|||MODULUSOFSUBGRADEREACTIONUNIT|IfcModulusOfSubgradeReactionMeasure|
|Moisture diffusivity|Derived|||m3 / s|||MOISTUREDIFFUSIVITYUNIT|IfcMoistureDiffusivityMeasure|
|Molecular weight|Derived|||g / mol|||MOLECULARWEIGHTUNIT|IfcMolecularWeightMeasure|
|Moment of inertia|Derived|||m4|||MOMENTOFINERTIAUNIT|IfcMomentOfInertiaMeasure|
|-||||||||IfcMonetaryMeasure|
|(Non negative length)|||m|||LENGTHUNIT||IfcNonNegativeLengthMeasure|
|-||||||||IfcNormalisedRatioMeasure|
|-||||||||IfcNumericMeasure|
|-||||||||IfcParameterValue|
|Planar force|Derived|||N / m2|||PLANARFORCEUNIT|IfcPlanarForceMeasure|
|Plane angle|SI / Derived|radian|rad|m / m = 1|RADIAN|PLANEANGLEUNIT||IfcPlaneAngleMeasure|
|(Positive length)|||m|||LENGTHUNIT||IfcPositiveLengthMeasure|
|(Positive plane angle)|||rad|||PLANEANGLEUNIT||IfcPositivePlaneAngleMeasure|
|-||||||||IfcPositiveRatioMeasure|
|Power|SI / Derived|watt|W|J / s|WATT|POWERUNIT||IfcPowerMeasure|
|Pressure, stress|SI / Derived|pascal|Pa|N / m2|PASCAL|PRESSUREUNIT||IfcPressureMeasure|
|-||||||||IfcRatioMeasure|
|-||||||||IfcReal|
|Rotational frequency|Derived|||cycles / s|||ROTATIONALFREQUENCYUNIT|IfcRotationalFrequencyMeasure|
|Rotational mass|Derived|||kg · m2|||ROTATIONALMASSUNIT|IfcRotationalMassMeasure|
|Rotational stiffness|Derived|||N · m / rad|||ROTATIONALSTIFFNESSUNIT|IfcRotationalStiffnessMeasure|
|Sectional area integral|Derived|||m5|||SECTIONALAREAINTEGRALUNIT|IfcSectionalAreaIntegralMeasure|
|Section modulus|Derived|||m3|||SECTIONMODULUSUNIT|IfcSectionModulusMeasure|
|Shear modulus|Derived|||N / m2|||SHEARMODULUSUNIT|IfcShearModulusMeasure|
|Solid angle|SI / Derived|steradin|sr|m2 / m2 = 1|STERADIAN|SOLIDANGLEUNIT||IfcSolidAngleMeasure|
|Sound power||watt|W|W|||SOUNDPOWERUNIT|IfcSoundPowerMeasure|
|Sound power level||decibel|db|W / W|||SOUNDPOWERLEVELUNIT|IfcSoundPowerLevelMeasure|
|Sound pressure||pascal|Pa|Pa|||SOUNDPRESSUREUNIT|IfcSoundPressureMeasure|
|Sound pressure level||decibel|db|Pa / Pa|||SOUNDPRESSURELEVELUNIT|IfcSoundPressureLevelMeasure|
|Specific heat capacity|Derived|||J / kg· K|||SPECIFICHEATCAPACITYUNIT|IfcSpecificHeatCapacityMeasure|
|Temperature gradient||||K / m|||TEMPERATUREGRADIENTUNIT|IfcTemperatureGradientMeasure|
|Temperature change||||K / s|||TEMPERATURERATEOFCHANGEUNIT|IfcTemperatureRateOfChangeMeasure|
|-||||||||IfcText|
|Thermal admittance|Derived|||W / m2 · K|||THERMALADMITTANCEUNIT|IfcThermalAdmittanceMeasure|
|Thermal conductivity|Derived|||W / m · K|||THERMALCONDUCTIVITYUNIT|IfcThermalConductivityMeasure|
|Thermal expansion coefficient||||1 / K|||THERMALEXPANSIONCOEFFICIENTUNIT|IfcThermalExpansionCoefficientMeasure|
|Thermal resistance|Derived|||m2 · K / W|||THERMALRESISTANCEUNIT|IfcThermalResistanceMeasure|
|Thermal transmittance|Derived|||W / m2 · K|||THERMALTRANSMITTANCEUNIT|IfcThermalTransmittanceMeasure|
|Thermodynamic temperature|SI / Basic|kelvin|K||KELVIN|THERMODYNAMICTEMPERATUREUNIT||IfcThermodynamicTemperatureMeasure|
|-||||||||IfcTime     (lexical representation according to ISO 8601)|
|Time|SI / Basic|second|s||SECOND|TIMEUNIT||IfcTimeMeasure|
|-||||||||IfcTimeStamp|
|Torque|Derived|||N· m|||TORQUEUNIT|IfcTorqueMeasure|
|Vapor permeability|Derived|||kg / s · m · Pa|||VAPORPERMEABILITYUNIT|IfcVaporPermeabilityMeasure|
|Volume|SI / Derived|cubic metre|m3|m3|CUBIC_METRE|VOLUMEUNIT||IfcVolumeMeasure|
|Volumetric flow rate|Derived|||m3 / s|||VOLUMETRICFLOWRATEUNIT|IfcVolumetricFlowRateMeasure|
|Warping constant||||m6|||WARPINGCONSTANTUNIT|IfcWarpingConstantMeasure|
|Warping moment|Derived|||N · m2|||WARPINGMOMENTUNIT|IfcWarpingMomentMeasure|

Table 1 &mdash; Measures and units
