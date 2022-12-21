from select import select
import torch
import numpy as np
import cv2
from torchvision.transforms import ToTensor as tt
import torchvision.transforms as transforms
from lib.core.general import non_max_suppression
from lib.models.YOLOP import get_net
from lib.dataset import LoadImages
import rospy
from sensor_msgs.msg import CompressedImage, Image
from tools.revise import show_seg_result
from lib.config import cfg
from lib.utils.utils import create_logger, select_device
import matplotlib.pyplot as plt
from numpy import random

#model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True)
class YOLOP:
    def __init__(self, ros=False, device='cpu', img_size=640):
        self.tf = tt()
        self.img_size = img_size
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        self.transform=transforms.Compose([transforms.ToTensor(),self.normalize,])
        self.logger, _, _ = create_logger(cfg, cfg.LOG_DIR, 'demo')
        self.device = select_device(self.logger, device)
        self.model = get_net(cfg)
        self.cpt = torch.load('weights/End-to-end.pth', map_location=self.device)
        self.model.load_state_dict(self.cpt['state_dict'])
        self.model = self.model.to(self.device)
        #self.model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True)
        if ros != False:
            rospy.init_node('yolop')
            self.pub_d = rospy.Publisher('/yolop_det', Image, 1)
            self.pub_l = rospy.Publisher('/yolop_ll', Image, 1)
        self.half = self.device.type != 'cpu'
        if self.half: self.model.half()
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.names))]
        self.img = torch.zeros((1, 3, self.img_size, self.img_size), device=self.device)
        _ = self.model(self.img.half() if self.half else self.img) if self.device.type != 'cpu' else None
    def n2t(self, img):
        img = np.ascontiguousarray(img)
        return self.tf(img)
    def detect(self,img):
        img_det = img
        #img = self.n2t(img)
        img = self.transform(img).to(self.device)
        img = img.half() if self.half else img.float()
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        det_out, da_seg_out, ll_seg_out = self.model(img)
        inf_out, _, _ = det_out
        det_pred = non_max_suppression(inf_out, 0.25, 0.45, classes=None)
        det = det_pred[0]
        _, _, height, width = img.shape
        ll_seg_mask = torch.nn.functional.interpolate(ll_seg_out, scale_factor=1, mode='bilinear')
        _, ll_seg_mask = torch.max(ll_seg_mask, 1)
        ll_seg_mask = ll_seg_mask.int().squeeze().cpu().numpy()
        img_det, ll_img = show_seg_result(img_det, (ll_seg_mask, ll_seg_mask), _, _)
        return img_det, ll_img
yolop = YOLOP()
#yolop = YOLOP(ros=True, device='0', img_size=320)
cap = cv2.VideoCapture('/home/kau/code/YOLOP-main/challenge_video.mp4')
#img0 = cv2.imread('test.jpg', cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
#img = cv2.imread('test.jpg')
while True:
    ret, img = cap.read()
    img_det, ll_img = yolop.detect(img)
    #print(img.shape)
    #cv2.imshow('original', img)
    cv2.imshow('img', img_det)
    cv2.imshow('ll', ll_img)
    key = cv2.waitKey(50)
    if key == 27:
        break

'''
def camera_cb(data):
    np_arr = np.frombuffer(data.data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


rospy.init_node('yolop')
camera_sub = rospy.Subcriber('/image_jpeg/compressed', CompressedImage, camera_cb, queue_size = 1)
rate = rospy.Rate(1)
while rospy.is_shutdown() is not True:
    rate.sleep()
cv2.destroyAllWindows()

'''