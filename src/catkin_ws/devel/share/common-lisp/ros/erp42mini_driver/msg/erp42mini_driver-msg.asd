
(cl:in-package :asdf)

(defsystem "erp42mini_driver-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "erpminiCmdMsg" :depends-on ("_package_erpminiCmdMsg"))
    (:file "_package_erpminiCmdMsg" :depends-on ("_package"))
    (:file "erpminiStatusMsg" :depends-on ("_package_erpminiStatusMsg"))
    (:file "_package_erpminiStatusMsg" :depends-on ("_package"))
  ))