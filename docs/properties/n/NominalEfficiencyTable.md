NominalEfficiencyTable
======================

The nominal efficiency of the boiler as defined by the manufacturer. For steam boilers, a function of inlet temperature versus steam pressure. Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: InletTemperature(IfcThermodynamicTemperatureMeasure) and OutletTemperature(IfcThermodynamicTemperatureMeasure) in DefiningValues, and NominalEfficiency(IfcNormalisedRatioMeasure) in DefinedValues. For example, DefininfValues(InletTemp, OutletTemp), DefinedValues(null, NominalEfficiency). The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcResourceConstraintRelationship.
