# IfcBooleanResult

The _IfcBooleanResult_ is the result of applying a Boolean operation to two operands being solids.
<!-- end of short definition -->

> EXAMPLE If the first operand is a block and the second operand is a solid cylinder of suitable dimensions and location, the boolean result produced with the difference operator would be a block with a circular hole.

> NOTE Definition according to ISO/CD 10303-42:1992
> A Boolean result is the result of a regularized operation on two solids to create a new solid. Valid operations are regularized union, regularized intersection, and regularized difference. For purpose of Boolean operations, a solid is considered to be a regularized set of points. The final Boolean result depends upon the operation and the two operands. In the case of the difference operator the order of the operands is also significant. The operator can be either union, intersection or difference. The effect of these operators is described below: > * Union on two solids is the new solid that is the regularization of the set of all points that are in either the first operand or the second operand or in both.
> * Intersection on two solids is the new solid that is the regularization of the set of all points that are in both the first operand and the second operand.
> * The result of the difference operation on two solids is the regularization of the set of all points which are in the first operand, but not in the second operand.

> NOTE Corresponding STEP type **boolean_result** defined in ISO 10303-42.

> HISTORY New entity in IFC1.5.1.

## Attributes

### Operator
The Boolean operator used in the operation to create the result.

### FirstOperand
The first operand to be operated upon by the Boolean operation.

### SecondOperand
The second operand specified for the operation.

### Dim
The space dimensionality of this entity. It is identical with the space dimensionality of the first operand. A where rule ensures that both operands have the same space dimensionality.

## Formal Propositions

### SameDim
The dimensionality of the first operand shall be the same as the dimensionality of the second operand.

### FirstOperandClosed
If the _FirstOperand_ is of type _IfcTessellatedFaceSet_ it has to be a closed tessellation.

### SecondOperandClosed
If the _SecondOperand_ is of type _IfcTessellatedFaceSet_ it has to be a closed tessellation.
