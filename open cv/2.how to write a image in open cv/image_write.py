author:Mayank Priy 
# In this section i will show you how you can write a image on directory.Here when we write a image it create a clone of image or we can say that it create a dupicate of image in directory where we stored this python file.
#we can change this directory by giving the file location where we want to save the clone of this image.
import cv2 
image=cv2.imread("messi.jpg")
cv2.imshow("output image",image)
 #now we will use "imwrite" module or function of open cv to create a clone of image 
 #we have to give the name of the clone image with extention of our choice like(.jpg,.png)
cv2.imwrite("clonemessi.jpg",image)# here we gave the name of our clone image with an extention (.jpg)
cv2.imwrite("clonemessi.png",image)#here we gave the name of our clone image with an extention (.png)
cv2.waitKey(0)
cv2.distroyAllWindow()
