; Auto-generated. Do not edit!


(cl:in-package erp42mini_driver-msg)


;//! \htmlinclude erpminiCmdMsg.msg.html

(cl:defclass <erpminiCmdMsg> (roslisp-msg-protocol:ros-message)
  ((dir
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
   (encoder_reset
    :reader encoder_reset
    :initarg :encoder_reset
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass erpminiCmdMsg (<erpminiCmdMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <erpminiCmdMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'erpminiCmdMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erp42mini_driver-msg:<erpminiCmdMsg> is deprecated: use erp42mini_driver-msg:erpminiCmdMsg instead.")))

(cl:ensure-generic-function 'dir-val :lambda-list '(m))
(cl:defmethod dir-val ((m <erpminiCmdMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:dir-val is deprecated.  Use erp42mini_driver-msg:dir instead.")
  (dir m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <erpminiCmdMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:speed-val is deprecated.  Use erp42mini_driver-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'steer-val :lambda-list '(m))
(cl:defmethod steer-val ((m <erpminiCmdMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:steer-val is deprecated.  Use erp42mini_driver-msg:steer instead.")
  (steer m))

(cl:ensure-generic-function 'brake-val :lambda-list '(m))
(cl:defmethod brake-val ((m <erpminiCmdMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:brake-val is deprecated.  Use erp42mini_driver-msg:brake instead.")
  (brake m))

(cl:ensure-generic-function 'encoder_reset-val :lambda-list '(m))
(cl:defmethod encoder_reset-val ((m <erpminiCmdMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp42mini_driver-msg:encoder_reset-val is deprecated.  Use erp42mini_driver-msg:encoder_reset instead.")
  (encoder_reset m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <erpminiCmdMsg>) ostream)
  "Serializes a message object of type '<erpminiCmdMsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'dir) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'steer)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'brake)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'encoder_reset) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <erpminiCmdMsg>) istream)
  "Deserializes a message object of type '<erpminiCmdMsg>"
    (cl:setf (cl:slot-value msg 'dir) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steer) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'brake) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'encoder_reset) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<erpminiCmdMsg>)))
  "Returns string type for a message object of type '<erpminiCmdMsg>"
  "erp42mini_driver/erpminiCmdMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'erpminiCmdMsg)))
  "Returns string type for a message object of type 'erpminiCmdMsg"
  "erp42mini_driver/erpminiCmdMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<erpminiCmdMsg>)))
  "Returns md5sum for a message object of type '<erpminiCmdMsg>"
  "7cd932a7d18e4566ffe6515ef5ba19c0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'erpminiCmdMsg)))
  "Returns md5sum for a message object of type 'erpminiCmdMsg"
  "7cd932a7d18e4566ffe6515ef5ba19c0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<erpminiCmdMsg>)))
  "Returns full string definition for message of type '<erpminiCmdMsg>"
  (cl:format cl:nil "bool dir~%int16 speed~%int16 steer~%int16 brake~%bool encoder_reset~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'erpminiCmdMsg)))
  "Returns full string definition for message of type 'erpminiCmdMsg"
  (cl:format cl:nil "bool dir~%int16 speed~%int16 steer~%int16 brake~%bool encoder_reset~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <erpminiCmdMsg>))
  (cl:+ 0
     1
     2
     2
     2
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <erpminiCmdMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'erpminiCmdMsg
    (cl:cons ':dir (dir msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':steer (steer msg))
    (cl:cons ':brake (brake msg))
    (cl:cons ':encoder_reset (encoder_reset msg))
))
