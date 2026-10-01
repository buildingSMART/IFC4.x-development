# IfcElement

An element is a generalization of all components that make up a facility.
<!-- end of short definition -->

Elements are physically existent objects, although they might be void elements, such as holes. Elements either remain permanently in the facility, or only temporarily, as formwork does. Elements can be either assembled on site or pre-manufactured and built in on site.

> EXAMPLE Examples of elements in a building construction context are walls, floors, windows and recesses.

The elements can be logically contained by a spatial structure element that constitutes a certain level within a project structure hierarchy (site, building, storey or space). This is done by using the _IfcRelContainedInSpatialStructure_ relationship. An element can have material and quantity information assigned through the _IfcRelAssociatesMaterial_ and _IfcRelDefinesByProperties_ relationship.

In addition an element can be declared to be a specific occurrence of an element type (and thereby be defined by the element type properties) using the _IfcRelDefinesByType_ relationship. An element can also be defined as an element assembly that is a group of semantically and topologically related elements that form a higher level part of the facility. Those element assemblies are defined by virtue of the _IfcRelAggregates_ relationship.

> EXAMPLE Examples for element assembly are complete Roof Structures, made by several Roof Areas, or a Stair, composed by Flights and Landings.

Elements that perform the same function may be grouped by an "Element Group By Function". It is realized by an instance of _IfcGroup_ with the _ObjectType_ ='ElementGroupByFunction'.

> HISTORY New entity in IFC1.0

## Attributes

### Tag
The tag (or label) identifier at the particular instance of a product, e.g. the serial number, or the position number. It is the identifier at the occurrence level.

### FillsVoids
Reference to the _IfcRelFillsElement_ relationship that puts the element as a filling into the opening created within another element.

### ConnectedTo
Reference to the element connection relationship. The relationship then refers to the other element to which this element is connected to.

### IsInterferedByElements
Reference to the interference relationship to indicate the element that is interfered. The relationship, if provided, indicates that this element has an interference with one or many other elements.
> NOTE There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_.

> IFC4 CHANGE New inverse relationship.

### InterferesElements
Reference to the interference relationship to indicate the element that interferes. The relationship, if provided, indicates that this element has an interference with one or many other elements.
> NOTE There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_.

> IFC4 CHANGE New inverse relationship.

### HasProjections
Projection relationship that adds a feature (using a Boolean union) to the _IfcBuiltElement_.

### HasOpenings
Reference to the _IfcRelVoidsElement_ relationship that creates an opening in an element. An element can incorporate zero-to-many openings. For each opening, that voids the element, a new relationship _IfcRelVoidsElement_ is generated.

### IsConnectionRealization
Reference to the connection relationship with realizing element. The relationship, if provided, assigns this element as the realizing element to the connection, which provides the physical manifestation of the connection relationship.

### ProvidesBoundaries
Reference to space boundaries by virtue of the objectified relationship _IfcRelSpaceBoundary_. It defines the concept of an element bounding spaces.

### ConnectedFrom
Reference to the element connection relationship. The relationship then refers to the other element that is connected to this element.

### ContainedInStructure
Containment relationship to the spatial structure element, to which the element is primarily associated. This containment relationship has to be hierarchical, i.e. an element may only be assigned directly to zero or one spatial structure.

### HasCoverings
Reference to _IfcCovering_ by virtue of the objectified relationship _IfcRelCoversBldgElements_. It defines the concept of an element having coverings associated.

### HasSurfaceFeatures
Reference to the _IfcRelAdheresToElement_ relationship that adheres a _IfcSurfaceFeature_ to an element. An element can incorporate zero-to-many surface features in one relationship.

## Concepts

### Body AdvancedBrep Geometry

An _IfcElement_ (so far no further constraints are defined at the level of its subtypes or by view definitions) may be represented as a single or multiple boundary representation models, which include advanced surfaces, usually referred to as NURBS surfaces. The 'AdvancedBrep' representation allows for the representation of complex free-form element shape.

> NOTE View definitions or implementer agreements may restrict or disallow the use of 'AdvancedBrep' geometry.

### Body AdvancedSwept Directrix Geometry



### Body AdvancedSwept DiskSolid PolyCurve Geometry



### Body AdvancedSwept Tapered Geometry



