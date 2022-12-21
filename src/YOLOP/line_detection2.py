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
from cv_bridge import CvBridge
import math
from geometry_msgs.msg import Point

past_angle = 0 #angle 초기화
time = 0

def edges(masked):
    edges = cv2.Canny(masked, 100, 150)  # 가장자리 검출, 캐니 검출기 사용
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80, maxLineGap=50)
    return lines
    
def mak_mat(lines): #행렬화
    mat_lines = np.asarray(lines)
    mat_lines = np.squeeze(mat_lines)
    return mat_lines

def detect_slope(lines):
    if lines.ndim>1:
        x = lines[:, 2] - lines[:, 0]
        y = lines[:, 3] - lines[:, 1]
        slope = y/x
        slope = slope*180/np.pi
    else:
        # print('dsfdfsd: ', lines[0])
        x = lines[2] - lines[0]
        y = lines[3] - lines[1]   
        slope = np.array(y/x)
        slope = slope*180/np.pi

    return slope

def draw_line(list, pic, flag): 
    print(list)
    if flag == 1:
        if list is not None:
            for line in list:
                x1, y1, x2, y2 = line
                cv2.line(pic, (x1, y1), (x2, y2), (0, 255, 0), 5)

        cv2.imshow("picture", pic)
       


def stop_line(lines):
    stop1 = np.argmin(lines[:, 1])
    stop2 = np.argmin(lines[:, 3])
    if(slope(stop1) == slope(stop2) or -100<slope(stop1)<-80):
        # print("stop")
        return  stop1, stop2

def detect_line(slope, lines):
    global past_angle 
    real_line = []
    min_ang = np.min(slope)
    if(min_ang>0):
        min_ang = 0
    else:
        real_line.append(lines[np.argmin(slope)])
    max_ang = np.max(slope)
    if(max_ang<0):
        max_ang = 0
    else:
        real_line.append(lines[np.argmax(slope)])
    real_line = np.array(real_line)
    angle = (min_ang + max_ang)/2 # 현재 측정한 값
    print(angle)
    if (np.any(abs(slope) < 2)):  # 정지선인지 확인하기, 정지선일 가능성이 있는 직선 존재 확인
        print('stop')
        slope = np.array((slope,))
        slope = slope[np.where((slope>-10) & (slope<10))] # stopline delete
        if len(slope) > 0: #after delete angle
            min_ang = np.min(slope)
            max_ang = np.max(slope)
            #print(min_ang, max_ang)
            angle = (min_ang + max_ang) # 현재 측정한 값
            angle = past_angle
            return angle , list, 0
        else: # no slope
            #print(min_ang, max_ang)
            time += 1
            return past_angle, list, 0
    elif (past_angle-5 < angle < past_angle + 5): #reliable angle
        past_angle = angle  # 과거 값 저장해놓기
        # prev_angle = angle
        return angle, real_line, 1
    else: 
        #print(min_ang, max_ang)
        # if(prev_angle == )
        # prev_angle = angle
        return past_angle, real_line, 1 #!!!!!!!!!

def region_of_interest(img, vertices, color3=(255,255,255), color1=255):

    mask = np.zeros_like(img)   
    if len(img.shape) > 2:
        color = color3
    else: 
        color = color1
    
    cv2.fillPoly(mask, vertices, color)
    
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image


def parking(slope):

    index = np.where(slope>0)
    slope =np.delete(slope, index)

    return slope

