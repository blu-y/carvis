// Generated by gencpp from file rtcm_msgs/Message.msg
// DO NOT EDIT!


#ifndef RTCM_MSGS_MESSAGE_MESSAGE_H
#define RTCM_MSGS_MESSAGE_MESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace rtcm_msgs
{
template <class ContainerAllocator>
struct Message_
{
  typedef Message_<ContainerAllocator> Type;

  Message_()
    : header()
    , message()  {
    }
  Message_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , message(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _message_type;
  _message_type message;





  typedef boost::shared_ptr< ::rtcm_msgs::Message_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rtcm_msgs::Message_<ContainerAllocator> const> ConstPtr;

}; // struct Message_

typedef ::rtcm_msgs::Message_<std::allocator<void> > Message;

typedef boost::shared_ptr< ::rtcm_msgs::Message > MessagePtr;
typedef boost::shared_ptr< ::rtcm_msgs::Message const> MessageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rtcm_msgs::Message_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rtcm_msgs::Message_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rtcm_msgs::Message_<ContainerAllocator1> & lhs, const ::rtcm_msgs::Message_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.message == rhs.message;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rtcm_msgs::Message_<ContainerAllocator1> & lhs, const ::rtcm_msgs::Message_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rtcm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rtcm_msgs::Message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rtcm_msgs::Message_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtcm_msgs::Message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtcm_msgs::Message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtcm_msgs::Message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtcm_msgs::Message_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rtcm_msgs::Message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "883b1fb65b83ccf75497c21f2d63052d";
  }

  static const char* value(const ::rtcm_msgs::Message_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x883b1fb65b83ccf7ULL;
  static const uint64_t static_value2 = 0x5497c21f2d63052dULL;
};

template<class ContainerAllocator>
struct DataType< ::rtcm_msgs::Message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rtcm_msgs/Message";
  }

  static const char* value(const ::rtcm_msgs::Message_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rtcm_msgs::Message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# A message representing a single RTCM message.\n"
"std_msgs/Header header\n"
"\n"
"uint8[] message\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::rtcm_msgs::Message_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rtcm_msgs::Message_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.message);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Message_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rtcm_msgs::Message_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rtcm_msgs::Message_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "message[]" << std::endl;
    for (size_t i = 0; i < v.message.size(); ++i)
    {
      s << indent << "  message[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.message[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // RTCM_MSGS_MESSAGE_MESSAGE_H
