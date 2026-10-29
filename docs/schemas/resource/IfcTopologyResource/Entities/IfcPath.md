# IfcPath

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> A path is a topological entity consisting of an ordered collection of oriented edges, such that the edge start vertex of each edge coincides with the edge end of its predecessor. The path is ordered from the edge start of the first oriented edge to the edge end of the last edge. The BOOLEAN value sense in the oriented edge indicates whether the edge direction agrees with the direction of the path (TRUE) or is the opposite direction (FALSE).
>
> An individual edge can only be referenced once by an individual path. An edge can be referenced by multiple paths. An edge can exist independently of a path.

> NOTE Entity adapted from **path** defined in ISO 10303-42.

> HISTORY New entity in IFC2.0

**Informal Propositions**

1. A path has dimensionality 1.
2. A path is arcwise connected.
3. The edges of the path do not intersect except at common vertices.
4. A path has a finite, non-zero extent.

## Attributes

### EdgeList
The list of oriented edges which are concatenated together to form this path.

## Formal Propositions

### IsContinuous
The end vertex of each edge shall be the same as the start vertex of its successor.
