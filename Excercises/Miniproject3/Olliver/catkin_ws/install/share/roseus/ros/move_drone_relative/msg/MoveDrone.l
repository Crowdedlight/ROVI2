;; Auto-generated. Do not edit!


(when (boundp 'move_drone_relative::MoveDrone)
  (if (not (find-package "MOVE_DRONE_RELATIVE"))
    (make-package "MOVE_DRONE_RELATIVE"))
  (shadow 'MoveDrone (find-package "MOVE_DRONE_RELATIVE")))
(unless (find-package "MOVE_DRONE_RELATIVE::MOVEDRONE")
  (make-package "MOVE_DRONE_RELATIVE::MOVEDRONE"))

(in-package "ROS")
;;//! \htmlinclude MoveDrone.msg.html


(defclass move_drone_relative::MoveDrone
  :super ros::object
  :slots (_x _y _z _yaw ))

(defmethod move_drone_relative::MoveDrone
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:yaw __yaw) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _yaw (float __yaw))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _yaw
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get move_drone_relative::MoveDrone :md5sum-) "52d0ade995d52d04cae303675aa442a7")
(setf (get move_drone_relative::MoveDrone :datatype-) "move_drone_relative/MoveDrone")
(setf (get move_drone_relative::MoveDrone :definition-)
      "# This contains the position of a point in free space
float64 x
float64 y
float64 z
float64 yaw

")



(provide :move_drone_relative/MoveDrone "52d0ade995d52d04cae303675aa442a7")


