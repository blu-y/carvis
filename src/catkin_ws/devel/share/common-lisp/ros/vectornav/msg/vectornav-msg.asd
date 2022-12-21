
(cl:in-package :asdf)

(defsystem "vectornav-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Ins" :depends-on ("_package_Ins"))
    (:file "_package_Ins" :depends-on ("_package"))
  ))