#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import NavSatFix
from haversine import haversine
from pyproj import Proj, transform
from geometry_msgs.msg import Point
from sensor_msgs.msg import NavSatFix
import numpy as np
import cv2
from sensor_msgs.msg import Imu
import math
import rospkg
import time
global x
global y

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
    
def getB(yaw, deltak):
    """
    Calculates and returns the B matrix
    3x2 matix -> number of states x number of control inputs
    The control inputs are the forward speed and the
    rotation rate around the z axis from the x-axis in the 
    counterclockwise direction.
    [v,yaw_rate]
    Expresses how the state of the system [x,y,yaw] changes
    from k-1 to k due to the control commands (i.e. control input).
    :param yaw: The yaw angle (rotation angle around the z axis) in rad 
    :param deltak: The change in time from time step k-1 to k in sec
    """
    B = np.array([  [np.cos(yaw)*deltak, 0],
                    [np.sin(yaw)*deltak, 0],
                    [0, deltak]])
    return B
 
def ekf(Q_k, H_k, R_k, A_k_minus_1, process_noise_v_k_minus_1, z_k_observation_vector, state_estimate_k_minus_1, 
        control_vector_k_minus_1, P_k_minus_1, dk, sensor_noise_w_k,angular_velocity_covariance_z):
    """
    Extended Kalman Filter. Fuses noisy sensor measurement to 
    create an optimal estimate of the state of the robotic system.
         
    INPUT
        :param z_k_observation_vector The observation from the Odometry
            3x1 NumPy Array [x,y,yaw] in the global reference frame
            in [meters,meters,radians].
        :param state_estimate_k_minus_1 The state estimate at time k-1
            3x1 NumPy Array [x,y,yaw] in the global reference frame
            in [meters,meters,radians].
        :param control_vector_k_minus_1 The control vector applied at time k-1
            3x1 NumPy Array [v,v,yaw rate] in the global reference frame
            in [meters per second,meters per second,radians per second].
        :param P_k_minus_1 The state covariance matrix estimate at time k-1
            3x3 NumPy Array
        :param dk Time interval in seconds
             
    OUTPUT
        :return state_estimate_k near-optimal state estimate at time k  
            3x1 NumPy Array ---> [meters,meters,radians]
        :return P_k state covariance_estimate for time k
            3x3 NumPy Array                 
    """
    ######################### Predict #############################
    # Predict the state estimate at time k based on the state 
    # estimate at time k-1 and the control input applied at time k-1.
    state_estimate_k = A_k_minus_1 @ (
            state_estimate_k_minus_1) + (
            getB(state_estimate_k_minus_1[2],dk)) @ (
            control_vector_k_minus_1) + (
            process_noise_v_k_minus_1)
             
    print(f'State Estimate Before EKF={state_estimate_k}')
             
    # Predict the state covariance estimate based on the previous
    # covariance and some noise
    P_k = A_k_minus_1 @ P_k_minus_1 @ A_k_minus_1.T + (
            Q_k)
         
    ################### Update (Correct) ##########################
    # Calculate the difference between the actual sensor measurements
    # at time k minus what the measurement model predicted 
    # the sensor measurements would be for the current timestep k.
    measurement_residual_y_k = z_k_observation_vector - (
            (H_k @ state_estimate_k) + (
            sensor_noise_w_k))
 
    print(f'Observation={z_k_observation_vector}')
             
    # Calculate the measurement residual covariance
    S_k = H_k @ P_k @ H_k.T + R_k
         
    # Calculate the near-optimal Kalman gain
    # We use pseudoinverse since some of the matrices might be
    # non-square or singular.
    K_k = P_k @ H_k.T @ np.linalg.pinv(S_k)
         
    # Calculate an updated state estimate for time k
    state_estimate_k = state_estimate_k + (np.reshape(K_k @ measurement_residual_y_k.T,(3,)))

    # Update the state covariance estimate for time k
    P_k = P_k - (K_k @ H_k @ P_k)
    P_k[2][2] = angular_velocity_covariance_z
    # Print the best (near-optimal) estimate of the current state of the robot
    print(f'State Estimate After EKF={state_estimate_k}')
 
    # Return the updated state and covariance estimates
    return state_estimate_k, P_k, z_k_observation_vector


