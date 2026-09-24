# IfcAudioVisualAppliance

An audio-visual appliance is a device that displays, captures, transmits, or receives audio or video.
<!-- end of short definition -->

Audio-visual appliances may be fixed in place or may be able to be moved from one space to another. They may require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source. Audio-visual appliances may be connected to data circuits including specialist circuits for audio visual purposes only.

> HISTORY New entity in IFC4

>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAudioVisualApplianceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no audio visual appliance type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAudioVisualApplianceType_.

## Concepts

### Aggregation



#### MaycontainIfcAudioVisualAppliancecomponents_IfcAudioVisualAppliance

May contain IfcAudioVisualAppliance components.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Power_AMPLIFIER_ELECTRICAL

Receives electrical power.

#### SINK_Input_AMPLIFIER_AUDIOVISUAL

Input audio.

#### SOURCE_Speakers_AMPLIFIER_ELECTROACCOUSTIC

Audio speaker(s), which may be aggregated for separate speaker channels.

#### SINK_Power_CAMERA_ELECTRICAL

Receives electrical power.

#### SINK_Control_CAMERA_CONTROL

Receives control signal.

#### SOURCE_Network_CAMERA_DATA

Network access.

#### SOURCE_Output_CAMERA_AUDIOVISUAL

Captured video.

#### SINK_Power_DISPLAY_ELECTRICAL

Receives electrical power.

#### SINK_Control_DISPLAY_CONTROL

Receives control signal.

#### SINK_Input1_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input2_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input3_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input4_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input5_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input6_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input7_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Input8_DISPLAY_AUDIOVISUAL

Input audio/video source.

#### SINK_Power_MICROPHONE_ELECTRICAL

Receives electrical power.

#### SOURCE_Output_MICROPHONE_AUDIOVISUAL

Captured audio.

#### SINK_Power_PLAYER_ELECTRICAL

Receives electrical power.

#### SINK_Control_PLAYER_CONTROL

Receives control signal.

#### SOURCE_Output_PLAYER_AUDIOVISUAL

Rendered media content.

#### SINK_Power_PROJECTOR_ELECTRICAL

Receives electrical power.

#### SINK_Control_PROJECTOR_CONTROL

Receives control signal.

#### SINK_Output_PROJECTOR_AUDIOVISUAL

Input audio/video source.

#### SINK_Power_RECEIVER_ELECTRICAL

Receives electrical power.

#### SINK_Control_RECEIVER_CONTROL

Receives control signal.

#### SOURCE_Network_RECEIVER_DATA

Network access.

#### SINK_Input1_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input2_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input3_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input4_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input5_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input6_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input7_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input8_RECEIVER_AUDIOVISUAL

Input audio/video source.

#### SOURCE_Output1_RECEIVER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output2_RECEIVER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Speakers1_RECEIVER_ELECTROACCOUSTIC

Audio speaker(s), which may be aggregated for separate speaker channels.

#### SOURCE_Speakers2_RECEIVER_ELECTROACCOUSTIC

Audio speaker(s), which may be aggregated for separate speaker channels.

#### SINK_Input_SPEAKER_ELECTROACCOUSTIC

Amplified audio input.

#### SINK_Power_SWITCHER_ELECTRICAL

Receives electrical power.

#### SINK_Control_SWITCHER_CONTROL

Receives control signal.

#### SOURCE_Network_SWITCHER_DATA

Network access.

#### SINK_Input1_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input2_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input3_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input4_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input5_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input6_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input7_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SINK_Input8_SWITCHER_AUDIOVISUAL

Input audio/video source.

#### SOURCE_Output1_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output2_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output3_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output4_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output5_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output6_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output7_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SOURCE_Output8_SWITCHER_AUDIOVISUAL

Output audio/video zone.

#### SINK_Power_TELEPHONE_ELECTRICAL

Receives electrical power.

#### SINK_Phone_TELEPHONE_TELEPHONE

Telecommunications network.

#### SINK_Power_TUNER_ELECTRICAL

Receives electrical power.

#### SINK_Control_TUNER_CONTROL

Receives control signal.

#### SINK_Input_TUNER_TV

Receives modulated data feed such as satellite, cable, or over-the-air.

#### SOURCE_Output_TUNER_AUDIOVISUAL

Rendered media content.

### Property Sets for Objects



### Quantity Sets