### Body Brep Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented as a single or multiple Boundary Representation models (which are restricted to be faceted Brep's with or without voids). The Brep representation allows for the representation of complex element shape.


![Brep representation](../../../../figures/ifcbuildingelement-brep-layout1.gif)

Figure 150 — Building element body boundary representation

> EXAMPLE  As shown in Figure 150, the Brep representation is given by an _IfcShapeRepresentation_, which includes one or more items, all of type _IfcFacetedBrep_. In some cases it may be useful to also expose a simple representation as a bounding box representation of the same complex shape.

### Body CSG Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented as a CSG primitive or CSG tree. The CSG representation allows for the representation of complex element shape.

> NOTE View definitions or implementer agreements may restrict or disallow the use of 'CSG' geometry.

### Body SectionedSolidHorizontal



### Body SurfaceModel Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented as a single or multiple surface models, based on either shell or face based surface models. It may also include tessellated models.


![surface model](../../../../figures/ifcbuildingelement-surfacemodel-layout1.gif)

Figure 149 — Element surface model representation


> EXAMPLE As shown in Figure 149, the surface model representation is given by an _IfcShapeRepresentation_, which includes a single item which is either an _IfcShellBasedSurfaceModel_, or an _IfcFaceBasedSurfaceModel_. In some cases it may also be useful to expose a simple representation as a bounding box representation of the same complex shape.


### Body SurfaceOrSolidModel Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented as a mixed representation, including surface and solid models.

### Body SweptSolid Composite Geometry



### Body SweptSolid CompositeCurve Geometry



### Body SweptSolid ParameterizedProfile Geometry



### Body SweptSolid PolyCurve Geometry



### Body Tessellation Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented as a single or multiple tessellated surface models, in particular triangulated surface models.

### Box Geometry

![bounding box](../../../../figures/ifcbuildingelement-boundingbox-layout1.gif)

Figure 148 — Building element box representation

> EXAMPLE  Any _IfcElement_ may be represented by a bounding box, which shows the maximum extent of the body within the object coordinate system established by the _IfcObjectPlacement_. As shown in Figure 148, the bounding box representation is given by an _IfcShapeRepresentation_ that includes a single item: an _IfcBoundingBox_.

### CoG Geometry

The 'CoG', Center of Gravity, shape representation is used as a means to verify the correct import by comparing the CoG of the imported geometry with the explicitly provided CoG created during export.

### Element Interference

### Element Nesting

A host element can nest connected components. This should be used when there is a specific position or form factor to attach specific elements.

> EXAMPLE A sink has a pre-drilled hole to attach a faucet.

### Element Openings



### Element Projecting



### Element Voiding Features



### FootPrint Annotation Geometry



### FootPrint GeomSet PolyCurve Geometry



### FootPrint Geometry



#### FootPrint_GeometricCurveSet

Any collection of points and curves representing the floor plan projection.

#### FootPrint_Annotation2D

Any collection of points and curves, and additional hatching and text representing the floor plan projection.

### Mapped Geometry

Any _IfcElement_ (so far no further constraints are defined at the level of its subtypes) may be represented using the 'MappedRepresentation'. This shall be supported as it allows for reusing the geometry definition of a type at all occurrences of the same type. The results are more compact data sets.

The same constraints, as given for 'SurfaceOrSolidModel', 'SurfaceModel', 'Tessellation', 'Brep', and 'AdvancedBrep' geometric representation, shall apply to the _IfcRepresentationMap_.

### Product Grid Placement



### Product Linear Placement

Product placement with a _Product Linear Placement_ template. It defines the local coordinate system based on the curve which is referenced by _IfcLinearPlacement.RelativePlacement_ which is an _IfcAxis2PlacementLinear.Location_ using an _IfcPointByDistanceExpression.BasisCurve_. The local coordinate system is based on the tangent of the curve at Location, its normal in the global Z plane and the cross product of the aforementioned vectors.

### Product Local Placement

The object placement for any subtype of IfcElement is defined by the _IfcObjectPlacement_, either _IfcLocalPlacement_ or _IfcGridPlacement_, which defines the local object coordinate system that is referenced by all geometric representations of that _IfcElement_.

#### IfcLocalPlacement_IfcLocalPlacement

Relative placement according to position and rotation relative to container.

### Property Sets for Objects



### Surface Feature Adherence



### Surface Sectioned Geometry



### Surface Tessellation Geometry



