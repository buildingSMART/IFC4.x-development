# IfcBooleanClippingResult

A clipping result is defined as a special subtype of the general _IfcBooleanResult_. It constrains the operands and the operator of the Boolean result.
<!-- end of short definition -->

A clipping result is the Boolean difference between a swept solid and a half space solid, or between the result of the Boolean difference and a half space solid. Hence more than one difference operation can be applied to achieve the final Boolean result.

> HISTORY New entity in IFC2x.

## Formal Propositions

### FirstOperandType
The first operand of the Boolean clipping operation shall be either an IfcSweptAreaSolid, an IfcSweptDiskSolid or (in case of more than one clipping) an IfcBooleanClippingResult.

### SecondOperandType
The second operand of the Boolean clipping operation shall be an IfcHalfSpaceSolid.

### OperatorType
The Boolean operator for clipping is always "Difference".
