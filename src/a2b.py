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
from utils2 import pathReader, findLocalPath,purePursuit,cruiseControl,vaildObject,pidController,velocityPlanning,latticePlanner
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray
from math import cos,sin,sqrt,pow,atan2,pi
import serial

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
        
        self.pure_pursuit = purePursuit()
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
    def direction(self, ang):
        
        print("angle: ", ang)
        dir = int(ang * 2000 / 28.169014085 )
        
        # print(dir)
        bits = 16
        if dir ==0:
            self.steer1 = 0
            self.steer0 = 0
            degree = dir / 71
            # print("Direction :{}",degree, "deg ^" )
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

        self.velocity = 3

        #publisher
        # global_path_pub= rospy.Publisher('/global_path',Path, queue_size=1)
        # local_path_pub= rospy.Publisher('/local_path',Path, queue_size=1)
        # ctrl_pub = rospy.Publisher('/ctrl_cmd',CtrlCmd, queue_size=1)
        # traffic_pub = rospy.Publisher("/SetTrafficLight",SetTrafficLight,queue_size=1)


        ctrl_msg= CtrlCmd()
        
        #subscriber
        rospy.Subscriber("/after_ekf", Point, self.statusCB)
        rospy.Subscriber('/adaptive_clustering/poses', PoseArray, self.objectInfoCB)
      


        self.global_path=path_reader.read_txt(self.path_name+".txt")



        #class
        path_reader=pathReader()
        pure_pursuit=purePursuit()
        self.cc=cruiseControl(0.5,1)
        self.vo=vaildObject(self.traffic_info)
        pid=pidController()       


        self.status_msg=EgoVehicleStatus()

        vel_planner=velocityPlanning(60/3.6,1.5)
        vel_profile=vel_planner.curveBasedVelocity(self.global_path,100)

        #time var
        count=0
        rate = rospy.Rate(30) # 30hz

        lattice_current_lane=3

        while not rospy.is_shutdown():

            if self.is_status==True  and self.is_obj==True:
                local_path,self.current_waypoint=findLocalPath(self.global_path,self.status_msg)
                
                self.vo.get_object(self.object_num,self.object_info[0],self.object_info[1],self.object_info[2])
                global_obj,local_obj=self.vo.calc_vaild_obj([self.status_msg.position.x,self.status_msg.position.y,self.status_msg.heading/180*pi])

                ########################  lattice  ########################
                vehicle_status=[self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi,self.status_msg.velocity.x/3.6]
                lattice_path,selected_lane=latticePlanner(local_path,global_obj,vehicle_status,lattice_current_lane)
                lattice_current_lane=selected_lane
                                
                if selected_lane != -1: 
                    local_path=lattice_path[selected_lane]                
                
                if len(lattice_path)==7:                    
                    for i in range(1,8):
                        globals()['lattice_path_{}_pub'.format(i)].publish(lattice_path[i-1])
                ########################  lattice  ########################

                if self.is_traffic == True:
                    if self.traffic_control == "True":
                        self.tl_msg.trafficLightStatus=16
                        ###################### traffic_control ######################
                        self.set_traffic_data= SetTrafficLight()
                        self.set_traffic_data.trafficLightIndex = self.tl_msg.trafficLightIndex
                        self.set_traffic_data.trafficLightStatus = 16 ##set greenlight 
                        traffic_pub.publish(self.set_traffic_data)

                    self.cc.checkObject(local_path,global_obj,local_obj,[self.tl_msg.trafficLightIndex,self.tl_msg.trafficLightStatus])

                else :
                    self.cc.checkObject(local_path,global_obj,local_obj)

                pure_pursuit.getPath(local_path)
                pure_pursuit.getEgoStatus(self.status_msg)

                # print('====================================')
                # print(pure_pursuit.steering_angle())
                ctrl_msg.steering=-pure_pursuit.steering_angle() 
                cc_vel = self.cc.acc(local_obj,self.status_msg.velocity.x,vel_profile[self.current_waypoint],self.status_msg)
                
                target_velocity = cc_vel
                ctrl_msg.velocity=cc_vel
                

                control_input=pid.pid(target_velocity,self.status_msg.velocity) ## 속도 제어를 위한 PID 적용 (target Velocity, Status Velocity)
                
                if control_input > 0 :
                    ctrl_msg.accel= control_input
                    ctrl_msg.brake= 0

                else :
                    ctrl_msg.accel= 0
                    ctrl_msg.brake= -control_input

                # vel = (self.status_msg.velocity.x * self.status_msg.velocity.x + self.status_msg.velocity.y *self.status_msg.velocity.y) ** (0.5)
                if self.velocity < 3.0  and target_velocity<=0.0:
                    ctrl_msg.accel=0
                    ctrl_msg.brake=0
                

                local_path_pub.publish(local_path)
                ctrl_pub.publish(ctrl_msg)

                self.steering_angle=ctrl_msg.steering
                self.print_info()

                byte = ([0x53, 0x54, 0x58, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,0x0D,0x0A])
                number = byte[0:14]  #byte per number
                data = number


                # Velocity Control
                my_car.accelerate(self.velocity)
            
                # Direction Control 
                try:
                    my_car.direction(self.steering_angle)                    
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





            
            if count/300==1 :
                global_path_pub.publish(self.global_path)
                count=0
            count+=1

            rate.sleep()


    def print_info(self):

        os.system('clear')
        print('--------------------status-------------------------')
        print('position :{0} ,{1}, {2}'.format(self.status_msg.position.x,self.status_msg.position.y,self.status_msg.position.z))
        print('velocity :{} km/h'.format(self.velocity))
        print('heading :{} deg'.format(self.status_msg.heading))

        print('--------------------controller-------------------------')
        print('target steering_angle :{} deg'.format(self.steering_angle))

        print('--------------------localization-------------------------')
        print('all waypoint size: {} '.format(len(self.global_path.poses)))
        print('current waypoint : {} '.format(self.current_waypoint))

        if self.is_traffic==True:
            print('--------------------trafficLight-------------------------')
            print('traffic index : {}'.format(self.tl_msg.trafficLightIndex))
            print('traffic type : {}'.format(self.tl_msg.trafficLightType))
            print('traffic status : {}'.format(self.tl_msg.trafficLightStatus))


    def statusCB(self,data):
        self.status_msg=EgoVehicleStatus()

        self.status_msg.position=data
        # br = tf.TransformBroadcaster()
        # br.sendTransform((self.status_msg.x, self.status_msg.y, 0),
        #                 quaternion_from_euler(0, 0, self.status_msg.heading/180*pi),
        #                 rospy.Time.now(),
        #                 "gps",
        #                 "map")
        self.is_status=True                 

    def objectInfoCB(self,data):

        self.object_num=0+len(data.poses)+0
        # object_type=[]
        object_pose_x=[]
        object_pose_y=[]
        object_velocity=[]
        for num in range(0) :
            object_type.append(data.npc_list[num].type)
            object_pose_x.append(data.npc_list[num].position.x)
            object_pose_y.append(data.npc_list[num].position.y)
            object_velocity.append(data.npc_list[num].velocity.x)

        for num in range(len(data.poses)) :
            # object_type.append(data.poses[num].type)
            object_pose_x.append(data.poses[num].position.x)
            object_pose_y.append(data.poses[num].position.y)
            object_velocity.append(0)

        for num in range(0) :
            object_type.append(data.pedestrian_list[num].type)
            object_pose_x.append(data.pedestrian_list[num].position.x)
            object_pose_y.append(data.pedestrian_list[num].position.y)
            object_velocity.append(data.pedestrian_list[num].velocity.x)

        self.object_info=[object_pose_x,object_pose_y,object_velocity]
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