;; Auto-generated. Do not edit!


(when (boundp 'erp_driver::erpCmdMsg)
  (if (not (find-package "ERP_DRIVER"))
    (make-package "ERP_DRIVER"))
  (shadow 'erpCmdMsg (find-package "ERP_DRIVER")))
(unless (find-package "ERP_DRIVER::ERPCMDMSG")
  (make-package "ERP_DRIVER::ERPCMDMSG"))

(in-package "ROS")
;;//! \htmlinclude erpCmdMsg.msg.html


(defclass erp_driver::erpCmdMsg
  :super ros::object
  :slots (_e_stop _gear _speed _steer _brake ))

(defmethod erp_driver::erpCmdMsg
  (:init
   (&key
    ((:e_stop __e_stop) nil)
    ((:gear __gear) 0)
    ((:speed __speed) 0)
    ((:steer __steer) 0)
    ((:brake __brake) 0)
    )
   (send-super :init)
   (setq _e_stop __e_stop)
   (setq _gear (round __gear))
   (setq _speed (round __speed))
   (setq _steer (round __steer))
   (setq _brake (round __brake))
   self)
  (:e_stop
   (&optional __e_stop)
   (if __e_stop (setq _e_stop __e_stop)) _e_stop)
  (:gear
   (&optional __gear)
   (if __gear (setq _gear __gear)) _gear)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:steer
   (&optional __steer)
   (if __steer (setq _steer __steer)) _steer)
  (:brake
   (&optional __brake)
   (if __brake (setq _brake __brake)) _brake)
  (:serialization-length
   ()
   (+
    ;; bool _e_stop
    1
    ;; uint8 _gear
    1
    ;; uint8 _speed
    1
    ;; int32 _steer
    4
    ;; uint8 _brake
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _e_stop
       (if _e_stop (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _gear
       (write-byte _gear s)
     ;; uint8 _speed
       (write-byte _speed s)
     ;; int32 _steer
       (write-long _steer s)
     ;; uint8 _brake
       (write-byte _brake s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _e_stop
     (setq _e_stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _gear
     (setq _gear (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _speed
     (setq _speed (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int32 _steer
     (setq _steer (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _brake
     (setq _brake (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get erp_driver::erpCmdMsg :md5sum-) "6c8d779558341c7cf957ab6058219fbb")
(setf (get erp_driver::erpCmdMsg :datatype-) "erp_driver/erpCmdMsg")
(setf (get erp_driver::erpCmdMsg :definition-)
      "bool e_stop
uint8 gear
uint8 speed
int32 steer
uint8 brake
")



(provide :erp_driver/erpCmdMsg "6c8d779558341c7cf957ab6058219fbb")


