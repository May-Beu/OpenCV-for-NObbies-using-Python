import cv2
import numpy as np 
image=cv2.imread('messi.jpg')
cv2.imshow("Original",image)
cv2.waitKey(0)
B,G,R=cv2.split(image)
# now creating zero matrix for extraction of RGB component seprately
zeros=np.zeros(image.shape[:2],dtype="uint8")
#for Blue Color
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
#for Green Color
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
#for Red Color
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)
cv2.destroyAllWindows()