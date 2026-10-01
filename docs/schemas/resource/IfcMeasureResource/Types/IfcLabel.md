# IfcLabel

A label is the term by which something may be referred to. It is a string which represents the human-interpretable name of something and shall have a natural-language meaning.
<!-- end of short definition -->

Type: STRING of up to 255 characters

> NOTE Type adapted from **label** defined in ISO 10303-41.

> HISTORY New type in IFC2x.

> IFC4 CHANGE Previously recommended size restriction of 255 characters is now mandatory.

Value restrictions

As a human-readable string for naming purposes, a label is usually human-specified and locale-dependent (in contrast to purely machine-readable identifiers, _IfcIdentifier_).

> NOTE The set of characters that may appear in STRINGs exchanged in the exchange structure as defined in ISO 10303.21 is provided in ISO 10646. The encoding of characters in case of file-based exchange is defined in ISO 10303-21 and ISO 10303-28. Among else, these specifications define the encoding of 8-bit characters from ISO 8859-1...-16 and of 2-byte and 4-byte Unicode characters from ISO 10646.

> NOTE While _IfcIdentifier_ is restricted to 255 characters, the size in exchange files after encoding may be considerably larger than 255 octets, depending on the particular encoding and on the contents of the identifier.
