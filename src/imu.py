#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Imu
import math
import time
from geometry_msgs.msg import Point

def quaternion_to_euler(q):
    (x, y, z, w) = (q[0], q[1], q[2], q[3])
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(t0, t1) * 180 / np.pi
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = math.asin(t2) * 180 / np.pi
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(t3, t4) * 180 / np.pi
    return [yaw, pitch, roll]


class IMUParser:
    def __init__(self):
        global pub
        rospy.init_node('imu', anonymous=True)    
        self.start_time = time.time()
        self.calib = []
        self.xyw = Point()
        self.image_sub = rospy.Subscriber("vectornav/IMU", Imu, self.callback)
        # rospy.Subscriber("ublox_gps/fix", NavSatFix, self.callback)
        rospy.spin()
        #subscriber


    def callback(self, data):
        rate=rospy.Rate(40)
        rate.sleep()
        print("orientation:")
        quaternion = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        euler = quaternion_to_euler(quaternion)
        
        self.time_pass = time.time() - self.start_time
        
        print(self.time_pass)
        if self.time_pass < 1:
            self.calib.append(euler[0])
        else:
            euler[0] -= sum(self.calib)/len(self.calib)
        print(euler)
        self.xyw.z = euler[0]
        pub = rospy.Publisher("/imu_calibrated", Point, queue_size = 1)
        pub.publish(self.xyw)

if __name__ == '__main__':
    try:
        imu_parser = IMUParser()
    except rospy.ROSInterruptException:
        pass