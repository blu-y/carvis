
"use strict";

let GpgsvSatellite = require('./GpgsvSatellite.js');
let Gpgst = require('./Gpgst.js');
let Gpgga = require('./Gpgga.js');
let Gpgsv = require('./Gpgsv.js');
let Sentence = require('./Sentence.js');
let Gprmc = require('./Gprmc.js');
let Gpgsa = require('./Gpgsa.js');

module.exports = {
  GpgsvSatellite: GpgsvSatellite,
  Gpgst: Gpgst,
  Gpgga: Gpgga,
  Gpgsv: Gpgsv,
  Sentence: Sentence,
  Gprmc: Gprmc,
  Gpgsa: Gpgsa,
};
