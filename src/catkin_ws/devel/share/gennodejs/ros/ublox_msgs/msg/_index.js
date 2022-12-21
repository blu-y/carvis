
"use strict";

let NavSOL = require('./NavSOL.js');
let NavVELECEF = require('./NavVELECEF.js');
let EsfMEAS = require('./EsfMEAS.js');
let NavATT = require('./NavATT.js');
let RxmRAWX = require('./RxmRAWX.js');
let RxmALM = require('./RxmALM.js');
let CfgDAT = require('./CfgDAT.js');
let MonVER = require('./MonVER.js');
let CfgINF = require('./CfgINF.js');
let CfgUSB = require('./CfgUSB.js');
let CfgNMEA6 = require('./CfgNMEA6.js');
let HnrPVT = require('./HnrPVT.js');
let EsfRAW = require('./EsfRAW.js');
let RxmSFRB = require('./RxmSFRB.js');
let AidALM = require('./AidALM.js');
let RxmEPH = require('./RxmEPH.js');
let CfgDGNSS = require('./CfgDGNSS.js');
let RxmRTCM = require('./RxmRTCM.js');
let CfgCFG = require('./CfgCFG.js');
let NavVELNED = require('./NavVELNED.js');
let NavPVT = require('./NavPVT.js');
let NavDGPS_SV = require('./NavDGPS_SV.js');
let CfgSBAS = require('./CfgSBAS.js');
let UpdSOS = require('./UpdSOS.js');
let Ack = require('./Ack.js');
let NavRELPOSNED = require('./NavRELPOSNED.js');
let NavSTATUS = require('./NavSTATUS.js');
let CfgNAV5 = require('./CfgNAV5.js');
let NavPOSECEF = require('./NavPOSECEF.js');
let MonHW6 = require('./MonHW6.js');
let EsfSTATUS = require('./EsfSTATUS.js');
let CfgGNSS = require('./CfgGNSS.js');
let CfgNMEA7 = require('./CfgNMEA7.js');
let NavCLOCK = require('./NavCLOCK.js');
let EsfRAW_Block = require('./EsfRAW_Block.js');
let NavSVINFO_SV = require('./NavSVINFO_SV.js');
let RxmRAW = require('./RxmRAW.js');
let NavSVIN = require('./NavSVIN.js');
let MonGNSS = require('./MonGNSS.js');
let CfgNAVX5 = require('./CfgNAVX5.js');
let CfgRST = require('./CfgRST.js');
let AidHUI = require('./AidHUI.js');
let NavSVINFO = require('./NavSVINFO.js');
let NavSAT_SV = require('./NavSAT_SV.js');
let CfgANT = require('./CfgANT.js');
let EsfINS = require('./EsfINS.js');
let RxmSFRBX = require('./RxmSFRBX.js');
let CfgNMEA = require('./CfgNMEA.js');
let CfgINF_Block = require('./CfgINF_Block.js');
let CfgGNSS_Block = require('./CfgGNSS_Block.js');
let CfgTMODE3 = require('./CfgTMODE3.js');
let RxmRAW_SV = require('./RxmRAW_SV.js');
let CfgMSG = require('./CfgMSG.js');
let NavSAT = require('./NavSAT.js');
let EsfSTATUS_Sens = require('./EsfSTATUS_Sens.js');
let CfgPRT = require('./CfgPRT.js');
let UpdSOS_Ack = require('./UpdSOS_Ack.js');
let MonHW = require('./MonHW.js');
let NavSBAS = require('./NavSBAS.js');
let NavTIMEGPS = require('./NavTIMEGPS.js');
let RxmRAWX_Meas = require('./RxmRAWX_Meas.js');
let NavDOP = require('./NavDOP.js');
let CfgRATE = require('./CfgRATE.js');
let RxmSVSI = require('./RxmSVSI.js');
let NavPOSLLH = require('./NavPOSLLH.js');
let NavDGPS = require('./NavDGPS.js');
let NavPVT7 = require('./NavPVT7.js');
let MgaGAL = require('./MgaGAL.js');
let AidEPH = require('./AidEPH.js');
let CfgHNR = require('./CfgHNR.js');
let NavTIMEUTC = require('./NavTIMEUTC.js');
let TimTM2 = require('./TimTM2.js');
let MonVER_Extension = require('./MonVER_Extension.js');
let RxmSVSI_SV = require('./RxmSVSI_SV.js');
let NavSBAS_SV = require('./NavSBAS_SV.js');
let Inf = require('./Inf.js');

