IfcSharedMgmtElements
=====================

The **IfcSharedMgmtElements** schema defines basic concepts that are common to management throughout the various stages of the building lifecycle. The primary classes in the schema are all subtypes of _IfcControl_ and act to manage or regulate the conduct of the project in some way. This schema, along with _IfcProcessExtension_ and _IfcConstructionMgmtDomain_, provide a set of models that can be used by applications needing to share information concerning construction and facilities management related issues.

The objective of the **IfcSharedMgmtElements** schema is to capture information that supports the control of project scope, cost, and time. The aim is to provide support for exchange and sharing of minimal information concerning the subjects in scope; the extent of the model will not support the more detailed ideas found in more specialized management applications.

The following are within the scope of this part of the specifications:

* Cost schedules supporting hierarchical rows and columns of costs and quantities.
* Orders including purchase orders, change orders, and work orders.
* Permits for access and carrying out work.
* Requests to be fulfilled.

The following are outside of the scope of this part of the specifications:

* Transaction details that may be supported by or support electronic commerce.

> IFC4 CHANGE  The former schema _IfcFacilitiesMgmtDomain_ has been merged into this schema to include the entities _IfcPermit_ and _IfcActionRequest_, as each entity now also supports use in construction as well as facilities management.
