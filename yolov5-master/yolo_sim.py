import numpy as np
import pandas as pd
import cv2
import os
import glob
import matplotlib.pyplot as plt
import pickle
import torch
from time import time
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import CompressedImage

#model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp19/weights/best.pt', force_reload=True) 
model.cuda()
#model.cpu()

def yolo_pipeline(img):
    global df
    yolo = model(img)
    df = yolo.pandas().xyxy[0]
    yolo.display(render=True)

def camera_cb(data):
    np_arr = np.frombuffer(data.data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    yolo_pipeline(img)
    cv2.imshow('object', img)
    cv2.waitKey(1)
    #key = cv2.waitKey(frameRate)

#cap = cv2.VideoCapture('videoplayback.mp4')
frameRate = 30

rospy.init_node("yolo")
camera_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, camera_cb, queue_size = 1)

rate = rospy.Rate(frameRate)
while rospy.is_shutdown() is not True:
    rate.sleep()

cv2.destroyAllWindows()
