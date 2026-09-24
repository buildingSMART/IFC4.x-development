# IfcCommunicationsAppliance

A communications appliance transmits and receives electronic or digital information as data or sound.
<!-- end of short definition -->

Communication appliances may be fixed in place or may be able to be moved from one space to another. Communication appliances require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCommunicationsApplianceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no communications appliance type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCommunicationsApplianceType_.

## Concepts

### Aggregation



#### COMPUTER_IfcAudioVisualAppliance

Computers may be aggregated into audio-visual components such as displays, cameras, speakers, or microphones.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Power_ANTENNA_ELECTRICAL

Receives electrical power.

#### SINK_Radio_ANTENNA_SIGNAL

Electromagnetic waves.

#### SOURCE_Signal_ANTENNA_SIGNAL

The modulated analog signal in a circuit, such as a cable connected to a modem.

#### SINK_Power_COMPUTER_ELECTRICAL

Receives electrical power.

#### SINK_Network_COMPUTER_DATA

A network connection, may be wired or wireless (implicit antenna), such as a cable connected from a data outlet jack or from a router communications appliance. While communication is bidirectional, the router-end is considered to be the source.

#### SOURCE_Device_COMPUTER_CONTROL

A device connection such as USB or serial, which may connect to equipment such as a building automation controller.

#### SOURCE_Display_COMPUTER_AUDIOVISUAL

Audio/video output, such as a cable connected to a display, which may be aggregated into separate channels.

#### SINK_Power_FAX_ELECTRICAL

Receives electrical power.

#### SINK_Phone_FAX_TELEPHONE

Telephone connection.

#### SINK_Power_MODEM_ELECTRICAL

Receives electrical power.

#### SINK_Signal_MODEM_SIGNAL

Modulated analog signal, typically a cable connecting from a communications junction box or an antenna.

#### SOURCE_Internet_MODEM_DATA

Internet data network.

#### SOURCE_Television_MODEM_TV

Television modulated signal.

#### SOURCE_Telephone_MODEM_TELEPHONE

Telephone communications.

#### SINK_Power_PRINTER_ELECTRICAL

Receives electrical power.

#### SINK_Network_PRINTER_DATA

A network connection, may be wired or wireless.

#### SINK_Phone_PRINTER_TELEPHONE

Telephone connection for fax support.

#### SINK_Power_REPEATER_ELECTRICAL

Receives electrical power.

#### SINK_Input_REPEATER_SIGNAL

The receiving signal.

#### SOURCE_Output_REPEATER_SIGNAL

The transmitted amplified signal.

#### SINK_Power_ROUTER_ELECTRICAL

Receives electrical power.

#### SINK_Uplink_ROUTER_DATA

Uplink from another network, such as a cable connected to another router or modem accessing the Internet.

#### SOURCE_WiFi_ROUTER_DATA

A wireless access point.

#### SOURCE_Link1_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link2_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link3_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link4_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link5_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link6_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link7_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

#### SOURCE_Link8_ROUTER_DATA

A network link to a routed device such as a cable connecting to a computer.

### Property Sets for Objects



### Quantity Sets



