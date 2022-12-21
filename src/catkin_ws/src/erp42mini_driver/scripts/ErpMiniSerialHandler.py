#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
import numpy as np
import serial

from erp_driver.msg import erpminiCmdMsg, erpminiStatusMsg
from ByteHandler import ErpMiniMsg2Packet, Packet2ErpMiniMsg, ERROR_DICT
from rospy.client import ERROR

'''
SEND 14 BYTES
┌─────┬─────┬─────┬─────┬───────┬───────────┬─────────┬───────┬──────┬──────┬──────┐
│  S  │  T  │  X  │ Dir │ Speed │   Steer   │    Br   │ EnRst │ ETX0 │ ETX1 │ CLC  │
├─────┼─────┼─────┼─────┼───────┼───────────┼─────────┼───────┼──────┼──────┼──────┤
│0x53 │0x54 │0x58 │ 0,1 │0 ~ 800│ 1300~1800 │1300~1800│ 0, 1  │ 0x0D │ 0x0A │ CLC  │
└─────┴─────┴─────┴─────┴───────┴───────────┴─────────┴───────┴──────┴──────┴──────┘

RECV 23 BYTES
┌─────┬─────┬─────┬─────┬──────┬───────┬───────────┬─────────┬───────┬───────┬─────┬─────┬──────┬──────┬─────┐
│  S  │  T  │  X  │ M/A │ Dir  │ Speed │   Steer   │    Br   │ EnRst │  ENC  │ GL  │ GR  │ ETX0 │ ETX1 │ CLC │ 
├─────┼─────┼─────┼─────┼──────┼───────┼───────────┼─────────┼───────┼───────┼─────┼─────┼──────┼──────┼─────┤
│0x53 │0x54 │0x58 │     │ 0,1  │0 ~ 800│ 1300~1800 │1300~1800│ 0, 1  │ ±2^31 │    cm     │ 0x0D │ 0x0A │ CLC │
└─────┴─────┴─────┴─────┴──────┴───────┴───────────┴─────────┴───────┴───────┴─────┴─────┴──────┴──────┴─────┘
'''

class ERPMiniHandler:
    def __init__(self) -> None:
        rospy.init_node("erpmini_base")
        _port = rospy.get_param("/erpmini_base/port")
        _baudrate = rospy.get_param("/erpmini_base/baudrate")
        rospy.loginfo("erpmini_base::Uart Port : %s", _port)
        rospy.loginfo("erpmini_base::Baudrate  : %s", _baudrate)

        #self.seri = serial.Serial(port=_port, baudrate=_baudrate)
        rospy.logdebug("erpmini_base::Serial %s Connected", _port)
        self.packet = None

        self.erpMotionMsg_pub = rospy.Publisher(
            "/erpmini_status",
            erpminiStatusMsg,
            queue_size=3
        )
        self.erpCmdMsg_sub = rospy.Subscriber(
            "/erpmini_ctrl_cmd",
            erpminiCmdMsg,
            self.sendPacket
        )

    def recvPacket(self) -> None:
        msg = Packet2ErpMiniMsg(self.seri.read(18))
        if msg < 0:
            rospy.logerr("Packet does not match protocol {0}", ERROR_DICT[msg])
            rospy.signal_shutdown("There's problem with Serial communication")
        self.erpMotionMsg_pub.publish(msg)
        
    def sendPacket(self, _data: erpminiCmdMsg) -> None:
        self.packet = ErpMiniMsg2Packet(_data)
    
    def serialSend(self):
        self.seri.write(self.packet)

if __name__ == "__main__":
    ehandler = ERPMiniHandler()
    rate = rospy.Rate(20)
    while rospy.is_shutdown() is not True:
        #ehandler.recvPacket()
        if ehandler.packet is not None:
            #ehandler.serialSend()
            pass
        rate.sleep()