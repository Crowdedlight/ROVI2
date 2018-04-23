;; Auto-generated. Do not edit!


(when (boundp 'move_drone_relative::Yaw)
  (if (not (find-package "MOVE_DRONE_RELATIVE"))
    (make-package "MOVE_DRONE_RELATIVE"))
  (shadow 'Yaw (find-package "MOVE_DRONE_RELATIVE")))
(unless (find-package "MOVE_DRONE_RELATIVE::YAW")
  (make-package "MOVE_DRONE_RELATIVE::YAW"))
(unless (find-package "MOVE_DRONE_RELATIVE::YAWREQUEST")
  (make-package "MOVE_DRONE_RELATIVE::YAWREQUEST"))
(unless (find-package "MOVE_DRONE_RELATIVE::YAWRESPONSE")
  (make-package "MOVE_DRONE_RELATIVE::YAWRESPONSE"))

(in-package "ROS")





(defclass move_drone_relative::YawRequest
  :super ros::object
  :slots (_yaw ))

(defmethod move_drone_relative::YawRequest
  (:init
   (&key
    ((:yaw __yaw) 0)
    )
   (send-super :init)
   (setq _yaw (round __yaw))
   self)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:serialization-length
   ()
   (+
    ;; int64 _yaw
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _yaw
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _yaw (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _yaw) (= (length (_yaw . bv)) 2)) ;; bignum
              (write-long (ash (elt (_yaw . bv) 0) 0) s)
              (write-long (ash (elt (_yaw . bv) 1) -1) s))
             ((and (class _yaw) (= (length (_yaw . bv)) 1)) ;; big1
              (write-long (elt (_yaw . bv) 0) s)
              (write-long (if (>= _yaw 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _yaw s)(write-long (if (>= _yaw 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _yaw
#+(or :alpha :irix6 :x86_64)
      (setf _yaw (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _yaw (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass move_drone_relative::YawResponse
  :super ros::object
  :slots (_success ))

(defmethod move_drone_relative::YawResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass move_drone_relative::Yaw
  :super ros::object
  :slots ())

(setf (get move_drone_relative::Yaw :md5sum-) "5716b384c1467b02f1781ea35048d5a3")
(setf (get move_drone_relative::Yaw :datatype-) "move_drone_relative/Yaw")
(setf (get move_drone_relative::Yaw :request) move_drone_relative::YawRequest)
(setf (get move_drone_relative::Yaw :response) move_drone_relative::YawResponse)

(defmethod move_drone_relative::YawRequest
  (:response () (instance move_drone_relative::YawResponse :init)))

(setf (get move_drone_relative::YawRequest :md5sum-) "5716b384c1467b02f1781ea35048d5a3")
(setf (get move_drone_relative::YawRequest :datatype-) "move_drone_relative/YawRequest")
(setf (get move_drone_relative::YawRequest :definition-)
      "int64 yaw
---
bool success

")

(setf (get move_drone_relative::YawResponse :md5sum-) "5716b384c1467b02f1781ea35048d5a3")
(setf (get move_drone_relative::YawResponse :datatype-) "move_drone_relative/YawResponse")
(setf (get move_drone_relative::YawResponse :definition-)
      "int64 yaw
---
bool success

")



(provide :move_drone_relative/Yaw "5716b384c1467b02f1781ea35048d5a3")


