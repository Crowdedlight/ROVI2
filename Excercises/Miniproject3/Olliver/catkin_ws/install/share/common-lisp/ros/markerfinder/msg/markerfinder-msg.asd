
(cl:in-package :asdf)

(defsystem "markerfinder-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MarkerPose" :depends-on ("_package_MarkerPose"))
    (:file "_package_MarkerPose" :depends-on ("_package"))
  ))