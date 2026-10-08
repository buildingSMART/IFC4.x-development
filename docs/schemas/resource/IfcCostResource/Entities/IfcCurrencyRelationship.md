# IfcCurrencyRelationship

_IfcCurrencyRelationship_ defines the rate of exchange that applies between two designated currencies at a particular time and as published by a particular source.
<!-- end of short definition -->

An _IfcCurrencyRelationship_ is used where there may be a need to reference an _IfcCostValue_ in one currency to an _IfcCostValue_ in another currency. It takes account of fact that currency exchange rates may vary by requiring the recording the date and time of the currency exchange rate used and the source that publishes the rate. There may be many sources and there are different strategies for currency conversion (spot rate, forward buying of currency at a fixed rate).

The source for the currency exchange is defined as an instance of _IfcLibraryInformation_ that includes a name and a URL.

> HISTORY New entity in IFC2x2.

> IFC4 CHANGE Subtyped from _IfcResourceLevelRelationship_, attribute order changed.

## Attributes

### RelatingMonetaryUnit
The monetary unit from which an exchange is derived. For instance, in the case of a conversion from GBP to USD, the relating monetary unit is GBP.

### RelatedMonetaryUnit
The monetary unit to which an exchange results. For instance, in the case of a conversion from GBP to USD, the related monetary unit is USD.

### ExchangeRate
The currently agreed ratio of the amount of a related monetary unit that is equivalent to a unit amount of the relating monetary unit in a currency relationship. For instance, in the case of a conversion from GBP to USD, the value of the exchange rate may be 1.486 (USD) : 1 (GBP).

### RateDateTime
The date and time at which an exchange rate applies.
> IFC4 CHANGE Type changed from IfcDateTimeSelect. Attribute made optional.

### RateSource
The source from which an exchange rate is obtained.
