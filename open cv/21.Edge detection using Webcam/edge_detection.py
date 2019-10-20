import cv2
image=cv2.VideoCapture(0)
def edge_detection(img):
    #turning into gray scale
    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #now bluring the image for clear output
    blur_image=cv2.GaussianBlur(gray_image,(3,3),1)
    #now to find edge
    edge_image=cv2.Canny(blur_image,35,70)
    #now changing into binary image to see clear image as output
    ret1,frame1=cv2.threshold(edge_image,127,255,cv2.THRESH_BINARY)
    return frame1    
while True:
    ret,frame=image.read()
    cv2.imshow("output",edge_detection(frame))
    cv2.imshow("original",frame)
    if cv2.waitKey(1)==13:
        break
image.release()
cv2.destroyAllWindows()    