#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import rospy
import rospkg
import numpy as np
from nav_msgs.msg import Path,Odometry
from std_msgs.msg import Float64,Int16,Float32MultiArray
from geometry_msgs.msg import PoseStamped,Point
from morai_msgs.msg import EgoVehicleStatus,ObjectStatusList,CtrlCmd,GetTrafficLightStatus,SetTrafficLight
from utils import pathReader, findLocalPath,purePursuit,cruiseControl,vaildObject,pidController,velocityPlanning,latticePlanner
# import tf
from math import cos,sin,sqrt,pow,atan2,pi
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseArray
import serial
import time

from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray

from utils import purePursuit_track
import numpy as np
import time

bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
xonxoff = False
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
ser.open()


class Car:
    def __init__(self, speed=0, steer1=0, steer0=0):
        
        self.pure_pursuit = purePursuit_track()
        self.speed = speed
        self.steer1 = steer1
        self.steer0 = steer0
    def say_state(self):
        print("Speed: {} kph".format(self.speed))
        # print("Running")
    def accelerate(self, speed):
        y = speed * 10
        if 200 < y:
            self.speed = 0
            print("Speed value error!")
        else:
            sp = (int(y))
            self.speed = sp

    def direction(self, ang2):
        dir = int(ang2 * 2000 / 28.169014085 )

        bits = 16
        if dir ==0:
            self.steer1 = 0
            self.steer0 = 0
            degree = dir / 71
            print("Direction :{}",degree, "deg ^" )
        elif 0 < dir <= 255:
            st0 = 0
            a = hex((0 << bits) + dir)
            a = a[2:]
            a = a.zfill(len(a) + len(a) % 2)
            b = ''.join(a[i:i + 1] for i in range(0, len(a), 1))
            st1 = (int(b, 16))               
            degree = ((st0*256 + st1)/71)
            self.steer1 = st1
            self.steer0 = st0
            # print("Steering :{} Rigth", degree, "deg ")
        elif 0 < dir <= 2000:
            a = hex((0 << bits) + dir)
            nn = hex((0 << bits) + dir)
            a = a[3:]
            nn = nn[1:3]
            a = a.zfill(len(a) + len(a) % 2)
            b = ''.join(a[i:i + 3] for i in range(0, len(a), 3))
            st00 = ''.join(nn[i:i +1] for i in range(1,len(nn),3))
            st1 = (int(b, 16))
            st0 = (int(st00))
            degree = ((st0*256 + st1)/71)
            self.steer1 = st1
            self.steer0 = st0
            # print("Steering :{} Rigth", degree, "deg ")
        elif 2000 < dir: 
            a = hex((0 << bits) + 2000)
            nn = hex((0 << bits) + 2000)
            a = a[3:]
            nn = nn[1:3]
            a = a.zfill(len(a) + len(a) % 2)
            b = ''.join(a[i:i + 3] for i in range(0, len(a), 3))
            st00 = ''.join(nn[i:i +1] for i in range(1,len(nn),3))
            st1 = (int(b, 16))
            st0 = (int(st00))
            degree = ((st0*256 + st1)/71)
            self.steer1 = st1
            self.steer0 = st0

        elif dir < -2000:
            def tohex(val, nbits):
                return hex((val + (1 << nbits)) % (1 << nbits))
            minus = (tohex(-2000, 16))
            #st1
            minus1 = minus[4:]
            st1 = (int(minus1, 16))
            ##st0
            minus0 = minus[2:4]
            st0 = (int(minus0, 16))
            self.steer1 = st1
            self.steer0 = st0
            degree = -2000/71

        elif -2000 <= dir < 0:
            def tohex(val, nbits):
                return hex((val + (1 << nbits)) % (1 << nbits))
            minus = (tohex(dir, 16))
            #st1
            minus1 = minus[4:]
            st1 = (int(minus1, 16))
            ##st0
            minus0 = minus[2:4]
            st0 = (int(minus0, 16))
            self.steer1 = st1
            self.steer0 = st0
            degree = dir/71
            # print("Steering : {} Left", degree, "deg ")


