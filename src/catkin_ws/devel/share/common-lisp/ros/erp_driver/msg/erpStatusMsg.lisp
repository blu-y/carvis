; Auto-generated. Do not edit!


(cl:in-package erp_driver-msg)


;//! \htmlinclude erpStatusMsg.msg.html

(cl:defclass <erpStatusMsg> (roslisp-msg-protocol:ros-message)
  ((control_mode
    :reader control_mode
    :initarg :control_mode
    :type cl:fixnum
    :initform 0)
   (e_stop
    :reader e_stop
    :initarg :e_stop
    :type cl:boolean
    :initform cl:nil)
   (gear
    :reader gear
    :initarg :gear
    :type cl:fixnum
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0)
   (steer
    :reader steer
    :initarg :steer
    :type cl:integer
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
   (alive
    :reader alive
    :initarg :alive
    :type cl:fixnum
    :initform 0))
)

(cl:defclass erpStatusMsg (<erpStatusMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <erpStatusMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'erpStatusMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name erp_driver-msg:<erpStatusMsg> is deprecated: use erp_driver-msg:erpStatusMsg instead.")))

(cl:ensure-generic-function 'control_mode-val :lambda-list '(m))
(cl:defmethod control_mode-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:control_mode-val is deprecated.  Use erp_driver-msg:control_mode instead.")
  (control_mode m))

(cl:ensure-generic-function 'e_stop-val :lambda-list '(m))
(cl:defmethod e_stop-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:e_stop-val is deprecated.  Use erp_driver-msg:e_stop instead.")
  (e_stop m))

(cl:ensure-generic-function 'gear-val :lambda-list '(m))
(cl:defmethod gear-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:gear-val is deprecated.  Use erp_driver-msg:gear instead.")
  (gear m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:speed-val is deprecated.  Use erp_driver-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'steer-val :lambda-list '(m))
(cl:defmethod steer-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:steer-val is deprecated.  Use erp_driver-msg:steer instead.")
  (steer m))

(cl:ensure-generic-function 'brake-val :lambda-list '(m))
(cl:defmethod brake-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:brake-val is deprecated.  Use erp_driver-msg:brake instead.")
  (brake m))

(cl:ensure-generic-function 'encoder-val :lambda-list '(m))
(cl:defmethod encoder-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:encoder-val is deprecated.  Use erp_driver-msg:encoder instead.")
  (encoder m))

(cl:ensure-generic-function 'alive-val :lambda-list '(m))
(cl:defmethod alive-val ((m <erpStatusMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader erp_driver-msg:alive-val is deprecated.  Use erp_driver-msg:alive instead.")
  (alive m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <erpStatusMsg>) ostream)
  "Serializes a message object of type '<erpStatusMsg>"
  (cl:let* ((signed (cl:slot-value msg 'control_mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'e_stop) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gear)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'steer)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'encoder)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'alive)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <erpStatusMsg>) istream)
  "Deserializes a message object of type '<erpStatusMsg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'control_mode) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'e_stop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gear)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'steer) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brake)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'encoder) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'alive)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<erpStatusMsg>)))
  "Returns string type for a message object of type '<erpStatusMsg>"
  "erp_driver/erpStatusMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'erpStatusMsg)))
  "Returns string type for a message object of type 'erpStatusMsg"
  "erp_driver/erpStatusMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<erpStatusMsg>)))
  "Returns md5sum for a message object of type '<erpStatusMsg>"
  "c9878ccc909e763ca6b607c34a8914ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'erpStatusMsg)))
  "Returns md5sum for a message object of type 'erpStatusMsg"
  "c9878ccc909e763ca6b607c34a8914ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<erpStatusMsg>)))
  "Returns full string definition for message of type '<erpStatusMsg>"
  (cl:format cl:nil "int8 control_mode~%bool e_stop~%uint8 gear~%uint8 speed~%int32 steer~%uint8 brake~%int32 encoder~%uint8 alive~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'erpStatusMsg)))
  "Returns full string definition for message of type 'erpStatusMsg"
  (cl:format cl:nil "int8 control_mode~%bool e_stop~%uint8 gear~%uint8 speed~%int32 steer~%uint8 brake~%int32 encoder~%uint8 alive~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <erpStatusMsg>))
  (cl:+ 0
     1
     1
     1
     1
     4
     1
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <erpStatusMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'erpStatusMsg
    (cl:cons ':control_mode (control_mode msg))
    (cl:cons ':e_stop (e_stop msg))
    (cl:cons ':gear (gear msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':steer (steer msg))
    (cl:cons ':brake (brake msg))
    (cl:cons ':encoder (encoder msg))
    (cl:cons ':alive (alive msg))
))
