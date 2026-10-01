# IfcEdgeLoop

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An edge_loop is a loop with nonzero extent. It is a path in which the start and end vertices are the same. Its domain, if present, is a closed curve. An edge_loop may overlap itself.

> NOTE Entity adapted from **edge_loop** defined in ISO 10303-42.

> HISTORY New entity in IFC2x2.

**Informal Propositions**

1. The genus of the _IfcEdgeLoop_ shall be 1 or greater.
2. The Euler formula shall be satisfied: (number of vertices) + genus - (number of edges) = 1;
3. No edge may be referenced more than once by the same _IfcEdgeLoop_ with the same sense. For this purpose, an edge which is not an oriented edge is considered to be referenced with the sense TRUE.

## Attributes

### EdgeList
A list of oriented edge entities which are concatenated together to form this path.

### Ne
The number of elements in the edge list.

## Formal Propositions

### IsClosed
The start vertex of the first edge shall be the same as the end vertex of the last edge. This ensures that the path is closed to form a loop.

### IsContinuous
The end vertex of each edge shall be the same as the start vertex of its successor.
