#!/usr/bin/env python3
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage



def wrapping(image): #bird eye view로 변환
    (h, w) = (image.shape[0], image.shape[1])

    source = np.float32([[480, 320], [86, 467], [850, 320], [1076, 446]])
    destination = np.float32([[300, 160], [200, 600], [950, 160], [1000, 600]])

    transform_matrix = cv2.getPerspectiveTransform(source, destination)
    minv = cv2.getPerspectiveTransform(destination, source)
    _image = cv2.warpPerspective(image, transform_matrix, (w, h)) #투시변환 시킴; 입력 영상의 점 4개를 출력 영상의 점 4개의 위치로 변환

    return _image, minv #투시변환한 이미지와 원래 이미지를 반환함

def color_filter(image):
    frame = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_yellow = np.array([0, 100, 100])
    up_yellow = np.array([60, 255, 200])

    low = np.array([0, 0, 200])
    up = np.array([180, 255, 255])
    #mask = cv2.inRange(hsv, low, up)

    yellow_mask = cv2.inRange(hsv, low_yellow, up_yellow) #노란색 차선
    white_mask = cv2.inRange(hsv, low, up) #흰색 차선 
    mask = cv2.bitwise_or(yellow_mask, white_mask) #노란색차선, 흰색차선 비트 합연산
    masked = cv2.bitwise_and(frame, frame, mask = mask) #원본이미지와 비트 곱연산

    return masked, frame

def edges(masked, frame):
    #image = cv2.resize(masked, (0, 0), dst = None, fx = 0.1, fy = 0.1, interpolation = cv2.INTER_AREA)
    # _gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(_gray, 100, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(masked, 75, 150) #가장자리 검출, 캐니 검출기 사용
    

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold = 100, maxLineGap=50) #직선 검출
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    return 


def callback(data):
    np_arr = np.fromstring(data.data, np.uint8)
    orig_frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


    # Code
    image, image_verse = wrapping(orig_frame)
    image, frame= color_filter(image)
    _gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(_gray, 160, 255, cv2.THRESH_BINARY)
    edges(thresh, frame)
    # cv2.imshow("Image window", orig_frame)
    cv2.waitKey(1)


if __name__ == '__main__':
    try:
        rospy.init_node('camera', anonymous=True)
        rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, callback)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass