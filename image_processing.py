# import cv2
# flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)\

import cv2
import numpy as np

img = cv2.imread('blue.jpeg')
cv2.imshow('img', img)
# print("si")
cv2.waitKey()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('gray', gray)
# print("si")
cv2.waitKey()
l1 = np.array([50, 60, 70])
l2 = np.array([130, 255, 255])
mask = cv2.inRange(gray, l1, l2)
cv2.imshow('mask', mask)
cv2.waitKey()
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('res',res)
cv2.waitKey()
