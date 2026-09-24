# IfcSubedge

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A subedge is an edge whose domain is a connected portion of the domain of an existing edge. The topological constraints on a subedge are the same as those on an edge.

> NOTE Entity adapted from **subedge** defined in ISO 10303-42.

> HISTORY New entity in IFC2x2.

**Informal Propositions**

1. The domain of the subedge is formally defined to be the domain of the parent edge, as trimmed by the subedge start vertex and subedge end vertex.
2. The start vertex and end vertex shall be within the union of the domains of the vertices of the parent edge and the domain of the _parent edge_.

## Attributes

### ParentEdge
The Edge, or Subedge, which contains the Subedge.
