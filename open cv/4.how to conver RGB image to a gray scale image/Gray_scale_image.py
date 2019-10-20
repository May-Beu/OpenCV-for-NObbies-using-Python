#all the black and white image in image processing term is called Grey scale Images
#it is called Grey scaled Images Because image shade in pixel of image is in between Black and White
import cv2
image=cv2.imread("messi.jpg")
cv2.imshow("Output image",image)
cv2.waitKey()
# there are various method to turn image in Grey Scale
#Method 1
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_image",grey_image)
cv2.waitKey(0)

#Method 2
image2=cv2.imread("messi.jpg",0)
cv2.imshow("Output image2",image2)
cv2.waitKey()
cv2.distroyAllWindow()

