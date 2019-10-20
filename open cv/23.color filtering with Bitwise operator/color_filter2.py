import cv2 
import numpy as np
image=cv2.VideoCapture(0)
while True:
    ret,frame=image.read()
#now converting  RGB into HSV 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#now we can filter our ouput with our desired color
# example- for blue color
    lower_range=np.array([110,50,50])
    upper_range=np.array([130,255,255])   
    filter_img=cv2.inRange(hsv,lower_range,upper_range)
    #now using bitwise operator for color filtering
    color_bitwise=cv2.bitwise_and(frame,frame,mask=filter_img)
    cv2.imshow("filter output",filter_img)
    cv2.imshow("original output",frame)
    cv2.imshow("bitwise filter",color_bitwise)
    if cv2.waitKey(1)==13:
        break
image.release() 
cv2.destroyAllWindows()    