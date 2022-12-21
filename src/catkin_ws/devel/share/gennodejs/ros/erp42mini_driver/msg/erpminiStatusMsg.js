// Auto-generated. Do not edit!

// (in-package erp42mini_driver.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class erpminiStatusMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.dir = null;
      this.speed = null;
      this.steer = null;
      this.brake = null;
      this.encoder = null;
      this.garmin_left_range = null;
      this.garmin_right_range = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
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
      if (initObj.hasOwnProperty('encoder')) {
        this.encoder = initObj.encoder
      }
      else {
        this.encoder = 0;
      }
      if (initObj.hasOwnProperty('garmin_left_range')) {
        this.garmin_left_range = initObj.garmin_left_range
      }
      else {
        this.garmin_left_range = 0.0;
      }
      if (initObj.hasOwnProperty('garmin_right_range')) {
        this.garmin_right_range = initObj.garmin_right_range
      }
      else {
        this.garmin_right_range = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type erpminiStatusMsg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [dir]
    bufferOffset = _serializer.bool(obj.dir, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.int8(obj.speed, buffer, bufferOffset);
    // Serialize message field [steer]
    bufferOffset = _serializer.int16(obj.steer, buffer, bufferOffset);
    // Serialize message field [brake]
    bufferOffset = _serializer.int16(obj.brake, buffer, bufferOffset);
    // Serialize message field [encoder]
    bufferOffset = _serializer.int32(obj.encoder, buffer, bufferOffset);
    // Serialize message field [garmin_left_range]
    bufferOffset = _serializer.float32(obj.garmin_left_range, buffer, bufferOffset);
    // Serialize message field [garmin_right_range]
    bufferOffset = _serializer.float32(obj.garmin_right_range, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type erpminiStatusMsg
    let len;
    let data = new erpminiStatusMsg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [dir]
    data.dir = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [steer]
    data.steer = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [brake]
    data.brake = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [encoder]
    data.encoder = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [garmin_left_range]
    data.garmin_left_range = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [garmin_right_range]
    data.garmin_right_range = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'erp42mini_driver/erpminiStatusMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '70b456b10b901dac2ec24fcef9df6573';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    bool dir
    int8 speed
    int16 steer
    int16 brake
    int32 encoder
    float32 garmin_left_range
    float32 garmin_right_range
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new erpminiStatusMsg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

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

    if (msg.encoder !== undefined) {
      resolved.encoder = msg.encoder;
    }
    else {
      resolved.encoder = 0
    }

    if (msg.garmin_left_range !== undefined) {
      resolved.garmin_left_range = msg.garmin_left_range;
    }
    else {
      resolved.garmin_left_range = 0.0
    }

    if (msg.garmin_right_range !== undefined) {
      resolved.garmin_right_range = msg.garmin_right_range;
    }
    else {
      resolved.garmin_right_range = 0.0
    }

    return resolved;
    }
};

module.exports = erpminiStatusMsg;
