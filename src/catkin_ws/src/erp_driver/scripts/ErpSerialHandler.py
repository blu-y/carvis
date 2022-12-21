#! /usr/bin/env python3

from struct import pack
import rospy
from erp_driver.msg import erpStatusMsg, erpCmdMsg

import serial
import numpy as np

from ByteHandler import ErpMsg2Packet, Packet2ErpMsg

'''
SEND BYTES
┌─────┬─────┬─────┬─────┬─────┬──────┬───────┬───────┬────┬─────┬──────┬──────┐
│  S  │  T  │  X  │ A,M │  E  │ Gear │ Speed │ Steer │ Br │ Al  │ ETX0 │ ETX1 │
├─────┼─────┼─────┼─────┼─────┼──────┼───────┼───────┼────┼─────┼──────┼──────┤
│0x53 │0x54 │0x58 │0 , 1│0 , 1│0,1,2 │0 ~ 200│ ±2000 │1~33│0~255│ 0x0D │ 0x0A │
└─────┴─────┴─────┴─────┴─────┴──────┴───────┴───────┴────┴─────┴──────┴──────┘

RECV BYTES
┌─────┬─────┬─────┬─────┬─────┬──────┬───────┬───────┬────┬───────┬─────┬──────┬──────┐
│  S  │  T  │  X  │ A,M │  E  │ Gear │ Speed │ Steer │ Br │  ENC  │ Al  │ ETX0 │ ETX1 │ 
├─────┼─────┼─────┼─────┼─────┼──────┼───────┼───────┼────┼───────┼─────┼──────┼──────┤
│0x53 │0x54 │0x58 │0 , 1│0 , 1│0,1,2 │0 ~ 200│ ±2000 │1~33│ ±2^31 │0~255│ 0x0D │ 0x0A │
└─────┴─────┴─────┴─────┴─────┴──────┴───────┴───────┴────┴───────┴─────┴──────┴──────┘
'''

START_BITS = "535458"

class ERPHandler:
    def __init__(self) -> None:
        rospy.init_node("erp_base")
        _port = rospy.get_param("/erp_base/port")
        _baudrate = rospy.get_param("/erp_base/baudrate")
        rospy.loginfo("erp_base::Uart Port : %s", _port)
        rospy.loginfo("erp_base::Baudrate  : %s", _baudrate)

        self.seri = serial.Serial(port=_port, baudrate=_baudrate)
        rospy.logdebug("Serial %s Connected", _port)
        self.alive = 0
        self.packet = erpCmdMsg()
        self.packet.gear = 0
        self.packet.e_stop = False
        self.packet.brake = 1

        self.erpMotionMsg_pub = rospy.Publisher(
            "/erp42_status",
            erpStatusMsg,
            queue_size=3
        )
        self.erpCmdMsg_sub = rospy.Subscriber(
            "/erp42_ctrl_cmd",
            erpCmdMsg,
            self.sendPacket
        )

    def recvPacket(self) -> None:
        packet = self.seri.read(18).hex()
        if packet.find(START_BITS) is not 0:
            end, data = packet.split(START_BITS)
            packet = bytes.fromhex(START_BITS + data + end)
        self.erpMotionMsg_pub.publish(
            Packet2ErpMsg(packet)
        )
        
    def sendPacket(self, _data: erpCmdMsg) -> None:
        self.packet = _data

    def serialSend(self):
        packet = ErpMsg2Packet(self.packet, self.alive)
        print(packet)
        self.seri.write(packet)
        self.alive += 1
        if self.alive is 256:
            self.alive = 0


if __name__ == "__main__":
    ehandler = ERPHandler()
    rate = rospy.Rate(20)
    while rospy.is_shutdown() is False:
        ehandler.recvPacket()
        ehandler.serialSend()
        rate.sleep()
