#! /usr/bin/env python3

import struct
import numpy as np
from erp_driver.msg import erpStatusMsg, erpCmdMsg

ERROR_DICT = {
    -1 : "SPEED VALUE",
    -2 : "STEER VALUE",
    -3 : "BRAKE VALUE"
}


def Packet2ErpMsg(_byte: bytes) -> erpStatusMsg:
    formated_packet = struct.unpack('<BBBBBHHHIBHHBBB', _byte)
    msg = erpStatusMsg()
    msg.control_mode = formated_packet[3]
    msg.e_stop = bool(formated_packet[4])
    msg.gear = formated_packet[5]
    msg.speed = formated_packet[6]
    msg.steer = -formated_packet[7]
    msg.brake = formated_packet[8]
    msg.encoder = -np.int32(formated_packet[9])
    msg.alive = formated_packet[10]
    return msg


def ErpMsg2Packet(_msg: erpCmdMsg, _alive: np.uint8) -> list:
    header = "STX".encode()
    tail="\r\n".encode()

    data = struct.pack(
        ">BBBHhBB", 1,
        _msg.e_stop,
        _msg.gear,
        _msg.speed,
        _msg.steer,
        _msg.brake,
        _alive
    )
    packet = header + data + tail
    return packet
