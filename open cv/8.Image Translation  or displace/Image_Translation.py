import cv2
import numpy as np
image=cv2.imread('messi.jpg')
# storing the height and width of image
height,width=image.shape[:2]
print(height)
print(width)
#now decreasing the height and width by half or 2
#you can divide by as your requirement
half_height=height/2
half_width=width/2
print(half_height)
print(half_width)
#now we have to create a translation matrix
T=np.float32([[1,0,half_width],[0,1,half_height]])   
print(T) 
#now we will use WrapAffine Transfromation for shifting of image from original Position
Transformed_image=cv2.warpAffine(image,T,(width,height))
cv2.imshow("original image",image)
cv2.imshow("displace image",Transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()