#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import NavSatFix
from haversine import haversine


class erp_gps():
    def __init__(self):
        rospy.init_node('gps', anonymous=True)
        #subscriber
        rospy.Subscriber("ublox_gps/fix", NavSatFix, self.gpsCB)
        rospy.spin()

    def gpsCB(self,data):
        print("latitude {}".format(data.latitude))
        print("longitude {}".format(data.longitude))

        # haversine(lyon, paris)


if __name__ == '__main__':
    try:
        gps=erp_gps()
    except rospy.ROSInterruptException:
        pass