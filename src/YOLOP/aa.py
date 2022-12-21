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

def edges(masked):
    edges = cv2.Canny(masked, 100, 150)  # 가장자리 검출, 캐니 검출기 사용
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=140, maxLineGap=50)
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

def draw_line(lines, masked): 
    #lines = np.squeeze(lines)
    #if(flag == 0): #직선차선 그릴 때
    min_arg = np.argmin(slope)
    max_arg = np.argmax(slope)
    # print(lines[min_arg])
    x1, y1, x2, y2 = lines[min_arg]
    cv2.line(masked, (x1, y1), (x2, y2), (0, 255, 0), 5)
    x1, y1, x2, y2 = lines[max_arg]
    cv2.line(masked, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow("masked", masked)
    #if(flag == 1): #정지차선 그릴 때
        #return 0

def stop_line(lines):
    stop1 = np.argmin(lines[:, 1])
    stop2 = np.argmin(lines[:, 3])
    if(slope(stop1) == slope(stop2) or -100<slope(stop1)<-80):
        # print("stop")
        return  stop1, stop2

def detect_line(slope, lines):
    global past_angle 
    min_ang = np.min(slope)
    max_ang = np.max(slope)
    # print(slope)
    angle = (min_ang + max_ang) # 현재 측정한 값
    # print(np.any(abs(slope) < 2))
    if (np.any(abs(slope) < 2)):  # 정지선인지 확인하기, 정지선일 가능성이 있는 직선 존재 확인
        # stop_arg1 = np.minarg(slope)
        # stop_arg2 = np.maxarg(slope)
        # if(stop_line(lines) == 1): #정지선으로 인식했다면
        print('stop')
        # index = np.where(slope<10)


        # index = np.where(-10<slope[index])
    
        slope = np.array((slope,))

        slope = slope[np.where((slope>-10) & (slope<10))]

        if len(slope) > 0:
            min_ang = np.min(slope)
            max_ang = np.max(slope)
            # print(min_ang, max_ang)
            angle = (min_ang + max_ang) # 현재 측정한 값
            past_angle = angle
            # print(min_ang, max_ang)
            return angle
        # stop_line(lines)
        else:
            # print(min_ang, max_ang)
            return past_angle
        
    elif (past_angle-10<angle<past_angle+10): 
        print('right')
        past_angle = angle  # 과거 값 저장해놓기
        #draw_line(lines, slope, img, 0)
        # draw_line(lines, masked) 
        return angle
        
    else:  # trust한 값일 때, 정지선을 max or min으로 잡더라도 past 값과의 차이로 계속 유지해서 직선 각도를 반환함
        return past_angle

def parking(slope):

    index = np.where(slope>0)
    slope =np.delete(slope, index)

    return slope

#model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True)
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

cap = cv2.VideoCapture(4)
yolop = YOLOP()
while True: 
    ret, img = cap.read()
    # print(img.shape)
    # img =cv2.resize(img, (640, 480))
    img_det, ll_img = yolop.detect(img)

    lines = edges(ll_img.astype('uint8'))

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]

            # cv2.line(img_det, (x1, y1), (x2, y2), (0, 255, 0), 5)


        lines = mak_mat(lines)
        
        slope = detect_slope(lines)

        detect_line(slope, lines)

        yolop.line.x = 0
        yolop.line.z = detect_slope(line)  

        try:
            parking_ang = parking(slope)
            yolop.line.y = parking_ang[0]
        except:
            pass
        
    cv2.imshow("frame", img_det)
    print(yolop.line.z/2)

    key = cv2.waitKey(1)

    if key == 27:
        cv2.destroyAllWindows()
        break

cap.release()





