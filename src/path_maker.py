#!/usr/bin/env python

import rospy
import rospkg
from datetime import datetime
from geometry_msgs.msg import Point

rospack = rospkg.RosPack()
ROS_HOME = rospack.get_path('pure_pursuit')

f = None

def callback(coordinate):
    print('===============')
    global f
    f.write(str(coordinate.x) + ' ' + str(coordinate.y) + ' ' + '0' + '\n')


if __name__ == '__main__':
    rospy.init_node("path_maker")

    now = datetime.now()

    f = open('/home/kau/catkin_ws/path/path.txt', 'w')
    rospy.Subscriber('utmk_coordinate', Point, callback)


    while not rospy.is_shutdown():
        pass

    f.close()