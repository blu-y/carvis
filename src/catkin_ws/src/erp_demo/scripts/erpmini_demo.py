#! /usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from erp_demo.cfg import erpmini_controlConfig
from erp_driver.msg import erpminiCmdMsg

class ErpMiniDemo:
    def __init__(self):
        rospy.init_node("erpmini_demo")

        self.tempMsg = None
        self.srv = Server(erpmini_controlConfig, self.paramValueReceiver)
        self.msg_pub = rospy.Publisher(
            "/erpmini_ctrl_cmd",
            erpminiCmdMsg,
            queue_size=5
        )

    def paramValueReceiver(self, _config, _level):
        e_msg = erpminiCmdMsg()
        e_msg.dir = _config["dir"]
        e_msg.speed = _config["speed"]
        e_msg.steer = _config["steer"]
        e_msg.brake = _config["brake"]
        e_msg.encoder_reset = _config["encoder_reset"]
        self.tempMsg = e_msg
        return _config

    def publishMsg(self):
        if self.tempMsg is not None:
            self.msg_pub.publish(self.tempMsg)


def run():
    emd = ErpMiniDemo()
    rate = rospy.Rate(20)
    while rospy.is_shutdown() is not True:
        emd.publishMsg()
        rate.sleep()


if __name__ == "__main__":
    run()
