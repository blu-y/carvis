
(cl:in-package :asdf)

(defsystem "erp_driver-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "erpCmdMsg" :depends-on ("_package_erpCmdMsg"))
    (:file "_package_erpCmdMsg" :depends-on ("_package"))
    (:file "erpStatusMsg" :depends-on ("_package_erpStatusMsg"))
    (:file "_package_erpStatusMsg" :depends-on ("_package"))
  ))