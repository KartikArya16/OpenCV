
import numpy as np
import cv2
img=cv2.imread('messi.png',-1)
cv2.imshow('image',img)
k=cv2.waitKey(2000)
if k == 27:
   [] cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray1.png',img)
    cv2.destroyAllWindows()
