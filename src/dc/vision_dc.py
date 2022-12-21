import cv2 
import numpy as np
import pyrealsense2 as rs
import matplotlib.pyplot as plt

class DepthCamera:
    def __init__(self):
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        config = rs.config()
        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        # Start streaming
        self.pipeline.start(config)
    def get_frame(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        if not depth_frame or not color_frame:
            return False, None, None
        return True, depth_image, color_image
    def release(self):
        self.pipeline.stop()

def color_filter(img, th):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[hsv[:,:,2]<th] = 0
    return img

def grayscale(img): 
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold): 
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices, color3=(255,255,255), color1=255): 

    mask = np.zeros_like(img) 
    
    if len(img.shape) > 2: 
        color = color3
    else: 
        color = color1
        
   
    cv2.fillPoly(mask, vertices, color)
    
   
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def draw_lines(img, lines, color=[0, 0, 255], thickness=2): 
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    #line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #draw_lines(line_img, lines)

    return lines

def weighted_img(img, initial_img, a=1, b=1, c=0): 
    return cv2.addWeighted(initial_img, a, img, b, c)

def van_point(line1, line2):
    # line_arr : x1 y1 x2 y2
    line1 = line1.astype(np.float16)
    line2 = line2.astype(np.float16)
    [x1, y1, x2, y2] = line1[0]
    a1 = (y2-y1)/(x2-x1)
    b1 = y1-a1*x1
    [x1, y1, x2, y2] = line2[0]
    a2 = (y2-y1)/(x2-x1)
    b2 = y1-a1*x1
    x = (b2-b1)/(a1-a2)
    y = a1*x+b1
    return x, y

#capture = cv2.VideoCapture(0)
dc = DepthCamera()
frameRate = 33
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#print(type(capture))
while cv2.waitKey(33) < 0:
    
    ret, depth, image = dc.get_frame()
    
    #ret, image = capture.read()

    height, width = image.shape[:2] 

    image = color_filter(image, 200)
        
    gray_img = grayscale(image)
    
    blur_img = gaussian_blur(gray_img, 3)
        
    canny_img = canny(blur_img, 70, 210) 

    #cv2.imshow('result',canny_img) 

    vertices = np.array([[(10,height),(width/2-60, height/2-40), (width/2+60, height/2-40), (width-10,height)]], dtype=np.int32)
    #ROI_img = region_of_interest(canny_img, vertices) 
    ROI_img = np.copy(canny_img)
    ROI_img[:300] = 0
        
    line_arr = hough_lines(ROI_img, 1, 1 * np.pi/180, 30, 10, 20) 
    line_arr = np.squeeze(line_arr)
    if line_arr.size > 1 : 
        #print(line_arr)
        if line_arr.size == 4 : slope_degree = (np.arctan2(line_arr[1] - line_arr[3], line_arr[0] - line_arr[2]) * 180) / np.pi
        else : 	slope_degree = (np.arctan2(line_arr[:,1] - line_arr[:,3], line_arr[:,0] - line_arr[:,2]) * 180) / np.pi
        #print(slope_degree)
# slope calculate
# line_arr : x1 y1 x2 y2

        line_arr = line_arr[np.abs(slope_degree)<160]
        slope_degree = slope_degree[np.abs(slope_degree)<160]

        line_arr = line_arr[np.abs(slope_degree)>95]
        slope_degree = slope_degree[np.abs(slope_degree)>95]

        L_lines, R_lines = line_arr[(slope_degree>0),:], 		line_arr[(slope_degree<0),:]
        temp = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        L_lines, R_lines = L_lines[:,None], R_lines[:,None]
                #
                #draw_lines(temp, L_lines)
                #draw_lines(temp, R_lines)
                 
        average_R_lines = R_lines.mean(axis=0).astype(int)
        average_L_lines = L_lines.mean(axis=0).astype(int)
                ##draw_lines(temp, average_L_lines)
                #draw_lines(temp, average_R_lines)
        cv2.line(image, (average_R_lines[0,0], average_R_lines[0,1]), (average_R_lines[0,2], average_R_lines[0,3]), color=[0, 0, 255], thickness=2)
                #cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        cv2.line(image, (average_L_lines[0,0], average_L_lines[0,1]), (average_L_lines[0,2], average_L_lines[0,3]), color=[0, 0, 255], thickness=2)
        vx, vy = van_point(average_L_lines, average_R_lines)
        print(vx, vy)
        if vy > 290 : print('turn left')
        if vy < 350 : print('turn right')
        else: print('stright')
    temp = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    result = weighted_img(temp, image) 
    #cv2.imshow('result',result)
    cv2.imshow('result',result) 
    cv2.waitKey(0)

