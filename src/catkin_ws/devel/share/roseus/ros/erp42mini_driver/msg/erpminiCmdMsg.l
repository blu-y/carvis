;; Auto-generated. Do not edit!


(when (boundp 'erp42mini_driver::erpminiCmdMsg)
  (if (not (find-package "ERP42MINI_DRIVER"))
    (make-package "ERP42MINI_DRIVER"))
  (shadow 'erpminiCmdMsg (find-package "ERP42MINI_DRIVER")))
(unless (find-package "ERP42MINI_DRIVER::ERPMINICMDMSG")
  (make-package "ERP42MINI_DRIVER::ERPMINICMDMSG"))

(in-package "ROS")
;;//! \htmlinclude erpminiCmdMsg.msg.html


(defclass erp42mini_driver::erpminiCmdMsg
  :super ros::object
  :slots (_dir _speed _steer _brake _encoder_reset ))

(defmethod erp42mini_driver::erpminiCmdMsg
  (:init
   (&key
    ((:dir __dir) nil)
    ((:speed __speed) 0)
    ((:steer __steer) 0)
    ((:brake __brake) 0)
    ((:encoder_reset __encoder_reset) nil)
    )
   (send-super :init)
   (setq _dir __dir)
   (setq _speed (round __speed))
   (setq _steer (round __steer))
   (setq _brake (round __brake))
   (setq _encoder_reset __encoder_reset)
   self)
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
  (:encoder_reset
   (&optional __encoder_reset)
   (if __encoder_reset (setq _encoder_reset __encoder_reset)) _encoder_reset)
  (:serialization-length
   ()
   (+
    ;; bool _dir
    1
    ;; int16 _speed
    2
    ;; int16 _steer
    2
    ;; int16 _brake
    2
    ;; bool _encoder_reset
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _dir
       (if _dir (write-byte -1 s) (write-byte 0 s))
     ;; int16 _speed
       (write-word _speed s)
     ;; int16 _steer
       (write-word _steer s)
     ;; int16 _brake
       (write-word _brake s)
     ;; bool _encoder_reset
       (if _encoder_reset (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _dir
     (setq _dir (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16 _speed
     (setq _speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _steer
     (setq _steer (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _brake
     (setq _brake (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _encoder_reset
     (setq _encoder_reset (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get erp42mini_driver::erpminiCmdMsg :md5sum-) "7cd932a7d18e4566ffe6515ef5ba19c0")
(setf (get erp42mini_driver::erpminiCmdMsg :datatype-) "erp42mini_driver/erpminiCmdMsg")
(setf (get erp42mini_driver::erpminiCmdMsg :definition-)
      "bool dir
int16 speed
int16 steer
int16 brake
bool encoder_reset
")



(provide :erp42mini_driver/erpminiCmdMsg "7cd932a7d18e4566ffe6515ef5ba19c0")


