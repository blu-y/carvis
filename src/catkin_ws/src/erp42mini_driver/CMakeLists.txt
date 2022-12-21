cmake_minimum_required(VERSION 3.0.2)
project(erp42mini_driver)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  sensor_msgs
  std_msgs
)

add_message_files(
  FILES
  erpminiStatusMsg.msg
  erpminiCmdMsg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)