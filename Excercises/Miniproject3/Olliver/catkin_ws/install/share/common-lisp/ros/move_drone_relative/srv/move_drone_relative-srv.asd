
(cl:in-package :asdf)

(defsystem "move_drone_relative-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveDrone" :depends-on ("_package_MoveDrone"))
    (:file "_package_MoveDrone" :depends-on ("_package"))
    (:file "Yaw" :depends-on ("_package_Yaw"))
    (:file "_package_Yaw" :depends-on ("_package"))
  ))