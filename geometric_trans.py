import cv2
import numpy as np
img=cv2.imread('bird1.jpg')
cv2.imshow('img', img)
cv2.waitKey()
res=cv2.resize(img,None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)
cv2.imshow('res1', res)
cv2.waitKey()

d1=200
d2=100
d3=(d1,d2)
resize_down=cv2.resize(img,d3,interpolation=cv2.INTER_LINEAR)
cv2.imshow('down', resize_down)
cv2.waitKey()