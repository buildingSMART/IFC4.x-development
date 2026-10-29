IfcTopologyResource
===================

The schema _IfcTopologyResource_ defines the resources used for topological representations. The primary application of this resource is its use in the Boundary representation of the shape or geometric form of a product model.

> NOTE  The definitions of this resource of the IFC model have been taken from [ISO 10303-42](../content/bibliography.htm#iso-10303-42). The IfcTopologyResource refers to the clause 5, "Topology" of the standard. The reference is ISO/IS 10303-42:1994, pp. 122. The improved definitions of the second edition, ISO/DIS 10303-42:1999 have been used, when applicable.

The definitions taken from ISO/IS 10303-42:1994 have undergone an adaptation process, characterized by:

* adaptation of the IFC naming convention (inner majuscules and Ifc prefix)
* adaptation of the ISO 10303 entities, where multiple inheritance or non-exclusive inheritance (that is, AND or ANDOR subtype constraints) are used
* selection of a subset of the IR, using subtype and select pruning
* omission of the name attribute at the representation item

The topological representation of the shape is defined following the adaptation of 10303-42. The type, class, and function semantic definition sections follow the adapted wording of the working draft, which is clearly indicated and quoted at each reference. The definitions on geometric and topological representation (when taken from ISO/CD 10303-42:1992) are explicitly excluded from the copyright of this specification.

> For more information on the definitions as defined in the formal ISO standard please refer to: ISO/IS 10303-42:1994, Industrial Automation Systems and Integration: Product Data Representation and Exchange - Part 42: Integrated Generic Resources. Geometric and Topological Representation. The formal standard can be obtained through the local publishers of standards in each individual country.

The following are within the scope of the topology schema:

* definition of the fundamental topological entities vertex, edge, and face, each with a specialized subtype to enable it to be associated with the geometry of a point, curve, or surface, respectively;
* collections of the basic entities to form topological structures of path, loop and shell and constraints to ensure the integrity of these structures;
* orientation of topological entities.
