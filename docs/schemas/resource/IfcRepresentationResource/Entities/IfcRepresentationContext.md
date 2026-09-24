# IfcRepresentationContext

The _IfcRepresentationContext_ defines the context to which the _IfcRepresentation_ of a product is related.
<!-- end of short definition -->

> NOTE Definition from ISO 10303-42
> A representation context is a context in which a set of representation items are related.

> NOTE Entity adapted from **representation_context** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5.

> IFC4 CHANGE Entity made abstract, had been deprecated from instantiation since IFC2x2.

## Attributes

### ContextIdentifier
The optional identifier of the representation context as used within a project.

### ContextType
The description of the type of a representation context. The supported values for context type are to be specified by implementers agreements.

### RepresentationsInContext
All shape representations that are defined in the same representation context.
