import cv2
import numpy as np
image=cv2.imread('messi.jpg')
cv2.imshow("original",image)
cv2.waitKey(0)
#using '*' operator
img_array=np.ones(image.shape,dtype="uint8")*120
iadd=cv2.add(image,img_array)
cv2.imshow("add",iadd)
cv2.waitKey(0)
isubs=cv2.subtract(image,img_array)
cv2.imshow("substract",isubs)
cv2.waitKey(0)
imul=cv2.multiply(image,img_array)
cv2.imshow("multiply",imul)
cv2.waitKey(0)
idiv=cv2.divide(image,img_array)
cv2.imshow("divide",idiv)
cv2.waitKey(0)
#using '+' operator
img_array2=np.zeros(image.shape,dtype="uint8")+50
iadd2=cv2.add(image,img_array)
cv2.imshow("add2",iadd2)
cv2.waitKey(0)
cv2.destroyAllWindows()

