import cv2
image=cv2.VideoCapture(0)
while True:
    ret,frame=image.read()
    cv2.imshow("output",frame)
    if cv2.waitKey(1)==13:
        break
image.release()
cv2.destroyAllWindows()    