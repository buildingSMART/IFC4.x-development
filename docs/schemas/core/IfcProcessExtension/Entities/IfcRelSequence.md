# IfcRelSequence

_IfcRelSequence_ is a sequential relationship between processes where one process must occur before the other in time and where the timing of the relationship may be described as a type of sequence. The relating process (_IfcRelSequence.RelatingProcess_) is considered to be the predecessor in the relationship (has precedence) whilst the related process (_IfcRelSequence.RelatedProcess_) is the successor.
<!-- end of short definition -->

_IfcRelSequence_ is defined as one-to-one relationship; therefore it assigns one predecessor to one successor.

> HISTORY New entity in IFC1.0.

> IFC4 CHANGE Relocated to _IfcProcessExtension_ schema. _TimeLag_ and _SequenceType_ made optional. _USERDEFINED_ added to the _IfcSequenceEnum_ enumeration. _UserDefinedSequenceType_ attribute added. WHERE rule controlling use of the _USERDEFINED_ enumeration added.

**Use definitions**

_IfcRelSequence_ is used to describe the logical sequence relationship that exists between two processes. This logical relationship identifies that there is a predecessor or relating process and a successor or related process. In IFC, there may be one predecessor and one successor in the relationship. Many occurrences of _IfcRelSequence_ may exist to describe the sequence relationships of a predecessor task with many successor tasks or of many predecessor tasks with one successor task, thus enabling a m:n sequence relationship between tasks. Please note that sequence relationships can be used to define dependencies between process occurrences but also between process types (for further information see _IfcRelDefinesByObject_ and _IfcTaskType_). In case of defining dependencies between process occurrences sequence relationships should stay within the limits of a directed, non-cyclic graph.

A sequence type may be set for a sequence. For tasks assigned to a work schedule, it is expected that the sequence type will be asserted. For a process map, where the sequence relationship between processes is simply a logical flow, it need not be asserted.

A time lag may be assigned to a sequence, and the sequence type defines the way in which the time lag applies to the sequence either as a ratio or percentage of time duration (e.g. start successor task when predecessor is 50% complete) or as a time measure (e.g. start successor task 1 week after commencement of the predecessor task). Care should be used when assigning a time lag to a sequence depending on the setting of the sequence type since there is no checking that the time lag value is in keeping with the sequence type set.

## Attributes

### RelatingProcess
Reference to the process, that is the predecessor.

### RelatedProcess
Reference to the process, that is the successor.

### TimeLag
Time duration of the sequence, it is the time lag between the predecessor and the successor as specified by the _SequenceType_.

### SequenceType
The way in which the time lag applies to the sequence.

### UserDefinedSequenceType
Allows for specification of user defined type of the sequence beyond the enumeration values (_START_START_, _START_FINISH_ _FINISH_START_, _FINISH_FINISH_) provided by _SequenceType_ attribute of type _IfcSequenceEnum_. When a value is provided for attribute _UserDefinedSequenceType_ in parallel the attribute _SequenceType_ shall have enumeration value _USERDEFINED_.

> IFC4 CHANGE Attribute added

## Formal Propositions

### AvoidInconsistentSequence
The _RelatingProcess_ shall not point to the same instance as the _RelatedProcess_.

### CorrectSequenceType
The attribute _UserDefinedSequenceType_ must be asserted when the value of _SequenceType_ is set to _USERDEFINED_.
