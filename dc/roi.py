import cv2
import numpy as np

# make ROI mask binary image

cap = cv2.VideoCapture('videoplayback.mp4')
ret, img = cap.read()
[y, x] = img.shape[0:2]
[t, b, h, o] = [.3, 1, .35, 0]

o = 1 - o
h = o - h
#[t, b, h, o] = [top, bottom, height, offset] (%)
p1 = (x*(.5+.5*b)-1, y*o-1)
p2 = (x*(.5+.5*t)-1, y*h)
p3 = (x*(.5-.5*t), y*h)
p4 = (x*(.5-.5*b), y*o-1)
vert = np.array([[p1, p2, p3, p4]], dtype=np.int32)
mask = np.zeros_like(img)
cv2.fillPoly(mask, vert, (255,255,255))
roi_img = cv2.bitwise_and(img, mask)
cv2.imwrite('mask.jpg', mask)
cv2.imshow('mask', mask)
cv2.waitKey(0)