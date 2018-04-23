
(cl:in-package :asdf)

(defsystem "move_drone_relative-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveDrone" :depends-on ("_package_MoveDrone"))
    (:file "_package_MoveDrone" :depends-on ("_package"))
  ))