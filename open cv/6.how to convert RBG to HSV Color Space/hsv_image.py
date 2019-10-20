import cv2
image=cv2.imread('messi.jpg')
cv2.imshow("Original Output",image)
img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Output",img)
# if we want to see the seprate values for hsv
cv2.imshow("Hue Channel",img[:,:,0])
cv2.imshow("Saturation",img[:,:,1])
cv2.imshow("Value",img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()