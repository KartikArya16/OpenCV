import cv2
import numpy as np
img = cv2.imread("bird1.jpg")
l=img.copy()
gp=[l]
for i in range(6):      #gausian pyramid
    l=cv2.pyrDown(l)
    gp.append(l)
    #cv2.imshow(str(i),l)
l=gp[5]
lp=[l]
#expanded=cv2.pyrUp(gp[2])
#cv2.imshow("exp",expanded)
#cv2.waitKey()
#cv2.imshow("2",gp[1])
#cv2.waitKey()
#'''
for i in range(5,0,-1):
    expanded=cv2.pyrUp(gp[i])
    lap=cv2.subtract(gp[i-1], expanded)
    cv2.imshow(str(i),lap)
#'''
cv2.imshow("u",img)
cv2.imshow("original",img)
cv2.waitKey()
cv2.destroyAllWindows()