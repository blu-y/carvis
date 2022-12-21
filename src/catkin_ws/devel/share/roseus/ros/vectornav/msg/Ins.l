;; Auto-generated. Do not edit!


(when (boundp 'vectornav::Ins)
  (if (not (find-package "VECTORNAV"))
    (make-package "VECTORNAV"))
  (shadow 'Ins (find-package "VECTORNAV")))
(unless (find-package "VECTORNAV::INS")
  (make-package "VECTORNAV::INS"))

(in-package "ROS")
;;//! \htmlinclude Ins.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass vectornav::Ins
  :super ros::object
  :slots (_header _time _week _utcTime _insStatus _yaw _pitch _roll _latitude _longitude _altitude _nedVelX _nedVelY _nedVelZ _attUncertainty _posUncertainty _velUncertainty ))

(defmethod vectornav::Ins
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:time __time) 0.0)
    ((:week __week) 0)
    ((:utcTime __utcTime) 0)
    ((:insStatus __insStatus) 0)
    ((:yaw __yaw) 0.0)
    ((:pitch __pitch) 0.0)
    ((:roll __roll) 0.0)
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    ((:altitude __altitude) 0.0)
    ((:nedVelX __nedVelX) 0.0)
    ((:nedVelY __nedVelY) 0.0)
    ((:nedVelZ __nedVelZ) 0.0)
    ((:attUncertainty __attUncertainty) (make-array 3 :initial-element 0.0 :element-type :float))
    ((:posUncertainty __posUncertainty) 0.0)
    ((:velUncertainty __velUncertainty) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _time (float __time))
   (setq _week (round __week))
   (setq _utcTime (round __utcTime))
   (setq _insStatus (round __insStatus))
   (setq _yaw (float __yaw))
   (setq _pitch (float __pitch))
   (setq _roll (float __roll))
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   (setq _altitude (float __altitude))
   (setq _nedVelX (float __nedVelX))
   (setq _nedVelY (float __nedVelY))
   (setq _nedVelZ (float __nedVelZ))
   (setq _attUncertainty __attUncertainty)
   (setq _posUncertainty (float __posUncertainty))
   (setq _velUncertainty (float __velUncertainty))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:week
   (&optional __week)
   (if __week (setq _week __week)) _week)
  (:utcTime
   (&optional __utcTime)
   (if __utcTime (setq _utcTime __utcTime)) _utcTime)
  (:insStatus
   (&optional __insStatus)
   (if __insStatus (setq _insStatus __insStatus)) _insStatus)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:nedVelX
   (&optional __nedVelX)
   (if __nedVelX (setq _nedVelX __nedVelX)) _nedVelX)
  (:nedVelY
   (&optional __nedVelY)
   (if __nedVelY (setq _nedVelY __nedVelY)) _nedVelY)
  (:nedVelZ
   (&optional __nedVelZ)
   (if __nedVelZ (setq _nedVelZ __nedVelZ)) _nedVelZ)
  (:attUncertainty
   (&optional __attUncertainty)
   (if __attUncertainty (setq _attUncertainty __attUncertainty)) _attUncertainty)
  (:posUncertainty
   (&optional __posUncertainty)
   (if __posUncertainty (setq _posUncertainty __posUncertainty)) _posUncertainty)
  (:velUncertainty
   (&optional __velUncertainty)
   (if __velUncertainty (setq _velUncertainty __velUncertainty)) _velUncertainty)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _time
    8
    ;; uint16 _week
    2
    ;; uint64 _utcTime
    8
    ;; uint16 _insStatus
    2
    ;; float32 _yaw
    4
    ;; float32 _pitch
    4
    ;; float32 _roll
    4
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ;; float64 _altitude
    8
    ;; float32 _nedVelX
    4
    ;; float32 _nedVelY
    4
    ;; float32 _nedVelZ
    4
    ;; float32[3] _attUncertainty
    (* 4    3)
    ;; float32 _posUncertainty
    4
    ;; float32 _velUncertainty
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint16 _week
       (write-word _week s)
     ;; uint64 _utcTime
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _utcTime (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _utcTime) (= (length (_utcTime . bv)) 2)) ;; bignum
              (write-long (ash (elt (_utcTime . bv) 0) 0) s)
              (write-long (ash (elt (_utcTime . bv) 1) -1) s))
             ((and (class _utcTime) (= (length (_utcTime . bv)) 1)) ;; big1
              (write-long (elt (_utcTime . bv) 0) s)
              (write-long (if (>= _utcTime 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _utcTime s)(write-long (if (>= _utcTime 0) 0 #xffffffff) s)))
     ;; uint16 _insStatus
       (write-word _insStatus s)
     ;; float32 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float32 _nedVelX
       (sys::poke _nedVelX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _nedVelY
       (sys::poke _nedVelY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _nedVelZ
       (sys::poke _nedVelZ (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32[3] _attUncertainty
     (dotimes (i 3)
       (sys::poke (elt _attUncertainty i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _posUncertainty
       (sys::poke _posUncertainty (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _velUncertainty
       (sys::poke _velUncertainty (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint16 _week
     (setq _week (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint64 _utcTime
     
#+(or :alpha :irix6 :x86_64)
      (setf _utcTime (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _utcTime (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; uint16 _insStatus
     (setq _insStatus (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _yaw
     (setq _yaw (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pitch
     (setq _pitch (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _roll
     (setq _roll (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float32 _nedVelX
     (setq _nedVelX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _nedVelY
     (setq _nedVelY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _nedVelZ
     (setq _nedVelZ (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32[3] _attUncertainty
   (dotimes (i (length _attUncertainty))
     (setf (elt _attUncertainty i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32 _posUncertainty
     (setq _posUncertainty (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _velUncertainty
     (setq _velUncertainty (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get vectornav::Ins :md5sum-) "f15f75d40252c44bbfc42358abc151e2")
(setf (get vectornav::Ins :datatype-) "vectornav/Ins")
(setf (get vectornav::Ins :definition-)
      "Header header

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

")



(provide :vectornav/Ins "f15f75d40252c44bbfc42358abc151e2")


