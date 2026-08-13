---
title: "Fisker Ocean"
---

# Fisker Ocean

The Fisker Ocean was produced between 2022-2024, and came with three battery variants

- 73kWH  LFP
- 113kWh NMC
- 106kWh NMC

The typelabel on the battery specifies the capacity

![image](../images/fisker-ocean-01.png)

## Battery overview

![image](../images/fisker-ocean-02.png)

The front connectors has coolant ports, HV and LV connectors. On the back of the battery there is another HV connection.

![image](../images/fisker-ocean-03.png)

## Low voltage connector

The low voltage connector has three CAN channels. The following pins are required:

- KL30: Brown/Red wire (permanent 12V)
- KL15: Brown/Blue wire (246mA draw)
- GND: Black/White (chassis)
- CAN H: Blue wire → CANHB
- CAN L: Violet wire → CANLB

![battery pinout1 ](../images/fisker-ocean-04.jpeg)

![image](../images/fisker-ocean-05.png)

#### DTCs
Descriptions soon integrated to software directly

* U120088;ACANBusOffFlt - Bus off;0xd20088 
* U025582;ACANComFlt - Alive / Sequence Incorrect / Not Updated;0xc25582
* P11D829;AllCurrSensorInvalid - Signal Invalid;0x11d829
* P120516;BMSSupplyVolHighFlt - Circuit Voltage Above Threshold;0x120516
* P12051C;BMSSupplyVolLowFlt - Circuit Voltage Below Threshold;0x12051c
* P120D94;BMSUnExpectPowerDownFlt - Unexpected Power Down;0x120D94
* P124400;BMUCmce2E - No Sub Type Information;0x124400
* P121674;BalCircuitFlt - Actuator Slipping;0x121674
* P12044B;BalCircuitTemHighFlt - Over Temperature;0x12044b
* P120496;BalCircuitTemInvalidFlt - Component Internal Failure;0x120496
* P118964;BatteryToG0OpenOrSTGFlt - Signal Plausibility Failure;0x118964
* P118965;BatteryToGoOutOfRangeFlt - Signal Has Too Few Transitions / Events;0x118965
* P160291;CSUResetFlt - Parametric;0x160291
* P118722;CellTempDiffHighLevel1 - Signal Amplitude > Maximum;0x118722
* P160148;CellTempHighLevel1 - Supervision Software Failure;0x160148
* P160149;CellTempHighLevel2 - Internal Electronic Failure;0x160149
* P119321;CellTempLowLevel1 - Signal Amplitude < Minimum;0x119321
* P118522;CellUnbalanceFlt - Signal Amplitude > Maximum;0x118522
* P118822;CellVolHighLevel1 - Signal Amplitude > Maximum;0x118822
* P121C01;CellVolHighLevel2 - General Electrical Failure;0x121c01
* P160123;CellVolHighLevel4 - Signal Stuck Low;0x160123
* P160114;CellVolLowLowLevel1 - Circuit Short to Ground or Open;0x160114
* P160115;CellVolLowLowLevel2 - Circuit Short To Battery or Open;0x160115
* P118E21;CellVolLowLevel3 - Signal Amplitude < Minimum;0x118e21
* P126004;CellVolOverRange - System Internal Failure;0x126004
* P121229;CellVolSampleWireOpenFlt - Signal Invalid;0x121229
* P160131;ChrgCurHighLevel1 - No Signal;0x160131
* P160132;ChrgCurHighLevel2 - Signal Low Time < Minimum;0x160132
* P160133;ChrgCurHighLevel3 - Signal Low Time > Maximum;0x160133
* P160310;CurMeasureMessageCRCFlt - ISO/SAE Reserved;0x160310
* P160307;CurMeasureMessageLostFlt - Mechanical Failure;0x160307
* P160312;CurMesRCFlt - Circuit Short To Battery;0x160312
* P160128;DisChrgCurHighLevel1 - Signal Bias Level Out of Range / Zero Adjustment Failure;0x160128
* P160129;DisChrgCurHighLevel2 - Signal Invalid;0x160129
* P118111;DisChrgCurHighLevel3 - Circuit Short To Ground;0x118111
* P126031;ExtWDEr - No Signal;0x126031
* P160245;GOasDatumPointRefVoltOutOfRangeFlt - Program Memory Failure;0x160245
* P160243;GOasDatumPointSPIFlt - Special Memory Failure;0x160243
* P126010;GIasDatumPointRefVoltOutOfRangeFlt - ISO/SAE Reserved;0x126010
* P126009;GIasDatumPointSPIFlt - Component Failure;0x126009
* P0A0A94;HVILOpenFlt - Unexpected Operation;0xa0a094
* P123D12;HVILShortToGNDFlt - Circuit Short To Battery;0x123d12
* P123D11;HVILShortToVCCFlt - Circuit Short To Ground;0x123d11
* P123D13;HVILOpenFlt - Circuit Open;0x123d13
* P123D15;HVILShortToGNDFlt - Circuit Short To Battery or Open;0x123d15
* P123D15;Hvil2ShortToGNDFlt - Circuit Short To Battery or Open;0x123d15
* P123D14;HVIL2ShortToVCCFlt - Circuit Short To Ground or Open;0x123d14
* P12231A;HVPoAndHVNeglsoFlt - Circuit Resistance Below Threshold;0x12231a
* P160102;HVRelayCloseFlt1 - General Signal Failure;0x160102
* P0AA61A;HVRelayCloseFlt2 - Circuit Resistance Below Threshold;0x0xa61a
* P160103;HVRelayOpenFlt1 - FM (Frequency Modulated) / PWM (Pulse Width Modulated) Failure;0x160103
* P120A1A;HVRelayOpenFlt2 - Circuit Resistance Below Threshold;0x120a1a
* P160098;InletWaterTempSensorFlt - Component or System Over Temperature;0x160098
* P126030;IntWDError - ISO/SAE Reserved;0x126030
* P11D729;IsoDetectCircuFlt - Signal Invalid;0x11d729
* P126002;KL30VolOutOfRangetoHighFlt - General Signal Failure;0x126002
* P126001;KI30VolOutOfRangetoLowFlt - General Electrical Failure;0x126001
* P126033;PCALFlt - Signal Low Time > Maximum;0x126033
* P126025;McAUDCFlt - Signal Shape / Waveform Failure;0x126025
* P0AA572;MainRelayOpenFlt - Actuator Stuck Open;0xa572
* P0AA473;MainNegRelayWeldFlt - Actuator Stuck Closed;0xa473
* P160212;MainNegativeContactorCoilCircuitOpenFlt - Circuit Short To Battery;0x160212
* P160210;MainNegativeContactorCoilCircuitShortToGNDFault - ISO/SAE Reserved;0x160210
* P160211;MainNegativeContactorCoilCircuitShortToPowerFault - Circuit Short To Ground;0x160211
* P160168;MainPosOrPreChrgRelayWeldFlt - Event Information;0x160168
* P0AA272;MainPosRelayOpenFlt - Actuator Stuck Open;0xa0a272
* P160254;MainPosToG0OpenStGFlt - Missing Calibration;0x160254
* P160255;MainPosToG0OutOfRangeFlt - Not Configured;0x160255
* P160208;MainPositiveContactorCoilCircuitOpenFault - Bus Signal / Message Failure;0x160208
* P160206;MainPositiveContactorCoilCircuitShortToGNDFault - Algorithm Based Failure;0x160206
* P160207;MainPositiveContactorCoilCircuitShortToPowerFault - Mechanical Failure;0x160207
* P126024;McuHwSelfTestFlt - Signal Stuck High;0x126024
* P126039;MemoryInvalidFlt_Level1 - Signal Has Too Few Pulses;0x126039
* P126003;ModuleVolDiffHighFlt - FM (Frequency Modulated) / PWM (Pulse Width Modulated) Failure;0x126003
* P126023;NTCImPlusModerateFlt - Signal Stuck Low;0x126023
* P126029;NVRAMError - Signal Invalid;0x126029
* P0A9513;PackHighVolCircuitOpenFlt - Circuit Open;0xa9513
* P160036;PackSoCHigh - Signal Frequency Too Low;0x160036
* P160037;PackSoCLow - Signal Frequency Too High;0x160037
* P122184;PackSoCHLowLevel1 - Signal Below Allowable Range;0x122184
* P122284;PackSoCHLowLevel2 - Signal Below Allowable Range;0x122284
* P160164;PackVolHighLevel1 - Signal Plausibility Failure;0x160164
* P160166;PackVolLowLevel1 - Signal Has Too Many Transitions / Events;0x160166
* P160167;PackVolLowLevel2 - Signal Incorrect After Event;0x160167
* P122019;PreChrgCurHigh - Circuit Current Above Threshold;0x122019
* P0AE372;PreChrgRelayOpenFlt - Actuator Stuck Open;0xae372
* P122011;PreChrgShortCircuit - Circuit Short to Ground;0x122011
* P122001;PreChrgTimeout - General Electrical Failure;0x122001
* P160216;PreChrgContactoilCircuitOpenFault - Circuit Voltage Below Threshold;0x160216
* P160215;PreChrgContactoilCircuitShortTPowerFault - Circuit Short to Battery or Open;0x160215
* P160214;PreChrgContactoilCircuitShortToGNDFault - Circuit Short to Ground or Open;0x160214
* P122092;PreChrge_too_much_in_short_time - Performance or Incorrect Operation;0x122092
* P126011;PrimaryCurMeasureMessageCRCFlt - Circuit Short to Ground;0x126011
* P120987;PrimaryCurMeasureMessageLostFlt - Missing Message;0x120987
* P118966;PrimaryCurSensorFlt - Signal Has Too Many Transitions / Events;0x118966
* P160524;PrimaryCurSensorZeroDriftHighFlt - Signal Stuck High;0x160524
* P126012;PrimaryCurresRCFlt - Circuit Short To Battery;0x126012
* P126013;PrimaryCurOutOfRange - Circuit Open;0x126013
* P126015;PrimaryCurDeviFlt - Circuit Short to Battery or Open;0x126015
* P126027;RAMError - Signal Rate of Change Above Threshold;0x126027
* P160342;RTCChipAbnormalFlt - General Memory Failure;0x160342
* P160134;ReChrCurHighLevel1 - Signal High Time < Minimum;0x160134
* P160135;ReChrCurHighLevel2 - Signal High Time > Maximum;0x160135
* P160136;ReChrCurHighLevel3 - Signal Frequency Too Low;0x160136
* P126032;RegisterError - Signal Low Time < Minimum;0x126032
* P160013;RelaySupplyPowerVolHighFlt - Circuit Open;0x160013
* P160010;RelaySupplyPowerVolLowFlt - ISO/SAE Reserved;0x160010
* P126037;SBCPwrToExtFlt_Level1 - Signal Frequency Too High;0x126037
* P126038;SBCPwrToExtFlt_Level2 - Signal Frequency Incorrect;0x126038
* P126035;SBCPwrToIntFlt_Level1 - Signal High Time > Maximum;0x126035
* P126036;SBCPwrToIntFlt_Level2 - Signal Frequency Too Low;0x126036
* P126034;SBCSelfTestFlt - Signal High Time < Minimum;0x126034
* U120388;SCANBusOffFlt - Bus off;0x20388
* U120308;SCANComFlt - Bus Signal / Message Failure;0x20308
* P26022;SampleChipHardwareFlt - Signal Amplitude > Maximum;0x126022
* P160532;SecondaryCurSensorZeroDriftHighFlt - Signal Low Time < Minimum;0x160532
* P126014;SecondaryCurOutOfRange - Circuit Short To Ground or Open;0x126014
* P126019;TempSensorCriticalHighFlt - Circuit Current Above Threshold;0x126019
* P126020;TempSensorCriticalLowFlt - ISO/SAE Reserved;0x126020
* P21429;TempSensorMinorFlt - Signal Invalid;0x121429
* P126017;TempSensorOutofRangeHighFlt - Circuit Voltage Above Threshold;0x126017
* P126018;TempSensorOutofRangeLowFlt - Circuit Current Below Threshold;0x126018
* P21FA29;TempSensorSeriousFlt - Signal Invalid;0x12fa29
* P126000;TempSensorValueE2Flt - No Sub Type Information;0x126000
* P160344;TempSoftwareExpirationFlt - Data Memory Failure;0x160344
* P160343;TempSoftwareReminderOfDueDate - Special Memory Failure;0x160343
* P160363;ThermalRunawayDetectionCircuitOpnFlt - Circuit / Component Protection Time Out ;0x160363
* P126026;UnExpectRestFlt - Signal Rate of Change Below Threshold;0x126026
* P11D730;VCU_EccCoolantdefeat - ISO/SAE Reserved;0x11d730
* P160165;PackVolHighLevel2 - Signal Has Too Few Transitions;0x160165
* P126044;BMSCalbPSLowPowerParFit - Data Memory Failure;0x126044
* P160038;BMS_SystemError_OmissionOfKL15 - Signal Frequency Incorrect;0x160038
* P126043;BPSToBMSHardwareupFault - Special Memory Failure;0x126043
* P126045;BatteryPressureMessageLost - Program Memory Failure;0x126045
* P126042;BatteryPressureSensorFlt - General Memory Failure;0x126042
* P0A7E22;CellTempHighLevel3 - Signal Amplitude > Maximum;0xa7e22
* P160061;CrashFromHardwarePWMFlt - Signal Calculation Failure;0x160061
* P160062;CrashFromHardwarePWMSlightFlt - Signal Compare Failure;0x160062
* P160065;CrashPWMAbnormal - Signal Has Too Few Transitions / Events;0x160065
* P160066;CrashPWMAbnormal - Signal Has Too Many Transitions / Events;0x160066
* P160064;CrashPWMShortToGNDFlt - Signal Plausibility Failure;0x160064
* P160063;CrashPWMShortToVsorOpen - Circuit / Component Protection Time-Out;0x160063
* P123D16;HVIL3OpenFlt - Circuit Voltage Below Threshold;0x123d16
* P123D18;HVIL3ShortToGNDFlt - Circuit Current Below Threshold;0x123d18
* P123D17;HVIL3ShortToVCCFlt - Circuit Voltage Above Threshold;0x123d17
* P160228;MainNegCnctrAgeLevel1Flt - Signal Bias Level Out of Range / Zero Adjustment Failure;0x160228
* P160229;MainNegCnctrAgeLevel2Flt - Signal Invalid;0x160229
* P160169;MainNegRelayWeldFlt - ISO/SAE Reserved;0x160169
* P160226;MainPosCnctrAgeLevel1Flt - Signal Rate of Change Below Threshold;0x160226
* P160227;MainPosCnctrAgeLevel2Flt - Signal Rate of Change Above Threshold;0x160227
* P160173;MainPosOrMainNegRelayWeldFlt - Actuator Stuck Closed;0x160173
* P160099;OutletWaterTemSensorFlt - Exceeded Learning Limit;0x160099
* P125098;OverTempLvl4Flt - Component or System Over Temperature;0x125098
* P160230;PreChrgcCnctrAgeLevel1Flt - ISO/SAE Reserved;0x160230
* P160231;PreChrgcCnctrAgeLevel2Flt - No Signal;0x160231
* P126028;ROMError - Signal Bias Level Out of Range / Zero Adjustment Failure;0x126028
* P123A24;ThermalRunawayFlt - Signal Stuck High;0x123a24
* P120886;VCUComCheckFlt - Signal Invalid;0x120886
* P160290;PrimaryCurrSCECCDOUBLEFlt;0x160290
* P160522;PrimaryCurrSUECCDOUBLEFlt;0x160522
* P160509;PrimaryCurrStatusMessageLostFlt;0x160509
* P160519;PrimaryCurrSTemHighFit;0x160519
* P160521;PrimaryCurrSTemHighFit2;0x160521
* P160510;PrimaryCurrentSensorReportSupplyVoltageFlt;0x160510
* P160531;SecondaryCurrentSensorReportSupplyVoltageHighFlt;0x160531
* P160530;SecondaryCurrentSensorReportSupplyVoltageLowFlt;0x160530
* P11D732;SbCTCD_PVNegCnctrStuckCloseFlt - Signal Low Time < Minimum;0x11d732
* P11D733;SbCTCD_PVPosCnctrStuckCloseFlt - Signal Low Time > Maximum;0x11d733
* P11D731;SbCTCD_PVPosCnctrStuckOpenFlt - No Signal;0x11d731
* P160294;PVNegCnctrAgeLevel1Flt;0x160294
* P160295;PVNegCnctrAgeLevel2Flt;0x160295
* P160292;PVPosCnctrAgeLevel1Flt;0x160292
* P160293;PVPosCnctrAgeLevel2Flt;0x160293
* P125016;CellVoltLowLevel4;0x125016
* P160146;OCLevel2_Charge;0x160146
* P160142;OCLevel2_Discharge;0x160142
* U025583;VCUComFlt;0xc25583
* P160301;NTCImPlausMinorFlt;0x160301
* P160303;NTCImPlausSeriousFlt;0x160303

