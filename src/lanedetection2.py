#!/usr/bin/env python3
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage
import sys
import math
import cv2 as cv
import numpy as np
from std_msgs.msg import String, Empty, UInt16, UInt8

def region_of_interest(img, vertices, color3=(255,255,255), color1=255):

    mask = np.zeros_like(img)   
    if len(img.shape) > 2:
        color = color3
    else: 
        color = color1
    
    cv2.fillPoly(mask, vertices, color)
    
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def cal_dist(x1, y1, x2, y2, a, b):
    area = abs((x1-a) * (y2-b) - (y1-b) * (x2 - a))
    AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
    distance = area/AB
    return distance

def get_fitline(src,f_lines): 
    length = 40 
    x1, y1, x2, y2 = f_lines[0], f_lines[1], f_lines[2], f_lines[3]
    angle = (math.atan2((y2-y1),(x2-x1)))
    if angle is not np.inf:
        x1, y1 = int(((src.shape[0]-1)-y1)/np.tan(angle) + x1) , src.shape[0]-15
        x2, y2 = int(((src.shape[0]/2-length)-y2)/np.tan(angle) + x2) , int(src.shape[0]/2-length)
    
        result = np.array([x1,y1,x2,y2])
    return result


def callback(data):
    np_arr = np.fromstring(data.data, np.uint8)
    src = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    src = cv2.resize(src, (320, 180))

    dst = cv.Canny(src, 50, 200, None, 3)
    roi = region_of_interest(dst, vertices)   
    cdst = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    linesP = cv.HoughLinesP(roi, 1, np.pi / 180, 50, None, 10, 10)
    L_lines = []; R_lines= []; L_distance = []; R_distance = []
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]    
            x1, y1, x2, y2 = l	
            angle = (math.atan2((y2-y1),(x2-x1)))
            if -90*np.pi/180 < angle < -20*np.pi/180 and x1 < 200:
                L_lines.append(l)
                L_distance.append(cal_dist(l[0], l[1], l[2], l[3], 160, 180))
                #cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 3, cv.LINE_AA)
            elif 20*np.pi/180 < angle < 90*np.pi/180 and x1 > 120:
                R_lines.append([l[2], l[3], l[0], l[1]])    
                R_distance.append(cal_dist(l[0], l[1], l[2], l[3], 160, 180))
                #cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 3, cv.LINE_AA)
            
            #cv.line(src, (x1, y1), (x2, y2), (0, 0, 255), 3, cv.LINE_AA)
        
        if len(L_distance) != 0:  
            L_line = L_lines[np.argmin(L_distance)]
            L_line = get_fitline(src,L_line)
            x1, y1, x2, y2 = L_line
            L_angle = -(math.atan2((y2-y1),(x2-x1)))
            cv.line(src, (L_line[0], L_line[1]), (L_line[2], L_line[3]), (0, 255, 0), 3, cv.LINE_AA)
        else:
            L_angle=np.pi/2


        if len(R_distance) != 0:  
            R_line = R_lines[np.argmin(R_distance)]           
            R_line = get_fitline(src,R_line)   
            x1, y1, x2, y2 = R_line
            R_angle = -(math.atan2((y2-y1),(x2-x1)))
            cv.line(src, (R_line[0], R_line[1]), (R_line[2], R_line[3]), (0, 255, 0), 3, cv.LINE_AA)
        else:
            R_angle=np.pi/2


        center = (R_angle + L_angle)/2
        #center = center.astype(int)
        #cv.arrowedLine(src, (center[0], center[1]), (center[2], center[3]), (255, 0, 0), 3, cv.LINE_AA) 
        motor_ref = 180 - (center)*180/np.pi
        pub_servo.publish(motor_ref)
    cv.imshow("roi", roi)
    cv.imshow("src", src)
    cv2.waitKey(1)
    

    # diff = (ang - motor_ref) 
    
    # ang = ang - diff*Kp + (diff-prev_diff)*Kd
    print(motor_ref)




if __name__ == '__main__':
    try:
        vertices = np.array([[(0,180),(80,0), (320-80,0), (320-0,180)]], dtype=np.int32)  ## ROI
        rospy.init_node('camera', anonymous=True)
        pub_servo = rospy.Publisher('/lane_angle', UInt16, queue_size = 10)
        rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, callback)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass