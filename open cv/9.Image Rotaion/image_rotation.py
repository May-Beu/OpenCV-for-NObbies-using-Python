import cv2
import numpy as np
image=cv2.imread('messi.jpg')
height,width=image.shape[:2]
img=cv2.getRotationMatrix2D((width/2,height/2),180,1)
imgs=cv2.warpAffine(image,img,(width,height))
cv2.imshow("rotation",imgs)
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.destroyAllWindows(0)