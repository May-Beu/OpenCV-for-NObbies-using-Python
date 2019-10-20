import cv2
import numpy as np
image=cv2.imread('messi.jpg')
cv2.imshow("original",image)
cv2.waitKey(0)
#creating a kernal matrix
ones_matrix=np.ones((3,3),np.float32)/9
#now for bluring
image_blur=cv2.filter2D(image,-1,ones_matrix)
cv2.imshow("blur image",image_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()