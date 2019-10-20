#Binary Images: it is those kind of image whose pixel value are either 1 or 0 ,
#1-White and 0-black
import cv2
image=cv2.imread('messi.jpg',0)#here we have conveted the image into gray scale by giving layer value "0"
cv2.imshow("Output",image)
#Now we will change our image into binary image
'''Thresholding is a technique in OpenCV, 
which is the assignment of pixel values in relation to the threshold value provided.
In thresholding, each pixel value is compared with the threshold value.
If the pixel value is smaller than the threshold, it is set to 0, otherwise,
it is set to a maximum value (generally 255).'''
#https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
ret,img=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
