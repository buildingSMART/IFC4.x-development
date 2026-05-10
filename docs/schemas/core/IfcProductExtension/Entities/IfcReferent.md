# IfcReferent

_IfcReferent_ defines a position at a particular offset along an alignment curve.
<!-- end of short definition -->

Referents may be used for several scenarios:

* positioning physical elements at common locations along an alignment curve (e.g. bridge piers)
* indicating transitions for cross-sections (e.g. beginning of curvature where road is relatively flat, maximum curvature having super-elevated cross-slope to accommodate design speed)
* indicating events at a specific location (e.g. change in width or superelevation)
* indicating broken chainage where distance measurements reset or reverse directions, or have jumps.
* indicating domain-specific design parameters (via property sets) at locations along an alignment curve

> NOTE Referents can be nested to alignments, using _IfcRelNests_, to describe stations along an alignment. Being _IfcRelNests.RelatedObjects_ an ordered list, the first nested referent is the starting station of a given alignment. _IfcReferent_ must preceed IfcAlignmentHorizontal, IfcAlignmentVertical, and IfcAlignmentCant when present in the same _IfcRelNests.RelatedObjects_ list.

> NOTE The stationing value of any object can be provided, using an _IfcReferent_ and the respective _Pset_Stationing_. The relationship between the given object and the referent indicating its stationing value is an _IfcRelPositions_. 

## Attributes

### PredefinedType
Predefined types to define the particular type of the referent.

### RestartDistance
Optional value in case of broken linear referencing required to keep stationing further down the alignment unchanged.