module.exports = {
  NavSOL: NavSOL,
  NavVELECEF: NavVELECEF,
  EsfMEAS: EsfMEAS,
  NavATT: NavATT,
  RxmRAWX: RxmRAWX,
  RxmALM: RxmALM,
  CfgDAT: CfgDAT,
  MonVER: MonVER,
  CfgINF: CfgINF,
  CfgUSB: CfgUSB,
  CfgNMEA6: CfgNMEA6,
  HnrPVT: HnrPVT,
  EsfRAW: EsfRAW,
  RxmSFRB: RxmSFRB,
  AidALM: AidALM,
  RxmEPH: RxmEPH,
  CfgDGNSS: CfgDGNSS,
  RxmRTCM: RxmRTCM,
  CfgCFG: CfgCFG,
  NavVELNED: NavVELNED,
  NavPVT: NavPVT,
  NavDGPS_SV: NavDGPS_SV,
  CfgSBAS: CfgSBAS,
  UpdSOS: UpdSOS,
  Ack: Ack,
  NavRELPOSNED: NavRELPOSNED,
  NavSTATUS: NavSTATUS,
  CfgNAV5: CfgNAV5,
  NavPOSECEF: NavPOSECEF,
  MonHW6: MonHW6,
  EsfSTATUS: EsfSTATUS,
  CfgGNSS: CfgGNSS,
  CfgNMEA7: CfgNMEA7,
  NavCLOCK: NavCLOCK,
  EsfRAW_Block: EsfRAW_Block,
  NavSVINFO_SV: NavSVINFO_SV,
  RxmRAW: RxmRAW,
  NavSVIN: NavSVIN,
  MonGNSS: MonGNSS,
  CfgNAVX5: CfgNAVX5,
  CfgRST: CfgRST,
  AidHUI: AidHUI,
  NavSVINFO: NavSVINFO,
  NavSAT_SV: NavSAT_SV,
  CfgANT: CfgANT,
  EsfINS: EsfINS,
  RxmSFRBX: RxmSFRBX,
  CfgNMEA: CfgNMEA,
  CfgINF_Block: CfgINF_Block,
  CfgGNSS_Block: CfgGNSS_Block,
  CfgTMODE3: CfgTMODE3,
  RxmRAW_SV: RxmRAW_SV,
  CfgMSG: CfgMSG,
  NavSAT: NavSAT,
  EsfSTATUS_Sens: EsfSTATUS_Sens,
  CfgPRT: CfgPRT,
  UpdSOS_Ack: UpdSOS_Ack,
  MonHW: MonHW,
  NavSBAS: NavSBAS,
  NavTIMEGPS: NavTIMEGPS,
  RxmRAWX_Meas: RxmRAWX_Meas,
  NavDOP: NavDOP,
  CfgRATE: CfgRATE,
  RxmSVSI: RxmSVSI,
  NavPOSLLH: NavPOSLLH,
  NavDGPS: NavDGPS,
  NavPVT7: NavPVT7,
  MgaGAL: MgaGAL,
  AidEPH: AidEPH,
  CfgHNR: CfgHNR,
  NavTIMEUTC: NavTIMEUTC,
  TimTM2: TimTM2,
  MonVER_Extension: MonVER_Extension,
  RxmSVSI_SV: RxmSVSI_SV,
  NavSBAS_SV: NavSBAS_SV,
  Inf: Inf,
};
