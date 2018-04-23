; Auto-generated. Do not edit!


(cl:in-package move_drone_relative-srv)


;//! \htmlinclude Yaw-request.msg.html

(cl:defclass <Yaw-request> (roslisp-msg-protocol:ros-message)
  ((yaw
    :reader yaw
    :initarg :yaw
    :type cl:integer
    :initform 0))
)

(cl:defclass Yaw-request (<Yaw-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Yaw-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Yaw-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name move_drone_relative-srv:<Yaw-request> is deprecated: use move_drone_relative-srv:Yaw-request instead.")))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <Yaw-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_drone_relative-srv:yaw-val is deprecated.  Use move_drone_relative-srv:yaw instead.")
  (yaw m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Yaw-request>) ostream)
  "Serializes a message object of type '<Yaw-request>"
  (cl:let* ((signed (cl:slot-value msg 'yaw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Yaw-request>) istream)
  "Deserializes a message object of type '<Yaw-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yaw) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Yaw-request>)))
  "Returns string type for a service object of type '<Yaw-request>"
  "move_drone_relative/YawRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Yaw-request)))
  "Returns string type for a service object of type 'Yaw-request"
  "move_drone_relative/YawRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Yaw-request>)))
  "Returns md5sum for a message object of type '<Yaw-request>"
  "5716b384c1467b02f1781ea35048d5a3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Yaw-request)))
  "Returns md5sum for a message object of type 'Yaw-request"
  "5716b384c1467b02f1781ea35048d5a3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Yaw-request>)))
  "Returns full string definition for message of type '<Yaw-request>"
  (cl:format cl:nil "int64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Yaw-request)))
  "Returns full string definition for message of type 'Yaw-request"
  (cl:format cl:nil "int64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Yaw-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Yaw-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Yaw-request
    (cl:cons ':yaw (yaw msg))
))
;//! \htmlinclude Yaw-response.msg.html

(cl:defclass <Yaw-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Yaw-response (<Yaw-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Yaw-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Yaw-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name move_drone_relative-srv:<Yaw-response> is deprecated: use move_drone_relative-srv:Yaw-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <Yaw-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_drone_relative-srv:success-val is deprecated.  Use move_drone_relative-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Yaw-response>) ostream)
  "Serializes a message object of type '<Yaw-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Yaw-response>) istream)
  "Deserializes a message object of type '<Yaw-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Yaw-response>)))
  "Returns string type for a service object of type '<Yaw-response>"
  "move_drone_relative/YawResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Yaw-response)))
  "Returns string type for a service object of type 'Yaw-response"
  "move_drone_relative/YawResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Yaw-response>)))
  "Returns md5sum for a message object of type '<Yaw-response>"
  "5716b384c1467b02f1781ea35048d5a3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Yaw-response)))
  "Returns md5sum for a message object of type 'Yaw-response"
  "5716b384c1467b02f1781ea35048d5a3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Yaw-response>)))
  "Returns full string definition for message of type '<Yaw-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Yaw-response)))
  "Returns full string definition for message of type 'Yaw-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Yaw-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Yaw-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Yaw-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Yaw)))
  'Yaw-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Yaw)))
  'Yaw-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Yaw)))
  "Returns string type for a service object of type '<Yaw>"
  "move_drone_relative/Yaw")