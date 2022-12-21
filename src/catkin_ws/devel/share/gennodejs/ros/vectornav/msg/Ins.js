// Auto-generated. Do not edit!

// (in-package vectornav.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Ins {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.time = null;
      this.week = null;
      this.utcTime = null;
      this.insStatus = null;
      this.yaw = null;
      this.pitch = null;
      this.roll = null;
      this.latitude = null;
      this.longitude = null;
      this.altitude = null;
      this.nedVelX = null;
      this.nedVelY = null;
      this.nedVelZ = null;
      this.attUncertainty = null;
      this.posUncertainty = null;
      this.velUncertainty = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0.0;
      }
      if (initObj.hasOwnProperty('week')) {
        this.week = initObj.week
      }
      else {
        this.week = 0;
      }
      if (initObj.hasOwnProperty('utcTime')) {
        this.utcTime = initObj.utcTime
      }
      else {
        this.utcTime = 0;
      }
      if (initObj.hasOwnProperty('insStatus')) {
        this.insStatus = initObj.insStatus
      }
      else {
        this.insStatus = 0;
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = 0.0;
      }
      if (initObj.hasOwnProperty('pitch')) {
        this.pitch = initObj.pitch
      }
      else {
        this.pitch = 0.0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
      if (initObj.hasOwnProperty('latitude')) {
        this.latitude = initObj.latitude
      }
      else {
        this.latitude = 0.0;
      }
      if (initObj.hasOwnProperty('longitude')) {
        this.longitude = initObj.longitude
      }
      else {
        this.longitude = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
      }
      if (initObj.hasOwnProperty('nedVelX')) {
        this.nedVelX = initObj.nedVelX
      }
      else {
        this.nedVelX = 0.0;
      }
      if (initObj.hasOwnProperty('nedVelY')) {
        this.nedVelY = initObj.nedVelY
      }
      else {
        this.nedVelY = 0.0;
      }
      if (initObj.hasOwnProperty('nedVelZ')) {
        this.nedVelZ = initObj.nedVelZ
      }
      else {
        this.nedVelZ = 0.0;
      }
      if (initObj.hasOwnProperty('attUncertainty')) {
        this.attUncertainty = initObj.attUncertainty
      }
      else {
        this.attUncertainty = new Array(3).fill(0);
      }
      if (initObj.hasOwnProperty('posUncertainty')) {
        this.posUncertainty = initObj.posUncertainty
      }
      else {
        this.posUncertainty = 0.0;
      }
      if (initObj.hasOwnProperty('velUncertainty')) {
        this.velUncertainty = initObj.velUncertainty
      }
      else {
        this.velUncertainty = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Ins
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.float64(obj.time, buffer, bufferOffset);
    // Serialize message field [week]
    bufferOffset = _serializer.uint16(obj.week, buffer, bufferOffset);
    // Serialize message field [utcTime]
    bufferOffset = _serializer.uint64(obj.utcTime, buffer, bufferOffset);
    // Serialize message field [insStatus]
    bufferOffset = _serializer.uint16(obj.insStatus, buffer, bufferOffset);
    // Serialize message field [yaw]
    bufferOffset = _serializer.float32(obj.yaw, buffer, bufferOffset);
    // Serialize message field [pitch]
    bufferOffset = _serializer.float32(obj.pitch, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float32(obj.roll, buffer, bufferOffset);
    // Serialize message field [latitude]
    bufferOffset = _serializer.float64(obj.latitude, buffer, bufferOffset);
    // Serialize message field [longitude]
    bufferOffset = _serializer.float64(obj.longitude, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float64(obj.altitude, buffer, bufferOffset);
    // Serialize message field [nedVelX]
    bufferOffset = _serializer.float32(obj.nedVelX, buffer, bufferOffset);
    // Serialize message field [nedVelY]
    bufferOffset = _serializer.float32(obj.nedVelY, buffer, bufferOffset);
    // Serialize message field [nedVelZ]
    bufferOffset = _serializer.float32(obj.nedVelZ, buffer, bufferOffset);
    // Check that the constant length array field [attUncertainty] has the right length
    if (obj.attUncertainty.length !== 3) {
      throw new Error('Unable to serialize array field attUncertainty - length must be 3')
    }
    // Serialize message field [attUncertainty]
    bufferOffset = _arraySerializer.float32(obj.attUncertainty, buffer, bufferOffset, 3);
    // Serialize message field [posUncertainty]
    bufferOffset = _serializer.float32(obj.posUncertainty, buffer, bufferOffset);
    // Serialize message field [velUncertainty]
    bufferOffset = _serializer.float32(obj.velUncertainty, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Ins
    let len;
    let data = new Ins(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [week]
    data.week = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [utcTime]
    data.utcTime = _deserializer.uint64(buffer, bufferOffset);
    // Deserialize message field [insStatus]
    data.insStatus = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [yaw]
    data.yaw = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pitch]
    data.pitch = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [latitude]
    data.latitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [longitude]
    data.longitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [nedVelX]
    data.nedVelX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [nedVelY]
    data.nedVelY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [nedVelZ]
    data.nedVelZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [attUncertainty]
    data.attUncertainty = _arrayDeserializer.float32(buffer, bufferOffset, 3)
    // Deserialize message field [posUncertainty]
    data.posUncertainty = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [velUncertainty]
    data.velUncertainty = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 88;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vectornav/Ins';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f15f75d40252c44bbfc42358abc151e2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    float64 time	# GPS time of week in seconds
    uint16 week		# GPS week (week)
    uint64 utcTime	# The current UTC time. The year is given as a signed byte year offset from the year 2000. E.g. 2013 as 13.
                    # Fields:       year    month    day    hour    min    sec    ms
                    # Byte offset:  0       1        2      3       4      5      6|7
    
    # INS Status
    # Name		Bit Offset	Format	Description
    # Mode		0			2 bits	Indicates the current mode of the INS filter.
    #								0 = Not tracking. Insufficient dynamic motion to estimate attitude.
    #								1 = Sufficient dynamic motion, but solution not within performance specs.
    #								2 = INS is tracking and operating within specifications.
    # GpsFix	2			1 bit	Indicates whether the GPS has a proper fix
    # Error 	3			4 bits	Sensor measurement error code
    #								0 = No errors detected.
    # 								Name			Bit Offset	Format	Description
    #								Time Error		0			1 bit	High if INS filter loop exceeds 5 ms.
    #								IMU Error		1			1 bit	High if IMU communication error is detected.
    #								Mag/Pres Error	2			1 bit	High if Magnetometer or Pressure sensor error is detected.
    #								GPS Error		3			1 bit	High if GPS communication error is detected.
    #Reserved	7			9 bits	Reserved for future use.
    uint16 insStatus
    
    float32 yaw		# Yaw angle relative to true north. (degree)
    float32 pitch	# Yaw angle relative to true north (degree)
    float32 roll	# Pitch angle relative to horizon (degree)
    
    float64 latitude	# INS solution position in geodetic latitude (degree)
    float64 longitude	# INS solution position in geodetic longitude (degree)
    float64 altitude	# Height above ellipsoid. (WGS84) (meter)
    
    float32 nedVelX		# INS solution velocity in NED frame. (North) (m/s)
    float32 nedVelY		# INS solution velocity in NED frame. (East) (m/s)
    float32 nedVelZ		# INS solution velocity in NED frame. (Down) (m/s)
    
    float32[3] attUncertainty	# Uncertainty in attitude estimate (yaw, pitch and roll in degrees)
    float32 posUncertainty	# Uncertainty in position estimate (m)
    float32 velUncertainty	# Uncertainty in velocity estimate (m/s)
    
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
    const resolved = new Ins(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0.0
    }

    if (msg.week !== undefined) {
      resolved.week = msg.week;
    }
    else {
      resolved.week = 0
    }

    if (msg.utcTime !== undefined) {
      resolved.utcTime = msg.utcTime;
    }
    else {
      resolved.utcTime = 0
    }

    if (msg.insStatus !== undefined) {
      resolved.insStatus = msg.insStatus;
    }
    else {
      resolved.insStatus = 0
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = 0.0
    }

    if (msg.pitch !== undefined) {
      resolved.pitch = msg.pitch;
    }
    else {
      resolved.pitch = 0.0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    if (msg.latitude !== undefined) {
      resolved.latitude = msg.latitude;
    }
    else {
      resolved.latitude = 0.0
    }

    if (msg.longitude !== undefined) {
      resolved.longitude = msg.longitude;
    }
    else {
      resolved.longitude = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
    }

    if (msg.nedVelX !== undefined) {
      resolved.nedVelX = msg.nedVelX;
    }
    else {
      resolved.nedVelX = 0.0
    }

    if (msg.nedVelY !== undefined) {
      resolved.nedVelY = msg.nedVelY;
    }
    else {
      resolved.nedVelY = 0.0
    }

    if (msg.nedVelZ !== undefined) {
      resolved.nedVelZ = msg.nedVelZ;
    }
    else {
      resolved.nedVelZ = 0.0
    }

    if (msg.attUncertainty !== undefined) {
      resolved.attUncertainty = msg.attUncertainty;
    }
    else {
      resolved.attUncertainty = new Array(3).fill(0)
    }

    if (msg.posUncertainty !== undefined) {
      resolved.posUncertainty = msg.posUncertainty;
    }
    else {
      resolved.posUncertainty = 0.0
    }

    if (msg.velUncertainty !== undefined) {
      resolved.velUncertainty = msg.velUncertainty;
    }
    else {
      resolved.velUncertainty = 0.0
    }

    return resolved;
    }
};

module.exports = Ins;
