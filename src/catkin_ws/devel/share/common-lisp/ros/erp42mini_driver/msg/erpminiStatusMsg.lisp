; Auto-generated. Do not edit!


(cl:in-package erp42mini_driver-msg)


;//! \htmlinclude erpminiStatusMsg.msg.html

(cl:defclass <erpminiStatusMsg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (dir
    :reader dir
    :initarg :dir
    :type cl:boolean
    :initform cl:nil)
   (speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0)
   (steer
    :reader steer
    :initarg :steer
    :type cl:fixnum
    :initform 0)
   (brake
    :reader brake
    :initarg :brake
    :type cl:fixnum
    :initform 0)
   (encoder
    :reader encoder
    :initarg :encoder
    :type cl:integer
    :initform 0)
   (garmin_left_range
    :reader garmin_left_range
    :initarg :garmin_left_range
    :type cl:float
    :initform 0.0)
   (garmin_right_range
    :reader garmin_right_range
    :initarg :garmin_right_range
    :type cl:float
    :initform 0.0))
)

(cl:defclass erpminiStatusMsg (<erpminiStatusMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <erpminiStatusMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'erpminiStatusMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erp42mini_driver-msg:<erpminiStatusMsg> is deprecated: use erp42mini_driver-msg:erpminiStatusMsg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:header-val is deprecated.  Use erp42mini_driver-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'dir-val :lambda-list '(m))
(cl:defmethod dir-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:dir-val is deprecated.  Use erp42mini_driver-msg:dir instead.")
  (dir m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:speed-val is deprecated.  Use erp42mini_driver-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'steer-val :lambda-list '(m))
(cl:defmethod steer-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:steer-val is deprecated.  Use erp42mini_driver-msg:steer instead.")
  (steer m))

(cl:ensure-generic-function 'brake-val :lambda-list '(m))
(cl:defmethod brake-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:brake-val is deprecated.  Use erp42mini_driver-msg:brake instead.")
  (brake m))

(cl:ensure-generic-function 'encoder-val :lambda-list '(m))
(cl:defmethod encoder-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:encoder-val is deprecated.  Use erp42mini_driver-msg:encoder instead.")
  (encoder m))

(cl:ensure-generic-function 'garmin_left_range-val :lambda-list '(m))
(cl:defmethod garmin_left_range-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:garmin_left_range-val is deprecated.  Use erp42mini_driver-msg:garmin_left_range instead.")
  (garmin_left_range m))

(cl:ensure-generic-function 'garmin_right_range-val :lambda-list '(m))
(cl:defmethod garmin_right_range-val ((m <erpminiStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:garmin_right_range-val is deprecated.  Use erp42mini_driver-msg:garmin_right_range instead.")
  (garmin_right_range m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <erpminiStatusMsg>) ostream)
  "Serializes a message object of type '<erpminiStatusMsg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'dir) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'steer)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'brake)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'encoder)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'garmin_left_range))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'garmin_right_range))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <erpminiStatusMsg>) istream)
  "Deserializes a message object of type '<erpminiStatusMsg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:slot-value msg 'dir) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steer) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'brake) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'encoder) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'garmin_left_range) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'garmin_right_range) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<erpminiStatusMsg>)))
  "Returns string type for a message object of type '<erpminiStatusMsg>"
  "erp42mini_driver/erpminiStatusMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'erpminiStatusMsg)))
  "Returns string type for a message object of type 'erpminiStatusMsg"
  "erp42mini_driver/erpminiStatusMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<erpminiStatusMsg>)))
  "Returns md5sum for a message object of type '<erpminiStatusMsg>"
  "70b456b10b901dac2ec24fcef9df6573")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'erpminiStatusMsg)))
  "Returns md5sum for a message object of type 'erpminiStatusMsg"
  "70b456b10b901dac2ec24fcef9df6573")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<erpminiStatusMsg>)))
  "Returns full string definition for message of type '<erpminiStatusMsg>"
  (cl:format cl:nil "Header header~%bool dir~%int8 speed~%int16 steer~%int16 brake~%int32 encoder~%float32 garmin_left_range~%float32 garmin_right_range~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'erpminiStatusMsg)))
  "Returns full string definition for message of type 'erpminiStatusMsg"
  (cl:format cl:nil "Header header~%bool dir~%int8 speed~%int16 steer~%int16 brake~%int32 encoder~%float32 garmin_left_range~%float32 garmin_right_range~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <erpminiStatusMsg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     2
     2
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <erpminiStatusMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'erpminiStatusMsg
    (cl:cons ':header (header msg))
    (cl:cons ':dir (dir msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':steer (steer msg))
    (cl:cons ':brake (brake msg))
    (cl:cons ':encoder (encoder msg))
    (cl:cons ':garmin_left_range (garmin_left_range msg))
    (cl:cons ':garmin_right_range (garmin_right_range msg))
))
