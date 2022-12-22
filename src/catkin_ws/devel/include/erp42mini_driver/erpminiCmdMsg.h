// Generated by gencpp from file erp42mini_driver/erpminiCmdMsg.msg
// DO NOT EDIT!


#ifndef ERP42MINI_DRIVER_MESSAGE_ERPMINICMDMSG_H
#define ERP42MINI_DRIVER_MESSAGE_ERPMINICMDMSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace erp42mini_driver
{
template <class ContainerAllocator>
struct erpminiCmdMsg_
{
  typedef erpminiCmdMsg_<ContainerAllocator> Type;

  erpminiCmdMsg_()
    : dir(false)
    , speed(0)
    , steer(0)
    , brake(0)
    , encoder_reset(false)  {
    }
  erpminiCmdMsg_(const ContainerAllocator& _alloc)
    : dir(false)
    , speed(0)
    , steer(0)
    , brake(0)
    , encoder_reset(false)  {
  (void)_alloc;
    }



   typedef uint8_t _dir_type;
  _dir_type dir;

   typedef int16_t _speed_type;
  _speed_type speed;

   typedef int16_t _steer_type;
  _steer_type steer;

   typedef int16_t _brake_type;
  _brake_type brake;

   typedef uint8_t _encoder_reset_type;
  _encoder_reset_type encoder_reset;





  typedef boost::shared_ptr< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> const> ConstPtr;

}; // struct erpminiCmdMsg_

typedef ::erp42mini_driver::erpminiCmdMsg_<std::allocator<void> > erpminiCmdMsg;

typedef boost::shared_ptr< ::erp42mini_driver::erpminiCmdMsg > erpminiCmdMsgPtr;
typedef boost::shared_ptr< ::erp42mini_driver::erpminiCmdMsg const> erpminiCmdMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator1> & lhs, const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator2> & rhs)
{
  return lhs.dir == rhs.dir &&
    lhs.speed == rhs.speed &&
    lhs.steer == rhs.steer &&
    lhs.brake == rhs.brake &&
    lhs.encoder_reset == rhs.encoder_reset;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator1> & lhs, const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace erp42mini_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7cd932a7d18e4566ffe6515ef5ba19c0";
  }

  static const char* value(const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7cd932a7d18e4566ULL;
  static const uint64_t static_value2 = 0xffe6515ef5ba19c0ULL;
};

template<class ContainerAllocator>
struct DataType< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "erp42mini_driver/erpminiCmdMsg";
  }

  static const char* value(const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool dir\n"
"int16 speed\n"
"int16 steer\n"
"int16 brake\n"
"bool encoder_reset\n"
;
  }

  static const char* value(const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dir);
      stream.next(m.speed);
      stream.next(m.steer);
      stream.next(m.brake);
      stream.next(m.encoder_reset);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct erpminiCmdMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::erp42mini_driver::erpminiCmdMsg_<ContainerAllocator>& v)
  {
    s << indent << "dir: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.dir);
    s << indent << "speed: ";
    Printer<int16_t>::stream(s, indent + "  ", v.speed);
    s << indent << "steer: ";
    Printer<int16_t>::stream(s, indent + "  ", v.steer);
    s << indent << "brake: ";
    Printer<int16_t>::stream(s, indent + "  ", v.brake);
    s << indent << "encoder_reset: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.encoder_reset);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ERP42MINI_DRIVER_MESSAGE_ERPMINICMDMSG_H