class YOLOP:
    def __init__(self, ros=False, device='cpu', img_size=640, topic='/camera/color/image_raw/compressed'):
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
        self.line = Point()
        self.for_left_line = Point()
        self.pub = rospy.Publisher('/line_angle', Point, queue_size =  1)
        self.pub2 = rospy.Publisher('/line_angle2', Point, queue_size =  1)

        #self.model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True)
        if ros != False:
 
            self.rospy = rospy.init_node('yolop')
            self.bridge = CvBridge()
        self.half = self.device.type != 'cpu'
        if self.half: self.model.half()
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.names))]
        self.img = torch.zeros((1, 3, self.img_size, self.img_size), device=self.device)
        _ = self.model(self.img.half() if self.half else self.img) if self.device.type != 'cpu' else None
        self.model.eval()
    def callback(self, data):
        img = self.bridge.compressed_imgmsg_to_cv2(data.data, "bgr8")
        img_det, ll_img = self.detect(img)
       
    def n2t(self, img):
        img = np.ascontiguousarray(img)
        return self.tf(img)
    def detect(self,img):
        with torch.no_grad():
            img_det = img
            #img = self.n2t(img)
            img = self.transform(img).to(self.device)
            img = img.half() if self.half else img.float()
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            det_out, da_seg_out, ll_seg_out = self.model(img)
            inf_out, _ = det_out
            det_pred = non_max_suppression(inf_out, 0.25, 0.45, classes=None)
            det = det_pred[0]
            _, _, height, width = img.shape
            ll_seg_mask = torch.nn.functional.interpolate(ll_seg_out, scale_factor=1, mode='bilinear')
            _, ll_seg_mask = torch.max(ll_seg_mask, 1)
            ll_seg_mask = ll_seg_mask.int().squeeze().cpu().numpy()
            img_det, ll_img = show_seg_result(img_det, (ll_seg_mask, ll_seg_mask), _, _)
            #ll = self.lines(ll_img)
            #return img_det, ll_img, ll
            return img_det, ll_img
    def lines(self, img):
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print()
        line = cv2.HoughLinesP(img, 1, np.pi/180, 300)
        for i in range(len(line)):
                for x1, y1, x2, y2 in line[i]:
                    cv2.line(img, (x1,y1),(x2,y2),(0,0,255),3)
        return img


openCvVidCapIds = []

for i in range(100):
    try:
        cap = cv2.VideoCapture(i)
        if cap is not None and cap.isOpened():
            openCvVidCapIds.append(i)
        # end if
    except:
        pass

# yolop = YOLOP()
yolop = YOLOP(ros=True)
rospy.init_node('yolop')
rate = rospy.Rate(1)

print(openCvVidCapIds)


cap = cv2.VideoCapture(openCvVidCapIds[2])
cap2 = cv2.VideoCapture(openCvVidCapIds[1])  

vertices = np.array([[(0,480),(120,120), (640-120,120), (640-0,480)]], dtype=np.int32)  ## ROI
while True: 
    ret, img = cap.read()
    ret2, img2 = cap2.read()
 


    # img = region_of_interest(img, vertices)  
    # img2 = region_of_interest(img2, vertices)  

    img_det, ll_img = yolop.detect(img)
    img_det2, ll_img2 = yolop.detect(img2)

    lines = edges(ll_img.astype('uint8'))
    lines2 = edges(ll_img2.astype('uint8'))
    # print('loop')

    if lines is not None:
        # for line in lines:
        #     x1, y1, x2, y2 = line[0]
        #     #cv2.line(img_det, (x1, y1), (x2, y2), (0, 255, 0), 5)


        lines = mak_mat(lines)
        # print(lines)
        
        slope = detect_slope(lines)
        
        detect_line(slope, lines)

        yolop.line.x = 0
        yolop.line.z, draw_list, flaggg = detect_line(slope, lines)
        try:
            draw_line(draw_list, img_det, flaggg)
        except:
            pass
        yolop.for_left_line.y = 0
        yolop.for_left_line.z = 0     

        try:       
            yolop.for_left_line.x = np.max(slope)
            parking_ang1 = parking(slope)
            yolop.line.y = np.max(parking_ang1)
        except:
            pass
    else:
        yolop.line.z = 9999
    if lines2 is not None:
        for line in lines2:
            x1, y1, x2, y2 = line[0]

            cv2.line(img_det2, (x1, y1), (x2, y2), (0, 255, 0), 5)


        lines2 = mak_mat(lines2)
        # print(lines2)
        
        slope2 = detect_slope(lines2)
        detect_line(slope2, lines2)
   
        try:
            parking_ang2 = parking(slope2)
            yolop.line.x = np.mean(parking_ang2)
        except:
            pass
    yolop.pub.publish(yolop.line)
    yolop.pub2.publish(yolop.for_left_line)
    cv2.imshow("frame", img_det)
    cv2.imshow("frame2", img_det2)

    
    key = cv2.waitKey(1)

    if key == 27:
        cv2.destroyAllWindows()
        cap.release()
        cap2.release()
        break
cap.release()
cap2.release()


while rospy.is_shutdown() is not True:  
    rate.sleep()


