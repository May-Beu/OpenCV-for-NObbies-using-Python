import cv2
import numpy as np
image=cv2.imread('messi.jpg')
cv2.imshow("original",image)
cv2.waitKey(0)
#box six filter
img_blur=cv2.blur(image,(3,3))
cv2.imshow("box size blur",img_blur)
cv2.waitKey(0)
#using gaussian blur
img_gaussian=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("gaussian blur",img_gaussian)
cv2.waitKey(0)
#using meadian blur
img_median=cv2.medianBlur(image,5)
cv2.imshow("median blur",img_median)
cv2.waitKey(0)
# using bilateral blur
img_bilatertal=cv2.bilateralFilter(image,5,100,100)
cv2.imshow("bilateral blur",img_bilatertal)
cv2.waitKey(0)
cv2.destroyAllWindows()