class erp_gps():
    def __init__(self):
        global pub
        self.xyw = Point()
        self.start_time = time.time()
        rospy.init_node('ekf', anonymous=True)
        #subscriber
        rospy.Subscriber("vectornav/IMU", Imu, self.callback)


        # rospy.Subscriber("utmk_coordinate", Point, self.gps_x_y)
        self.fps = 125
        self.dk = 1/self.fps
        self.calib = []
        np.set_printoptions(precision=3,suppress=True)

        self.A_k_minus_1 = np.array([[1.0,  0,   0],
                                    [  0,1.0,   0],
                                    [  0,  0, 1.0]])
        self.process_noise_v_k_minus_1 = np.array([0.01,0.01,0.003])          
        self.Q_k = np.array([[1.0,   0,   0],
                            [  0, 1.0,   0],
                            [  0,   0, 1.0]])                       
        self.H_k = np.array([[1.0,  0,   0],
                            [  0,1.0,   0],
                            [  0,  0, 1.0]])                           
        self.R_k = np.array([[1.0,   0,    0],
                            [  0, 1.0,    0],
                            [  0,    0, 1.0]]) 
        self.sensor_noise_w_k = np.array([0.07,0.07,0.04])     
        self.state_estimate_k_minus_1 = np.array([0.0,0.0,0.0])  
        self.control_vector_k_minus_1 = np.array([4.5,0.0]) 
        self.P_k_minus_1 = np.array([[0.1,  0,   0],
                                    [  0,0.1,   0],
                                    [  0,  0, 0.1]])   
        self.x = 0.0
        self.y = 0.0
        pub = rospy.Publisher("/after_ekf", Point, queue_size = 1)
        rospy.spin()

    def wgs84_to_utmk_x(self,data):
        self.x = data.x


    def wgs84_to_utmk_y(self,data):
        self.y = data.y

    def callback(self,data):


        rospy.Subscriber("utmk_coordinate", Point, self.wgs84_to_utmk_x)
        rospy.Subscriber("utmk_coordinate", Point, self.wgs84_to_utmk_y)

        rate=rospy.Rate(self.fps)   
        rate.sleep()
        quaternion = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        euler = quaternion_to_euler(quaternion)

        self.time_pass = time.time() - self.start_time
  
        print(self.time_pass)
        if self.time_pass < 3:
            self.calib.append(euler[0])
        else:
            euler[0] -= sum(self.calib)/len(self.calib)
        # Create a list of sensor observations at successive timesteps
        # Each list within z_k is an observation vector.

        z_k = np.array([[self.x,self.y,euler[0]]])

                                

        # near-optimal state and covariance estimates
        optimal_state_estimate_k, covariance_estimate_k, z_k_observation_vector = ekf(
            self.Q_k, self.H_k, self.R_k,
            self.A_k_minus_1,
            self.process_noise_v_k_minus_1,
            z_k, # Most recent sensor measurement
            self.state_estimate_k_minus_1, # Our most recent estimate of the state
            self.control_vector_k_minus_1, # Our most recent control input
            self.P_k_minus_1, # Our most recent state covariance matrix
            self.dk,
            self.sensor_noise_w_k,
            data.orientation_covariance[8]) # Time interval
        
        # Get ready for the next timestep by updating the variable values
        state_estimate_k_minus_1 = optimal_state_estimate_k
        P_k_minus_1 = covariance_estimate_k
        
        # Print a blank line
        # self.xyw.x = optimal_state_estimate_k[0]
        # self.xyw.y = optimal_state_estimate_k[1]
        # self.xyw.z = optimal_state_estimate_k[2] # z is heading for this case


        self.xyw.x = z_k_observation_vector[0][0]
        self.xyw.y = z_k_observation_vector[0][1]
        self.xyw.z = z_k_observation_vector[0][2] # z is heading for this case

        pub.publish(self.xyw)
        print()






if __name__ == '__main__':
    try:    
        gps=erp_gps()
    except rospy.ROSInterruptException:
        pass