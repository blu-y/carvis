;; Auto-generated. Do not edit!


(when (boundp 'erp42mini_driver::erpminiStatusMsg)
  (if (not (find-package "ERP42MINI_DRIVER"))
    (make-package "ERP42MINI_DRIVER"))
  (shadow 'erpminiStatusMsg (find-package "ERP42MINI_DRIVER")))
(unless (find-package "ERP42MINI_DRIVER::ERPMINISTATUSMSG")
  (make-package "ERP42MINI_DRIVER::ERPMINISTATUSMSG"))

(in-package "ROS")
;;//! \htmlinclude erpminiStatusMsg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass erp42mini_driver::erpminiStatusMsg
  :super ros::object
  :slots (_header _dir _speed _steer _brake _encoder _garmin_left_range _garmin_right_range ))

(defmethod erp42mini_driver::erpminiStatusMsg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:dir __dir) nil)
    ((:speed __speed) 0)
    ((:steer __steer) 0)
    ((:brake __brake) 0)
    ((:encoder __encoder) 0)
    ((:garmin_left_range __garmin_left_range) 0.0)
    ((:garmin_right_range __garmin_right_range) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _dir __dir)
   (setq _speed (round __speed))
   (setq _steer (round __steer))
   (setq _brake (round __brake))
   (setq _encoder (round __encoder))
   (setq _garmin_left_range (float __garmin_left_range))
   (setq _garmin_right_range (float __garmin_right_range))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:dir
   (&optional __dir)
   (if __dir (setq _dir __dir)) _dir)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:steer
   (&optional __steer)
   (if __steer (setq _steer __steer)) _steer)
  (:brake
   (&optional __brake)
   (if __brake (setq _brake __brake)) _brake)
  (:encoder
   (&optional __encoder)
   (if __encoder (setq _encoder __encoder)) _encoder)
  (:garmin_left_range
   (&optional __garmin_left_range)
   (if __garmin_left_range (setq _garmin_left_range __garmin_left_range)) _garmin_left_range)
  (:garmin_right_range
   (&optional __garmin_right_range)
   (if __garmin_right_range (setq _garmin_right_range __garmin_right_range)) _garmin_right_range)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _dir
    1
    ;; int8 _speed
    1
    ;; int16 _steer
    2
    ;; int16 _brake
    2
    ;; int32 _encoder
    4
    ;; float32 _garmin_left_range
    4
    ;; float32 _garmin_right_range
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _dir
       (if _dir (write-byte -1 s) (write-byte 0 s))
     ;; int8 _speed
       (write-byte _speed s)
     ;; int16 _steer
       (write-word _steer s)
     ;; int16 _brake
       (write-word _brake s)
     ;; int32 _encoder
       (write-long _encoder s)
     ;; float32 _garmin_left_range
       (sys::poke _garmin_left_range (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _garmin_right_range
       (sys::poke _garmin_right_range (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _dir
     (setq _dir (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _speed
     (setq _speed (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _speed 127) (setq _speed (- _speed 256)))
   ;; int16 _steer
     (setq _steer (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _brake
     (setq _brake (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int32 _encoder
     (setq _encoder (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _garmin_left_range
     (setq _garmin_left_range (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _garmin_right_range
     (setq _garmin_right_range (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get erp42mini_driver::erpminiStatusMsg :md5sum-) "70b456b10b901dac2ec24fcef9df6573")
(setf (get erp42mini_driver::erpminiStatusMsg :datatype-) "erp42mini_driver/erpminiStatusMsg")
(setf (get erp42mini_driver::erpminiStatusMsg :definition-)
      "Header header
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

")



(provide :erp42mini_driver/erpminiStatusMsg "70b456b10b901dac2ec24fcef9df6573")


