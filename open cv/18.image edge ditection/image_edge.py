import cv2
import numpy as np
image=cv2.imread('messi.jpg',0)
# extracting slop edges
x=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
y=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.imshow("slop x",x)
cv2.waitKey(0)
cv2.imshow("slop y",y)
cv2.waitKey(0)
#Type 1-for  viewing sobel image combine,we use bitwise or 
sobel_img=cv2.bitwise_or(x,y)
cv2.imshow("sobel image",sobel_img)
cv2.waitKey(0)
#type 2- finding the edges using Laplacing
laplacian_img=cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow("Laplacian",laplacian_img)
cv2.waitKey(0)
#type 3- finding the edges using canny
canny_img=cv2.Canny(image,50,200)
cv2.imshow("canny ",canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()