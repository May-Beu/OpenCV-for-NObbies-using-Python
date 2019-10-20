import cv2
import numpy as np
image=cv2.imread('messi.jpg')
cv2.imshow("Original",image)
cv2.waitKey(0)
#using Linear interplotaion
img1=cv2.resize(image,None,fx=0.50,fy=0.50)
cv2.imshow("Linear IP",img1)
cv2.waitKey(0)
#using cubic interplotation
img2=cv2.resize(image,None,fx=0.50,fy=0.50,interpolation=cv2.INTER_CUBIC)
cv2.imshow("cubic IP",img2)
cv2.waitKey(0)
img3=cv2.resize(image,(100,100),interpolation=cv2.INTER_AREA)
cv2.imshow("Area IP",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()