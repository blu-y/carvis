import cv2
import numpy as np
from math import degrees

def mask2line(img, n=5, show=0):
    # n = scaling factor
    # show = 1 : return img(scaled), line
    # show = 0 : return line
    img_l = np.copy(img)
    [y, x, _] = img_l.shape
    y = int(y/n)
    x = int(x/n)
    img_l = cv2.resize(img_l, (x, y))
    img_c = cv2.Canny(img_l, 75, 150)
    line = np.squeeze(np.array(cv2.HoughLinesP(img_c, 1, np.pi/360, 50, minLineLength=10, maxLineGap=10)))
    if show == 1:
        if line is not None:
            for l in line:
                [x1, y1, x2, y2] = l
                cv2.line(img_l, (x1,y1),(x2,y2),(0,255,0), 3)
        return img_l, line*n
    return line*n

def mask2steer(img):
    # return : steer signal (-2000 ~ 2000)
    #                       - left, + right
    line = mask2line(img)
    [y, x, _] = img.shape
    mid = x/2
    line = np.pad(line, ((0,0),(0,3)), 'constant', constant_values=0).astype(float) # pad array [[x1, y1, x2, y2, a, b, x_intc]]
    line[:,4] = (line[:,3] - line[:,1])/(line[:,2] - line[:,0]) # a = (y2-y1)/(x2-x1)
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
steer = mask2steer(img)
print(steer)