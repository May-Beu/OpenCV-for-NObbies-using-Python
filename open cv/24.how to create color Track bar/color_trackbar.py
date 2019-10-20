import cv2
import numpy as np

def empty(x):
    pass

# Create a black image, a window
image= np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,empty)
cv2.createTrackbar('G','image',0,255,empty)
cv2.createTrackbar('B','image',0,255,empty)

# create switch for ON/OFF 
remote= '0 : OFF \n1 : ON'
cv2.createTrackbar(remote, 'image',0,1,empty)

while(1):
    cv2.imshow('image',image)
    if cv2.waitKey(1)==13:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(remote,'image')

    if s == 0:
        image[:] = 0
    else:
        image[:] = [b,g,r]

cv2.destroyAllWindows()