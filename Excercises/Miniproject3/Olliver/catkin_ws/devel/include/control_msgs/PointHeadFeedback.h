// Generated by gencpp from file control_msgs/PointHeadFeedback.msg
// DO NOT EDIT!


#ifndef CONTROL_MSGS_MESSAGE_POINTHEADFEEDBACK_H
#define CONTROL_MSGS_MESSAGE_POINTHEADFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace control_msgs
{
template <class ContainerAllocator>
struct PointHeadFeedback_
{
  typedef PointHeadFeedback_<ContainerAllocator> Type;

  PointHeadFeedback_()
    : pointing_angle_error(0.0)  {
    }
  PointHeadFeedback_(const ContainerAllocator& _alloc)
    : pointing_angle_error(0.0)  {
  (void)_alloc;
    }



   typedef double _pointing_angle_error_type;
  _pointing_angle_error_type pointing_angle_error;





  typedef boost::shared_ptr< ::control_msgs::PointHeadFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::control_msgs::PointHeadFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct PointHeadFeedback_

typedef ::control_msgs::PointHeadFeedback_<std::allocator<void> > PointHeadFeedback;

typedef boost::shared_ptr< ::control_msgs::PointHeadFeedback > PointHeadFeedbackPtr;
typedef boost::shared_ptr< ::control_msgs::PointHeadFeedback const> PointHeadFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::control_msgs::PointHeadFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace control_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/home/olliver/localbuild/catkin_ws/src/common_msgs/geometry_msgs/msg'], 'actionlib_msgs': ['/home/olliver/localbuild/catkin_ws/src/common_msgs/actionlib_msgs/msg'], 'trajectory_msgs': ['/home/olliver/localbuild/catkin_ws/src/common_msgs/trajectory_msgs/msg'], 'control_msgs': ['/home/olliver/localbuild/catkin_ws/devel/share/control_msgs/msg', '/home/olliver/localbuild/catkin_ws/src/control_msgs/control_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::control_msgs::PointHeadFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_msgs::PointHeadFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_msgs::PointHeadFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cce80d27fd763682da8805a73316cab4";
  }

  static const char* value(const ::control_msgs::PointHeadFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcce80d27fd763682ULL;
  static const uint64_t static_value2 = 0xda8805a73316cab4ULL;
};

template<class ContainerAllocator>
struct DataType< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "control_msgs/PointHeadFeedback";
  }

  static const char* value(const ::control_msgs::PointHeadFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
float64 pointing_angle_error\n\
\n\
";
  }

  static const char* value(const ::control_msgs::PointHeadFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pointing_angle_error);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PointHeadFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::control_msgs::PointHeadFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::control_msgs::PointHeadFeedback_<ContainerAllocator>& v)
  {
    s << indent << "pointing_angle_error: ";
    Printer<double>::stream(s, indent + "  ", v.pointing_angle_error);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTROL_MSGS_MESSAGE_POINTHEADFEEDBACK_H
