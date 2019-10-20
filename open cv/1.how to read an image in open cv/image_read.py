#author:Mayank Priy 
# in this section i will show you how you can open a image using open cv 
import cv2
#imread function or module of opencv is used to read a image from your directory
image=cv2.imread("messi.jpg")
cv2.imshow("image output",image)
cv2.waitKey(0)
cv2.distroyAllWindow()