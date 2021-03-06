import numpy as np
import cv2
# Load two images
img1 = cv2.imread('messi.png')
img2 = cv2.imread('open.png')
#image = cv2.bitwise_and(img1,img2)
#cv2.imshow('and',image)
#cv2.waitKey()
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
print(rows,cols)
roi = img1[0:rows, 0:cols ]
print(roi)
cv2.imshow('roi',roi)
print("si")
cv2.waitKey()
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('mask',mask)
print("hi")
cv2.waitKey()
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
print("jj")
cv2.waitKey()
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1',img1_bg)
cv2.waitKey()
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2',img2_fg)
cv2.waitKey()
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey()
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
