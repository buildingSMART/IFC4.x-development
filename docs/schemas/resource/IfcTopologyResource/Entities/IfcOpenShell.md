# IfcOpenShell

<!-- end of short definition -->

> NOTE Definition according to ISO/CD 10303-42:1992
> An open shell is a shell of the dimensionality 2. Its domain, if present, is a finite, connected, oriented, 2-manifold with boundary, but is not a closed surface. It can be thought of as a closed shell with one or more holes punched in it. The domain of an open shell satisfies 0 < Ξ < 1. An open shell is functionally more general than a face because its domain can have handles.
>
> The shell is defined by a collection of faces, which may be oriented faces. The sense of each face, after taking account of the orientation, shall agree with the shell normal as defined below. The orientation can be supplied directly as a BOOLEAN attribute of an oriented face, or be defaulted to TRUE if the shell member is a face without the orientation attribute.
>
> The following combinatorial restrictions on open shells and geometrical restrictions on their domains are designed, together with the informal propositions, to ensure that any domain associated with an open shell is an orientable manifold. > * Each face reference shall be unique.
> * An open shell shall have at least one face.
> * A given face may exist in more than one open shell.


> The boundary of an open shell consists of the edges that are referenced only once by the face - bounds (loops) of its faces, together with all of their vertices. The domain of an open shell, if present, contains all edges and vertices of its faces.
>
> NOTE Note that this is slightly different from the definition of a face domain, which includes none of its bounds. For example, a face domain may exclude an isolated point or line segment. An open shell domain may not. (See the algorithm for computing below.)

> NOTE Entity adapted from **open_shell** defined in ISO 10303-42.

> HISTORY New entity in IFC2x.

**Informal Propositions**

1. Every edge shall be referenced exactly twice by the face bounds of the face.
2. Each oriented edge shall be unique.
3. No edge shall be referenced by more than two faces.
4. Distinct faces of the shell do not intersect, but may share edges or vertices.
5. Distinct edges do not intersect but may share vertices.
6. Each face reference shall be unique.
7. The loops of the shell shall not be a mixture of poly loop and other loop types. Note: this is given, since only poly loop is defined as face bound definition.
8. The closed shell shall be an oriented arcwise connected 2-manifold.
9. The Euler equation shall be satisfied.
