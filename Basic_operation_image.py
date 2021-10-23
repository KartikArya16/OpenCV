import cv2
import numpy as np
img=cv2.imread('messi.png')
cv2.imshow('image',img)
cv2.waitKey()
px=img[100,100]             #accesing the pixels
print(px)
b=img[100,100]
print(b)
cv2.imshow('blue',b)
cv2.waitKey()

img[10,10]=[0,0,255]      #modifying the pixels
print(img[100,100])
cv2.imshow('image',img)
cv2.waitKey()
print(img.shape)        #accessing image property
print(img.size)         #total no. of pixel

print(img.dtype)        #image datatype

img[:,:,0]=0            #changing all red pixel to zero
cv2.imshow('image',img)
cv2.waitKey()