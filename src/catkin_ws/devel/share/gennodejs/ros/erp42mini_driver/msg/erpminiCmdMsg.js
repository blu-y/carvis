// Auto-generated. Do not edit!

// (in-package erp42mini_driver.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class erpminiCmdMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dir = null;
      this.speed = null;
      this.steer = null;
      this.brake = null;
      this.encoder_reset = null;
    }
    else {
      if (initObj.hasOwnProperty('dir')) {
        this.dir = initObj.dir
      }
      else {
        this.dir = false;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0;
      }
      if (initObj.hasOwnProperty('steer')) {
        this.steer = initObj.steer
      }
      else {
        this.steer = 0;
      }
      if (initObj.hasOwnProperty('brake')) {
        this.brake = initObj.brake
      }
      else {
        this.brake = 0;
      }
      if (initObj.hasOwnProperty('encoder_reset')) {
        this.encoder_reset = initObj.encoder_reset
      }
      else {
        this.encoder_reset = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type erpminiCmdMsg
    // Serialize message field [dir]
    bufferOffset = _serializer.bool(obj.dir, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.int16(obj.speed, buffer, bufferOffset);
    // Serialize message field [steer]
    bufferOffset = _serializer.int16(obj.steer, buffer, bufferOffset);
    // Serialize message field [brake]
    bufferOffset = _serializer.int16(obj.brake, buffer, bufferOffset);
    // Serialize message field [encoder_reset]
    bufferOffset = _serializer.bool(obj.encoder_reset, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type erpminiCmdMsg
    let len;
    let data = new erpminiCmdMsg(null);
    // Deserialize message field [dir]
    data.dir = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [steer]
    data.steer = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [brake]
    data.brake = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [encoder_reset]
    data.encoder_reset = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erp42mini_driver/erpminiCmdMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7cd932a7d18e4566ffe6515ef5ba19c0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool dir
    int16 speed
    int16 steer
    int16 brake
    bool encoder_reset
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new erpminiCmdMsg(null);
    if (msg.dir !== undefined) {
      resolved.dir = msg.dir;
    }
    else {
      resolved.dir = false
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0
    }

    if (msg.steer !== undefined) {
      resolved.steer = msg.steer;
    }
    else {
      resolved.steer = 0
    }

    if (msg.brake !== undefined) {
      resolved.brake = msg.brake;
    }
    else {
      resolved.brake = 0
    }

    if (msg.encoder_reset !== undefined) {
      resolved.encoder_reset = msg.encoder_reset;
    }
    else {
      resolved.encoder_reset = false
    }

    return resolved;
    }
};

module.exports = erpminiCmdMsg;
