import cv2
import numpy as np
#import pyrealsense2 as rs
import matplotlib.pyplot as plt

def roi(img, mask):
    img = cv2.bitwise_and(img, mask)
    return img

def color_filter(img, th):
    ret = np.zeros_like(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ret[hsv[:,:,2]>th] = 255
    ret[hsv[:,:,0]<50] = 255
    return ret

th = 200
mask = cv2.imread('mask.jpg')
cap = cv2.VideoCapture('videoplayback.mp4')
frameRate = 30

if cap.isOpened():
    while True:
        #ret, frame = cap.read()
        ret, img = cap.read()
        if not(ret):
            break
        img = cv2.GaussianBlur(img, (5,5), 0)
        cf = color_filter(img, 170)
        reg = roi(cf, mask)
        cv2.imshow('img', img)
        cv2.imshow('reg', reg)
        cv2.imshow('cf', cf)
        key = cv2.waitKey(frameRate)
        if key == 27:
            break
cv2.destroyAllWindows()
