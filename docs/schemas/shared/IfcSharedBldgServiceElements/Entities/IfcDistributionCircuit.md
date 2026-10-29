# IfcDistributionCircuit

A distribution circuit is a partition of a distribution system that is conditionally switched such as an electrical circuit.
<!-- end of short definition -->

> HISTORY New entity in IFC4.

> IFC4 CHANGE For electrical power systems, _IfcElectricalCircuit_ has been used for low-voltage (12-1000 V) power circuits and has been replaced by _IfcDistributionCircuit_ in IFC4; _IfcDistributionSystem_ with PredefinedType 'ELECTRICAL' should be used for overall power systems, and _IfcDistributionCircuit_ with PredefinedType 'ELECTRICAL' should be used for each switched circuit.

****Composition Use Definition****

An _IfcDistributionCircuit_ may aggregate an _IfcDistributionSystem_ using the _IfcRelAggregates_ relationship where _RelatingObject_ refers to the _IfcDistributionSystem_ and _RelatedObjects_ includes one or more _IfcDistributionCircuit_ groups.

An _IfcDistributionCircuit_ may be aggregated into sub-circuits using the _IfcRelAggregates_ relationship where _RelatingObject_ refers to the parent _IfcDistributionCircuit_ and _RelatedObjects_ refers to one or more _IfcDistributionCircuit_ sub-circuits.

****Assignment Use Definition****

An _IfcDistributionCircuit_ should be assigned to an _IfcDistributionPort_ on an _IfcFlowController_ element indicating the host or origination of the system using the _IfcRelAssignsToProduct_ relationship.

Each device whose operation is conditional based upon the state of the circuit is assigned to the _IfcDistributionCircuit_ via the _IfcRelAssignsToGroup_ relationship. An _IfcDistributionElement_ may belong to multiple systems or circuits, however only one _IfcDistributionSystem_ or _IfcDistributionCircuit_ of a particular _PredefinedType_.
