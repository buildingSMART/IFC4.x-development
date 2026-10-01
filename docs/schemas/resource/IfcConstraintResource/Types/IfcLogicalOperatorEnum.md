# IfcLogicalOperatorEnum

_IfcLogicalOperatorEnum_ is an enumeration that defines the logical operators that may be applied for the satisfaction of one or more operands (_IfcConstraint_) at a time.
<!-- end of short definition -->

The following tables illustrates application of _IfcLogicalOperatorEnum_ in a case of three operands, A, B and C, for each operator.


|Operand|||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|A|F|F|F|T|F|T|T|T|
|B|F|F|T|F|T|F|T|T|
|C|F|T|F|F|T|T|F|T|
|RESULT|F|F|F|F|F|F|F|T|

Table 1 - LOGICALAND(A,B,C)

|Operand|||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|A|F|F|F|T|F|T|T|T|
|B|F|F|T|F|T|F|T|T|
|C|F|T|F|F|T|T|F|T|
|RESULT|F|T|T|T|T|T|T|T|

Table 2 - LOGICALOR(A,B,C)

|Operand|||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|A|F|F|F|T|F|T|T|T|
|B|F|F|T|F|T|F|T|T|
|C|F|T|F|F|T|T|F|T|
|RESULT|F|T|T|T|F|F|F|F|

Table 3 - LOGICALXOR(A,B,C)

|Operand|||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|A|F|F|F|T|F|T|T|T|
|B|F|F|T|F|T|F|T|T|
|C|F|T|F|F|T|T|F|T|
|RESULT|T|T|T|T|T|T|T|F|

Table 4 - LOGICALNOTAND(A,B,C)

|Operand|||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|A|F|F|F|T|F|T|T|T|
|B|F|F|T|F|T|F|T|T|
|C|F|T|F|F|T|T|F|T|
|RESULT|T|F|F|F|F|F|F|F|

Table 5 - LOGICALNOTOR(A,B,C)

> HISTORY New enumeration in IFC2.0.

> IFC4 CHANGE Extended to include LOGICALXOR, LOGICALNOTAND and LOGICALNOTOR.

## Items

### LOGICALAND
Defines a relationship between operands whereby the result is true if all operands are true, and false if at least one operand is false.

### LOGICALOR
Defines a relationship between operands whereby the result is true if at least one operand is true, and false if all operands are false.

### LOGICALXOR
Defines a relationship between operands whereby the result is true if exactly one operand is true (exclusive or).

### LOGICALNOTAND
Defines a relationship between operands whereby the result is true if at least one operand is false, and false if all operands are true.

### LOGICALNOTOR
Defines a relationship between operands whereby the result is true if all operands are false, and false if at least one operand is true.
