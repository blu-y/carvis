#! /usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from erp_demo.cfg import erp42_controlConfig
from erp_driver.msg import erpCmdMsg

class Erp42Demo:
    def __init__(self):
        rospy.init_node("erp42_demo")

        self.tempMsg = None
        self.srv = Server(erp42_controlConfig, self.paramValueReceiver)
        self.msg_pub = rospy.Publisher(
            "/erp42_ctrl_cmd",
            erpCmdMsg,
            queue_size=5
        )

    def paramValueReceiver(self, _config, _level):
        e_msg = erpCmdMsg()
        e_msg.e_stop = _config["e_stop"]
        e_msg.gear = _config["gear"]
        e_msg.speed = _config["speed"]
        e_msg.steer = _config["steer"]
        e_msg.brake = _config["brake"]
        self.tempMsg = e_msg
        return _config

    def publishMsg(self):
        if self.tempMsg is not None:
            self.msg_pub.publish(self.tempMsg)


def run():
    emd = Erp42Demo()
    rate = rospy.Rate(20)
    while rospy.is_shutdown() is not True:
        emd.publishMsg()
        rate.sleep()


if __name__ == "__main__":
    run()
