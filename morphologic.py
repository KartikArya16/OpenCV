import cv2
import numpy as np
img=cv2.imread("1.jpg")
cv2.imshow('img', img)
cv2.waitKey()
kernel=np.ones((5,5),np.uint8)
er=cv2.erode(img,kernel,iterations=1)
dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('er', er)
cv2.waitKey()
cv2.imshow('dilation', dilation)
cv2.waitKey()