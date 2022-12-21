import cv2
import numpy as np
from math import degrees

def mask2line(img, scale=5, show=0):
    # n = scaling factor
    # show = 1 : imshow line_l
    img_l = np.copy(img)
    [y, x, _] = img_l.shape
    y = int(y/scale)
    x = int(x/scale)
    img_l = cv2.resize(img_l, (x, y))
    img_c = cv2.Canny(img_l, 75, 150)
    line = np.squeeze(np.array(cv2.HoughLinesP(img_c, 1, np.pi/360, 50, minLineLength=100/scale, maxLineGap=10)))
    if show == 1:
        if line is not None:
            for l in line:
                [x1, y1, x2, y2] = l
                cv2.line(img_l, (x1,y1),(x2,y2),(0,255,0), 3)
            cv2.imshow('img_l', img_l)
            cv2.waitKey(0)
        return line*scale
    return line*scale

def mask2steer(img, scale=1, show=0):
    # return : steer signal (-2000 ~ 2000)
    #                       - left, + right
    line = mask2line(img, scale=scale, show=show)
    #print(len(line))
    [y, x, _] = img.shape
    mid = x/2
    line = np.pad(line, ((0,0),(0,3)), 'constant', constant_values=0).astype(float) # pad array [[x1, y1, x2, y2, a, b, x_intc]]
    line[:,4] = (line[:,3] - line[:,1])/(line[:,2] - line[:,0]) # a = (y2-y1)/(x2-x1)
    stop = line[line[:,4]==0]
    line = np.delete(line,line[:,4]==0,axis=0)
    line[:,5] = line[:,1] - line[:,4] * line[:,0]  # b = y1-ax1
    line[:,6] = (y - line[:,5]) / line[:,4] # y=y' intercept, x = (y'-b)/a
    line = line[np.argsort(line[:,-1]),:] # sort by intercept
    l = line[line[:,-1]<=mid][-1] # closest left line
    r = line[line[:,-1]>mid][0] # closest right line
    v = np.array([int((r[5]-l[5])/(l[4]-r[4])-mid),int(l[4]*(r[5]-l[5])/(l[4]-r[4])+l[5]-y)]) # vanishing point (x-mid,y)
    v = v/np.linalg.norm(v) # normalize
    u = np.array([0,-1]) # unit vector (car heading front)
    th = degrees(np.arccos(np.dot(u,v)))*np.sign(v[0])
    return int(th/37*2000) # ERP steering -37 ~ 37 deg, ERP steering serial -2000 ~ 2000

img = cv2.imread('mask.png')
# img_l, line = mask2line(img, show=1)
# cv2.imshow('line', img_l)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
steer = mask2steer(img, show=1)
print(steer)