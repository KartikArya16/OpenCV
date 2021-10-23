import cv2
import numpy as np
img=cv2.imread('bird1.jpg')
b=cv2.blur(img,(5,5),0)
cv2.imshow('b', b)
cv2.waitKey()

b1=cv2.medianBlur(img,11)
cv2.imshow('b1', b1)
cv2.waitKey()