class erp_planner():
    def __init__(self):
        rospy.init_node('erp42_total', anonymous=True)
        
        if ser.isOpen():
            print(ser.name + ' is connected...')
            print("Serial details parameters:", ser)

        my_car = Car()

        arg = rospy.myargv(argv=sys.argv)
        self.path_name='/home/kau/catkin_ws/path/path'
        self.velocity = 5

        ctrl_msg= CtrlCmd()
        
        #subscriber
        rospy.Subscriber("/line_angle", Point, self.linedetection)
        rospy.Subscriber("/line_angle2", Point, self.linedetection2)
        rospy.Subscriber("/imu_calibrated", Point, self.statusCB)
        rospy.Subscriber('/adaptive_clustering/poses', PoseArray, self.objectInfoCB)


        #class
        self.cc=cruiseControl(0.5,1)

        pid=pidController()       

        
        #read path
        self.object_info_msg=PoseArray()
        self.status_msg=Point()
        self.line=Point()
        self.line2=Point()
        self.threshold = 7

        vel_planner=velocityPlanning(60/3.6,1.5)

        #time var
        count=0
        rate = rospy.Rate(120) # 30hz

        
        i = 0
        j = 0
        prev_heading = 0
        my_heading = self.stat
        us_msg.z
        ref_steer = my_heading
        prev_time = time.time()
        first = []

        print(' Input Mission Number: ')
        j = int(input('Number : '))


        while not rospy.is_shutdown():
            my_heading = self.status_msg.z
            # print('current angle: ', my_heading)
            # print(j)

            byte = ([0x53, 0x54, 0x58, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,0x0D,0x0A])
            number = byte[0:14]  #byte per number
            data = number

            left_steering = 8



            # No Mission Start
            if j == 0:
                self.velocity = 3
                my_heading = self.status_msg.z
                print('my_heading: ', my_heading)
                print('No Mission Start!!!!!!!')
                # Velocity Control
                my_car.accelerate(self.velocity)
                # try:   
                print(self.line.z)

                if abs(self.line.z) > 10:
                    print("Lane Keeping Sytem on !!!!")
                    # if my_heading > 0:
                    # my_car.direction((self.line.z)/2) # self.line.z * 0.5
                    # print('target angle: ',(self.line.z)/2)
                    # else:
                    my_car.direction(-(self.line.z)/2) # self.line.z * 0.5
                    print('target angle: ', -(self.line.z)/2)
                else:
                    my_car.direction(-my_heading)
                # except:                  
                #     pass

                for data in range(2):
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()



            # Parking Mission
            elif j == 1:   
                print('Parking Start!!!!!!!')
                ref_steer = -self.line.y
                my_heading = self.status_msg.z

                byte = ([0x53, 0x54, 0x58, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,0x0D,0x0A])
                number = byte[0:14]  #byte per number
                data = number
                left_steering = 8           
    
                if i <= 20:
                    print('Preparing!!!!!!!!!')
                    first.append(abs(self.line.x))
                    try:   
                        self.velocity = 0
                        my_car.accelerate(self.velocity)
                        print('target angle: ', 0)
                        my_car.direction(0)
                    except:
                        pass

                    for data in range(2):
                        # time.sleep(0.1)
                        number[11] = data
                        number[8] = my_car.steer0
                        number[9] = my_car.steer1
                        number[6] = 0
                        number[7] = my_car.speed
                        send = ser.write(serial.to_bytes(number))
                        read = ser.readline()
                    
                else:
                    
                    self.velocity = 2
                    my_car.accelerate(self.velocity)
                    ref = sum(first) / 20
                    print('ref: ', ref)
                    diff = abs(self.line.x) - ref
                    
                    if diff > 3:
                        flag = 1 
                    
                    print('diff: ', diff)
                    if flag == 0:
                        print('Ready!!!!!!!!!!!')
                        try:   
                            print('target angle: ', 0)
                            my_car.direction(0)
                        except:
                            pass

                        for data in range(2):
                            # time.sleep(0.1)
                            number[11] = data
                            number[8] = my_car.steer0
                            number[9] = my_car.steer1
                            number[6] = 0
                            number[7] = my_car.speed
                            send = ser.write(serial.to_bytes(number))
                            read = ser.readline()
                    elif flag == 1:
                        print('heading: ', my_heading)
                        # if abs(my_heading + ref) < 55:
                        try:   
                            
                            print('Flag 1')
                            print('target angle: ', 10)
                            
                            my_car.direction(10)
                        except:
                            pass

                        for data in range(20):
                            # time.sleep(0.1)
                            number[11] = data
                            number[8] = my_car.steer0
                            number[9] = my_car.steer1
                            number[6] = 0
                            number[7] = my_car.speed
                            send = ser.write(serial.to_bytes(number))
                            read = ser.readline()
                        flag = 2
            
                    elif flag == 2:
                        print('heading: ', my_heading)
                        if abs(my_heading + ref) < 55:
                            try:   
                                
                                print('Go!!!!!!!!!!!')
                                print('target angle: ', self.line.z)
                                
                                my_car.direction(self.line.z)
                            except:
                                pass

                            for data in range(20):
                                # time.sleep(0.1)
                                number[11] = data
                                number[8] = my_car.steer0
                                number[9] = my_car.steer1
                                number[6] = 0
                                number[7] = my_car.speed
                                send = ser.write(serial.to_bytes(number))
                                read = ser.readline()
                            flag = 2
                        else:
                            my_car.accelerate(0)
                            try:   
                                print('Stop!!!!!!!!!!!')
                                print('target angle: ', 0)
                                my_car.direction(0)
                            except:
                                pass

                            for data in range(200):
                                # time.sleep(0.1)
                                number[11] = data
                                number[8] = my_car.steer0
                                number[9] = my_car.steer1
                                number[6] = 0
                                number[7] = my_car.speed
                                send = ser.write(serial.to_bytes(number))
                                read = ser.readline()  



            # Go Straight
            elif j == 2:
                print('Go Straight!!!!!!!')
                # Velocity Control
                my_car.accelerate(self.velocity)
                # print(self.line.z)
                # Direction Control 
                try:   
                    if abs(self.line.z) > 3:
                        print("Lane Keeping Sytem on !!!!")
                        my_car.direction(my_heading - self.line.z * 0.5)
                        print('target angle: ', my_heading - self.line.z * 0.5)
                    else:
                        my_car.direction(-my_heading)
                        print('target angle: ', -my_heading)
                except:                  
                    pass

                for data in range(2):
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()




            # Left Turn
            elif j == 3:
                print('Left Curve!!!!!!!')
                # Velocity Control
                my_car.accelerate(4)
                ref_steer = -self.line2.x
                try:   
                    print('target angle: ', ref_steer)
                    my_car.direction(ref_steer)
                except:
                    pass

                for data in range(2):
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()




            # Static Obstacle Avoidance
            elif j == 4:
                print('Static Obstacle Avoidance!!!!!!!')

                try:   
                    if i == 0:
                        print("First Obstacle!!!")
                        x_ref = self.object_info_msg.poses[0].position.x
                        y_ref = self.object_info_msg.poses[0].position.y + 2
                    else:
                        print("Second Obstacle!!!")
                        x_ref = self.object_info_msg.poses[0].position.x
                        y_ref = self.object_info_msg.poses[0].position.y - 2
                    self.velocity = 7
                    my_car.accelerate(self.velocity)
                    print('x_ref: ', x_ref)
                    print('y_ref: ', y_ref)
                    my_car.direction_xy(x_ref, y_ref, 0)
                    prev_x_ref = x_ref
                    prev_y_ref = y_ref
                    diff = ((x_ref - prev_x_ref) ** 2 + (y_ref -  prev_y_ref) ** 2) ** 0.5
                    print('diff: ', diff)
                    if x_ref < 1:
                        i = 1


                except:
                    pass

                for data in range(2):
                    # time.sleep(0.1)
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()



            # Left Turn
            elif j == 5:
                print('Left Curve!!!!!!!')
                # Velocity Control
                my_car.accelerate(4)
                ref_steer = -self.line2.x
                try:   
                    print('target angle: ', ref_steer)
                    my_car.direction(ref_steer)
                except:
                    pass

                for data in range(2):
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()


            # Moving Obstacle Avoidance
            elif j == 6:
                print('Moving Obstacle Avoidance!!!!!!!')

                try:   
                    if i == 0:
                        print("First Obstacle!!!")
                        x_ref = self.object_info_msg.poses[0].position.x
                        y_ref = self.object_info_msg.poses[0].position.y + 3
                    else:
                        print("Second Obstacle!!!")
                        x_ref = self.object_info_msg.poses[0].position.x
                        y_ref = self.object_info_msg.poses[0].position.y - 3
                    self.velocity = 4
                    my_car.accelerate(self.velocity)
                    print('x_ref: ', x_ref)
                    print('y_ref: ', y_ref)
                    my_car.direction_xy(x_ref, y_ref, 0)
                    prev_x_ref = x_ref
                    prev_y_ref = y_ref
                    diff = ((x_ref - prev_x_ref) ** 2 + (y_ref -  prev_y_ref) ** 2) ** 0.5
                    print('diff: ', diff)
                    if x_ref < 1:
                        i = 1

                except:
                    pass

                for data in range(2):
                    # time.sleep(0.1)
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()



            # No Mission Start must be changed
            else:
                print('Right Turn and Straigt Forward Mission Start!!!!!!!')
                # Velocity Control
                my_car.accelerate(self.velocity)
                try:   
                    if abs(self.line.z) > 3:
                        print("Lane Keeping Sytem on !!!!")
                        my_car.direction(ref_steer-(my_heading + self.line.z * 0.5))
                        print('target angle: ', ref_steer-(my_heading + self.line.z * 0.5))
                    else:
                        my_car.direction(ref_steer-my_heading)
                        print('target angle: ',ref_steer -my_heading)
                except:                  
                    pass

                for data in range(2):
                    number[11] = data
                    number[8] = my_car.steer0
                    number[9] = my_car.steer1
                    number[6] = 0
                    number[7] = my_car.speed
                    send = ser.write(serial.to_bytes(number))
                    read = ser.readline()

            rate.sleep()




    def linedetection(self,data):
        # self.line=Point()
        self.line=data
    def linedetection2(self,data):
        # self.line=Point()
        self.line2=data
    def statusCB(self,data):
        self.status_msg=Point()
        self.status_msg=data

        self.is_status=True  

    def objectInfoCB(self,data):
        self.object_num=len(data.poses)
        object_pose_x=[]
        object_pose_y=[]

        for num in range(len(data.poses)) :
            object_pose_x.append(data.poses[num].position.x)
            object_pose_y.append(data.poses[num].position.y)

        self.object_info=[object_pose_x,object_pose_y]
        self.is_obj=True

    def getTL_callback(self,msg):
        self.is_traffic=True
        self.tl_msg=GetTrafficLightStatus()
        self.tl_msg=msg
        
    
if __name__ == '__main__':
    try:
        kcity_pathtracking=erp_planner()
    except rospy.ROSInterruptException:
        pass